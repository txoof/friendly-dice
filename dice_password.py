#!/usr/bin/python
import random, string

myrg=random.SystemRandom()

# words - number of words in password 
def passGen(words=5):
  password=''
  myfile=open('diceware8K_edit.txt')
  array=myfile.read().splitlines()

  for i in range(0, words):
    word=array[myrg.randrange(0, len(array)-1)]
    password=password+word+' '
  return(password)

def addFeatures():
  string.letters='ABCDEFGHJKMNPQRSTUVWXYZ'
  feature=myrg.choice(string.letters)
  feature=feature+str(myrg.randint(2, 9))
  return(feature)



  

def main():
  passwords=100
  for j in range(0, passwords):
    password=passGen(2)
    password=password+addFeatures()
    print password

main()
