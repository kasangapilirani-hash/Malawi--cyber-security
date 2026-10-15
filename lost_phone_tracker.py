#!/usr/bin/env python3
# 🇲🇼 Malawi Lost Phone Finder - SIM Change Tracker
# Free, works with SMS, no internet needed
# By Patience Kasanga - 2026

import os, json, time, subprocess

CONFIG_FILE = "my_tracker_config.json"

def run_cmd(cmd):
    try: return subprocess.check_output(cmd, shell=True, text=True).strip()
    except: return ""

def setup():
    print("🇲🇼 Malawi Lost Phone Finder - SETUP")
    print("This will protect your phone if stolen.\n")
    trusted = input("Enter trusted number to alert (e.g. brother's Airtel): +265").strip()
    if not trusted.startswith("+"): trusted = "+265" + trusted
    name = input("Your name: ").strip()
    
    config = {"trusted_number": trusted, "owner_name": name, "original_sim": run_cmd("termux-telephony-deviceinfo | grep subscriberId")}
    with open(CONFIG_FILE, "w") as f: json.dump(config, f)
    print(f"\n✅ Saved! If SIM changes, SMS will go to {trusted}")
    print("\nTo work you NEED:")
    print("1. Install Termux:API app from F-Droid")
    print("2. Run: pkg install termux-api")
    print(f"3. Run: python lost_phone_tracker.py --start")
    return config

def get_location():
    loc = run_cmd("termux-location --provider gps --request once")
    try:
        import json as js
        data = js.loads(loc)
        lat = data['latitude']; lon = data['longitude']
        return f"https://maps.google.com/?q={lat},{lon}"
    except:
        return "Location unavailable (turn on GPS)"

def send_alert(trusted, msg):
    # Uses free SMS via your own SIM
    cmd = f'termux-sms-send -n {trusted} "{msg}"'
    run_cmd(cmd)
    print(f"📤 ALERT SENT to {trusted}: {msg}")

def monitor():
    if not os.path.exists(CONFIG_FILE):
        print("Run setup first: python lost_phone_tracker.py --setup")
        return
    with open(CONFIG_FILE) as f: cfg = json.load(f)
    trusted = cfg['trusted_number']
    print(f"🔒 Monitoring... Trusted: {trusted} (Ctrl+C to stop)")
    print("If SIM changes, I will send SMS with location.")
    
    last_sim = run_cmd("termux-telephony-deviceinfo")
    while True:
        current = run_cmd("termux-telephony-deviceinfo")
        if current and current != last_sim and "subscriberId" in current:
            loc = get_location()
            imei = run_cmd("termux-telephony-deviceinfo | grep deviceId")
            msg = f"🚨 FONI YABEDWA! {cfg['owner_name']} phone SIM changed! Loc: {loc} {imei} Help!"
            send_alert(trusted, msg)
            last_sim = current
        time.sleep(30)  # check every 30 sec

if __name__ == "__main__":
    import sys
    if "--setup" in sys.argv: setup()
    elif "--start" in sys.argv: monitor()
    else:
        print("Usage:\n  python lost_phone_tracker.py --setup  (first time)\n  python lost_phone_tracker.py --start  (start protection)")
