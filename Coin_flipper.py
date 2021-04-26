from random import *
#Flip a coin randomly and return 'H' for heads or 'T' for tails
def coinFlip():
  if randrange(2)==0:
    return 'Heads'
  return 'Tails'
print(coinFlip)
