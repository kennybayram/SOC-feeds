<div align="center">

# SOC-FEEDS
### Real-Time Open-Source Threat Intelligence & IoC Aggregator

[![Threat Feed Automation](https://github.com/kennybayram/SOC-feeds/actions/workflows/main.yml/badge.svg)](https://github.com/kennybayram/SOC-feeds/actions/workflows/main.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Maintained](https://img.shields.io/badge/Maintained%3D-Yes-green.svg)](https://github.com/kennybayram/SOC-feeds/actions)

*Automated, high-precision security feeds designed for Security Operations Centers (SOC), SIEM integrations, and perimeter firewalls.*

---

### 🌍 Select Language / Dil Seçimi

[🇹🇷 Türkçe](#türkçe) | [🇬🇧 English](#english) | [🇩🇪 Deutsch](#deutsch) | [🇫🇷 Français](#français) | [🇪🇸 Español](#español) | [🇮🇹 Italiano](#italiano) | [🇳🇱 Nederlands](#nederlands) | [🇵🇱 Polski](#polski) | [🇸🇪 Svenska](#svenska) | [🇩🇰 Dansk](#dansk) | [🇫🇮 Suomi](#suomi) | [🇵🇹 Português](#português) | [🇬🇷 Ελληνικά](#ελληνικά) | [🇨🇿 Čeština](#čeština) | [🇭🇺 Magyar](#magyar) | [🇷🇴 Română](#română) | [🇧🇬 Български](#български) | [🇸🇰 Slovenčina](#slovenčina) | [🇭🇷 Hrvatski](#hrvatski) | [🇸🇮 Slovenščina](#slovenščina) | [🇱🇹 Lietuvių](#lietuvių) | [🇱🇻 Latviešu](#latviešu) | [🇪🇪 Eesti](#eesti) | [🇮🇪 Gaeilge](#gaeilge) | [🇲🇹 Malti](#malti)

</div>

---

<a name="türkçe"></a>
## 🇹🇷 Türkçe

### Kurumsal Genel Bakış
**SOC-feeds**, kritik ağ altyapılarını, Güvenlik Operasyon Merkezlerini (SOC) ve kurumsal çevre güvenliğini korumak amacıyla tasarlanmış otomatik bir Tehdit İstihbaratı (Threat Intelligence) toplama ve derleme motorudur. Sistem; dünya çapındaki güvenilir, açık kaynaklı ve resmi istihbarat kaynaklarından zararlı IP adreslerini, etki alanlarını (domain), URL'leri ve zararlı yazılım hash değerlerini saatlik periyotlarla derler, temizler, mükerrer kayıtları ayıklar ve güncel tutar.

### Entegrasyon ve Kullanım Alanları
* **Güvenlik Duvarları (Next-Gen Firewalls):** Palo Alto, Fortinet, Check Point, Cisco ASA/FTD sistemlerinde IP ve Domain bazlı otomatik bloklama (External Dynamic Lists).
* **SIEM & SOAR Platformları:** Wazuh, Zabbix, Splunk, Elastic Stack, Microsoft Sentinel üzerinde log korelasyonu ve tehdit avcılığı (Threat Hunting).
* **E-Posta Güvenlik Ağ Geçitleri (SEG):** Phishing ve zararlı URL/domain tespiti.

### Veri Kaynakları (Threat Intelligence Feeds)
Sistem aşağıdaki resmi ve küresel güvenlik kaynaklarından anlık veri çekmektedir:
1. **USOM URL List:** Türkiye Ulusal Siber Olaylara Müdahale Merkezi zararlı bağlantı listesi.
2. **CISA KEV:** Bilinen ve aktif olarak istismar edilen zaafiyet katalogları.
3. **Abuse.ch Ecosystem:**
   - *URLHaus:* Zararlı yazılım dağıtan aktif URL havuzu.
   - *ThreatFox:* Paylaşılan IoC ve tehdit göstergeleri.
   - *MalwareBazaar:* Güncel zararlı dosya hash (SHA256/MD5) değerleri.
   - *Feodo Tracker:* Botnet C2 (Command & Control) IP adresleri.
   - *SSLBL:* Kötü amaçlı SSL sertifikaları ve IP eşleşmeleri.
4. **Spamhaus Project:**
   - *DROP & EDROP:* Siber suçlular tarafından suiistimal edilen IP blokları.
   - *DBL (Domain Block List):* Zararlı ve spam domain havuzu.
5. **PhishTank & OpenPhish:** Doğrulanmış oltalama (phishing) URL ve site veritabanı.
6. **Emerging Threats & FireHOL:** Kompromize edilmiş, saldırı amaçlı kullanılan IP blok setleri (Level 1).
7. **Blocklist.de, DShield & CINSSCORE:** Saldırı raporlayan küresel honeypot ve güvenlik sensörü verileri.
8. **Binary Defense & IPsum:** Çoklu kaynak tabanlı kötü amaçlı IP derecelendirme listeleri.
9. **Tor Project:** Anonimleştirme ve saldırı çıkış düğümü (Exit Node) IP listeleri.

---

<a name="english"></a>
## 🇬🇧 English

### Corporate Overview
**SOC-feeds** is an automated Threat Intelligence collection and aggregation engine architected to empower Security Operations Centers (SOCs), SIEM solutions, and enterprise perimeter defenses. The system autonomously aggregates, sanitizes, deduplicates, and continuously updates malicious IP addresses, domains, URLs, and file hashes hourly from globally recognized, open-source, and official threat feeds.

### Integration & Use Cases
* **Next-Generation Firewalls (NGFW):** External Dynamic Lists (EDL) for automated IP/Domain blocking on Palo Alto, Fortinet, Check Point, and Cisco platforms.
* **SIEM & SOAR Platforms:** Log correlation and threat hunting integration for Wazuh, Zabbix, Splunk, Elastic Stack, and Microsoft Sentinel.
* **Email Security Gateways (SEG):** Real-time phishing URL and malicious domain detection.

### Intelligence Sources
Aggregates high-fidelity data from the following official and global sources:
1. **USOM URL List:** National Cyber Incident Response Center of Türkiye malicious URL feed.
2. **CISA KEV:** Known Exploited Vulnerabilities Catalog.
3. **Abuse.ch Suite:**
   - *URLHaus:* Active malware distribution URLs.
   - *ThreatFox:* Shared indicators of compromise (IoCs).
   - *MalwareBazaar:* Recent malware file hashes (SHA256/MD5).
   - *Feodo Tracker:* Botnet Command & Control (C2) IP blocklists.
   - *SSLBL:* Malicious SSL certificates and associated IPs.
4. **Spamhaus Project:**
   - *DROP & EDROP:* Cybercriminal-operated IP networks.
   - *DBL (Domain Block List):* Malicious domain repository.
5. **PhishTank & OpenPhish:** Verified global phishing URL repositories.
6. **Emerging Threats & FireHOL:** Aggregated compromised IP blocklists (Level 1).
7. **Blocklist.de, DShield & CINSSCORE:** Global honeypot and attack sensor threat telemetry.
8. **Binary Defense & IPsum:** Multi-source reputation-based malicious IP rankings.
9. **Tor Project:** Active anonymous network Exit Node IP directories.

---

<a name="deutsch"></a>
## 🇩🇪 Deutsch

### Unternehmensübersicht
**SOC-feeds** ist eine automatisierte Threat-Intelligence-Sammelengine zur Unterstützung von Security Operations Centern (SOC), SIEM-Lösungen und Perimetersicherheitsarchitekturen.

**Integration:** Next-Gen Firewalls (Palo Alto, Fortinet), SIEM (Wazuh, Splunk, Elastic) und E-Mail-Gateways.  
**Datenquellen:** USOM, CISA KEV, Abuse.ch (URLHaus, ThreatFox, MalwareBazaar, Feodo, SSLBL), Spamhaus (DROP, DBL), PhishTank, OpenPhish, Tor Exit Nodes, FireHOL, DShield und weitere globale Feeds.

---

<a name="français"></a>
## 🇫🇷 Français

### Aperçu Professionnel
**SOC-feeds** est un moteur automatisé de collecte de Cyberveille conçu pour renforcer les SOC, les solutions SIEM et la sécurité périmétrique.

**Intégration:** Pare-feu nouvelle génération (Palo Alto, Fortinet), SIEM (Wazuh, Splunk) et passerelles de messagerie.  
**Sources de Données:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield, etc.

---

<a name="español"></a>
## 🇪🇸 Español

### Resumen Corporativo
**SOC-feeds** es un motor automatizado de Inteligencia de Amenazas diseñado para potenciar los SOC, soluciones SIEM y la seguridad perimetral.

**Integración:** Firewalls de nueva generación, plataformas SIEM/SOAR y pasarelas de seguridad.  
**Fuentes de Datos:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield, etc.

---

<a name="italiano"></a>
## 🇮🇹 Italiano
**Panoramica:** Motore automatizzato di Cyber Threat Intelligence per SOC, SIEM e difese perimetriche.  
**Integrazione:** Firewall NGFW, SIEM (Wazuh, Splunk), analisi forense.  
**Fonti:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

<a name="nederlands"></a>
## 🇳🇱 Nederlands
**Overzicht:** Geautomatiseerde Threat Intelligence-engine voor SOC's, SIEM-oplossingen en netwerkbeveiliging.  
**Integratie:** Firewalls (Palo Alto, Fortinet), SIEM-platforms.  
**Bronnen:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

<a name="polski"></a>
## 🇵🇱 Polski
**Przegląd:** Zautomatyzowany silnik Threat Intelligence dla centrów SOC i systemów SIEM.  
**Integracja:** Firewalle nowej generacji, platformy SIEM/SOAR.  
**Źródła:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Exit Nodes, FireHOL, DShield.

---

<a name="svenska"></a>
## 🇸🇪 Svenska
**Översikt:** Automatiserad hotunderrättelsemotor för SOC, SIEM och perimetersäkerhet.  
**Integration:** Brandväggar, SIEM-plattformar.  
**Källor:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

<a name="dansk"></a>
## 🇩🇰 Dansk
**Oversigt:** Automatiseret Threat Intelligence-motor til SOC, SIEM og perimetersikkerhed.  
**Integration:** Firewall-systemer, SIEM-arkitektur.  
**Kilder:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

<a name="suomi"></a>
## 🇫🇮 Suomi
**Yleiskatsaus:** Automaattinen uhkatiedon keruumoottori SOC- ja SIEM-ympäristöihin.  
**Integrointi:** Palomuurit, SIEM-alustat.  
**Lähteet:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

<a name="português"></a>
## 🇵🇹 Português
**Visão Geral:** Motor automatizado de Threat Intelligence para SOCs e soluções SIEM.  
**Integração:** Firewalls de nova geração, plataformas de correlação de logs.  
**Fontes:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

<a name="ελληνικά"></a>
## 🇬🇷 Ελληνικά
**Επισκόπηση:** Αυτοματοποιημένη μηχανή Threat Intelligence για SOC και SIEM.  
**Ενοποίηση:** Firewalls, συστήματα ανίχνευσης απειλών.  
**Πηγές:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

<a name="čeština"></a>
## 🇨🇿 Čeština
**Přehled:** Automatizovaný nástroj Threat Intelligence pro SOC a SIEM řešení.  
**Integrace:** NGFW firewally, SIEM platformy.  
**Zdroje:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

<a name="magyar"></a>
## 🇭🇺 Magyar
**Áttekintés:** Automatikus fenyegetésfelderítési motor SOC és SIEM rendszerekhez.  
**Integráció:** Tűzfalak, SIEM platformok.  
**Források:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

<a name="română"></a>
## 🇷🇴 Română
**Prezentare:** Motor automatizat de Threat Intelligence pentru SOC și SIEM.  
**Integrare:** Firewall-uri, platforme de securitate.  
**Surse:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

<a name="български"></a>
## 🇧🇬 Български
**Преглед:** Автоматизирана система за разузнаване на заплахи за SOC и SIEM.  
**Интеграция:** Мрежови защитни стени, SIEM платформи.  
**Източници:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

<a name="slovenčina"></a>
## 🇸🇰 Slovenčina
**Prehľad:** Automatizovaný nástroj Threat Intelligence pre SOC a SIEM.  
**Integracja:** Firewally, SIEM systémy.  
**Zdroje:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

<a name="hrvatski"></a>
## 🇭🇷 Hrvatski
**Pregled:** Automatizirani sustav Threat Intelligence za SOC i SIEM rješenja.  
**Integracija:** Vatrozidni sustavi (Firewalls), SIEM.  
**Izvori:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

<a name="slovenščina"></a>
## 🇸🇮 Slovenščina
**Pregled:** Avtomatiziran sistem Threat Intelligence za SOC in SIEM.  
**Integracija:** Požarni zidovi, varnostne platforme.  
**Viri:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

<a name="lietuvių"></a>
## 🇱🇹 Lietuvių
**Apžvalga:** Automatinis grėsmių žvalgybos įrankis SOC ir SIEM sistemoms.  
**Integracija:** Ugniasienės, SIEM platformos.  
**Šaltiniai:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

<a name="latviešu"></a>
## 🇱🇻 Latviešu
**Pārskats:** Automatizēts draudu izlūkošanas rīks SOC un SIEM.  
**Integrācija:** Ugunsmūri, SIEM platformas.  
**Avoti:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

<a name="eesti"></a>
## 🇪🇪 Eesti
**Ülevaade:** Automatiseeritud ohuveebiluure mootor SOC-i ja SIEM-i jaoks.  
**Integreerimine:** Tulemüürid, SIEM süsteemid.  
**Allikad:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

<a name="gaeilge"></a>
## 🇮🇪 Gaeilge
**Overview:** Automated Threat Intelligence engine for SOC and SIEM solutions.  
**Integration:** Firewalls, SIEM platforms.  
**Sources:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

<a name="malti"></a>
## 🇲🇹 Malti
**Ħarsa Ġenerali:** Magna awtomatizzata ta' Threat Intelligence għal SOC u SIEM.  
**Integrazzjoni:** Firewalls, pjattaformi tas-sigurtà.  
**Sorsi:** USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

### 📂 Output Artifacts Format
The repository automatically maintains four clean, stripped, and deduplicated `.txt` artifacts featuring source attribution comments:
1. `threat_ip.txt` — Malicious IPv4 addresses & CIDRs
2. `threat_domain.txt` — Malicious domains
3. `threat_url.txt` — Full malicious URLs
4. `threat_hash.txt` — Malware SHA256/MD5 hashes

---
*Maintained for enterprise-grade automated threat prevention and security orchestration.*
