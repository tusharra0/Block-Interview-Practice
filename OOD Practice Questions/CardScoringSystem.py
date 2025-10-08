from enum import Enum

class Suit(Enum):
    SPADE = "Spade"
    CLUB = "Club"
    DIAMOND = "Diamond"
    HEART = "Heart"

class Card:
    def __init__(self,suit: Suit, rank:int):
        self.rank = rank 
        self.suit = suit 
    def __repr__(self):
        return f"{self.suit.value}--{self.rank}"

class Player:
    def __init__(self,name: str, cards: list[Card]):
        self.name = name
        self.cards = cards
        self.score = 0
    def add_to_score(self,points:int):
        self.score += points 
    
    def show_score(self):
        print(self.name+"'s Score: ",self.score)

class Game:
    def __init__(self,player: Player):
        self.player= player 


    def two_for_pair(self):
        hashmap = {}
        
        for card in self.player.cards:
            hashmap[card.rank] = hashmap.get(card.rank, 0) + 1

            
        score_to_add = 0
        for count in hashmap.values():
            if count>=2:
                pairs = (count*(count-1))//2
                score_to_add += 2*pairs 
        
        print("score_to_add",score_to_add)
        self.player.add_to_score(score_to_add)

    def score_of_five(self):
        # Loop through the list and then add it to a set.. if set;s len =1  

        suits = set()
        for card in self.player.cards:
            suits.add(card.suit)
        
        if len(suits)==1:
            self.player.add_to_score(5)
    
    #{7:1, 8:2, 1:2} 
    def add_to_15(self):
        hashmap = {}

        for card in self.player.cards:
            hashmap[card.rank] = hashmap.get(card.rank, 0) + 1

        count = 0
        for rank in hashmap:
            find = 15 - rank
            if find in hashmap:
                count += hashmap[rank] * hashmap[find]

        count = count // 2 
        score_to_add = count * 2

        self.player.add_to_score(score_to_add)
        print("Score from 15s:", score_to_add)

if __name__ == "__main__":
    cards = [
        Card(Suit.HEART,7),
        Card(Suit.SPADE,8),
        Card(Suit.CLUB,8),
        Card(Suit.DIAMOND,1),
        Card(Suit.HEART,1),
    ]

    player1 = Player("Tushar",cards)

    game = Game(player1)

    print("Players Hand:", player1.cards)
    game.add_to_15()

