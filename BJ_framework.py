import tkinter as tk
from tkinter import PhotoImage, messagebox
import random
cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

class Card:
    def __init__(self, suit: str, value: str):
        # TODO: Initialize the attributes
        self.suit = suit
        self.value = value

    def get_numeric_value(self) -> int:
        # TODO: Return the numeric value of the card
        return cards_values[self.value]

    def get_image(self):
        # TODO: Return the path to the card's image
        return f"img/{self.value}_of_{self.suit}.png"

class Deck:
    def __init__(self, suits , values):
        # TODO: Initialize the deck
        self.cards = [Card(suit,value) for suit in suits for value in values ]


    def shuffle(self):
        # TODO: Shuffle the cards
        random.shuffle(self.cards)


    def deal(self)-> Card:
        # TODO: Deal one card from the deck
        return self.cards.pop()


class EnglishDeck(Deck):
    def __init__(self):
        # TODO: Create a standard deck of 52 cards and shuffle them
        suits = ["spades", "hearts", "clubs", "diamonds"]
        cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        super().__init__(suits,cards)
        self.shuffle()


class Hand:
    def __init__(self):
        # TODO: Initialize the hand
        #hand needs to have space for taken cards
        self.cards = []


    def add_card(self, card: Card):
        # TODO: Add a card to the hand
        self.cards.append(card)

    def value(self)->int:
        # TODO: Return the total value of the hand
        hand_sum = sum(card.get_numeric_value() for card in self.cards)
        num_of_Ace = sum( 1 for card in self.cards if card.value=='A')
        while num_of_Ace and hand_sum >21:
            hand_sum -=10
            num_of_Ace -= 1
        return  hand_sum

class Player:
    def __init__(self, name):
        # TODO: Initialize the player's attributes
        self.name = name
        self.hand = Hand()

class BlackjackGame:
    def __init__(self):
        # TODO: Initialize the game's attributes
        self.deck = EnglishDeck()
        self.player = Player('PLAYER')
        self.dealer = Player('DEALER')


    def start_game(self):
        # TODO: Start a new game and deal two cards to each player

        self.player.hand.add_card(self.deck.deal())
        self.player.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal())
        #self.dealer.hand.add_card(self.deck.deal())


    def hit(self)-> bool:
        # TODO: Add a card to the player's hand

        self.player.hand.add_card(self.deck.deal())
        return self.player.hand.value() > 21




    def dealer_hit(self) -> bool:
        # TODO: Deal cards to the dealer based on blackjack's standard rules

        if self.dealer.hand.value() < 17:
            self.dealer.hand.add_card(self.deck.deal())
            return False
        return True



    def determine_winner(self):
        # TODO: Determine and return the winner of the game

        if self.player.hand.value() > 21:
            print('You have busted')

        while self.dealer.hand.value() < 17:
           self.dealer.hand.add_card(self.deck.deal())

        if self.dealer.hand.value() > 21 or self.player.hand.value() > self.dealer.hand.value():
            return f"{self.player.name} wins!"
        elif self.dealer.hand.value() > self.player.hand.value():
            return "The house wins."
        else:
            return "It's a tie!"


# The GUI code is provided, so students don't need to modify it
class BlackjackGUI:
    def __init__(self, game):
        self.game = game

        self.root = tk.Tk()
        self.root.title("Blackjack")

        # Frames for the player and the dealer
        self.player_frame = tk.Frame(self.root)
        self.player_frame.pack(side=tk.LEFT, padx=10)

        self.deck_frame = tk.Frame(self.root)
        self.deck_frame.pack(side=tk.LEFT, padx=10)

        self.dealer_frame = tk.Frame(self.root)
        self.dealer_frame.pack(side=tk.RIGHT, padx=10)

        # "Stand" button
        self.btn_stand = tk.Button(self.deck_frame, text="Stand", command=self.handle_stand, state=tk.NORMAL)
        self.btn_stand.pack(side=tk.BOTTOM)

        self.start_game()

    def start_game(self):
        self.game.start_game()
        self.update_interface()

    def handle_hit(self, event):
        if self.game.hit():
            self.update_interface()
            self.end_game("You've busted! The house wins.")
            return
        self.update_interface()

    def handle_stand(self):
        self.btn_stand.config(state=tk.DISABLED)
        while self.game.dealer_hit():
            self.update_interface()
        self.end_game(self.game.determine_winner())

    def update_interface(self):
        # Remove all widgets from player, deck, and dealer frames
        for widget in self.player_frame.winfo_children():
            widget.destroy()
        
        for widget in self.deck_frame.winfo_children():
            widget.destroy()

        for widget in self.dealer_frame.winfo_children():
            widget.destroy()

        # Player's cards
        player_previous_frame = tk.Frame(self.player_frame)
        player_previous_frame.pack(side=tk.LEFT, pady=10)

        for card in self.game.player.hand.cards[:-1]:  # All cards except the last one
            img = PhotoImage(file=card.get_image())
            img = img.subsample(3, 3)  # Resize the image (adjust according to your preference)
            lbl = tk.Label(player_previous_frame, image=img)
            lbl.image = img
            lbl.pack(side=tk.TOP, pady=5)  # Add vertical space between cards

        # The last card of the player in the center
        last_card = self.game.player.hand.cards[-1]
        img = PhotoImage(file=last_card.get_image())
        lbl = tk.Label(self.player_frame, image=img)
        lbl.image = img
        lbl.pack(side=tk.LEFT, padx=10)  # Center the last card horizontally a bit more
        
        # Deck in the middle
        img = PhotoImage(file="img/card_back_01.png")
        lbl = tk.Label(self.deck_frame, image=img, cursor="hand2")
        lbl.image = img
        lbl.pack(side=tk.TOP, padx=10)
        lbl.bind("<Button-1>", self.handle_hit)
        
        # "Stand" button below the deck
        self.btn_stand = tk.Button(self.deck_frame, text="Stand", command=self.handle_stand, state=tk.NORMAL)
        self.btn_stand.pack(side=tk.BOTTOM)

        # Dealer's cards
        dealer_previous_frame = tk.Frame(self.dealer_frame)
        dealer_previous_frame.pack(side=tk.RIGHT, pady=10)

        for card in self.game.dealer.hand.cards[:-1]:  # All cards except the last one
            img = PhotoImage(file=card.get_image())
            img = img.subsample(3, 3)  # Resize the image (adjust according to your preference)
            lbl = tk.Label(dealer_previous_frame, image=img)
            lbl.image = img
            lbl.pack(side=tk.TOP, pady=5)  # Add vertical space between cards

        # The last card of the dealer in the center
        last_card = self.game.dealer.hand.cards[-1]
        img = PhotoImage(file=last_card.get_image())
        lbl = tk.Label(self.dealer_frame, image=img)
        lbl.image = img
        lbl.pack(side=tk.RIGHT, padx=10)  # Center the last card horizontally a bit more

    def end_game(self, message):
        messagebox.showinfo("Result", message)
        self.root.quit()

    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    game_logic = BlackjackGame()
    app = BlackjackGUI(game_logic)
    app.run()