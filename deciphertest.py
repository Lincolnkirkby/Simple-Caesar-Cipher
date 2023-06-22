import random

decipheredtext = []
desire = "decipher"
characterlist = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
newcharacterlist = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
if desire == "decipher":
  text = input("input ciphered text:")
  key = input("what was the key used to generate the ciphered text?")
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
      testtext = text[abc].replace(newcharacterlist[cycle], characterlist[cycle])
      cycle += 1
    decipheredtext.append(testtext)
    abc +=1
print("".join(decipheredtext))