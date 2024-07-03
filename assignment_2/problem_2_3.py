# Friend finder
# Island runs from 0 to length from S to N
import math
import random
import sys


class DatumFinder:
    def __init__(self, length, location):
        self.island_length = length
        self.datum_location = location

    def get_sensor_reading(self, x):
        offset = x - self.datum_location
        if offset < 0:
            return "N"
        else:
            return "S"

    def find_datum(self):
        south = 0
        north = self.island_length
        count = 0
        while north - south > 1:
            count += 1
            mid = (south + north) // 2
            r = self.get_sensor_reading(mid)
            if r == "N":
                south, north = mid, north
            elif r == "S":
                south, north = south, mid
        return south, north, count


    def find_datum_in(self, south, north, count):
        count += 1
        if north - south <= 1:
            return south, north, count
        mid = (south + north) // 2
        r = self.get_sensor_reading(mid)
        if r == "N":
            return self.find_datum_in(mid, north, count)
        else:
            return self.find_datum_in(south, mid, count)

    def recursive_find_datum(self):
        return self.find_datum_in(0, self.island_length, 0)

    def find_datum_from_edges(self):
        offset = 1
        count = 0
        while offset <= self.island_length // 2:
            count += 1
            ds = self.get_sensor_reading(offset)
            dn = self.get_sensor_reading(self.island_length - offset)
            if ds == "S":
                return self.find_datum_in(offset // 2, offset, count)
            elif dn == "N":
                return self.find_datum_in(self.island_length - offset, self.island_length - offset // 2, count)
            offset *= 2
        return offset, self.island_length - offset, count

def run_experiment(island_length, nruns):
    avg = 0
    hi = 0
    lo = sys.maxsize
    for _ in range(nruns):
        find_object = DatumFinder(island_length, random.randint(0, island_length))
        _, _, n = find_object.find_datum_from_edges()
        if n > hi:
            hi = n
        if n < lo:
            lo = n
        avg += n
    avg = avg / nruns
    return lo, avg, hi


if __name__ == "__main__":

    length = 32
    while length < 2048 * 2048:
        print(f"L = {length} : Stats = {run_experiment(island_length=length, nruns=10)} : Predicted = {math.log2(length)}")
        length *= 2
