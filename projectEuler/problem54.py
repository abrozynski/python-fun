import poker

def problem54():
  
  player_1_wins = 0
  player_2_wins = 0
  ties = 0


  infile = open('poker.txt')
  outinfo=[]
  for line in infile:
    agame = poker.PokerGame()
    hand1 = poker.PokerHand(line[0:14])
    hand2 = poker.PokerHand(line[15:len(line)-2])
    result = agame.compare_hands(hand1, hand2)
    if result == 'Player 1':
      player_1_wins += 1
      outinfo.append([hand1.show_hand(), hand1.evaluation, hand2.show_hand(), hand2.evaluation])

#    outinfo.append([hand1.show_hand(),hand1.evaluation, hand2.show_hand(),hand2.evaluation, result])
      

  print player_1_wins, player_2_wins, ties
  return outinfo
