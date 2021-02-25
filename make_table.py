def make_table(cars, streets, max_time):
    pos_list = [[(None, None) for _ in cars] for _ in range(max_time)]
    tmp_cars = [car[0] for car in cars]
    for i, car in enumerate(cars):
        time = 0
        for name in car:
            street = streets[name]
            prev_time = time
            pos_list[time][i] = (tmp_cars[i], name)
            time += int(street["time"])
            tmp_cars[i] = name
            for j in range(prev_time + 1, time):
                pos_list[time][j] = (tmp_cars[i], None)
    return pos_list
