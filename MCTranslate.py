#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 19:25:02 2018

@author: charlesvantassel
"""

morse_alphabet = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.',
                  'G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..',
                  'M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.',
                  'S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
                  'Y':'-.--','Z':'--..','0':'-----','1':'.----','2':'..---',
                  '3':'...--','4':'....-','5':'.....','6':'-....','7':'--...',
                  '8':'---..','9':'----.','Ä':'.-.-','Á':'.--.-','Å':'.--.-',
                  'É':'..-..','Ñ':'--.--','Ö':'---.','Ü':'..--','&':'.-...',
                  '\'':'.----.','@':'.--.-.',')':'-.--.-','(':'-.--.',':':'---...',
                  ',':'--..--','=':'-...-','.':'.-.-.-','-':'-....-',
                  '+':'.-.-.','\"':'.-..-.','?':'..--..','/':'-..-.', ' ':' '}

morse_alph_reverse = {value:key for key,value in morse_alphabet.items()}

#translates string to morse code
def to_morse(to_trans):
    print()
    print("Translation:")
    to_trans = to_trans.upper()
    translated = ' '
    try:
        for char in to_trans:
            translated += morse_alphabet[char] + ' '
    except:
        print('Sorry, the message you typed is not able to be translated. Please try again.')
        print()
        to_morse(str(input("Please type the message you would like translated into Morse code: ")))
    return translated

#translates morse code into alphanumerical characters
"""def from_morse(to_trans):
    print()
    print("Translation:")
    translation = ''
    try:
        for i in to_trans:
            if i == ' ' and i + 1 == ' ':
                translation.join(' ')
            else:
                translation.join(morse_alph_reverse.get(i) for i in to_trans.split())
        return translation
    except:
        print('Sorry, the message you typed is not able to be translated. Please try again.')
        print()
        from_morse(str(input("Please type the message you would like translated from Morse code (separate letters by one space and words by two spaces): ")))"""
def from_morse(to_trans):
    print()
    print("Translation:")
    try:
        return ''.join(morse_alph_reverse.get(i) for i in to_trans.split())
    except:
        print('Sorry, the message you typed is not able to be translated. Please try again.')
        print()
        from_morse(str(input("Please type the message you would like translated from Morse code (separate letters by one space and words by two spaces): ")))

#FULL PROGRAM
again = True
while again == True:
    choice = input("Would you like to translate a message FROM morse code, or TO morse code? ")
    if choice.upper() == 'FROM' or choice.upper() == 'F':
        print(from_morse(str(input("Please type the message you would like translated into Morse code (separate letters by one space and words by two spaces): "))))
        print()
        another = input("Would you like to translate another? ")
        if another.upper() == 'YES' or another.upper() == 'Y':
            again = True
        else:
            again = False
    elif choice.upper() == 'TO' or choice.upper() == 'T':
        print(to_morse(str(input("Please type the message you would like translated into Morse code: "))))
        print()
        another = input("Would you like to translate another? ")
        if another.upper() == 'YES' or another.upper() == 'Y':
            again = True
        else:
            again = False
    else:
        print("Sorry, that is not an option, please try again.")
        print()
        again = True

