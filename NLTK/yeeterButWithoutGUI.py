from textblob import TextBlob
#TODO make this less of a cr*p mess

# kwargs are used to define the word types of the replacments

def yeet(text, yeetNouns = False, yeetVerbs = False, yeetAdj = False, yeetAdv = False):
    replacements = {}
    blob_object = TextBlob(text)
    tags = blob_object.tags

    split_text = []
    temp_word = []
    for count, character in enumerate(text):
        if character.isalpha() and count == len(text)-1:
            temp_word.append(character)
            split_text.append("".join(temp_word))
        elif character.isalpha():
            temp_word.append(character)
        else:
            split_text.append("".join(temp_word))
            temp_word = []
            split_text.append(character)
            
    tokens = split_text
    
    #tokens is the correct spliting of the text, equivalent to tokens

    words = [i for i in tokens if i.isalpha()]

    if yeetNouns:
        replacements['NN'] = "yeet"
        replacements['NNS'] = "yeets"
        replacements['NNP'] = "Yeet"
        
    if yeetVerbs:
        replacements['VBD'] = "yote"
        replacements['VBG'] = "yeeting"
        replacements['VBN'] = "yeeted"
        replacements['VBP'] = "yeets"

    if yeetAdj:
        replacements['JJ'] = "yeeting"
        replacements['JJR'] = "yeeter"
        replacements['JJS'] = "yeetest"

    if yeetAdv:
        replacements['RB'] = "yeetley"
        replacements['RBR'] = "yeeter"
        replacements['RBS'] = "yeetest"



    output = []
    # tokens is the split text
    print([(i, x) for i, x in enumerate(tokens)])
    for position, token in enumerate(tokens):
        if token in words:
            position = words.index(token)
            print(f"position is {position} and token is {token}")
            tag = tags[position][1]
            if tag in replacements:
                if token[0].isupper():
                    # upper case the word
                    new_word = list(replacements[tag])
                    new_word[0] = new_word[0].upper()
                    new_word = "".join(new_word)
                    output.append(new_word)

                else:
                    new_word = replacements[tag]
                    output.append(new_word)
            else:
                output.append(token)
        else:
            output.append(token)
    done = "".join(output)
    print(done)
