# 🇲🇼 Malawi Cyber Security Toolkit | Termux 2026

**By Pilirani Kasanga - Lilongwe**

All-in-one cyber security toolkit built for Malawi - detect Airtel Money / TNM Mpamba phishing, WhatsApp scams, and track lost phones.

### 🛡️ Tools Included

| Tool | What it does |
|------|--------------|
| `wa_phish_detector_v3.py` | **NEW v3** - Detects WhatsApp & Airtel Money phishing links |
| `phish_detector.py` | General phishing URL detector |
| `chichewa_detector.py` | Detects Chichewa scam messages (Muli bwanji scams) |
| `decode_link.py` | Decodes shortened/hidden malicious links |
| `check_imei.py` | Check if phone IMEI is valid/stolen |
| `gps_locator.py` | GPS location helper |
| `lost_phone_tracker.py` | Track lost phone via link |
| `device_scanner.py` | Scan network devices |
| `fretboard.py` | Bonus - Guitar fretboard trainer |

### 📲 Install in Termux

```bash
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/kasangapilirani-hash/Malawi--cyber-security.git
cd Malawi--cyber-security
python wa_phish_detector_v3.py
