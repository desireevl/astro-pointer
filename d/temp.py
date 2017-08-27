from skyfield.api import Topos, load
import time

lat = '27.469771 S'
lon = '153.025124 E'

planets = load('de421.bsp')

body = planets['Mars']
earth = planets['Earth']

ts = load.timescale()
t = ts.now()

myLocation = earth + Topos(lat, lon)
apparent = myLocation.at(t).observe(body).apparent()

alt, az, distance = apparent.altaz()
print(alt.degrees)
print(az.degrees)
print(distance)
