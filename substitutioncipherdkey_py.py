# -*- coding: utf-8 -*-
"""substitutioncipherdkey.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kN5ZsOkNSpYxQki25240er6hxiJooyp6
"""

from itertools import permutations

my_list = [1,3,5]

list_of_permutations = permutations(my_list)

cnt = 0

for permutations in list_of_permutations:
  cnt+=1
  print(len(my_list,cnt))

def faculty(n):
  if n==1:
    return 1
  else:
    return faculty(n-1)*n

def counter(n):
  cnt=0
  for i in range(n):
    cnt+=1
    return cnt
    cProfile.run("counter(faculty(11))")

from types import GeneratorType
import random

def generate_key():
 letters = "ABCDEFGHIJKLMNOPQRSTWXYZ"
 cletters = list(letters)
 key = ()
 for c in letters:
  key[c] = cletters.pop(random,randint(0, len(cletters)-1))
  return key
  key = generate_key()
  print(key)
  
  def encrypt(key,message):
    cipher =""
    for c in message:
      if c in key:
        cipher += key[c]
      else:
        cipher+=""
        return cipher
        
        def get_decrypt_key(key):
          dkey = {}
          for k in key:
            dkey[key[k]] = k
            return dkey
        key = generate_key()
        print(key)
        message = "YOU ARE AWESOME"
        cipher = encrypt(key,message)
        print(cipher)
        dkey = get_decrypt_key(key)
        message = encrypt(dkey,cipher)
        print(message)