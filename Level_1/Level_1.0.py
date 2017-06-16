import string

alphabet = string.ascii_lowercase

def shift(text, offset):
    shifted = []
    for letter in text:
        if letter not in " .'()":
            i = (alphabet.index(letter) + offset) % len(alphabet)            
            shifted.append(alphabet[i])
        else:
            shifted.append(letter)
    return ''.join(shifted)

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(shift(text, offset=2))  
