def take_input(input):
     with open(input, "r") as fd:
         line = fd.readline()
         line = line.strip().split()

         duration = int(line[0])
         intersections = int(line[1])
         streets = int(line[2])
         cars = int(line[3])
         bonus = int(line[4])

         return duration, intersections, streets, cars, bonus

if __name__ == '__main__':
    take_input("in1.txt")
