import random
#^ random is used to generate random numbers
cipheredtext = []
#^is the output used at the very end to display the ciphered/deciphered text
characterlist = [
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
  'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4',
  '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(',
  ')', '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', ',', '.', '/', '<',
  '>', '?'
]
#^list used to determine all characters affected
newcharacterlist = [
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
  'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4',
  '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(',
  ')', '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', ',', '.', '/', '<',
  '>', '?'
]
#^ this list is randomized and then compared to the original list for each character within the desired text

desire = "null"
#^ variable used to read whether the user is deciphering or ciphering text
while desire == "null":
  desire = input(
    "do you want to cipher text or do you want to decipher text? ").lower()
  if desire == "cipher" or desire == "c":
    desire = "cipher"
    continue
  elif desire == "decipher" or desire == "d":
    desire = "decipher"
    continue
  else:
    desire = "null"
    print(
      "error, only acceptable inputs are \"cipher\",\"decipher\",\"c\" and \"d\""
    )
#^ sed to determine the desire of the user, a.k.a whether they want to cipher or decipher

if desire == "cipher":
  textinputstr = "input the text you wish to be ciphered:"
  keyinputstr = "what is the key you would like to use to generate the ciphered text? \n make sure it's something you will remember:"

#^ text to only be displayed if ciphering
if desire == "decipher":
  textinputstr = "input the text you wish to be deciphered:"
  keyinputstr = "what was the key used to generate the ciphered text?"
#^ text to only be displayed if deciphering

text = input(textinputstr)
#^ the text to be ciphered or deciphered depending on the desire of the user
key = input(keyinputstr)
#^ used to determine the seed, which controls the randomness of the output, so that it can be replicated everytime using the same key
random.seed(key)
#^ sets the key as the seed
random.shuffle(newcharacterlist)
#^ randomizes the newcharacterlist based off of the seed to later be compared to the original list
textlength = len(text)
#^ gathers the length of the list to be used later on
newtext = text
#^ this text will be used to compare the original text to the new one
abc = 0
#^I had no idea what to call this variable, but its purpose is to only read and compare lists on one single character at a time, rather than the whole list at once, this stops the problems I was having before I implimented it, for example if I had affected the whole text at once and changed all a's with b's but later on replaced all b's with c's then all a's will have also become c's wich is undesireable, as not only would the text contain a lot more duplicate characters but it would be almost impossible to decipher the text back to its original state
while abc < textlength:
  cycle = 0
  testtext = newtext[abc]
  while cycle < 87:
    if testtext != text[abc]:
      cycle = 87
      continue
    if desire == "cipher":
      testtext = text[abc].replace(characterlist[cycle],
                                   newcharacterlist[cycle])
    if desire == "decipher":
      testtext = text[abc].replace(newcharacterlist[cycle],
                                   characterlist[cycle])
    cycle += 1
  cipheredtext.append(testtext)
  abc += 1
print("".join(cipheredtext))