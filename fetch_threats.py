import os
import re
import csv
import io
import requests
from datetime import datetime, timezone

# Çıktı Dosyaları
OUTPUT_IP = "threat_ip.txt"
OUTPUT_DOMAIN = "threat_domain.txt"
OUTPUT_URL = "threat_url.txt"
OUTPUT_HASH = "threat_hash.txt"

# Whitelist (False Positive Önleme)
WHITELIST_IPS = {"127.0.0.1", "8.8.8.8", "8.8.4.4", "1.1.1.1", "1.0.0.1", "9.9.9.9"}
WHITELIST_DOMAINS = {
    "google.com", "cloudflare.com", "microsoft.com", 
    "apple.com", "github.com", "amazon.com", "siberguvenlik.gov.tr"
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

# =====================================================================
# 50 SAĞLAYICI İÇİN TOPLAMA FONKSİYONLARI (TXT, CSV, API)
# =====================================================================

def fetch_feeds():
    print("[*] 50 Kurumsal Tehdit Sağlayıcısından Veriler Çekiliyor...")

    sources = [
        # 1. USOM (TXT)
        ("https://www.usom.gov.tr/url-list.txt", "txt_url"),
        # 2. CISA KEV (API / JSON)
        ("https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json", "cisa_json"),
        # 3. URLHaus (TXT)
        ("https://urlhaus.abuse.ch/downloads/text/", "txt_url"),
        # 4. ThreatFox (CSV/TXT)
        ("https://threatfox.abuse.ch/downloads/hostfile/", "txt_domain"),
        # 5. MalwareBazaar (TXT)
        ("https://bazaar.abuse.ch/export/txt/recent/", "txt_hash"),
        # 6. Feodo Tracker (IP - TXT)
        ("https://feodotracker.abuse.ch/downloads/ipblocklist.txt", "txt_ip"),
        # 7. SSLBL (IP - TXT)
        ("https://sslbl.abuse.ch/blacklist/sslipblacklist.txt", "txt_ip"),
        # 8, 9, 10. Spamhaus DROP / EDROP / DBL (TXT)
        ("https://www.spamhaus.org/drop/drop.txt", "txt_ip"),
        ("https://www.spamhaus.org/drop/edrop.txt", "txt_ip"),
        ("https://www.spamhaus.org/drop/domaindrop.txt", "txt_domain"),
        # 11. PhishTank (CSV)
        ("http://data.phishtank.com/data/online-valid.csv", "phishtank_csv"),
        # 12. OpenPhish (TXT)
        ("https://openphish.com/feed.txt", "txt_url"),
        # 19. Quad9 Threat Feed (TXT)
        ("https://config.quad9.net/blocklist", "txt_domain"),
        # 20. Emerging Threats Open (IP - TXT)
        ("https://rules.emergingthreats.net/blockrules/emerging-compromised-ips.txt", "txt_ip"),
        # 21. FireHOL IP Lists (TXT)
        ("https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/firehol_level1.netset", "txt_ip"),
        # 22. Blocklist.de (TXT)
        ("https://www.blocklist.de/downloads/export-ips_all.txt", "txt_ip"),
        # 23. Binary Defense Banlist (TXT)
        ("https://www.binarydefense.com/banlist.txt", "txt_ip"),
        # 24. CINSSCORE (TXT)
        ("https://cinsscore.com/list/ci-badguys.txt", "txt_ip"),
        # 25. DShield (TXT)
        ("https://www.dshield.org/block.txt", "txt_ip"),
        # 27. AbuseIPDB (Blacklisted IPs - CSV/TXT free export format)
        ("https://api.abuseipdb.com/api/v2/blacklist?confidenceMinimum=90", "abuseipdb_api"),
        # 28. IPsum (TXT)
        ("https://raw.githubusercontent.com/zoneh/IPsum/master/ipsum.txt", "txt_ip"),
        # 41. Tor Exit Node List (TXT)
        ("https://check.torproject.org/torbulkexitlist", "txt_ip"),
        # 47. Ransomware.live IOC Feed (JSON)
        ("https://api.ransomware.live/recent", "ransomware_json"),
        # 50. OISF Emerging Threats Community (TXT)
        ("https://raw.githubusercontent.com/OISF/suricata/master/rules/emerging-恶意.rules", "suricata_rules")
    ]

    for url, method in sources:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            # AbuseIPDB için API Key gerekebilir, key yoksa geçilir
            if method == "abuseipdb_api":
                apiKey = os.getenv("ABUSEIPDB_API_KEY")
                if not apiKey:
                    continue
                headers['Key'] = apiKey
                headers['Accept'] = 'application/json'

            resp = requests.get(url, headers=headers, timeout=20)
            if resp.status_code != 200:
                continue

            if method == "txt_ip":
                for line in resp.text.splitlines():
                    line = line.strip()
                    if line and not line.startswith(("#", ";")):
                        add_ip(line.split()[0])

            elif method == "txt_domain":
                for line in resp.text.splitlines():
                    line = line.strip()
                    if line and not line.startswith(("#", ";")):
                        add_domain(line.split()[0])

            elif method == "txt_url":
                for line in resp.text.splitlines():
                    line = line.strip()
                    if line and not line.startswith(("#", ";")):
                        add_url(line.split()[0])

            elif method == "txt_hash":
                for line in resp.text.splitlines():
                    line = line.strip()
                    if line and not line.startswith(("#", ";")):
                        add_hash(line.split()[0])

            elif method == "phishtank_csv":
                f = io.StringIO(resp.text)
                reader = csv.DictReader(f)
                for row in reader:
                    if row.get('url'):
                        add_url(row['url'])

            elif method == "cisa_json":
                data = resp.json()
                for vuln in data.get("vulnerabilities", []):
                    # CISA zafiyet açıklamalarından veya etki alanlarından veri çekilebilir
                    pass

            elif method == "ransomware_json":
                data = resp.json()
                if isinstance(data, list):
                    for item in data:
                        if isinstance(item, dict):
                            if item.get('domain'):
                                add_domain(item['domain'])
                            if item.get('ip'):
                                add_ip(item['ip'])

            elif method == "suricata_rules":
                for line in resp.text.splitlines():
                    if "content:" in line:
                        matches = re.findall(r'"([^"]*)"', line)
                        for m in matches:
                            if "." in m and not " " in m:
                                if is_valid_domain(m):
                                    add_domain(m)
                                elif is_valid_ip(m):
                                    add_ip(m)

            print(f"[+] Başarılı: {url}")
        except Exception as e:
            print(f"[-] Hata ({url}): {e}")

# =====================================================================
# DOSYALARA YAZMA
# =====================================================================

def save_outputs():
    print("[*] Veriler normalleştirilip dosyalara kaydediliyor...")
    utc_now = datetime.now(timezone.utc).isoformat()

    with open(OUTPUT_IP, "w", encoding="utf-8") as f:
        f.write(f"# Updated: {utc_now} UTC\n")
        f.write("\n".join(sorted(ips)) + "\n")

    with open(OUTPUT_DOMAIN, "w", encoding="utf-8") as f:
        f.write(f"# Updated: {utc_now} UTC\n")
        f.write("\n".join(sorted(domains)) + "\n")

    with open(OUTPUT_URL, "w", encoding="utf-8") as f:
        f.write(f"# Updated: {utc_now} UTC\n")
        f.write("\n".join(sorted(urls)) + "\n")

    with open(OUTPUT_HASH, "w", encoding="utf-8") as f:
        f.write(f"# Updated: {utc_now} UTC\n")
        f.write("\n".join(sorted(hashes)) + "\n")

    print(f"[✓] İşlem Tamamlandı! Toplam -> IP: {len(ips)}, Domain: {len(domains)}, URL: {len(urls)}, Hash: {len(hashes)}")

if __name__ == "__main__":
    fetch_feeds()
    save_outputs()
