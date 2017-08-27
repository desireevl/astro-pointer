# distance between import word and list  of words, shortest distances get displayed
# if nothing similar say no results
# make input lowercase
# if only one suggestion use that
from skyfield.api import load
from stars import STARS
import distance

def clean_names(name):
    if name.lower() == "jupiter":
        return "JUPITER_BARYCENTER"
    if name.lower() == "uranus":
        return "URANUS_BARYCENTER"
    if name.lower() == 'saturn':
        return "SATURN_BARYCENTER"
    if name.lower() == 'neptune':
        return "NEPTUNE_BARYCENTER"
    if name.lower() == 'pluto':
        return "PLUTO_BARYCENTER"
    return name

def levenshtein_dist(des_obj):
    stations_url = 'http://celestrak.com/NORAD/elements/stations.txt'
    satellites = load.tle(stations_url)

    satellites_list = [k for k in satellites]
    satellites_list.extend(["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Moon", "Sun"])
    satellites_list.extend(STARS)

    satellites_list_with_score = list(map(lambda x: (x, distance.levenshtein(des_obj.lower(), x.lower())), satellites_list))

    has_exact_match_list = list(filter(lambda x: x[1] == 0, satellites_list_with_score))
    similar_matches_list = list(map(lambda x: x[0], filter(lambda x: x[1] <= 3, satellites_list_with_score)))

    if len(has_exact_match_list) > 0:
        return clean_names(has_exact_match_list[0][0])
    else:
        return list(map(lambda x: clean_names(x), similar_matches_list))

if __name__ == '__main__':
    print(levenshtein_dist('TIangong'))

