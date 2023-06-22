import random

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
  key = input("or if you want a random key type \"xxx\":")
  if key == "xxx":
    key = random.randint(1, 2704)
    print("your randomly generated key is:", str(key), "try not to forget it")
  random.seed(key)
  random.shuffle(newcharacterlist)
  cycle = 0
  while cycle < 26:
    text = text.replace(characterlist[cycle], newcharacterlist[cycle])
    cycle += 1
  print(text)