# pseudo code
# game object
#    will run the show? don't know
#    should ask for a new deck
#    should ask if I would like to draw cards
# deck object
#    fields
#       will hold the deck id
#    methods
#       will get a new deck form cards api and store as deck id
# hand object
#    will hold my cards

class Engine:
    def __init__(self) -> None:
        pass
    class Deck:
        def __init__(self, deck_id):
            self.deck_id = deck_id
    
    my_deck = Deck("no_id")

    print(my_deck.deck_id)

my_game = Engine