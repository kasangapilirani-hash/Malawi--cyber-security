#!/usr/bin/env python3
# 🇲🇼 Malawi Chichewa Phishing Detector v3 - WORLD FIRST
# By Patience Kasanga - Lilongwe, 2026
# Detects Airtel Money / TNM Mpamba / ESCOM scams in Chichewa

import re

def detect(text):
    low = text.lower()
    score = 0
    reasons = []

    # 1. REAL messages whitelist - instantly SAFE
    if "kuchokera kwa" in low or "transaction id" in low or "tid:" in low:
        return 0, "🟢 SAFE - Ndi yowona (Real Airtel Money received)", ["Contains 'kuchokera kwa' - real receipt"]
    if "balance yanu" in low and "mwapambana" not in low:
        return 0, "🟢 SAFE - Balance check", ["Real balance message"]

    # 2. Scam dictionary - Chichewa core
    scams = {
        "mwapambana": 5, "mwajambula": 5, "mwasankhidwa": 5,
        "tumizani": 5, "tumidzeni": 5, "lowetsani pin": 6,
        "kuti mulandire": 3, "dinani ulalo": 4
    }
    for w, pts in scams.items():
        if w in low:
            score += pts
            reasons.append(f"Chichewa: '{w}' (+{pts})")

    # 3. Suspicious patterns
    if re.search(r"bit\.ly|tinyurl|t\.me/", low): 
        score+=4; reasons.append("Shortened scam link")
    if re.search(r"https?://", low) and ("pin" in low or "mwapambana" in low):
        score+=4; reasons.append("Link + PIN request")
    if "k500" in low and "k100,000" in low:
        score+=3; reasons.append("Classic advance fee: send small to get big")

    # 4. Verdict
    if score >= 7: v = "🔴 SCAM - MUSACHITE! Ndi chinyengo!"
    elif score >= 4: v = "🟡 ZOKAYIKITSA - Samalani, funsani kaye!"
    else: v = "🟢 SAFE - Zikuwoneka bwino"
    
    return score, v, reasons

if __name__ == "__main__":
    print("🇲🇼 Chichewa Detector v3 FINAL - Test\n")
    tests = [
        ("Moni, Airtel Money yanu yalowa K20,000 kuchokera kwa John", "SAFE"),
        ("ESCOM: Bill yanu ndi K15,000. Lipirani pa *211#", "SAFE"),
        ("Mwapambana K100,000 TNM Mpamba! Tumizani K500 kuti mulandire ndalama", "SCAM"),
        ("Mwapambana! Dinani bit.ly/malawi2026 kuti mulowetse PIN", "SCAM"),
    ]
    for sms, expected in tests:
        s,v,r = detect(sms)
        print(f"SMS: {sms}\n=> {v} Score {s} Expected {expected}\n")
    
    print("--- Paste your own SMS (Ctrl+C to exit) ---")
    while True:
        try:
            txt = input("\nPaste SMS > ")
            if not txt.strip(): continue
            s,v,r = detect(txt)
            print(f"\n{v} (Score {s})")
            for x in r: print(f" - {x}")
        except: break
