#!/usr/bin/env python3
import json, subprocess

print("📍 Malawi GPS - OWN PHONE ONLY")
print("Getting YOUR location...")

# Try last location first (instant), then live
for mode in [["termux-location", "-r", "last"], ["termux-location"]]:
    try:
        r = subprocess.run(mode, capture_output=True, text=True, timeout=60)
        data = json.loads(r.stdout)
        if "error" not in data:
            lat = data["latitude"]
            lon = data["longitude"]
            acc = data.get("accuracy",0)
            print(f"\n✅ YOUR LOCATION:")
            print(f"Lat: {lat}")
            print(f"Lon: {lon}")
            print(f"Accuracy: {acc:.1f}m")
            print(f"\n🗺️ https://www.google.com/maps?q={lat},{lon}")
            break
    except Exception as e:
        print(f"Trying... {e}")
        continue
else:
    print("❌ No GPS. Run: termux-location")
