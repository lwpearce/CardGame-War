import Deck

# the extend method on a list takes a list and merges it with another list


class Player:
    def __init__(self, name):
        self.all_cards = []
        self.name = name

# removes a card from a player's hand
    def remove_one(self):
        return self.all_cards.pop(0)  # pop removes an item from the list at position 0 (top)

# adds cards to a player's hand - either a list of cards or a single card
    def add_cards(self, new_cards):  # new_cards can be a single object or a list of objects
        if type(new_cards) == type([]):   # if it's a list
            self.all_cards.extend(new_cards)
        else:  #else it's one card
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
