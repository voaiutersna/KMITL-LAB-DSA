import json

def findStations(cities_needed, stations):
    cities_needed = set(cities_needed)
    selected = []

    while cities_needed:
       
        best_station = None
        best_covered = set()

        for name, cities in stations.items():
            covered = cities_needed & set(cities)
            if len(covered) > len(best_covered):
                best_station = name
                best_covered = covered

        if best_station is None:
            break

        selected.append(best_station)
        cities_needed -= best_covered
        del stations[best_station]

    return sorted(selected)


cities = json.loads(input())
n = int(input())

stations = {}
for _ in range(n):
    data = json.loads(input())
    stations[data["Name"]] = data["Cities"]


result = findStations(cities, stations)
print(result)
