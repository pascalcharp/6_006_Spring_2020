from lib.hash_map import HashMap


def tuple_hash(num):
    return hash(num)


class ReceiverStats:
    def __init__(self, receiver_id, stats=None):
        self.receiver_id = receiver_id
        self.stats = HashMap(tuple_hash, stats)
        self.average = self.calculate_average()

    def __len__(self):
        return len(self.stats)

    def calculate_average(self):
        sum = 0.0
        for _, p in self.stats:
            sum += p
        return sum / len(self.stats)

    def update_average(self):
        if len(self.stats) == 0:
            self.average = 0
        else:
            self.average = self.calculate_average()

    def update_points_for_game(self, game, points):
        try:
            self.stats.find(game)
            self.stats.remove(game)
        finally:
            self.stats.insert(game, points)
            self.update_average()

    def remove_game(self, game):
        self.stats.remove(game)
        self.update_average()
