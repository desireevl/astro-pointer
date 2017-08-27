from skyfield.api import Topos, load
from ham import levenshtein_dist
from driver.driver import rotate_to_azimuth, turn_to_altitude

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

if __name__ == '__main__':
    # get current coordinates from phone
    # searchable constellations/stars
    # browse celestrak for these
    # fix donwloaded files

    # get latitude and longitude from phone location
    latitude = '27.469771 S'
    longitude = '153.025124 E'

    # get desired object
    des_obj = input('Please enter a name: ')

    # gets current time
    ts = load.timescale()
    curr_time = ts.now()

    # loads ephemeris, gets planet locations
    planets = load('de421.bsp')

    # gets satellite element set
    # celestrak updates positions
    stations_url = 'http://celestrak.com/NORAD/elements/stations.txt'
    satellites = load.tle(stations_url)

    similiar_or_exact_names = levenshtein_dist(des_obj)

    if type(similiar_or_exact_names) != list:
        result = similiar_or_exact_names

    else:
        print('Please select object: ')
        for idx, i in enumerate(similiar_or_exact_names):
            print('{}: {}'.format(idx, i))
        idx = input('Your input: ')
        result = similiar_or_exact_names[int(idx)]

    print('You chose: {}'.format(result))
    print('Moving...')

    alt, az, distance = obj_location(result, latitude, longitude)
    print(alt,az,distance)
    rotate_to_azimuth(az)
    turn_to_altitude(alt)

    print('alt: {}, az: {}'.format(alt, az))

    print('Thanks for using astro-pointer!')
