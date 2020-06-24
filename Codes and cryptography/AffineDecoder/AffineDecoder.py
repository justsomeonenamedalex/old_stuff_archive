old_letter = ("")
new_letter = ("")
old_letter_num = 0
new_letter_num = 0
starttext = []
endtextlist = []
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
awnser = ("n")
coprimes=[1,3,5,7,9,11,15,17,19,21,23,25]


n = 26 #size of allhapbet
a = 1 #comprime with b
apos = 0
b = 1 # between 0 and n-1
c = 0 # modular multiplicative of a
# Encryption(L) = (AL+B)modulusN

#text = input("Start text")
text=("GYN OFCNDAG")
text=text.lower()
starttext = list(text)

#b = int(input("b is"))

#decoding

def check():
    endtextlist = []
    #a = random.randint(1,26)
    #b = random.randint(1,25)
    print("a is "+str(a))
    print("b is "+str(b))
    c = 21
    print("c is "+str(c))
    for i in range (0,len(starttext)):
        old_letter=(starttext[i])
        #print("old letter is"+old_letter)
        if old_letter not in alphabet:
            endtextlist.append(old_letter)
        else:
            old_letter_num = alphabet.index(old_letter)
            #print("old letter num is "+str(old_letter_num))
            x = old_letter_num
            new_letter_num = (c*(x-b))%n
            #print("new letter num is "+str(new_letter_num))
            new_letter = alphabet[new_letter_num]
            endtextlist.append(new_letter)
    endtext = ''.join(endtextlist)
    print(endtext)





def confirm():

    awnser = input("y/n?")
    if awnser == ("n"):
        check()


def increase():
    b=b+1

check()
while awnser == ("n"):
    
    b=b+1

    confirm()





