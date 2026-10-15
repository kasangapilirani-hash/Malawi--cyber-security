import json, os, datetime, urllib.parse

DB_FILE = "stolen_phones.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=2)

def report_stolen():
    print("\n--- REPORT STOLEN PHONE ---")
    imei = input("Enter IMEI (dial *#06#): ").strip()
    model = input("Enter phone model: ").strip()
    owner = input("Your name: ").strip()
    date_reported = datetime.datetime.now().strftime("%Y-%m-%d")
    
    db = load_db()
    for e in db:
        if e['imei'] == imei:
            print("Already reported!")
            return
    
    db.append({"imei": imei, "model": model, "owner": owner, "date_reported": date_reported})
    save_db(db)
    print(f"\n✅ Reported IMEI {imei} saved!")
    
    # NEW: Create WhatsApp alert link (replaces CallMeBot)
    msg = f"🚨 STOLEN PHONE REPORTED\nIMEI: {imei}\nModel: {model}\nOwner: {owner}\nDate: {date_reported}\n#BeSafeMalawi"
    link = f"https://wa.me/265998231577?text={urllib.parse.quote(msg)}"
    print(f"\nShare to WhatsApp Business:\n{link}")
    try:
        os.system(f'termux-open "{link}"')
    except:
        pass

def check_phone():
    imei = input("Enter IMEI to check before buying: ").strip()
    db = load_db()
    for entry in db:
        if entry['imei'] == imei:
            print(f"\n🔴 STOP! THIS PHONE IS STOLEN!")
            print(f"Model: {entry['model']}")
            print(f"Reported: {entry['date_reported']} by {entry['owner']}")
            print(f"Do NOT buy. Report seller to police.")
            # Alert link for buyer
            msg = f"⚠️ SOMEONE TRIED TO SELL STOLEN PHONE\nIMEI: {imei}\nModel: {entry['model']}"
            link = f"https://wa.me/265998231577?text={urllib.parse.quote(msg)}"
            print(f"\nAlert admin: {link}")
            try:
                os.system(f'termux-open "{link}"')
            except:
                pass
            return
    print(f"\n🟢 SAFE - IMEI {imei} not in stolen database")
    print("Still check: Ask for receipt, box, and check if SIM works")

if __name__ == "__main__":
    print("1. Report my stolen phone\n2. Check phone before buying")
    c = input("Choose 1 or 2: ").strip()
    if c=="1": report_stolen()
    else: check_phone()
