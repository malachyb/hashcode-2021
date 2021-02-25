def make_table(cars, streets, max_time):
    pos_list = [[(None, None) for _ in cars] for _ in range(max_time)]
    tmp_cars = [car[0] for car in cars]
    for i, car in enumerate(cars):
        time = 0
        for t, name in enumerate(car):
            if time < len(pos_list):
                street = streets[name]
                prev_time = time
                if t + 1 < len(car):
                    try:
                        pos_list[time][i] = (tmp_cars[i],
                                             next(iter(set(streets[name]["time"]).intersection(
                                                 set(streets[car[t + 1]]["time"])))))
                    except StopIteration:
                        pos_list[time][i] = (tmp_cars[i], None)
                time += int(street["time"])
                tmp_cars[i] = name
                for j in range(prev_time + 1, time):
                    if j < len(pos_list):
                        pos_list[j][i] = (tmp_cars[i], None)
    return pos_list
