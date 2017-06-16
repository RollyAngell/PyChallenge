from string import ascii_lowercase

letters = {value: index for index, value in enumerate(ascii_lowercase)}

def shift(text, amount=13):
    mapping = str.maketrans(ascii_lowercase, "".join(ascii_lowercase[(i+amount) % 26] for i in range(26)))
            
    return text.translate(mapping)
    
if __name__ == "__main__":
    print(shift("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.", 2))
    print(shift("map", 2))
