from enum import Enum
import random

class Color(Enum):
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"
    YELLOW = "Yellow"

class Card:
    def __init__(self, color, rank):
        self.color = color
        self.rank = rank
    def __repr__(self):
        return f"{self.color.value}-{self.rank}"

class Deck:
    def __init__(self):
        self.pile = []
        for element in Color:
            for i in range(10):
                self.pile.append(Card(element,i))
        random.shuffle(self.pile)

    def pop_card(self):
        if not self.pile:
            return None
        return self.pile.pop()

    def add_cards(self, cards):
        self.pile.extend(cards)
        random.shuffle(self.pile)

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_cards_to_player(self, card):
        self.cards.append(card)

    def has_playable_card(self, top_card):
        for card in self.cards:
            if card.color == top_card.color or card.rank == top_card.rank:
                return card
        return None

    def remove_card(self, card):
        self.cards.remove(card)

    def __repr__(self):
        return f"{self.name}({len(self.cards)} cards)"

class Game:
    def __init__(self, player1, player2, deck):
        self.player1 = player1
        self.player2 = player2
        self.deck = deck
        self.discard_pile = []

    def deal(self):
        for _ in range(7):
            self.player1.add_cards_to_player(self.deck.pop_card())
            self.player2.add_cards_to_player(self.deck.pop_card())

        top = self.deck.pop_card()
        self.discard_pile.append(top)
        print(f"Starting card: {top}")

    def play_turn(self, player):
        top_card = self.discard_pile[-1]
        playable = player.has_playable_card(top_card)

        if playable:
            player.remove_card(playable)
            self.discard_pile.append(playable)
            print(f"{player.name} plays {playable}")
        else:
            drawn = self.deck.pop_card()
            if not drawn:
                self.replenish_deck()
                drawn = self.deck.pop_card()
            if drawn:
                player.add_cards_to_player(drawn)
                print(f"{player.name} draws a card")

    def replenish_deck(self):
        if len(self.discard_pile) > 1:
            top = self.discard_pile.pop()
            to_shuffle = self.discard_pile.copy()
            self.discard_pile = [top]
            self.deck.add_cards(to_shuffle)
            print("Deck replenished from discard pile!")

    def start(self):
        self.deal()
        turn = 0
        while True:
            current = self.player1 if turn % 2 == 0 else self.player2
            self.play_turn(current)

            if not current.cards:
                print(f"\n🎉 {current.name} wins the game! 🎉")
                break

            turn += 1

if __name__ == "__main__":
    deck = Deck()
    player1 = Player("Tushar")
    player2 = Player("Guru")
    game = Game(player1, player2, deck)
    game.start()
