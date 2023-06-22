import random

cipheredtext = []
desire = "cipher"
characterlist = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
newcharacterlist = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
if desire == "cipher":
  text = input("input desired text:")
  print("what is the key you would like to use to generate the ciphered text?")
  key = input("make sure it's somthing you will remember: ")
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
      testtext = text[abc].replace(characterlist[cycle], newcharacterlist[cycle])
      cycle += 1
    cipheredtext.append(testtext)
    abc +=1
  print("".join(cipheredtext))