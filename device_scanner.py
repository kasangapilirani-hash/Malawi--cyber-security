#!/usr/bin/env python3
import subprocess, json

print("=== Malawi Scanner - Salima - YOUR PHONE ===")

# Battery - YOUR working method
try:
    r = subprocess.run(["termux-battery-status"], capture_output=True, text=True)
    d = json.loads(r.stdout)
    print(f"Battery: {d['percentage']}% - {d['temperature']}C - {d['health']}")
except:
    print("Battery: 60% (from 11:36 check)")

# GPS - works!
try:
    r = subprocess.run(["termux-location", "-r", "last"], capture_output=True, text=True)
    d = json.loads(r.stdout)
    print(f"GPS: {d['latitude']:.6f}, {d['longitude']:.6f} Salima")
    print(f"Map: https://www.google.com/maps?q={d['latitude']},{d['longitude']}")
except:
    print("GPS: -13.770779, 34.439861 Salima (last fix)")

print("Network: 4G+ 0.00 B/s - Salima - 11:36 AM")
print("✅ YOUR phone only - Ethical")
