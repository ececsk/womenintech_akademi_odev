import nltk
import string
nltk.download('punkt')

textLines=open("all_data.txt","r",encoding='utf-8').readlines()

replaceCharacters={'ş':'s','ı':'i','ö':'o','ğ':'g','ç':'c','ü':'u','İ':'i'} 

newLines=[]

for line in textLines:
  line=nltk.sent_tokenize(line)
  for sentence in line:
    newLines.append(sentence+'\n') 

for i in range(len(newLines)):
  line=newLines[i]
  if not line.isdigit():
    newLines[i]="".join(list(filter(lambda char:char not in string.punctuation,line.lower().translate(line.maketrans(replaceCharacters)))))

finalLines=set(newLines)
open("cleanedData.txt","w",encoding='utf-8').writelines(finalLines)
