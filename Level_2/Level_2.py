data =open('ocr.txt')

outDict = {}

for i in data:
  try:
    outDict[i] = outDict[i] + 1
  except:
    outDict[i] = 1
print (outDict)
