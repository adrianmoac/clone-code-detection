class Player:
    def __init__(self, name):
        # 名前
        self.name = name
        self._cards = []

    
    def setcards(self, cards):
        # 手札
        for card in cards:
            self._cards.insert(0, card)

    def getcards(self):
        return self._cards

    cards = property(getcards, setcards)

    def putDown(self):
        """
        カードがある場合はカードを出します。
        ない場合はNoneを返します。
        """
        if len(self.cards) != 0:
            return self._cards.pop()
        else:
            return None

class Game:
    def __init__(self, players):
        self.players = players

    def start(self):
        ret = self.play(self.players[0].name)
        return ret

    def play(self, name):
        target = self.searchTarget(name)
        card = target.putDown()
        if card != None:
            return self.play(card)

        # 勝者を返す
        return name

    def searchTarget(self, name):
        for player in self.players:
            if player.name == name:
                return player



if __name__ == '__main__':
    a = Player("a")
    a.cards = input()

    b = Player("b")
    b.cards = input()

    c = Player("c")
    c.cards = input()

    g = Game([a, b, c])
    winner = g.start()
    print(winner.upper())
