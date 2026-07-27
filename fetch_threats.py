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

# =====================================================================
# API VE DOSYA KAYNAKLARINDAN TÜM VERİLERİ ÇEKME FONKSİYONU
# =====================================================================

def fetch_feeds():
    print("[*] Tüm kurumsal API ve açık kaynak beslemelerinden tam veri çekme işlemi başlatıldı...")

    sources = [
        # 1. USOM / Siber Güvenlik Başkanlığı (TXT / API tabanlı resmi liste)
        ("https://www.usom.gov.tr/url-list.txt", "txt_url"),
        # 2. CISA KEV (API / JSON - Tüm bilinen istismar edilen zafiyetler ve etki alanları)
        ("https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json", "cisa_json"),
        # 3. URLHaus (TXT)
        ("https://urlhaus.abuse.ch/downloads/text/", "txt_url"),
        # 4. ThreatFox (TXT)
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
        # 28. IPsum (TXT)
        ("https://raw.githubusercontent.com/zoneh/IPsum/master/ipsum.txt", "txt_ip"),
        # 41. Tor Exit Node List (TXT)
        ("https://check.torproject.org/torbulkexitlist", "txt_ip"),
        # 47. Ransomware.live IOC Feed (JSON API)
        ("https://api.ransomware.live/recent", "ransomware_json"),
    ]

    for url, method in sources:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) CyberSecurityEngine/1.0'}
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
                data = resp.json()
                for vuln in data.get("vulnerabilities", []):
                    # CISA KEV kayıtlarındaki metinlerden veya olası IoC alanlarından domain/IP ayıklama
                    notes = vuln.get("shortDescription", "") + " " + vuln.get("vendorProject", "")
                    # Gerekli ek alanlar taranabilir

            elif method == "ransomware_json":
                data = resp.json()
                if isinstance(data, list):
                    for item in data:
                        if isinstance(item, dict):
                            if item.get('domain'):
                                add_domain(item['domain'])
                            if item.get('ip'):
                                add_ip(item['ip'])

            print(f"[+] Başarıyla çekildi ve işlendi: {url}")
        except Exception as e:
            print(f"[-] Kaynak çekilirken hata oluştu ({url}): {e}")

# =====================================================================
# DOSYALARA BİRLEŞTİREREK YAZMA (INCREMENTAL / MERGE MANTIĞI)
# =====================================================================

def save_outputs():
    print("[*] Mevcut kayıtlar ve yeni çekilen veriler birleştirilip güncelleniyor...")
    utc_now = datetime.now(timezone.utc).isoformat()

    # Eğer daha önceden oluşmuş dosyalar varsa, eski kayıtları da kaybetmemek için okuyup sete dahil et (Üzerine ekleme mantığı)
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

    # Dosyalara son hali yazılıyor
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

    print(f"[✓] Güncelleme Tamamlandı! Toplam Kayıt -> IP: {len(ips)}, Domain: {len(domains)}, URL: {len(urls)}, Hash: {len(hashes)}")

if __name__ == "__main__":
    fetch_feeds()
    save_outputs()
