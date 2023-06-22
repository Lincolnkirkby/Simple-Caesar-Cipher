import random
cipheredtext = []
characterlist = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
newcharacterlist = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
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

if desire == "cipher":
  textinputstr = "input the text you wish to be ciphered:"
  keyinputstr = "what is the key you would like to use to generate the ciphered text? \n make sure it's somthing you will remember:"
if desire == "decipher":
  textinputstr = "input the text you wish to be deciphered:"
  keyinputstr = "what was the key used to generate the ciphered text?"
text = input(textinputstr)
key = input(keyinputstr)
random.seed(key)
random.shuffle(newcharacterlist)
textlength = len(text)
newtext = text
abc = 0
while abc < textlength:
  cycle = 0
  testtext = newtext[abc]
  while cycle < 26:
    if testtext != text[abc]:
      cycle = 26
      continue
    if desire == "cipher":
      testtext = text[abc].replace(characterlist[cycle], newcharacterlist[cycle])
    if desire == "decipher":
      testtext = text[abc].replace(newcharacterlist[cycle], characterlist[cycle])
    cycle += 1
  cipheredtext.append(testtext)
  abc +=1
print("".join(cipheredtext))