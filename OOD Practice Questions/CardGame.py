# -------------------------------
# TWO PLAYER CARD GAME SIMULATION
# -------------------------------

from enum import Enum
import random

# CARD Numbers 1–13
# Suits: Spades, Hearts, Clubs, Diamonds
# 52 cards in total
# 2 players
# Each card = 1 point, winner gets 2 points (both cards)
# Draw = both get 1 point and keep their cards in respective pile

class Suit(Enum):
    SPADE = "Spade"
    HEART = "Heart"
    CLUB = "Club"
    DIAMOND = "Diamond"


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.suit.value}-{self.rank}"


class Deck:
    def __init__(self):
        self.card_pile = [Card(s, r) for s in Suit for r in range(1, 14)]
        random.shuffle(self.card_pile)

    def pop_one(self):
        if not self.card_pile:
            return -1
        return self.card_pile.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.leftover_pile = []
        self.score = 0

    def add_hand(self, card):
        self.hand.append(card)

    def add_to_lp(self, card):
        self.leftover_pile.append(card)

    def play_card(self):
        if not self.hand:
            return None
        return self.hand.pop()

    def add_to_score(self, points=2):
        self.score += points

    def get_score(self):
        return self.score


class Game:
    def __init__(self, player1, player2, deck):
        self.player1 = player1
        self.player2 = player2
        self.deck = deck

    def deal(self):
        """Deal all cards evenly to both players."""
        while True:
            card1 = self.deck.pop_one()
            card2 = self.deck.pop_one()
            if card1 == -1 or card2 == -1:
                break
            self.player1.add_hand(card1)
            self.player2.add_hand(card2)

    def play_round(self, round_num):
        """Play one round of the game."""
        card_one = self.player1.play_card()
        card_two = self.player2.play_card()

        if not card_one or not card_two:
            return False  # game over

        print(f"Round {round_num}: {self.player1.name} plays {card_one}, {self.player2.name} plays {card_two}")

        if card_one.rank > card_two.rank:
            self.player1.add_to_score(2)
            self.player1.add_to_lp(card_one)
            self.player1.add_to_lp(card_two)
        elif card_two.rank > card_one.rank:
            self.player2.add_to_score(2)
            self.player2.add_to_lp(card_one)
            self.player2.add_to_lp(card_two)
        else:
            self.player1.add_to_score(1)
            self.player2.add_to_score(1)
            self.player1.add_to_lp(card_one)
            self.player2.add_to_lp(card_two)

        return True

    def start(self):
        """Main game loop."""
        self.deal()
        round_num = 1
        while self.player1.hand and self.player2.hand:
            if not self.play_round(round_num):
                break
            round_num += 1
        self.decide_winner()

    def decide_winner(self):
        print("\n--- Game Over ---")
        print(f"{self.player1.name}: {self.player1.score} points")
        print(f"{self.player2.name}: {self.player2.score} points")

        if self.player1.score > self.player2.score:
            print(f"{self.player1.name} wins!")
        elif self.player2.score > self.player1.score:
            print(f"{self.player2.name} wins!")
        else:
            print("It's a draw!")


# -------------------------------
# Run the game
# -------------------------------
if __name__ == "__main__":
    deck = Deck()
    print("Total cards:", len(deck.card_pile))

    player1 = Player("Tushar")
    player2 = Player("Guru")

    game = Game(player1, player2, deck)
    game.start()
