# Reflex Based Vaccum Cleaner
def SimpleReflex_VacuumCleaner(location,status):
 if status=="Dirty":
    return "Suck"
 if location=="A":
     return "Move right"
 else:
    return "Move left"
rooms={"A":"Dirty","B":"Dirty"}
location="A"
print("Initial Environment:",rooms)
print("Initial location:",location)
for i in range(6):
    status=rooms[location]
    action=SimpleReflex_VacuumCleaner(location,status)
    print("Location:",location,"|Status:",status,"|Action:",action)
    if action=="Suck":
        rooms[location]="Clean"
    elif action=="Move right":
        location="B"
    elif action=="Move left":
        location="A"
print("Final Environment:",rooms)

# Output
Initial Environment: {'A': 'Dirty', 'B': 'Dirty'}
Initial location: A
Location: A |Status: Dirty |Action: Suck
Location: A |Status: Clean |Action: Move right
Location: B |Status: Dirty |Action: Suck
Location: B |Status: Clean |Action: Move left
Location: A |Status: Clean |Action: Move right
Location: B |Status: Clean |Action: Move left
Final Environment: {'A': 'Clean', 'B': 'Clean'}



#///////////////////////////////////////////////////////////////////////////////////////////////////

# Goal Based Vacuum Cleaner
def goal_based_agent(state):

    if state["A"] == "Dirty":

        if location == "A":
            return "Suck"
        else:
            return "Move Right"

    elif state["B"] == "Dirty":

        if location == "B":
            return "Suck"
        else:
            return "Move Left"

    else:
        return "Stop"
rooms = {
    "A": "Dirty",
    "B": "Dirty"
}
location = "A"
print("Initial Environment:",rooms)
print("Initial location:",location)
for i in range(6):

    state = rooms

    action = goal_based_agent(state)

    print("Location:", location,
          "| Status:", rooms[location],
          "| Action:", action)

    if action == "Suck":
        rooms[location] = "Clean"

    elif action == "Move Right":
        location = "B"

    elif action == "Move Left":
        location = "A"

    elif action == "Stop":
        break


# Output
Initial Environment: {'A': 'Dirty', 'B': 'Dirty'}
Initial location: A
Location: A | Status: Dirty | Action: Suck
Location: A | Status: Clean | Action: Move Left
Location: A | Status: Clean | Action: Move Left
Location: A | Status: Clean | Action: Move Left
Location: A | Status: Clean | Action: Move Left
Location: A | Status: Clean | Action: Move Left


#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# Tic-Tac-Toe
import random

board = [" "] * 9

human = input("Choose X or O: ").upper()

if human == "X":
    computer = "O"
else:
    computer = "X"


def display():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def win(x):

    if (board[0] == x and board[1] == x and board[2] == x) or \
       (board[3] == x and board[4] == x and board[5] == x) or \
       (board[6] == x and board[7] == x and board[8] == x) or \
       (board[0] == x and board[3] == x and board[6] == x) or \
       (board[1] == x and board[4] == x and board[7] == x) or \
       (board[2] == x and board[5] == x and board[8] == x) or \
       (board[0] == x and board[4] == x and board[8] == x) or \
       (board[2] == x and board[4] == x and board[6] == x):

        return True

    return False


# Goal-Based Agent
def computerChoice():

    # Try to win
    for i in range(9):

        if board[i] == " ":

            board[i] = computer

            if win(computer):
                board[i] = " "
                return i

            board[i] = " "

    # Try to block HUMAN
    for i in range(9):

        if board[i] == " ":

            board[i] = human

            if win(human):
                board[i] = " "
                return i

            board[i] = " "

    # Choose any empty position
    while True:

        pos = random.randint(0, 8)

        if board[pos] == " ":
            return pos


# Main game
for turn in range(9):

    display()

    # HUMAN TURN
    if turn % 2 == 0:

        while True:

            position = int(input("Enter position (1-9): ")) - 1

            if board[position] == " ":
                board[position] = human
                break

            else:
                print("Position already occupied! Try again.")

        if win(human):
            display()
            print("Human Wins!")
            break

    # COMPUTER TURN
    else:

        pos= computerChoice()

        board[pos] = computer

        print("Computer chose:", pos + 1)

        if win(computer):
            display()
            print("Computer Wins!")
            break

else:

    display()
    print("Game is a Draw!")

#Output
Choose X or O: X

  |   |  
--+---+--
  |   |  
--+---+--
  |   |  

Enter position (1-9): 1

X |   |  
--+---+--
  |   |  
--+---+--
  |   |  

Computer chose: 7

X |   |  
--+---+--
  |   |  
--+---+--
O |   |  

Enter position (1-9): 5

X |   |  
--+---+--
  | X |  
--+---+--
O |   |  

Computer chose: 9

X |   |  
--+---+--
  | X |  
--+---+--
O |   | O

Enter position (1-9): 8

X |   |  
--+---+--
  | X |  
--+---+--
O | X | O

Computer chose: 2

X | O |  
--+---+--
  | X |  
--+---+--
O | X | O

Enter position (1-9): 3

X | O | X
--+---+--
  | X |  
--+---+--
O | X | O

Computer chose: 6

X | O | X
--+---+--
  | X | O
--+---+--
O | X | O

Enter position (1-9): 4

X | O | X
--+---+--
X | X | O
--+---+--
O | X | O

Game is a Draw!



Rishi Kumar Chourasia 1BF24CS253

