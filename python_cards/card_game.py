import requests

class CardGame:
    def __init__(self):
        self.base_url = "https://www.deckofcardsapi.com/api/deck/"
        self.card_values = {"ACE":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "JACK":10, "QUEEN":10, "KING":10}

        self.dealer_hand = self.Hand()
        self.player_hand = self.Hand()

    def create_deck(self, number_of_decks):
        request_qery_string = f"new/shuffle/?deck_count={number_of_decks}"
        data = self.API.api_request(self.base_url, request_qery_string)
        self.deck_id = data["deck_id"]

    def draw_card(self, number_of_cards):
        request_qery_string = f"{self.deck_id}/draw/?count={number_of_cards}"
        data = self.API.api_request(self.base_url, request_qery_string)
        return data
    
    def deal_first_round(self):
        card_data = self.draw_card(4)
        self.dealer_hand.total_in_hand += self.card_values[card_data["cards"][0]['value']]
        self.dealer_hand.total_in_hand += self.card_values[card_data["cards"][2]['value']]
        self.player_hand.total_in_hand += self.card_values[card_data["cards"][1]['value']]
        print(f"Drawn card: {card_data["cards"][1]['value']} of {card_data["cards"][1]['suit']}")
        self.player_hand.total_in_hand += self.card_values[card_data["cards"][3]['value']]
        print(f"Drawn card: {card_data["cards"][3]['value']} of {card_data["cards"][3]['suit']}")

        print(f"Dealer hand: {self.dealer_hand.total_in_hand}")
        print(f"Player hand: {self.player_hand.total_in_hand}")

        print(f"remaining cards left in deck id {card_data["deck_id"]}: {card_data["remaining"]}")

    def deal(self):
        card_data = self.draw_card(2)
        self.dealer_hand.total_in_hand += self.card_values[card_data["cards"][0]['value']]
        self.player_hand.total_in_hand += self.card_values[card_data["cards"][1]['value']]

        print(f"Dealer hand: {self.dealer_hand.total_in_hand}")
        print(f"Player hand: {self.player_hand.total_in_hand}")
        print(f"Drawn card: {card_data["cards"][1]['value']} of {card_data["cards"][1]['suit']}")

        print(f"remaining cards left in deck id {card_data["deck_id"]}: {card_data["remaining"]}")


    class API:
        def api_request(base_url, requested_qery_string):
            response = requests.get(f"{base_url}{requested_qery_string}")
            return response.json()
    class Hand:
        def __init__(self):
            self.total_in_hand = 0

def main():
    game = CardGame()
    game.create_deck(1)

    print(game.deck_id)

    game.deal_first_round()

    while True:
        draw_again = input("Do you want to draw another card? (y/n): ").lower()
        print(draw_again)

        if draw_again == "y":
            game.deal()
        elif draw_again == "n":
            print("Game over. Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
