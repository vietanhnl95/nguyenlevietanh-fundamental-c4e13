from haversine import haversine



city_list = [
    {
        'name': "Hanoi",
        'Lati': 21.0277644,
        'Long': 105.83415979999995,
    },

    {
        'name': "Danang",
        'Lati': 16.0544068,
        'Long': 108.20216670000002,
    },

    {
        'name': "HCMC",
        'Lati': 10.8230989,
        'Long': 106.6296638,
    },

    {
        'name': "Hue",
        'Lati': 16.4498,
        'Long': 107.5623501,
    }
]

for i in range(len(city_list) - 1):
    city1 = city_list[i]
    for a in range(i + 1,len(city_list)):
        city2 = city_list[a]
        cord1 = (city1['Lati'],city1['Long'])
        cord2 = (city2['Lati'],city2['Long'])
        distance = haversine(cord1,cord2)

        print("Distance between {0} and {1}: {2}".format(city1['name'], city2['name'], distance))
