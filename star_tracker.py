# -*- coding: utf-8 -*-
import time
from skyfield.api import Topos, load

planets = load('de421.bsp')
earth = planets['earth']
jupiter = planets['jupiter barycenter']

ts = load.timescale()
YourLocation = earth + Topos('LATITUDE', 'LONGITUDE')

def calculate_target():
    t = ts.now()
    astrometric = YourLocation.at(t).observe(jupiter)
    alt, az, distance = astrometric.apparent().altaz()
    return alt.degrees, az.degrees

print("--- Star Tracker Otomasyonu Baslatildi ---")
print("Hedef: Jupiter | Konum: Your Location")
print("Sistem her 60 saniyede bir konumu hesaplayacak.\n")

try:
    while True:
        altitude, azimuth = calculate_target()

        if altitude < 0:
            print(f"[{time.strftime('%H:%M:%S')}] Jupiter su an ufkun altinda (Batmis). Alt: {altitude:.2f}, Az: {azimuth:.2f}")
        else:
            print(f"[{time.strftime('%H:%M:%S')}] [PC -> Arduino] HEDEF - Yukari: {altitude:.2f}, Saga: {azimuth:.2f}")

        time.sleep(60)

except KeyboardInterrupt:
    print("\nSistem manuel olarak durduruldu.")
