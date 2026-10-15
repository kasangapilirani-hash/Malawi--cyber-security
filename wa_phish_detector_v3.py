#!/usr/bin/env python3
"""
Malawi Cyber Security v3 - WhatsApp + Airtel Detector
Patience Kasanga | Lilongwe | 8:22 AM
"""
import re

def check_v3(url_or_msg):
    text = url_or_msg.lower()
    score = 0
    reasons = []

    # --- WHATSAPP SCAMS (NEW IN V3) ---
    if "wa.me" in text or "whatsapp" in text:
        if any(x in text for x in [".tk","free","bonus","50gb","100gb","win"]):
            score += 4
            reasons.append("WhatsApp + free bonus .tk combo = 99% scam in MW")
        if "pin" in text or "password" in text or "send code" in text:
            score += 4
            reasons.append("CRITICAL: Asking for PIN/code on WhatsApp!")
    
    # Forwarded many times trick
    if "forwarded many times" in text or "forwarded" in text:
        if "airtel" in text or "mpamba" in text or "tnm" in text:
            score += 2
            reasons.append("Forwarded Airtel/TNM message - verify with *211#")

    # --- V2 LOGIC (KEEP) ---
    for tld in [".tk",".ml",".ga",".cf",".gq"]:
        if tld in text:
            score += 3
            reasons.append(f"Free domain {tld} - scam")

    if "@" in text and "http" in text:
        score += 3
        reasons.append("@ hides real domain")
    
    if re.search(r"https?://\d+\.\d+\.\d+\.\d+", text):
        score += 3
        reasons.append("IP address not domain")

    for kw in ["airtel-money","mpamba","kyc-update","bonus"]:
        if kw in text and "airtel.com" not in text and "tnm.co.mw" not in text:
            score += 2
            reasons.append(f"Fake '{kw}' domain")

    # Result
    if score >= 4:
        return "🔴 SCAM - DELETE & BLOCK!", reasons, score
    elif score >= 2:
        return "🟡 SUSPICIOUS - Call *211# to verify", reasons, score
    else:
        return "🟢 SAFE", reasons, score

# Test Malawi real scams
print("=== Malawi v3 WhatsApp + Airtel Detector 🇲🇼 ===")
tests = [
    "https://wa.me/265994?text=Send your Airtel Money PIN to get 50GB",
    "Forwarded many times: Airtel Money free K50000 bonus https://airtel-bonus.tk",
    "https://airtel.com.mw/official",
    "wa.me/265888 FREE 100GB DATA airtel-money-malawi.tk"
]

for t in tests:
    res, rs, sc = check_v3(t)
    print(f"\nMSG: {t}\n{res} Score:{sc}")
    for r in rs:
        print(f" - {r}")

print("\n--- Paste WhatsApp message / URL (q to quit) ---")
while True:
    u = input("\n> ").strip()
    if u.lower() in ['q','quit']:
        break
    res, rs, sc = check_v3(u)
    print(f"{res} Score:{sc}")
    for r in rs:
        print(f" - {r}")
