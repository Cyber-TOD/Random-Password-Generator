import random
r = random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
length = int(input('How many charachters should your password have? '))
much = int(input('How many passwords do you want? '))

for p in range(much):
    password = ''
    for c in range(length):
        password += r.choice(chars)
    print(password)
