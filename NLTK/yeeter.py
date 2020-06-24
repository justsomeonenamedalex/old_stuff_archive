from textblob import TextBlob
text = input("input")
#print(text)
blob_object = TextBlob(text)
tags = blob_object.tags
#print(split_text)
#print(tags)
'''
replacements = {
    "JJ":"yeeting",
    "JJR":"yeeter",
    "JJS":"yeetest",
    "NN":"yeet",
    "NNS":"yeets",
    "NNP":"Yeet",
    "RB":"yeetly",
    "RBR":"yeeter",
    "RBS":"yeetest",
    "UH":"yeet",
    "VB":"yeet",
    "VBD":"yote",
    "VBG":"yeeting",
    "VBN":"yeeted",
    "VBP":"yeets"
}
'''


replacements = {
    "NN":"yeet",
    "NNS":"yeets",
    "NNP":"Yeet",
    "VB":"yeet",
    "VBD":"yote",
    "VBG":"yeeting",
    "VBN":"yeeted",
    "VBP":"yeets"
}
print("")
print("")
print("")
print("")


output = [replacements[i[1]] if i[1] in replacements else i[0] for i in tags]
print(" ".join(output))


def splitting(text):
    output = []
    word = []
    for i in text:
        if i.isalpha():
            word.append(i)
        else:
            output.append("".join(word))
            word = []
            output.append(i)
    return output
