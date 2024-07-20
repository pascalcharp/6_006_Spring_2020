from lib.ArbreBinaireAVL import ArbreBinaireAVL
from receiver_stats import ReceiverStats

class ReceiverKey:
    def __init__(self, id, avg):
        self.id = id
        self.avg = avg

    def __lt__(self, other):
        if self.avg == other.avg:
            return self.id < other.id
        return self.avg < other.avg

    def __gt__(self, other):
        if self.avg == other.avg:
            return self.id > other.id
        return self.avg > other.avg

    def __eq__(self, other):
        return self.id == other.id and self.avg == other.avg

    def __ne__(self, other):
        return self != other

    def __ge__(self, other):
        return not self < other

    def __le__(self, other):
        return not self > other


class ReceiverRoster:
    def __init__(self):
        self.rankings = ArbreBinaireAVL()

    def add_receiver(self, receiver, receiver_data=None):
        receiver_stats = ReceiverStats(receiver_id=receiver, stats=receiver_data)
        self.rankings.insert(receiver, receiver_stats)

    def record(self, game, receiver, points):
        pass

    def clear(self, game, receiver):
        pass

    def ranked_receiver(self, rank):
        pass
