"""
A simple high/low, terminal based, card game to apply the concepts of OOP in Python.
Implement three classes:
    1) Manage individual card objects
    2) Manage a deck of cards (that itself creates the card objects)
    3) Implement the game logic and actions and manages the card objects
"""

import random

class Card:
    def __init__(self, window, rank, suit, value):
        """
        This defines the Card class, which represents a single card in the deck with its rank, suit, and value.
        The `window` parameter can be used for GUI integration, but we won't use it here.
        """
        self.window = window
        self.rank = rank
        self.suit = suit
        self.value = value
        self.is_concealed = True

    def __str__(self):
        """
        :return: Reference to card object as a suit and rank as long as card is 'revealed'
        """
        if self.is_concealed == False:
            return f"{self.rank} of {self.suit}"
        else:
            return "No Cheating!"


    def reveal(self):
        """This method reveals the card by setting `is_concealed` to False."""
        self.is_concealed = False

    def conseal(self):
        """This method conceals the card by setting `is_concealed` to True"""
        self.is_concealed = True


class Deck:
    """
    The Deck class manages the collection of cards.
    SUIT_TUPLE defines the four suits in a standard deck of cards.
    STANDARD_DICT maps each card rank to its corresponding value in a standard deck.
        We can pass in a different mapping for other card games (such as only using 9-Ace, or having Ace be the high card).
    """
    # Class Variables - Applies to ALL decks
    SUIT_TUPLE = ('Diamonds', 'Clubs', 'Hearts', 'Spades')

    STANDARD_DICT = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                     '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                     'Jack': 11, 'Queen': 12, 'King': 13}


    def __init__(self, window, rankValueDict = STANDARD_DICT):
        # The constructor initializes the deck by creating cards for each suit and rank using the given rank-value dictionary.

        self.starting_deck_list = [] # The startingDeckList holds the original un-shuffled deck, which allows resetting the deck if needed.
        self.playing_deck_list = [] # The playingDeckList is the active deck used during gameplay, which can be shuffled and modified

        # Loop through the suit tuples which are class variables
        for suit in Deck.SUIT_TUPLE:

            # Loop through the card ranks, this gets passed into the initializer, so gets aliased to the STANDARD_DICT variable
            for rank, value in rankValueDict.items():
                oCard = Card(window, rank, suit, value) # Create an instance of each card using the Card class
                self.starting_deck_list.append(oCard) # Add the created instance to the list

        self.shuffle() # Call the shuffle method to shuffle deck

    def shuffle(self):
        """
        This method shuffles the deck and ensures all cards are concealed before shuffling.
        """
        self.playing_deck_list = self.starting_deck_list.copy() # The .copy method copies a list

        for oCard in self.playing_deck_list:
            oCard.conseal()

        random.shuffle(self.playing_deck_list)

    def getCard(self):
        """
        This method removes and returns the top card from the playing deck. Raises an error if no cards are left.
        """
        if len(self.playing_deck_list) == 0:
            raise IndexError('No more cards')
        return self.playing_deck_list.pop()

    def returnCardToDeck(self, oCard):
        # This method adds a card back to the top of the playing deck.
        self.playing_deck_list.insert(0, oCard)


class Game:
    def __init__(self):
        """
        The Game class handles the game logic, including initializing the deck and managing the score.
        """
        self.deck =  Deck(None) # Pass "None" for window as we are not using GUI
        self.score = 0 # Keep track of the score
        self.current_card = self.deck.getCard() # Get the top card
        self.current_card.reveal() # ... and reveal it

    def start_game(self):
        print("Welcome to the Higher or Lower Card Game!")
        print(f"The first card is: {self.current_card}\n")

        while True: # Continue drawing cards as long as there are cards to draw
            if len(self.deck.playing_deck_list) == 0:  # Checks if the deck is empty. If so, the game ends.
                print("No more cards in the deck. Game over!")
                break # This ends the loop, essentially ending the game

            guess = input("Will the next card be higher or lower? (h/l): ").strip().lower()
            if guess not in ['h', 'l']:# Check for a valid input
                print("Invalid input. Please type 'h' for higher or 'l' for lower.")
                continue # just ask again (run the while loop again)

            next_card =  self.deck.getCard() # Draw the next card
            next_card.reveal() # ... and reveal it
            print(f"The next card is: {next_card}")

            # Check the card
            if (guess == 'h' and next_card.value > self.current_card.value) or \
                    (guess == 'l' and next_card.value < self.current_card.value):

                # Increases the score by 1 for a correct guess.
                self.score +=1
                print("Correct guess! Your score is now:", self.score, '\n')

            else:
                # Decreases the score by 1 for an incorrect guess.
                self.score -=1
                print("Wrong guess. Your score is now:", self.score, '\n')

            self.current_card = next_card #Get ready to draw the next card

        print(f"Final score: {self.score}")
        print("Thanks for playing!")


if __name__ == "__main__":
    game = Game() # Create a game object
    game.start_game() # Start the Game!

"""
Modification ideas - 
    Add a betting system. The bet is relative to the risk taken.
    So a card such as a 2 or King (where guessing higher or lower is easy) only allows the player to win a portion of their bet
    while a card such as a 9 or 10 (where it can go either way) allows the player to win their full bet. 
"""
