import random

desire = "null"
while desire == "null":
  desire = input("do you want to cipher text or do you want to decipher text?").lower()
  if desire == "cipher" or desire == "c":
    desire = "cipher"
    continue
  elif desire == "decipher" or desire == "d":
    desire = "decipher"
    continue
  else: 
    desire = "null"
    print("error, only acceptable inputs are \"chipher\",\"decipher\",\"c\" and \"d\"")