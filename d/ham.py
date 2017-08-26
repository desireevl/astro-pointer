# distance between import word and list  of words, shortest distances get displayed
# if nothing similar say no results
# make input lowercase
# if only one suggestion use that
from skyfield.api import load
import distance
# import pandas as pd


def levenshtein_dist(des_obj):
    stations_url = 'http://celestrak.com/NORAD/elements/stations.txt'
    satellites = load.tle(stations_url)

    satellites_list = [k for k in satellites]

    # other_objs = pd.read_csv('other_objs_list.csv')
    # x = other_objs.values

    satellites_list_with_score = list(map(lambda x: (x, distance.levenshtein(des_obj.lower(), x.lower())), satellites_list))

    has_exact_match_list = list(filter(lambda x: x[1] == 0, satellites_list_with_score))
    similar_matches_list = list(map(lambda x: x[0], filter(lambda x: x[1] <= 3, satellites_list_with_score)))

    if len(has_exact_match_list) > 0:
        return has_exact_match_list[0][0]
    else:
        return similar_matches_list

if __name__ == '__main__':
    print(levenshtein_dist('TIangong'))

