"""
A simple high/low, terminal based, card game to apply the concepts of OOP in Python.
Implement three classes:
    1) Manage individual card objects
    2) Manage a deck of cards (that itself creates the card objects)
    3) Implement the game logic and actions and manages the card objects
"""

import random

class pass:
    def __init__pass:
        """
        This defines the Card class, which represents a single card in the deck with its rank, suit, and value.
        The `window` parameter can be used for GUI integration, but we won't use it here.
        """
        pass  # Placeholder for potential GUI or display integration



    def pass:
        """
        :return: Reference to card object as a suit and rank as long as card is 'revealed'
        """
        pass


    def pass:
        """This method reveals the card by setting `is_concealed` to False."""
        pass

    def pass:
        """This method conceals the card by setting `is_concealed` to True"""
        pass


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

    def pass:
        # The constructor initializes the deck by creating cards for each suit and rank using the given rank-value dictionary.

        pass # The startingDeckList holds the original un-shuffled deck, which allows resetting the deck if needed.
        pass # The playingDeckList is the active deck used during gameplay, which can be shuffled and modified

        # Loop through the suit tuples which are class variables
        for pass

            # Loop through the card ranks, this gets passed into the initializer, so gets aliased to the STANDARD_DICT variable
            for pass
                pass # Create an instance of each card using the Card class
                pass # Add the created instance to the list
        pass # Call the shuffle method to shuffle deck

    def pass:
        """
        This method shuffles the deck and ensures all cards are concealed before shuffling.
        """
        pass # The .copy method copies a list

        pass

    def pass:
        """
        This method removes and returns the top card from the playing deck. Raises an error if no cards are left.
        """
        pass

    def pass:
        # This method adds a card back to the top of the playing deck.
        pass


class Game:
    def pass:
        """
        The Game class handles the game logic, including initializing the deck and managing the score.
        """
        pass  # Pass "None" for window as we are not using GUI
        pass # Keep track of the score
        pass # Get the top card
       pass # ... and reveal it

    def pass:
        print("Welcome to the Higher or Lower Card Game!")
        print(f"The first card is: {self.current_card}\n")

        pass # Continue drawing cards as long as their are cards to draw
            pass # Checks if the deck is empty. If so, the game ends.
                print("No more cards in the deck. Game over!")
                pass # This ends the loop, essentially ending the game

            guess = input("Will the next card be higher or lower? (h/l): ").strip().lower()
            pass # Check for a valid input
                print("Invalid input. Please type 'h' for higher or 'l' for lower.")
                pass # just ask again (run the while loop again)

            pass # Draw the next card
            pass # ... and reveal it
            print(f"The next card is: {next_card}")

            # Check the card
            pass

                # Increases the score by 1 for a correct guess.
                pass
                print("Correct guess! Your score is now:", self.score, '\n')
            pass
                # Decreases the score by 1 for an incorrect guess.
                pass
                print("Wrong guess. Your score is now:", self.score, '\n')

            pass #Get ready to draw the next card

        print(f"Final score: {self.score}")
        print("Thanks for playing!")


if __name__ == "__main__":
    pass # Create a game object
    pass # Start the Game!

"""
Modification ideas - 
    Add a betting system. The bet is relative to the risk taken.
    So a card such as a 2 or King (where guessing higher or lower is easy) only allows the player to win a portion of their bet
    while a card such as a 9 or 10 (where it can go either way) allows the player to win their full bet. 
"""
