class Hand:
    # ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    # Adjusted for part2
    ranks = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.get_card_str()

    def get_card_str(self):
        d = sorted(
            {char: self.hand.count(char) for char in self.hand}.items(),
            key=lambda x: x[1],
            reverse=True,
        )
        # part2
        if "J" in self.hand:
            if d[0][0] != "J":
                temp_hand = self.hand.replace("J", d[0][0])
            elif len(d) > 1:
                temp_hand = self.hand.replace("J", d[1][0])
            else:
                temp_hand = self.hand
            d = sorted(
                {char: temp_hand.count(char) for char in temp_hand}.items(),
                key=lambda x: x[1],
                reverse=True,
            )
        self.strength = 99
        if len(d) == 1:
            self.strength = 1
        elif len(d) == 2:
            if d[0][1] == 4:
                self.strength = 2
            else:
                self.strength = 3
        elif len(d) == 3:
            if d[0][1] == 3:
                self.strength = 4
            else:
                self.strength = 5
        elif len(d) == 4:
            self.strength = 6
        else:
            self.strength = 7

    def __lt__(self, other):
        if self.strength == other.strength:
            ranks = "".join(self.ranks)
            num1 = ""
            num2 = ""
            for i in range(len(self.hand)):
                if not (self.hand[i] == other.hand[i]):
                    return ranks.find(self.hand[i]) < ranks.find(other.hand[i])
            return num1 < num2
        return self.strength < other.strength

    def __repr__(self):
        return self.hand + " " + str(self.strength)


if __name__ == "__main__":
    with open("day7.txt", "r") as f:
        lines = f.readlines()
    hands = []
    for line in lines:
        hand, bid = line.replace("\n", "").split(" ")
        hands.append(Hand(hand, bid))
    hands = sorted(hands, reverse=True)
    sm = 0
    for idx, hand in enumerate(hands):
        sm += (idx + 1) * int(hand.bid)
    print(sm)
