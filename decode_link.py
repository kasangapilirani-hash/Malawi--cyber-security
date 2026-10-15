import base64, urllib.parse

link = input("Paste suspicious link: ").strip()

print("\n--- DECODING ---\n")

# 1. URL decode ( %20 -> space )
decoded_url = urllib.parse.unquote(link)
if decoded_url != link:
    print(f"🔍 URL Decoded:\n{decoded_url}\n")

# 2. Base64 decode (try)
try:
    # Add padding if missing
    padded = link.split('/')[-1] + '===' 
    b64 = base64.b64decode(padded).decode()
    print(f"🔓 Base64 Decoded:\n{b64}\n")
except:
    pass

# 3. Check tricks
if '-' in link or '@' in link:
    print("⚠️  Trick: Real sites like airtel.mw NEVER have '-' or '@' in the middle")
if link.count('.') > 3:
    print("⚠️  Trick: Too many dots = fake subdomain")
if 'airtel' in link.lower() and 'airtel.mw' not in link.lower():
    print("🔴 FAKE AIRTEL! Real is only airtel.mw")

print("\nSafe check: Copy real domain only and search Google")
