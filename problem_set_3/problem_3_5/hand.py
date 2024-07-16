class Hand:
    def __init__(self, cards):
        if cards is None:
            cards = [0 for i in range(26)]
        self.cards = cards

    @classmethod
    def make_hand_from_deck(cls, index, num_card, deck):
        cards = [0 for i in range(26)]
        for i in range(num_card):
            cards[ord(deck[(index + i) % len(deck)]) - ord('a')] += 1
        return Hand(cards)

    @classmethod
    def make_new_hand(cls, old_hand, removed, added):
        cards = [e for e in old_hand.cards]
        cards[ord(removed) - ord('a')] -= 1
        cards[ord(added) - ord('a')] += 1
        return Hand(cards)

    def to_list(self):
        result = []
        for i in range(len(self.cards)):
            for j in range(self.cards[i]):
                result.append(chr(i + ord('a')))
        return result

    def __repr__(self):
        result = ""
        for i in range(len(self.cards)):
            for j in range(self.cards[i]):
                result += chr(i + ord('a'))
        return result

    def __hash__(self):
        hash_code = 1
        for i in range(len(self.cards)):
            hash_code = 31 * hash_code + (i + ord('a'))
        return hash_code

    def __eq__(self, other):
        return self.cards == other.cards

    def __lt__(self, other):
        return self.cards < other.cards


if __name__ == '__main__':
    deck = ['a', 'c', 'b', 'a', 'd', 'f', 'b', 'd', 'a', 'd']
    first_hand = Hand.make_hand_from_deck(8, 4, deck)
    second_hand = Hand.make_new_hand(first_hand, 'a', 'd')
    print(first_hand)
    print(second_hand)
    print(first_hand == first_hand)
    print(first_hand > second_hand)

