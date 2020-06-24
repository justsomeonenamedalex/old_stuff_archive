#imports
#import randint
import random
from spellchecker import SpellChecker
spell = SpellChecker()

#variables and lists


old_letter = ("")
new_letter = ("")
old_letter_num = 0
new_letter_num = 0
shiftvalue = 0
starttext = []
endtextlist = []
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet_shuffle = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
cont = True
crypto_alphabet_final = ["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"]
crypto_alphabet_temp = ["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"]
crypto_alphabet_left = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
starttextwords = []
currentwordlist = []
currentword = ("")


# 26 letters in alphabet






#read input
input = input("Start text (end with space)").lower()
starttext = list(input)


#seperate text
for i in range(0,len(starttext)):
    #print(currentwordlist)
    if starttext[i] in alphabet:
        currentwordlist.append(starttext[i])
    elif starttext[i] == (" "):
        currentword = (''.join(currentwordlist))
        #print(currentword)
        starttextwords.append(currentword)
        currentwordlist = []
        currentword = ("")

#sort list
starttextwords.sort(key=len, reverse = True)

# decode text
for i in range(0,len(starttextwords)):
    #sync temp list with final
    for l in range(0,len(alphabet)):
        crypto_alphabet_temp[l] = crypto_alphabet_final[l]
    #add new random letter
    #shuffle alphabet
    while guessing == True:
        random.shuffle(crypto_alphabet_left)
        crypto_alphabet_temp = crypto_alphabet_left
    
    
#shuffle alphabet
random.shuffle(alphabet_shuffle)
crypto_alphabet_temp = alphabet_shuffle

print(alphabet)
print(crypto_alphabet_temp)
#print(starttextwords)
