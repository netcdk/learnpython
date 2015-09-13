# Mini-project #6 - Blackjack by CDK
# Written on CodeSkulptor.org

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
score = 0
deck = []
player_hand = []
dealer_hand = []
message = "Let's go!"

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []

    def __str__(self):
        # return a string representation of a hand
        hand_cards = ""       
        for card in self.hand:
            hand_cards += str(card) + " "
        return hand_cards

    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        aces = False
        for card in self.hand:
            hand_value +=  VALUES[card.get_rank()]
            if card.get_rank() == "A":
                aces = True
        if (aces == True) and (hand_value <= 10):
            hand_value += 10
            return hand_value
        else:
            return hand_value

    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        card_index = 0
        for card in self.hand:
            if pos[1] == 300 and card_index == 0 and in_play == True:
                # draw card back
                canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
            else:
                card.draw(canvas, [pos[0] + (card_index % 10) * 100, pos[1] + (card_index // 10) * 100])
            card_index += 1
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        self.deck_index = 0
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        self.deck_index = 0
        random.shuffle(self.deck)
                
    def deal_card(self):
        # deal a card object from the deck
        self.deck_index -= 1
        return self.deck[self.deck_index]
        
    def __str__(self):
        # return a string representing the deck
        deck_cards = ""       
        for card in self.deck:
            deck_cards += str(card) + " "
        return deck_cards

#define event handlers for buttons
def deal():
    global in_play, score, deck, player_hand, dealer_hand, message
    # your code goes here
    if (in_play == True):
        score -= 1
        message = "You lose! New deal!"
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    in_play = True
    message = "Hit or stand?"
    
def hit():
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    global in_play, score, player_hand, message
    if (in_play == True):
        player_hand.add_card(deck.deal_card())
        if player_hand.get_value() <= 21:
            message = "Hit or stand?"
        else:
            score -= 1
            in_play = False
            message = "You bust! New deal?"
    
def stand():
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    global in_play, score, player_hand, dealer_hand, message
    if (in_play == True):
        while dealer_hand.get_value() <= 16:
            dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() > 21:
            score += 1
            message = "You win! New deal?"
        elif dealer_hand.get_value() >= player_hand.get_value():
            score -= 1
            message = "Dealer wins! New deal?"
        else:
            score += 1
            message = "You win! New deal?"
    in_play = False
    
# draw handler    
def draw(canvas):
    canvas.draw_text("Blackjack", [215, 50], 50, "White")
    canvas.draw_text("Dealer", [10, 290], 24, "White")
    dealer_hand.draw(canvas, [25, 300])
    canvas.draw_text("Player", [10, 90], 24, "White")
    player_hand.draw(canvas, [25, 100])
    canvas.draw_text("Your score: " + str(score), [400, 595], 24, "White")
    canvas.draw_text(message, [10, 595], 24, "Yellow")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()