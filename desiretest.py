desire = "null"
while desire == "null":
  desire = input("do you want to cipher text or do you want to decipher text?").lower()
  if desire == "cipher" or desire == "c":
   continue
  elif desire == "decipher" or desire == "d":
   continue
  else: 
    desire = "null"
    print("error, only acceptable inputs are \"chipher\",\"decipher\",\"c\" and \"d\"")
print(desire)