# SOC-FEEDS: Real-Time Open-Source Threat Intelligence & IoC Aggregator

<div align="center">
  <a href="#tr">Türkçe</a> | <a href="#en">English</a> | <a href="#de">Deutsch</a> | <a href="#fr">Français</a> | <a href="#es">Español</a> | <a href="#it">Italiano</a> | <a href="#nl">Nederlands</a> | <a href="#pl">Polski</a> | <a href="#sv">Svenska</a> | <a href="#da">Dansk</a> | <a href="#fi">Suomi</a> | <a href="#pt">Português</a> | <a href="#el">Ελληνικά</a> | <a href="#cs">Čeština</a> | <a href="#hu">Magyar</a> | <a href="#ro">Română</a> | <a href="#bg">Български</a> | <a href="#sk">Slovenčina</a> | <a href="#hr">Hrvatski</a> | <a href="#sl">Slovenščina</a> | <a href="#lt">Lietuvių</a> | <a href="#lv">Latviešu</a> | <a href="#ee">Eesti</a> | <a href="#ga">Gaeilge</a> | <a href="#mt">Malti</a>
  <br><br>
  <button onclick="copyReadme()" style="background:#2563eb; color:white; border:none; padding:8px 16px; border-radius:6px; cursor:pointer; font-weight:600;">README'yi Kopyala / Copy README</button>
</div>

---

## <a id="tr"></a>🇹🇷 Türkçe

### 📌 Kurumsal Genel Bakış
SOC-feeds, kritik ağ altyapılarını, Güvenlik Operasyon Merkezlerini (SOC) ve kurumsal çevre güvenliğini korumak amacıyla tasarlanmış otomatik bir Tehdit İstihbaratı (Threat Intelligence) toplama ve derleme motorudur. Sistem; dünya çapındaki güvenilir, açık kaynaklı ve resmi istihbarat kaynaklarından zararlı IP adreslerini, etki alanlarını (domain), URL'leri ve zararlı yazılım hash değerlerini saatlik periyotlarla derler, temizler, mükerrer kayıtları ayıklar ve güncel tutar.

### 📊 Anlık Veri & Güncellik İstatistikleri
* **Son Güncelleme (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **Tehdit Altındaki IP (threat_ip.txt)**: `0` kayıt
* **Zararlı Domain (threat_domain.txt)**: `0` kayıt
* **Zararlı URL (threat_url.txt)**: `0` kayıt
* **Zararlı Yazılım Hash (threat_hash.txt)**: `0` kayıt

### 🔌 Entegrasyon ve Kullanım Alanları
* **Güvenlik Duvarları (Next-Gen Firewalls)**: Palo Alto, Fortinet, Check Point, Cisco ASA/FTD sistemlerinde IP ve Domain bazlı otomatik bloklama (External Dynamic Lists).
* **SIEM & SOAR Platformları**: Wazuh, Zabbix, Splunk, Elastic Stack, Microsoft Sentinel üzerinde log korelasyonu ve tehdit avcılığı (Threat Hunting).
* **E-Posta Güvenlik Ağ Geçitleri (SEG)**: Phishing ve zararlı URL/domain tespiti.

### 🔗 Veri Kaynakları (Threat Intelligence Feeds)
Sistem aşağıdaki resmi ve küresel güvenlik kaynaklarından anlık veri çekmektedir:
* **USOM URL List**: Türkiye Ulusal Siber Olaylara Müdahale Merkezi zararlı bağlantı listesi.
* **CISA KEV**: Bilinen ve aktif olarak istismar edilen zaafiyet katalogları.
* **Abuse.ch Ecosystem**: URLHaus, ThreatFox, MalwareBazaar, Feodo Tracker, SSLBL.
* **Spamhaus Project**: DROP & EDROP, DBL (Domain Block List).
* **PhishTank & OpenPhish**: Doğrulanmış oltalama (phishing) URL ve site veritabanı.
* **Emerging Threats & FireHOL**: Kompromize edilmiş, saldırı amaçlı kullanılan IP blok setleri (Level 1).
* **Blocklist.de, DShield & CINSSCORE**: Küresel honeypot ve güvenlik sensörü verileri.
* **Binary Defense & IPsum**: Çoklu kaynak tabanlı kötü amaçlı IP derecelendirme listeleri.
* **Tor Project**: Anonimleştirme ve saldırı çıkış düğümü (Exit Node) IP listeleri.

---

## <a id="en"></a>🇬🇧 English

### 📌 Corporate Overview
SOC-feeds is an automated Threat Intelligence collection and aggregation engine architected to empower Security Operations Centers (SOCs), SIEM solutions, and enterprise perimeter defenses. The system autonomously aggregates, sanitizes, deduplicates, and continuously updates malicious IP addresses, domains, URLs, and file hashes hourly from globally recognized, open-source, and official threat feeds.

### 📊 Live Feed & Update Statistics
* **Last Updated (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **Threat IPs (threat_ip.txt)**: `0` entries
* **Malicious Domains (threat_domain.txt)**: `0` entries
* **Malicious URLs (threat_url.txt)**: `0` entries
* **Malware Hashes (threat_hash.txt)**: `0` entries

### 🔌 Integration & Use Cases
* **Next-Generation Firewalls (NGFW)**: External Dynamic Lists (EDL) for automated IP/Domain blocking on Palo Alto, Fortinet, Check Point, and Cisco platforms.
* **SIEM & SOAR Platforms**: Log correlation and threat hunting integration for Wazuh, Zabbix, Splunk, Elastic Stack, and Microsoft Sentinel.
* **Email Security Gateways (SEG)**: Real-time phishing URL and malicious domain detection.

### 🔗 Intelligence Sources
* USOM URL List, CISA KEV, Abuse.ch Suite (URLHaus, ThreatFox, MalwareBazaar, Feodo, SSLBL), Spamhaus (DROP, DBL), PhishTank, OpenPhish, Emerging Threats, FireHOL, Blocklist.de, DShield, CINSSCORE, Binary Defense, IPsum, and Tor Project.

---

## <a id="de"></a>🇩🇪 Deutsch

### 📌 Unternehmensübersicht
SOC-feeds ist eine automatisierte Threat-Intelligence-Sammelengine zur Unterstützung von Security Operations Centern (SOC), SIEM-Lösungen und Perimetersicherheitsarchitekturen.

### 📊 Live-Feed-Statistiken
* **Letzte Aktualisierung (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **Bedrohungs-IPs**: `0` | **Domains**: `0` | **URLs**: `0` | **Hashes**: `0`

### 🔌 Integration & Anwendungsfälle
* **Next-Gen Firewalls**: External Dynamic Lists für Palo Alto, Fortinet und Cisco.
* **SIEM & SOAR**: Log-Korrelation und Bedrohungsjagd für Wazuh, Splunk und Microsoft Sentinel.

### 🔗 Datenquellen
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Exit Nodes, FireHOL, DShield.

---

## <a id="fr"></a>🇫🇷 Français

### 📌 Aperçu Professionnel
SOC-feeds est un moteur automatisé de collecte de Cyberveille conçu pour renforcer les SOC, les solutions SIEM et la sécurité périmétrique.

### 📊 Statistiques en Direct
* **Dernière mise à jour (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **IPs de menaces**: `0` | **Domaines**: `0` | **URLs**: `0` | **Hashes**: `0`

### 🔌 Intégration & Cas d'Utilisation
* **Pare-feu nouvelle génération**: Listes dynamiques pour Palo Alto, Fortinet, Check Point.
* **SIEM & SOAR**: Corrélation de journaux et recherche de menaces (Wazuh, Splunk).

### 🔗 Sources de Données
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="es"></a>🇪🇸 Español

### 📌 Resumen Corporativo
SOC-feeds es un motor automatizado de Inteligencia de Amenazas diseñado para potenciar los SOC, soluciones SIEM y la seguridad perimetral.

### 📊 Estadísticas en Vivo
* **Última actualización (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **IPs de Amenaza**: `0` | **Dominios**: `0` | **URLs**: `0` | **Hashes**: `0`

### 🔌 Integración y Casos de Uso
* **Firewalls de nueva generación**: Listas dinámicas externas para bloqueo automatizado.
* **Plataformas SIEM/SOAR**: Integración para correlación de registros y búsqueda de amenazas.

### 🔗 Fuentes de Datos
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="it"></a>🇮🇹 Italiano

### 📌 Panoramica Aziendale
SOC-feeds è un motore automatizzato di Cyber Threat Intelligence per SOC, soluzioni SIEM e difese perimetriche aziendali.

### 📊 Statistiche in Tempo Reale
* **Ultimo aggiornamento (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **IP di Minaccia**: `0` | **Domain**: `0` | **URL**: `0` | **Hash**: `0`

### 🔌 Integrazione e Casi d'Uso
* **Firewall NGFW**: Liste dinamiche esterne per il blocco automatizzato su Palo Alto, Fortinet e Cisco.
* **SIEM & SOAR**: Correlazione dei log e Threat Hunting (Wazuh, Splunk, Elastic).

### 🔗 Fonti di Intelligence
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="nl"></a>🇳🇱 Nederlands

### 📌 Bedrijfsoverzicht
SOC-feeds is een geautomatiseerde Threat Intelligence-engine voor SOC's, SIEM-oplossingen en netwerkbeveiliging.

### 📊 Live Statistieken
* **Laatste update (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **Bedreigings-IP's**: `0` | **Domeinen**: `0` | **URL's**: `0` | **Hashes**: `0`

### 🔌 Integratie & Toepassingen
* **Next-Gen Firewalls**: External Dynamic Lists voor geautomatiseerde blokkering.
* **SIEM & SOAR**: Logkorrelatie en threat hunting voor Wazuh en Splunk.

### 🔗 Bronnen
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="pl"></a>🇵🇱 Polski

### 📌 Przegląd Korporacyjny
SOC-feeds to zautomatyzowany silnik Threat Intelligence dla centrów SOC, systemów SIEM i ochrony peryferyjnej.

### 📊 Statystyki na Żywo
* **Ostatnia aktualizacja (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **Zagrożone IP**: `0` | **Domeny**: `0` | **URL**: `0` | **Hashe**: `0`

### 🔌 Integracja i Zastosowania
* **Firewalle Nowej Generacji**: Listy dynamiczne do automatycznego blokowania.
* **SIEM & SOAR**: Korelacja logów i wyszukiwanie zagrożeń.

### 🔗 Źródła Danych
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="sv"></a>🇸🇪 Svenska

### 📌 Företagsöversikt
SOC-feeds är en automatiserad hotunderrättelsemotor för SOC, SIEM-lösningar och perimetersäkerhet.

### 📊 Live-statistik
* **Senast uppdaterad (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **Hot-IP**: `0` | **Domäner**: `0` | **URL:er**: `0` | **Hashar**: `0`

### 🔌 Integration & Användningsfall
* **Brandväggar (NGFW)**: Externa dynamiska listor för automatisk blockering.
* **SIEM & SOAR**: Loggkorrelation och hotjakt.

### 🔗 Källor
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="da"></a>🇩🇰 Dansk

### 📌 Virksomhedsoversigt
SOC-feeds er en automatiseret Threat Intelligence-motor til SOC, SIEM-løsninger og perimetersikkerhed.

### 📊 Live Statistik
* **Sidst opdateret (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **Trussels-IP'er**: `0` | **Domæner**: `0` | **URL'er**: `0` | **Hashes**: `0`

### 🔌 Integration & Anvendelse
* **Firewalls (NGFW)**: Eksterne dynamiske lister til automatisk blokering.
* **SIEM & SOAR**: Logkorrelation og trusselsjagt.

### 🔗 Kilder
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="fi"></a>🇫🇮 Suomi

### 📌 Yleiskatsaus
SOC-feeds on automaattinen uhkatiedon keruumoottori SOC-keskuksille, SIEM-ratkaisuille ja verkkoturvallisuudelle.

### 📊 Reaaliaikaiset Tilastot
* **Viimeksi päivitetty (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **Uhkatoiminnot IP**: `0` | **Verkkotunnukset**: `0` | **URL:t**: `0` | **Hashit**: `0`

### 🔌 Integrointi & Käyttötapaukset
* **Palomuurit**: Ulkoiset dynaamiset listat automatisoituun estämiseen.
* **SIEM & SOAR**: Lokikorrelaatio ja uhkien metsästys.

### 🔗 Lähteet
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="pt"></a>🇵🇹 Português

### 📌 Visão Geral Corporativa
SOC-feeds é um motor automatizado de Threat Intelligence para SOCs, soluções SIEM e defesas perimétricas.

### 📊 Estatísticas ao Vivo
* **Última atualização (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **IPs de Ameaça**: `0` | **Domínios**: `0` | **URLs**: `0` | **Hashes**: `0`

### 🔌 Integração e Casos de Uso
* **Firewalls de Nova Geração**: Listas dinâmicas para bloqueio automatizado.
* **SIEM & SOAR**: Correlação de logs e caça a ameaças.

### 🔗 Fontes de Dados
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="el"></a>🇬🇷 Ελληνικά

### 📌 Επισκόπηση
Το SOC-feeds είναι μια αυτοματοποιημένη μηχανή Threat Intelligence για SOC, λύσεις SIEM και ασφάλεια περιμέτρου.

### 📊 Στατιστικά σε Πραγματικό Χρόνο
* **Τελευταία Ενημέρωση (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **IP Απειλών**: `0` | **Domain**: `0` | **URL**: `0` | **Hashes**: `0`

### 🔌 Ενοποίηση & Χρήση
* **Firewalls Νέας Gen**: Εξωτερικές δυναμικές λίστες για αυτόματο αποκλεισμό.
* **SIEM & SOAR**: Συσχετισμός log και Threat Hunting.

### 🔗 Πηγές
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="cs"></a>🇨🇿 Čeština

### 📌 Přehled
SOC-feeds je automatizovaný nástroj Threat Intelligence pro SOC, SIEM řešení a perimetrovou bezpečnost.

### 📊 Živé Statistiky
* **Poslední aktualizace (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **Hrozby IP**: `0` | **Domény**: `0` | **URL**: `0` | **Hashe**: `0`

### 🔌 Integrace a Použití
* **NGFW Firewally**: Externí dynamické seznamy pro automatické blokování.
* **SIEM & SOAR**: Korelace logů a threat hunting.

### 🔗 Zdroje
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="hu"></a>🇭🇺 Magyar

### 📌 Áttekintés
A SOC-feeds egy automatizált fenyegetésfelderítési motor SOC-k, SIEM megoldások és peremhálózati védelem számára.

### 📊 Élő Statisztikák
* **Utolsó frissítés (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **Fenyegető IP-k**: `0` | **Domainek**: `0` | **URL-ek**: `0` | **Hashek**: `0`

### 🔌 Integráció és Használat
* **Tűzfalak**: Külső dinamikus listák az automatikus blokkoláshoz.
* **SIEM & SOAR**: Naplókorreláció és veszélykutatás.

### 🔗 Források
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="ro"></a>🇷🇴 Română

### 📌 Prezentare generală
SOC-feeds este un motor automatizat de Threat Intelligence pentru SOC, soluții SIEM și securitate perimetrică.

### 📊 Statistici Live
* **Ultima actualizare (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **IP-uri Amenințare**: `0` | **Domenii**: `0` | **URL-uri**: `0` | **Hash-uri**: `0`

### 🔌 Integrare și Utilizare
* **Firewall-uri NGFW**: Liste dinamice externe pentru blocare automată.
* **SIEM & SOAR**: Corelarea jurnalelor și vânătoarea de amenințări.

### 🔗 Surse de Date
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="bg"></a>🇧🇬 Български

### 📌 Преглед
SOC-feeds е автоматизирана система за разузнаване на заплахи за SOC, SIEM решения и мecждова защита.

### 📊 Статистики на Живо
* **Последна актуализация (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **IP адреси**: `0` | **Домейни**: `0` | **URL**: `0` | **Hashes**: `0`

### 🔌 Интеграция и Употреба
* **Мрежови защитни стени**: Динамични списъци за автоматично блокиране.
* **SIEM & SOAR**: Корелация на логове и откриване на заплахи.

### 🔗 Източници
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="sk"></a>🇸🇰 Slovenčina

### 📌 Prehľad
SOC-feeds je automatizovaný nástroj Threat Intelligence pre SOC, SIEM riešenia a ochranu obvodu siete.

### 📊 Živé Štatistiky
* **Posledná aktualizácia (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **Hrozby IP**: `0` | **Domény**: `0` | **URL**: `0` | **Hashes**: `0`

### 🔌 Integrácia a Použitie
* **Firewally**: Externé dynamické zoznamy na automatické blokovanie.
* **SIEM & SOAR**: Korelácia logov a vyhľadávanie hrozieb.

### 🔗 Zdroje
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="hr"></a>🇭🇷 Hrvatski

### 📌 Pregled
SOC-feeds je automatizirani sustav Threat Intelligence za SOC, SIEM rješenja i zaštitu perimetra.

### 📊 Statistika Uživo
* **Zadnje ažuriranje (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **IP adrese**: `0` | **Domene**: `0` | **URL-ovi**: `0` | **Hashevi**: `0`

### 🔌 Integracija i Primjena
* **Vatrozidi**: Vanjske dinamičke liste za automatsko blokiranje.
* **SIEM & SOAR**: Korelacija logova i lov na prijetnje.

### 🔗 Izvori
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="sl"></a>🇸🇮 Slovenščina

### 📌 Pregled
SOC-feeds je avtomatiziran sistem Threat Intelligence za SOC, SIEM rešitve in obrobno varnost.

### 📊 Statistika v Živo
* **Zadnja posodobitev (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **IP naslovi**: `0` | **Domene**: `0` | **URL-ji**: `0` | **Hashes**: `0`

### 🔌 Integracija in Uporaba
* **Požarni zidovi**: Zunanje dinamične seznami za samodejno blokiranje.
* **SIEM & SOAR**: Korelacija dnevnikov in iskanje groženj.

### 🔗 Viri
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="lt"></a>🇱🇹 Lietuvių

### 📌 Apžvalga
SOC-feeds yra automatinis grėsmių žvalgybos įrankis SOC, SIEM sistemoms ir perimetro apsaugai.

### 📊 Tiesioginė Statistika
* **Paskutinis atnaujinimas (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **Grėsmių IP**: `0` | **Domenai**: `0` | **URL**: `0` | **Hashes**: `0`

### 🔌 Integracija ir Naudojimas
* **Ugniasienės**: Išoriniai dinaminiai sąrašai automatiniam blokavimui.
* **SIEM & SOAR**: Žurnalų koreliacija ir grėsmių paieška.

### 🔗 Šaltiniai
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="lv"></a>🇱🇻 Latviešu

### 📌 Pārskats
SOC-feeds ir automatizēts draudu izlūkošanas rīks SOC, SIEM risinājumiem un perimetra drošībai.

### 📊 Tiešraides Statistikas
* **Pēdējā atjaunināšana (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **Draudu IP**: `0` | **Domēni**: `0` | **URL**: `0` | **Hashes**: `0`

### 🔌 Integrācija un Lietošana
* **Ugunsmūri**: Ārējie dinamiskie saraksti automātiskai bloķēšanai.
* **SIEM & SOAR**: Žurnālu korelācija un draudu medības.

### 🔗 Avoti
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="ee"></a>🇪🇪 Eesti

### 📌 Ülevaade
SOC-feeds on automatiseeritud ohuveebiluure mootor SOC-i, SIEM-i ja perimeetri turvalisuse jaoks.

### 📊 Reaalajas Statistika
* **Viimati uuendatud (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **Ohu IP-d**: `0` | **Domeenid**: `0` | **URL-id**: `0` | **Hashes**: `0`

### 🔌 Integreerimine ja Kasutamine
* **Tulemüürid**: Välised dünaamilised loendid automaatseks blokeerimiseks.
* **SIEM & SOAR**: Logide korrelatsioon ja ohtude jaht.

### 🔗 Allikad
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="ga"></a>🇮🇪 Gaeilge

### 📌 Forbhreathnú
Is inneall uathoibríoch Threat Intelligence é SOC-feeds le haghaidh SOCanna, réitigh SIEM, agus cosaint imlíne.

### 📊 Staitisticí Beo
* **Nuashonraithe Deireanach (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **IPanna Bagartha**: `0` | **Fearainneacha**: `0` | **URLanna**: `0` | **Hashes**: `0`

### 🔌 Comhtháthú & Úsáid
* **Ballaí Dóiteáin**: Liostaí dinimiciúla seachtracha le haghaidh blocála uathoibríoch.
* **SIEM & SOAR**: Comhghaolú logaí agus seilg bagairtí.

### 🔗 Foinsí
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## <a id="mt"></a>🇲🇹 Malti

### 📌 Ħarsa Ġenerali
SOC-feeds hija magna awtomatizzata ta' Threat Intelligence għal SOCs, soluzzjonijiet SIEM, u sigurtà perimetrali.

### 📊 Statistika Live
* **L-aħħar aġġornament (UTC)**: `YYYY-MM-DD HH:MM:SS`
* **IPs tat-Theddid**: `0` | **Oqsma (Domains)**: `0` | **URLs**: `0` | **Hashes**: `0`

### 🔌 Integrazzjoni u Użu
* **Firewalls**: Listi dinamiċi esterni għal imblukkar awtomatiku.
* **SIEM & SOAR**: Korrelazzjoni ta' log u tfittxija ta' theddid.

### 🔗 Sorsi
USOM, CISA KEV, Abuse.ch, Spamhaus, PhishTank, OpenPhish, Tor Project, FireHOL, DShield.

---

## 📂 Output Artifacts Format
The repository automatically maintains four clean, stripped, and deduplicated `.txt` artifacts featuring source attribution comments:
* `threat_ip.txt` — Malicious IPv4 addresses & CIDRs
* `threat_domain.txt` — Malicious domains
* `threat_url.txt` — Full malicious URLs
* `threat_hash.txt` — Malware SHA256/MD5 hashes

---

<script>
function copyReadme() {
    const text = document.body.innerText;
    navigator.clipboard.writeText(text).then(() => {
        alert("README içeriği panoya kopyalandı! / README copied to clipboard!");
    });
}
</script>
