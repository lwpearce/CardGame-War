import Card
import Deck
import Player

''' Game Logic:
We'll have Player1 - of type Player and Player2 of Player 2
- And a new Deck - of type Deck
we'll shuffle the new deck
use a for loop to add the cards to each player
Check for 0 cards in a player's list is the len(player's cards) == 0? set game_on = true
while game_on
    each player removes a card from their deck
    compare the cards 
    whichever player has the bigger card, gets both cards added to the bottom of their deck
    if war happens, if cards are equal, at_war = true
        while at_war
            each player draw a card
            compare cards
    winner gets all cards added to their card
    has a player won? game_on = false            
'''
# Game Setup
# create players
player_one = Player.Player("One")
player_two = Player.Player("Two")
# create deck
new_deck = Deck.Deck()
new_deck.shuffle_deck()

war_number_of_cards = 5
'''
split deck between 2 players
this is 26 because in deal_one, we're popping a card twice - 
1 for each player each time we go through the for loop
'''
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_number = 0  # keeps track of round
# While game_on
while game_on:

    round_number += 1
    print(f"Round {round_number}")
    # Check if we have a winner:
    if len(player_one.all_cards) == 0:
        print("Player One, out of cards! Player Two wins!")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print("Player Two, out of cards! Player One wins!")
        game_on = False
        break

    # Start a new round
    player_one_cards = [player_one.remove_one()]  # these are the current cards player one is playing in this round
    player_two_cards = [player_two.remove_one()]
    # now do comparison of cards - both players only have 1 card
    at_war = True
    # While at_war
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)  # add player 1's cards back to his deck
            player_one.add_cards(player_two_cards)  # add player 2 cards to player one's entire deck
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_two_cards)  # add player 1's cards back to his deck
            player_two.add_cards(player_one_cards)  # add player 2 cards to player one's entire deck
            at_war = False
        else:
            print('WAR');  # or if player has < 5 cards, just get the amount they have
            if len(player_one.all_cards) < war_number_of_cards:
                print('Player One unable to go to war')
                print('Player Two wins')
                game_on = False
                at_war = False
                break
            elif len(player_two.all_cards) < war_number_of_cards:
                print('Player Two unable to go to war')
                print('Player One wins')
                game_on = False
                at_war = False
                break
            else:
                for num in range(war_number_of_cards):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())