''' Implements a class called Player that represents a cricket player.The Player class should have method called play() which prints "The player is playing cricket Derive two classes . Batsman and Bowler, from the player class ,
Override the play() method in each derived class to print "The batsman is batting" and  "The bowler is bowling", respectively .
Write a program to create object of both the Batsman and Bowler classes and call the play() method for each object'''

# Define the base class Player 
class Player:
    def play(self):
        print("The player is playing cricket.")

# Define the derived class Batman
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

# Define the derived class Bowler
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Create object of Batman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# call the play() method for 
batsman.play()
bowler.play()