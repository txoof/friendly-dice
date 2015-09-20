#!/usr/bin/python
import random, string


# words - number of words in password 
def passGen(words=5):
  password=''
  myrg=random.SystemRandom()
  myfile=open('diceware8K_edit.txt')
  array=myfile.read().splitlines()

  for i in range(0, words):
    word=array[myrg.randrange(0, len(array)-1)]
    password=password+word+' '
  return(password)

def addFeatures():
  myrg=random.SystemRandom()
  feature=''
  

def main():
  passwords=100
  for j in range(0, passwords):
    password=passGen(3)
    print password

main()
