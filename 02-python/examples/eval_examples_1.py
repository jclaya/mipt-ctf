#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

num = random.randint(1, 100)

print "Guess the number! 1 to 100."

while True:
  guess = input('Your guess> ')
  if guess != num:
    print "Nope,", guess, "is wrong."
  else:
    print "You win!"
    break
