#!/usr/bin/env python3
import re

SCAM = ["airtel-money","airtelmoney","mpamba","bonus","free-data","kyc-update"]
BAD_TLD = [".tk",".ml",".ga",".cf",".gq"]

def check(url):
    u=url.lower(); s=0; r=[]
    for t in BAD_TLD:
        if t in u: s+=3; r.append(f"Free domain {t} - 90% scam in MW")
    for k in SCAM:
        if k in u and "airtel.com" not in u and "tnm.co.mw" not in u: s+=2; r.append(f"Keyword '{k}' fake domain")
    if "@" in u: s+=3; r.append("@ hides real domain")
    if u.count(".")>3: s+=1; r.append("Too many dots - spoof")
    if re.match(r"https?://\d+\.\d+",u): s+=3; r.append("IP not domain")
    if ("airtel" in u or "mpamba" in u) and u.startswith("http://"): s+=2; r.append("Money site no HTTPS")
    if s>=3: return "🔴 SCAM - DO NOT CLICK",r,s
    if s>=1: return "🟡 SUSPICIOUS",r,s
    return "🟢 SAFE",r,s

tests=["https://airtel-money-malawi.tk/bonus","http://192.168.1.1/airtel/login","https://airtel.com.mw","https://airtel.mw-bonus.com@scam.tk"]
print("=== Malawi Phishing v2 🇲🇼 ===")
for url in tests:
    res,rs,sc=check(url)
    print(f"\n{url}\n{res} Score:{sc}")
    for x in rs: print(f" - {x}")

print("\n--- Enter URL (q to quit) ---")
while True:
    u=input("URL> ").strip()
    if u in ['q','quit']: break
    res,rs,sc=check(u)
    print(f"{res} Score:{sc}")
    for x in rs: print(f" - {x}")
