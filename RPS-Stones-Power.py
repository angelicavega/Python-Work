#Problem Set 1
#Name: Angelica Vega-Aponte
#Time Spent: 1 hour
#Last Modified: Sept. 27, 2017
def rps():

    s = 'scissor'
    p = 'paper'
    r = 'rock'
    player1 = input ('player1 Rock, Paper, or Scissors?')
    player2 = input ('player2 Rock, Paper, or Scissors?')

    if (player1 != r and player1 != p and player1 != s) or \
       (player2 != r and player2 != p and player2 != s):

        print("invalid input. This player must choose from 'rock' , 'paper', and 'scissor'.")
    else:
        if (player1 == player2):
            print('tie')
        elif (player1 == 'rock' and player2== 'scissor') or\
        (player1 == 'scissor' and player2 == 'paper') or\
        (player1 == 'rock' and player2 == 'paper'):
            print('player1 wins')
        else:
            print('player2 wins')

#Problem Set 2
#Name: Angelica Vega-Aponte
#Time Spent: 90 minutes
#Last Modified: Sept. 27, 2017
def stones():
    stones = 100
    while  (stones > 0):
        while(True) :
            p1input = int(input('player 1 input a number between 1 and 5: '))
            if(p1input <=5):
                stones = stones - p1input
                print("in p1")
                print("stones: " + str(stones))
                break

        if stones == 0:
            break

        while  (stones > 0):
            p2input = int(input('player 2 input a number between 1 and 5: '))
            if(p2input <=5):
                stones = stones - p2input
                break
    print(stones)
    print('no more stones')
    
    


#Problem Set 3
#Name: Angelica Vega-Aponte
#Time Spent: 2 hours
#Last Modified: Sept. 27, 2017

def power():

    pwr = 2
    root = 1
    ans = 0

    x = int(input('Enter a positive integer: '))
    while 0< pwr <6:
    #increasing the pwr
        while root**pwr<=(x):
    #increasing the loop
            root=root+1
            #print 'root is:', root
            #print 'power is:', pwr
            if root **pwr==(x):
                print('the root is', root)
                print('the pwr is', pwr)
                ans = 1
    #because you to restart to loop
                root = 1
                pwr = pwr+1

    if ans != 1:
            print('No pair found')


#Problem Set 4
#Name: Angelica Vega-Aponte
#Time Spent: 30 minutes
#Last Modified: Sept. 27, 2017

def F(n):
    if n <= 1:
        return n
    else:
        return(F(n - 1) + F(n-2))

for i in range(10):
    print(F(i))
    


rps()
stones()
power()

