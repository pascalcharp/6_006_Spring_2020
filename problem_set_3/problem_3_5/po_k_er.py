from hand import Hand


def stable_sort_hands_for_index(index, hands_list):
    sorter = [[] for _ in range(26)]
    for hl in hands_list:
        sorter[ord(hl[index]) - ord('a')].append(hl)
    result = []
    for sorted_queue in sorter:
        while sorted_queue:
            result.append(sorted_queue.pop(0))
    return result


class HandComparator:
    def __init__(self, k, deck):
        first = 0
        last = k - 1
        self.k = k
        self.n = len(deck)
        self.hands = [Hand.make_hand_from_deck(0, self.k, deck)]
        for i in range(1, self.n):
            last = (last + 1) % self.n
            self.hands.append(Hand.make_new_hand(self.hands[i - 1], deck[first], deck[last]))
            first = (first + 1) % self.n
        self.hands_lists = []
        for i in range(0, self.n):
            self.hands_lists.append(self.hands[i].to_list())

    def __repr__(self):
        result = ""
        i = 0
        for hand in self.hands:
            result += f"Rang = {i} Cartes = {hand.__repr__()}\n"
            i += 1
        return result

    def same(self, i, j):
        return self.hands[i] == self.hands[j]

    def sort_hands(self):
        sorted_hands = [hand for hand in self.hands_lists]
        for m in range(self.k - 1, -1, -1):
            sorted_hands = stable_sort_hands_for_index(m, sorted_hands)
        return sorted_hands

    def count_hands(self):
        result = dict()
        sorted_hands = self.sort_hands()
        current_hand = sorted_hands[0]
        count = 0
        for hand in sorted_hands:
            if hand == current_hand:
                count += 1
            else:
                result[tuple(current_hand)] = count
                count = 1
                current_hand = hand
        result[tuple(current_hand)] = count
        return result


if __name__ == "__main__":
    cards = [1, 5, 3, 2, 5, 1, 2, 3, 2, 4]
    deck = [chr(cards[i] + ord('a')) for i in cards]
    print(deck)
    k = 3
    myObject = HandComparator(k, deck)
    print(myObject)
    print(myObject.sort_hands())
    print(myObject.count_hands())
