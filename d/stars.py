from skyfield.api import Star, load, Topos


STARS = [
    'sirius',
    'barnard',
    'vega',
    'alpha_crucis',
    'canopus',
    'alpha_centauri',
    'betelgeuse'
]

STAR_OBJS = {
    'sirius': Star(ra_hours=(6, 45, 8.91728),
                   dec_degrees=(-16, 42, 58.0171),
                   ra_mas_per_year=-546.01,
                   dec_mas_per_year=-1223.07,
                   parallax_mas=379.21,
                   radial_km_per_s=-5.5),
    'barnard': Star(ra_hours=(17, 57, 48.49803),
                   dec_degrees=(4, 41, 36.2072),
                   ra_mas_per_year=-798.71,
                   dec_mas_per_year=+10337.77,
                   parallax_mas=545.4,
                   radial_km_per_s=-110.6),
    'vega': Star(ra_hours=(18, 36, 56.33635),
                   dec_degrees=(38, 47, 1.2802),
                   ra_mas_per_year=200.94,
                   dec_mas_per_year=286.23,
                   parallax_mas=130.23,
                   radial_km_per_s=-13.9),
    'alpha_crucis': Star(ra_hours=(12, 26, 35.89522),
                   dec_degrees=(-63, 5, 56.7343),
                   ra_mas_per_year=-35.83,
                   dec_mas_per_year=-14.86,
                   parallax_mas=10.13,
                   radial_km_per_s=-11.2),
    'canopus': Star(ra_hours=(6, 23, 57.10988),
                   dec_degrees=(-52, 41, 44.3810),
                   ra_mas_per_year=19.93,
                   dec_mas_per_year=23.24,
                   parallax_mas=10.55,
                   radial_km_per_s=20.3),
    'alpha_centauri': Star(ra_hours=(14, 39, 36.49400),
                   dec_degrees=(-60, 50, 2.3737),
                   ra_mas_per_year=3679.25,
                   dec_mas_per_year=473.67,
                   parallax_mas=754.81,
                   radial_km_per_s=-21.4),
    'betelgeuse': Star(ra_hours=(5, 55, 10.30536),
                   dec_degrees=(7, 24, 25.4304),
                   ra_mas_per_year=24.95,
                   dec_mas_per_year=9.56,
                   parallax_mas=5.07,
                   radial_km_per_s=21.91),
}

if __name__ == '__main__':
    planets = load('de421.bsp')
    earth = planets['earth']

    ts = load.timescale()
    t = ts.now()

    lat = '27.469771 S'
    long = '153.025124 E'

    curr_loc = earth + Topos(lat, long)
    astrometric = curr_loc.at(t).observe(STAR_OBJS['sirius']).apparent()
    alt, az, distance = astrometric.altaz()

    print(alt.degrees)
    print(az.degrees)