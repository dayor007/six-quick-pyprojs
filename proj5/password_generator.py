import random

print('Welcome to your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?-_0123456789'

number = input('Amount of passwords to generate: ')
number = int(number)

length = input('Please input your password length')
length = int(length)

print('\nhere are your password(s): ')

for p in range(number):
    passwords = ''
    for c in range (length):
        passwords += random.choice(chars)
    print(passwords)

