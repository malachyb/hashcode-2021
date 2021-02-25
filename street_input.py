def street_input(filename, intersections, streets, cars):
    list_intersections = [[] for _ in range(intersections)]
    dict_streets = {}
    with open(filename, "r") as fd:
        lines = fd.readlines()
        for i in range(1, streets):
            line = lines[i].strip().split()

            list_intersections[int(line[0])].append(line[2])
            list_intersections[int(line[1])].append(line[2])

            dict_streets[line[2]] = {"time": line[3], "intersections": line[0:2]}
        list_cars = []
        for i in range(cars):
            line = lines[i].strip().split()
            list_cars.append(line[1:])

    return list_intersections, dict_streets, list_cars
