import requests

class CardGame:
    def __init__(self):
        self.base_url = "https://www.deckofcardsapi.com/api/deck/"

    def create_deck(self):
        response = requests.get(f"{self.base_url}/new/shuffle/?deck_count=1")
        data = response.json()
        self.deck_id = data["deck_id"]

    def draw_card(self):
        response = requests.get(f"{self.base_url}/{self.deck_id}/draw/?count={1}")
        data = response.json()
        return data

def main():
    game = CardGame()
    game.create_deck()

    while True:
        draw_again = input("Do you want to draw another card? (yes/no): ").lower()

        if draw_again == "yes" or "y":
            drawn_card_data = game.draw_card()
            print(f"Drawn card: {drawn_card_data["cards"][0]['value']} of {drawn_card_data["cards"][0]['suit']}")
            print(f"remaining cards left in deck id {drawn_card_data["deck_id"]}: {drawn_card_data["remaining"]}")
        elif draw_again == "no" or "n":
            print("Game over. Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
