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

print("Welcome to the simple offline cipher/decipher\n----------------------------------------------------------------")
#^friendly introduction
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
#^ used to determine the desire of the user, a.k.a whether they want to cipher or decipher

if desire == "cipher":
  textinputstr = "please input the text you wish to be ciphered:"
  keyinputstr = "----------------------------------------------------------------\nwhat is the key you would like to use to generate the ciphered text? \nmake sure it's something you will remember:"

#^ text to only be displayed if ciphering
if desire == "decipher":
  textinputstr = "please input the text you wish to be deciphered:"
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
#^I had no idea what to call this variable, but its purpose is to only read and compare lists on one single character at a time, rather than the whole list at once, this stops the problems I was having before I implimented it, for example if I had affected the whole text at once and changed all a's with b's but later on replaced all b's with c's then all a's will have also become c's wich is undesireable, as not only would the text contain a lot more duplicate characters but it would be almost impossible to decipher the text back to its original state, as there would be no way to dissern a c thats meant to be an a from a c thats meant to be a b
while abc < textlength:
  cycle = 0
  #^variable used to count how many characters in the (new)characterslist have been compared
  testtext = newtext[abc]
  #^ creates a testing variable based off of the abc-th  character in the newtext string
  while cycle < 87:
    #^ 87 is the number of characters in the characters list, we dont want it counting higher than that because there is nothing for the program to read
    if testtext != text[abc]:
      #^this checks if the chacter has been successfully changed or not
      cycle = 87
      #^ this is just to make sure it exits the while loop
      continue
    if desire == "cipher":
      testtext = text[abc].replace(characterlist[cycle],
                                   newcharacterlist[cycle])
      #^ if the user is ciphering we replace the character in the text if it alighns with the character in the cycles slot of the character list with the same numberd character in the newcharacterlist(the one thats been changed)
    if desire == "decipher":
      testtext = text[abc].replace(newcharacterlist[cycle],
                                   characterlist[cycle])
      #^ if the user is deciphering we replace the character in the text if it alighns with the character in the cycles slot of the newcharacterlist with the same numberd character in the character list(the default one)
    cycle += 1
    #^ increases the cylce variable making it now compare the next character in each list with the current character in the str
  cipheredtext.append(testtext)
  #^this triggers when the cycle is over (a.k.a the character in both lists are identacle) or if the character in the new str is different than the inputed str
  abc += 1
  #^ makes the code now affect the next letter in the original str
print("----------------------------------------------------------------\nthe "+desire+"ed version of",text,"using the key:"+key,"is:")
print("".join(cipheredtext))
#^prints the final newly ciphered/deciphered text