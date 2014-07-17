class TicTacToe:
  

  def __init__(self):
    print 'Would you like to play a game?'
    self.players=[player('X'), player('O')]
    self.gameBoard = board()
    self.current_turn = 0
 #   self.playGame()



  def takeTurn(self, current_player):
   print "Current Player: " + current_player.symbol
   index = int(raw_input("Choose: "))
   if self.gameBoard.spaceFree(index) == True:
    self.gameBoard.takeSpace(index, current_player.symbol)
   else:
    print "Choose Better"
    return self.takeTurn(current_player)

   
  def playGame(self):
   winner = self.gameOver()
   if winner == 'nobody':
    self.current_player = self.players[self.current_turn % len(self.players)]
    self.gameBoard.show()
    self.takeTurn(self.current_player)
    self.current_turn += 1
    return self.playGame()
   else:
    print "Congratulations " + winner


  def gameOver(self):
   #Note to self: make this better with math   

   winning_index_sets = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]]

   for x in winning_index_sets:
    boardRow = []
    for i in x:
     boardRow.append(self.gameBoard.state[i])
    if ((len(set(boardRow)) == 1) and (boardRow[0] != ' ')):
     winner = boardRow[0]
     break
   else:
     winner = 'nobody'
   return winner
   



class player:
  
  def __init__(self, _symbol):
   self.symbol = _symbol


class board:

  def __init__(self):
    self.state = []
    for i in range(0, 9):
     self.state.append(' ')

  def spaceFree(self, index):
    if (self.state[index] == ' '):
      return True
    else:
      return False

  def takeSpace(self, index, symbol):
   self.state[index] = symbol

  def show(self):
   print self.state[0] + "|" + self.state[1] + "|" + self.state[2]
   print '---------'
   print self.state[3]+ "|" + self.state[4] + "|" +  self.state[5]
   print '---------'  
   print self.state[6]+ "|" + self.state[7]+ "|" + self.state[8]
