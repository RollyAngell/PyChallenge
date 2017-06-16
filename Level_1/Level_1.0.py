import string

abecedario=string.ascii_lowercase

def contrase(text, offset):
    hack=[]
    for i in text:
        if i not in " .'()":
            a=(abecedario.index(i)+ offset) % len(abecedario)
            hack.append(abecedario[a])
        else:
            hack.append(i)
    return ''.join(hack)

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(contrase(text, offset=2))

            
