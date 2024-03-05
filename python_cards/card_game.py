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
    
    def calculate_total_value(self, hand):
        # hand is either
        # self.dealer_hand or
        # self.player_hand
        hand.total_in_hand = 0
        for value in hand.cards_in_hand:
            hand.total_in_hand += self.card_values[value['value']]
        print(hand.total_in_hand)
    
    def deal_first_round(self):
        response = self.draw_card(4)
        
        for index, value in enumerate(response["cards"]):
            if index % 2 == 0:
                self.dealer_hand.cards_in_hand.append(value)
            else:
                self.player_hand.cards_in_hand.append(value)

        print("Dealer hand:")
        for value in self.dealer_hand.cards_in_hand:
            print({value["code"]})
        print("Player hand:")
        for value in self.player_hand.cards_in_hand:
            print({value["code"]})

        self.calculate_total_value(self.dealer_hand)
        self.calculate_total_value(self.player_hand)

        print(f"remaining cards left in deck id {response["deck_id"]}: {response["remaining"]}")

    def deal(self):
        if self.dealer_hand.total_in_hand < 17:
            response = self.draw_card(2)
        
            for index, value in enumerate(response["cards"]):
                if index % 2 == 0:
                    self.dealer_hand.cards_in_hand.append(value)
                else:
                    self.player_hand.cards_in_hand.append(value)
        else:
            response = self.draw_card(1)
            self.player_hand.cards_in_hand.append(response["cards"][0])

        print("Dealer hand:")
        for value in self.dealer_hand.cards_in_hand:
            print({value["code"]})
        print("Player hand:")
        for value in self.player_hand.cards_in_hand:
            print({value["code"]})

        self.calculate_total_value(self.dealer_hand)
        self.calculate_total_value(self.player_hand)

        print(f"remaining cards left in deck id {response["deck_id"]}: {response["remaining"]}")


    class API:
        def api_request(base_url, requested_qery_string):
            response = requests.get(f"{base_url}{requested_qery_string}")
            return response.json()
    class Hand:
        def __init__(self):
            self.total_in_hand = 0
            self.cards_in_hand = [] # is a list of a dict of the card data

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
