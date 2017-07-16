from skyfield.api import Topos, load

# get coordinates
# get location of cel objs

# get latitude and longitude from phone location
latitude = '42.3583 N'
longitude = '71.0603 W'

#get desired object
des_obj = 'Mars'

# gets current time
ts = load.timescale()
curr_time = ts.now()

# loads ephemeris, gets planet locations
planets = load('de421.bsp')

# obj with capital letter
def obj_location(obj, lat, long):
    curr_obj = planets[obj]
    earth = planets['Earth']

    # topocentric is position measured relative to location on earth
    curr_loc = earth + Topos(lat, long)
    # .observe backdates to account for c (astrometric), .apparent takes deflection and abberation into account
    apparent_loc = curr_loc.at(curr_time).observe(curr_obj).apparent()

    # positive altitude is above horizon, negative is below
    # azimuth is angle, 0deg at north
    # altaz(temperature_C= , pressure_mbar= )
    alt, az, distance = apparent_loc.altaz()

    return(alt.degrees, az.degrees, distance)

print(obj_location(des_obj, latitude, longitude))