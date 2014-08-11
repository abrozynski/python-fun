import random

class Card:

  card_order = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
  suits = ['H', 'C', 'D', 'S']


  def __init__(self, card=None):
    if card is None:
      card = self.card_order[int(random.random()*len(self.card_order))]+self.suits[int(random.random()*len(self.suits))]
    self.number = card[0]
    self.suit = card[1]
    self.rank = self.card_order.index(self.number)    


  def __unicode__(self):
    return self.number + self.suit

  def __str__(self):
    return unicode(self).encode('utf-8')



class Deck:
  
  def __init__(self):
    self.card_list = []
    for rank in Card.card_order:
     for suit in Card.suits:
       self.card_list.append(rank + suit)
    self.shuffle()

  def shuffle(self):
    return random.shuffle(self.card_list)



class PokerHand:

  hand_order = ['high', 'pair', 'two pair', 'three of a kind', 'straight', 'flush', 'full house', 'four of a kind', 'straight flush']

  def __init__(self, string=None):
    if string == None:
      self.deal_hand()
    else:
      self.set_hand(string)
    self.show_hand()


  def show_hand(self):
    card_strings = []
    for card in self.hand:
      print str(card)
      card_strings.append(str(card))
    return card_strings

  def set_hand(self, hand_string):
    self.hand =[]
    for x in hand_string.split(' '):
      print x
      self.hand.append(Card(x))

    

  def deal_hand(self):
    self.hand = []
    for i in range(0, 5):
      nextCard = Card()
      if nextCard not in self.hand:
        self.hand.append(nextCard)

  def evaluate_hand(self):

    sorted_hand = sorted(self.hand, key=lambda card: card.rank)
    self.hand = sorted_hand
    self.hand_ranks = []
    for card in self.hand:
      self.hand_ranks.append(card.rank)


    rank_occurances = {}
    for card in self.hand:
      if card.number not in rank_occurances:
        rank_occurances[card.number]= self.hand_ranks.count(card.rank)
    print rank_occurances
    #straight flush

    if ((self.check_flush() == True) and (self.check_straight() == True)):
      self.evaluation = 'straight flush'
      self.high_card = self.hand[4]
      self.kickers = None
   
    elif self.check_flush() == True:
      self.evaluation = 'flush'
      self.high_card = self.hand[4]
      self.kickers = None

    elif self.check_straight() == True:
      self.evaluation = 'straight'
      self.high_card = self.hand[4]    
      self.kickers = None

    elif 4 in rank_occurances.values():
      self.evaluation = 'four of a kind'
      for card in self.hand:
       if rank_occurances[card.number] == 4:
         self.high_card = card
       else:
         self.kickers = [card]


    elif (3 in rank_occurances.values() and 2 in rank_occurances.values()):
      self.evaluation = 'full house'
      for card in self.hand:
        if rank_occurances[card.number] == 3:
          self.high_card = card
        else:
          self.kickers = [card]

    elif (3 in rank_occurances.values()):
      self.evaluation = 'three of a kind'
      self.kickers = []
      for card in self.hand:
        if rank_occurances[card.number] == 3:
          self.high_card = card
        else:
          self.kickers.append(card)


    
    elif (rank_occurances.values().count(2) == 2):
      self.evaluation = 'two pair'
      possible_high_cards = []
      for card in self.hand:
        if (rank_occurances[card.number] == 2 and card not in possible_high_cards):
          possible_high_cards.append(card)
        else:
          self.kickers = [card]
      self.high_card = possible_high_cards[1]

    elif (2 in rank_occurances.values()):
      self.evaluation = 'pair'
      self.kickers = []
      for card in self.hand:
        if (rank_occurances[card.number] == 2):
          self.high_card = card
        else:
          self.kickers.append(card)



    else:
      self.evaluation = 'high'
      self.high_card = self.hand[4]
      self.kickers = self.hand[0:4] 
    
    print self.evaluation, self.high_card
    if self.kickers != None:
      for kicker in  self.kickers:
        print str(kicker)

  def check_flush(self):
    hand_suits = []
    for card in self.hand:
      hand_suits.append(card.suit)
    print hand_suits
    if len(set(hand_suits)) == 1:
      return True
    else:
      return False



  def check_straight(self):

    if (len(set(self.hand_ranks)) == 5 and (self.hand_ranks[4] == self.hand_ranks[0]+4)):
      return True
    else:
      return False




class PokerGame:

    
  def compare_hands(self, hand1, hand2):
    hand1.evaluate_hand()
    print hand1.evaluation, hand1.high_card.number
    hand2.evaluate_hand()
    print hand2.evaluation, hand2.high_card.number
    if hand1.hand_order.index(hand1.evaluation) > hand2.hand_order.index(hand2.evaluation):
      return 'Player 1'
    elif hand1.hand_order.index(hand1.evaluation) < hand2.hand_order.index(hand2.evaluation):
      return 'Player 2'
    else:
      if hand1.high_card.rank > hand2.high_card.rank:
        return 'Player 1'
      elif hand2.high_card.rank >hand1.high_card.rank:
        return 'Player 2'
      else:
        return self.compare_kickers(hand1, hand2)

  def compare_kickers(self, hand1, hand2):
    hand1_kickers = []
    for card in hand1.kickers:
      hand1_kickers.append(card.rank)
    hand2_kickers = []
    for card in hand2.kickers:
      hand2_kickers.append(card.rank)
    hand1_kickers.reverse()
    hand2_kickers.reverse()

    for i in range(0, len(hand1_kickers)):
      if hand1_kickers[i] > hand2_kickers[i]:
        return 'Player 1'
      elif hand1_kickers[1] > hand2_kickers[i]:
        return 'Player 2'
      elif i == len(hand1_kickers)-1 :
        return 'Tie'


  def deal(self, players):
    deck = Deck()
    self.player_hands = []
    for i in range(0, players):
      hand = deck.card_list.pop()+ ' '
      for j in range(1, 5):
        hand  += deck.card_list.pop()+' '

      hand = hand[0:len(hand)-1]
      self.player_hands.append(PokerHand(hand))
#    return player_hands


     
