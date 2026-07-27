import os
import re
import csv
import io
import requests
from datetime import datetime, timezone
from collections import defaultdict

OUTPUT_IP = "threat_ip.txt"
OUTPUT_DOMAIN = "threat_domain.txt"
OUTPUT_URL = "threat_url.txt"
OUTPUT_HASH = "threat_hash.txt"

WHITELIST_IPS = {"127.0.0.1", "8.8.8.8", "8.8.4.4", "1.1.1.1", "1.0.0.1", "9.9.9.9"}
WHITELIST_DOMAINS = {
    "google.com", "cloudflare.com", "microsoft.com", 
    "apple.com", "github.com", "amazon.com", "siberguvenlik.gov.tr", "usom.gov.tr"
}

ip_sources = defaultdict(set)
domain_sources = defaultdict(set)
url_sources = defaultdict(set)
hash_sources = defaultdict(set)

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

def add_ip(ip, source):
    if is_valid_ip(ip):
        ips.add(ip)
        ip_sources[ip].add(source)

def add_domain(domain, source):
    if is_valid_domain(domain):
        domains.add(domain)
        domain_sources[domain].add(source)

def add_url(url, source):
    if url and url.startswith("http"):
        urls.add(url)
        url_sources[url].add(source)
        match = re.findall(r'https?://([^/]+)', url)
        if match:
            add_domain(match[0], f"{source} (Extracted)")

def add_hash(h, source):
    if h:
        h = h.strip().lower()
        if len(h) in (32, 40, 64) and all(c in "0123456789abcdef" for c in h):
            hashes.add(h)
            hash_sources[h].add(source)

def extract_hashes_from_text(text, source_name):
    potential_hashes = re.findall(r'\b[a-fA-F0-9]{32}\b|\b[a-fA-F0-9]{40}\b|\b[a-fA-F0-9]{64}\b', text)
    for h in potential_hashes:
        add_hash(h, source_name)

def fetch_feeds():
    print("[*] Tüm servislerden IP, Domain, URL ve Hash verileri toplanıyor...")

    sources = [
        ("USOM URL List", "https://www.usom.gov.tr/url-list.txt", "txt_url"),
        ("URLHaus", "https://urlhaus.abuse.ch/downloads/text/", "txt_url"),
        ("ThreatFox IOC List", "https://threatfox.abuse.ch/downloads/ioc_list/", "threatfox_csv"),
        ("MalwareBazaar Recent", "https://bazaar.abuse.ch/export/txt/recent/", "txt_hash"),
        ("Feodo Tracker", "https://feodotracker.abuse.ch/downloads/ipblocklist.txt", "txt_ip"),
        ("SSLBL", "https://sslbl.abuse.ch/blacklist/sslipblacklist.txt", "txt_ip"),
        ("Spamhaus DROP", "https://www.spamhaus.org/drop/drop.txt", "txt_ip"),
        ("Spamhaus EDROP", "https://www.spamhaus.org/drop/edrop.txt", "txt_ip"),
        ("Spamhaus DBL", "https://www.spamhaus.org/drop/domaindrop.txt", "txt_domain"),
        ("PhishTank", "http://data.phishtank.com/data/online-valid.csv", "phishtank_csv"),
        ("OpenPhish", "https://openphish.com/feed.txt", "txt_url"),
        ("Emerging Threats", "https://rules.emergingthreats.net/blockrules/emerging-compromised-ips.txt", "txt_ip"),
        ("FireHOL Level1", "https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/firehol_level1.netset", "txt_ip"),
        ("Blocklist.de", "https://www.blocklist.de/downloads/export-ips_all.txt", "txt_ip"),
        ("Binary Defense", "https://www.binarydefense.com/banlist.txt", "txt_ip"),
        ("CINSSCORE", "https://cinsscore.com/list/ci-badguys.txt", "txt_ip"),
        ("DShield", "https://www.dshield.org/block.txt", "txt_ip"),
        ("IPsum", "https://raw.githubusercontent.com/zoneh/IPsum/master/ipsum.txt", "txt_ip"),
        ("Tor Exit Nodes", "https://check.torproject.org/torbulkexitlist", "txt_ip"),
    ]

    for source_name, url, method in sources:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) CyberSecurityEngine/8.0'}
            resp = requests.get(url, headers=headers, timeout=30)
            if resp.status_code != 200:
                continue

            content = resp.text
            extract_hashes_from_text(content, f"{source_name} (Scan)")

            if method == "txt_ip":
                for line in content.splitlines():
                    line = line.strip()
                    if line and not line.startswith(("#", ";", "//")):
                        add_ip(line.split()[0], source_name)
            elif method == "txt_domain":
                for line in content.splitlines():
                    line = line.strip()
                    if line and not line.startswith(("#", ";", "//")):
                        add_domain(line.split()[0], source_name)
            elif method == "txt_url":
                for line in content.splitlines():
                    line = line.strip()
                    if line and not line.startswith(("#", ";", "//")):
                        add_url(line.split()[0], source_name)
            elif method == "txt_hash":
                for line in content.splitlines():
                    line = line.strip()
                    if line and not line.startswith(("#", ";", "//")):
                        parts = line.split(',')
                        val = parts[0].strip('"').strip()
                        add_hash(val, source_name)
            elif method == "threatfox_csv":
                for line in content.splitlines():
                    line = line.strip()
                    if line and not line.startswith("#"):
                        cols = line.split('"')
                        for col in cols:
                            col_clean = col.strip()
                            if len(col_clean) in (32, 40, 64):
                                add_hash(col_clean, source_name)
            elif method == "phishtank_csv":
                f = io.StringIO(content)
                reader = csv.DictReader(f)
                for row in reader:
                    if row.get('url'):
                        add_url(row['url'], source_name)

            print(f"[+] Başarılı ({source_name}): {url}")
        except Exception as e:
            print(f"[-] Hata ({source_name}): {e}")

def update_readme_stats():
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        print("[-] README.md bulunamadı, istatistik güncellenemedi.")
        return

    print("[*] README.md canlı istatistikleri güncelleniyor...")
    
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    stats_block = f"\n\n> **Live Statistics:** 🌐 IP: `{len(ips):,}` | 🗂️ Domain: `{len(domains):,}` | 🔗 URL: `{len(urls):,}` | 🔑 Hash: `{len(hashes):,}`"

    # Eski istatistik satırı varsa temizle
    content = re.sub(r"\n\n> \*\*Live Statistics:\*\*.*", "", content)
    
    # Başlığın hemen altına ekle
    content = content.replace("# SOC-FEEDS", f"# SOC-FEEDS{stats_block}")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[✓] README.md istatistikleri başarıyla işlendi.")

def save_outputs():
    print("[*] Tüm veriler işleniyor ve çıktı dosyaları yazılıyor...")
    utc_now = datetime.now(timezone.utc).isoformat()

    def write_feed_file(filename, data_set, source_dict):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# ==========================================================\n")
            f.write(f"# SOC-FEEDS INTELLIGENCE REPORT\n")
            f.write(f"# Last Updated: {utc_now} UTC\n")
            f.write(f"# Total Records: {len(data_set)}\n")
            f.write(f"# ==========================================================\n\n")
            
            for item in sorted(data_set):
                sources = ", ".join(sorted(source_dict[item])) if item in source_dict else "Source-Unknown"
                f.write(f"{item}  # Sources: [{sources}]\n")
            
            f.flush()
            os.fsync(f.fileno())

    write_feed_file(OUTPUT_IP, ips, ip_sources)
    write_feed_file(OUTPUT_DOMAIN, domains, domain_sources)
    write_feed_file(OUTPUT_URL, urls, url_sources)
    write_feed_file(OUTPUT_HASH, hashes, hash_sources)

    # README güncellemesini tetikle
    update_readme_stats()

    print(f"[✓] Tamamlandı -> IP: {len(ips)}, Domain: {len(domains)}, URL: {len(urls)}, Hash: {len(hashes)}")

if __name__ == "__main__":
    fetch_feeds()
    save_outputs()
