import os
import re
import csv
import io
import requests
from datetime import datetime, timezone

OUTPUT_IP = "threat_ip.txt"
OUTPUT_DOMAIN = "threat_domain.txt"
OUTPUT_URL = "threat_url.txt"
OUTPUT_HASH = "threat_hash.txt"

WHITELIST_IPS = {"127.0.0.1", "8.8.8.8", "8.8.4.4", "1.1.1.1", "1.0.0.1", "9.9.9.9"}
WHITELIST_DOMAINS = {
    "google.com", "cloudflare.com", "microsoft.com", 
    "apple.com", "github.com", "amazon.com", "siberguvenlik.gov.tr", "usom.gov.tr"
}

ips = set()
domains = set()
urls = set()
hashes = set()

def is_valid_ip(ip):
    if not ip or ip in WHITELIST_IPS:
        return False
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(p) <= 255 for p in parts)
    except ValueError:
        return False

def is_valid_domain(domain):
    if not domain:
        return False
    domain = domain.lower().strip()
    if domain in WHITELIST_DOMAINS or domain.endswith(tuple("." + d for d in WHITELIST_DOMAINS)):
        return False
    pattern = r"^(?!-)[a-z0-9-]{1,63}(?<!-)\.(?:[a-z0-9-]{1,63}(?<!-)\.)*[a-z]{2,}$"
    return bool(re.match(pattern, domain))

def add_ip(ip):
    if is_valid_ip(ip):
        ips.add(ip)

def add_domain(domain):
    if is_valid_domain(domain):
        domains.add(domain)

def add_url(url):
    if url and url.startswith("http"):
        urls.add(url)
        match = re.findall(r'https?://([^/]+)', url)
        if match:
            add_domain(match[0])

def add_hash(h):
    if h:
        h = h.strip().lower()
        if len(h) in (32, 64) and all(c in "0123456789abcdef" for c in h):
            hashes.add(h)

def fetch_feeds():
    print("[*] Tehdit istihbarat kaynaklarından veriler çekiliyor...")

    sources = [
        ("https://www.usom.gov.tr/url-list.txt", "txt_url"),
        ("https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json", "cisa_json"),
        ("https://urlhaus.abuse.ch/downloads/text/", "txt_url"),
        ("https://threatfox.abuse.ch/downloads/hostfile/", "txt_domain"),
        ("https://bazaar.abuse.ch/export/txt/recent/", "txt_hash"),
        ("https://feodotracker.abuse.ch/downloads/ipblocklist.txt", "txt_ip"),
        ("https://sslbl.abuse.ch/blacklist/sslipblacklist.txt", "txt_ip"),
        ("https://www.spamhaus.org/drop/drop.txt", "txt_ip"),
        ("https://www.spamhaus.org/drop/edrop.txt", "txt_ip"),
        ("https://www.spamhaus.org/drop/domaindrop.txt", "txt_domain"),
        ("http://data.phishtank.com/data/online-valid.csv", "phishtank_csv"),
        ("https://openphish.com/feed.txt", "txt_url"),
        ("https://rules.emergingthreats.net/blockrules/emerging-compromised-ips.txt", "txt_ip"),
        ("https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/firehol_level1.netset", "txt_ip"),
        ("https://www.blocklist.de/downloads/export-ips_all.txt", "txt_ip"),
        ("https://www.binarydefense.com/banlist.txt", "txt_ip"),
        ("https://cinsscore.com/list/ci-badguys.txt", "txt_ip"),
        ("https://www.dshield.org/block.txt", "txt_ip"),
        ("https://raw.githubusercontent.com/zoneh/IPsum/master/ipsum.txt", "txt_ip"),
        ("https://check.torproject.org/torbulkexitlist", "txt_ip"),
    ]

    for url, method in sources:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) CyberSecurityEngine/4.0'}
            resp = requests.get(url, headers=headers, timeout=25)
            if resp.status_code != 200:
                continue

            if method == "txt_ip":
                for line in resp.text.splitlines():
                    line = line.strip()
                    if line and not line.startswith(("#", ";", "//")):
                        add_ip(line.split()[0])
            elif method == "txt_domain":
                for line in resp.text.splitlines():
                    line = line.strip()
                    if line and not line.startswith(("#", ";", "//")):
                        add_domain(line.split()[0])
            elif method == "txt_url":
                for line in resp.text.splitlines():
                    line = line.strip()
                    if line and not line.startswith(("#", ";", "//")):
                        add_url(line.split()[0])
            elif method == "txt_hash":
                for line in resp.text.splitlines():
                    line = line.strip()
                    if line and not line.startswith(("#", ";", "//")):
                        add_hash(line.split()[0])
            elif method == "phishtank_csv":
                f = io.StringIO(resp.text)
                reader = csv.DictReader(f)
                for row in reader:
                    if row.get('url'):
                        add_url(row['url'])
            elif method == "cisa_json":
                pass

            print(f"[+] Başarılı: {url}")
        except Exception as e:
            print(f"[-] Hata ({url}): {e}")

def save_outputs():
    print("[*] Veriler işleniyor ve dosyalara kaydediliyor...")
    utc_now = datetime.now(timezone.utc).isoformat()

    def load_existing(filename, target_set, validator_func):
        if os.path.exists(filename):
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith("#"):
                            if validator_func(line):
                                target_set.add(line)
            except Exception:
                pass

    load_existing(OUTPUT_IP, ips, is_valid_ip)
    load_existing(OUTPUT_DOMAIN, domains, is_valid_domain)
    load_existing(OUTPUT_URL, urls, lambda u: u.startswith("http"))
    load_existing(OUTPUT_HASH, hashes, lambda h: len(h) in (32, 64))

    for filename, data in [(OUTPUT_IP, ips), (OUTPUT_DOMAIN, domains), (OUTPUT_URL, urls), (OUTPUT_HASH, hashes)]:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Updated: {utc_now} UTC\n")
            f.write("\n".join(sorted(data)) + "\n")
            f.flush()
            os.fsync(f.fileno())

    print(f"[✓] İşlem Tamamlandı -> IP: {len(ips)}, Domain: {len(domains)}, URL: {len(urls)}, Hash: {len(hashes)}")

if __name__ == "__main__":
    fetch_feeds()
    save_outputs()
