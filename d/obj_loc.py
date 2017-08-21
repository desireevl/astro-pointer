from skyfield.api import Topos, load

# get current coordinates from phone
# hamming distance for searching
# searchable constellations/stars
# browse celestrak for these

# get latitude and longitude from phone location
latitude = '-27.469771 S'
longitude = '153.025124 E'

# get desired object
des_obj = 'ISS (ZARYA)'

# gets current time
ts = load.timescale()
curr_time = ts.now()

# loads ephemeris, gets planet locations
planets = load('de421.bsp')

# gets satellite element set
# celestrak updates positions
stations_url = 'http://celestrak.com/NORAD/elements/stations.txt'
satellites = load.tle(stations_url)

def obj_location(obj, lat, long):
    try:
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

    except:
        satellite = satellites[obj]
        # subtracts vector location of observer from satellite
        difference = satellite - Topos(lat,long)
        # converts this difference to coordinates
        topocentric = difference.at(curr_time)
        alt, az, distance = topocentric.altaz()

    return alt.degrees, az.degrees, distance

print(obj_location(des_obj, latitude, longitude))
