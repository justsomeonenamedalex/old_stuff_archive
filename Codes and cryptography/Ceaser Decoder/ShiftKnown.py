#variables and lists


old_letter = ("")
new_letter = ("")
old_letter_num = 0
new_letter_num = 0
shiftvalue = 0
starttext = []
endtextlist = []
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# 26 letters in alphabet


#inputs

shiftvalue = input("What is the shift value?")

input = input("Start text").lower()


#print("Input is: "+ input)
starttext = list(input)
#print("startext is:")
#print(starttext)

starttext_length = len(starttext)

for i in range (0,starttext_length):
    old_letter=(starttext[i])
    if old_letter not in alphabet:
        endtextlist.append(old_letter)
    else:
        old_letter_num = alphabet.index(old_letter)
        new_letter_num = (old_letter_num)+(int(shiftvalue))
        if new_letter_num >= 25:
            new_letter_num = (new_letter_num)-26
        new_letter = alphabet[new_letter_num]
        #print(new_letter)
        endtextlist.append(new_letter)

endtext = ''.join(endtextlist).upper()
print(endtext)
