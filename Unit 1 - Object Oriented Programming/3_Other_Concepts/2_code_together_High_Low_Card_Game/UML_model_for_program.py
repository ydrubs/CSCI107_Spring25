"""
Demo program to show how a graph can be created with the graphviz library.
This does require Graphviz to be installed and the Path added to the system path.
...We also need to point our script to the bin folder of the path in order for it to work correctly.
"""

from graphviz import Digraph
import os


# Set the Graphviz path manually
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"
# Create a UML class diagram
uml = Digraph('High_Low_Card_Game', filename='high_low_card_game', format='png')

# Card Class
uml.node('Card', '''Card
-------------------
+ rank: str
+ suit: str
+ value: int
+ is_concealed: bool
-------------------
+ __str__(): str
+ reveal(): void
+ conceal(): void''')

# Deck Class
uml.node('Deck', '''Deck
-------------------
+ startingDeckList: list
+ playingDeckList: list
-------------------
+ shuffle(): void
+ getCard(): Card
+ returnCardToDeck(Card): void''')

# Game Class
uml.node('Game', '''Game
-------------------
+ deck: Deck
+ score: int
+ current_card: Card
-------------------
+ start_game(): void''')

# Relationships
uml.edge('Deck', 'Card', label='contains multiple')
uml.edge('Game', 'Deck', label='uses')
uml.edge('Game', 'Card', label='manages')

# Render UML diagram
uml_path = 'high_low_card_game.png'
uml.render(uml_path, format='png', cleanup=True)
uml_path
