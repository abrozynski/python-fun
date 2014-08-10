import poker

def problem54():
  
  player_1_wins = 0

  infile = open('poker.txt')
  for line in infile:
    agame = poker.PokerGame()
    hand1 = poker.PokerHand(line[0:14])
    hand2 = poker.PokerHand(line[15:len(line)-2])
    if agame.compare_hands(hand1, hand2) == 'Player 1':
      player_1_wins += 1

  return player_1_wins
