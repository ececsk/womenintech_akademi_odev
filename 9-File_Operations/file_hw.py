BHARFX = "Iİ"
KHARFX = "ıi"
PUNCTUATION = set("\"\'\.,/\\&%\+!\*/=(){}[]-_–:;?«»<>|^—¦’‘“·”…~′#`´­")
DIGITS = list("0123456789.,")
def lowerCaseLetter(sozcuk):
    ss = ''
    for i in range(len(sozcuk)):
        ok = False
        for j in range(len(BHARFX)):
            if sozcuk[i]== BHARFX[j]:
                ss += KHARFX[j]
                ok = True
                break
        if ok == False:
            ss += sozcuk[i]
    ss = ss.lower()
    return ss

def delPunctuationMarks(kelime):
    s = [h if h not in PUNCTUATION else ' ' for h in kelime]
    s = ''.join(s)
    # Eğer kelimede boşluk varsa, sonrasını at
    s = s.strip()
    return s

#def delDigits(word): #her rakamı siliyor istenen şekilde yapamadım.
#     s = [h for h in word if h not in DIGITS]
#     return "".join(s)


def digits(line1):
    for i in line1:
        if i.isdigit() == True:
            line1.remove(i)
            
def turkish_ch(harf):
    harfler = {'ç': 'c', 'Ç': 'c', 'ğ': 'g', 'Ğ': 'g',
               'ö': 'o', 'Ö': 'O', 'ş': 's', 'Ş': 'S',
               'ü': 'u', 'Ü': 'U'}
    return harfler[harf] if harf in harfler else harf

def replaceTurkishCh(sozcuk):
    s = [turkish_ch(harf) for harf in sozcuk]
    return "".join(s)

def split_words(metin):
    hamliste = metin.split() #Kelime kelime bölünmemesi için hamliste değiştirilmeli
    hamliste = list(map(lowerCaseLetter, hamliste))
    hamliste = list(map(delPunctuationMarks, hamliste))
    hamliste = list(map(replaceTurkishCh, hamliste))
    #hamliste = list(map(delDigits, hamliste))
    #hamliste = list(map(split_sentences, hamliste))
    return hamliste


def split_sentences(data):
    end_sentence = "!.?"
    for line in data:
        if line in end_sentence:
            data=data.replace(line,"\n")
    

def drop_duplicate(datalines):
    return set(datalines)



if __name__ == "__main__":
    dosya='all_data'
    fad="{}.txt".format(dosya)
    with open(fad,"r",encoding="utf8") as f:
        metin = f.read()


    #duplicate verilerden kurtulma işlemi 
    with open(fad,"r",encoding="utf-8") as f:
        datalines = f.readlines()
    with open(fad, 'w+',encoding="utf-8") as f:
        f.writelines(set(drop_duplicate(datalines)))


   #sayısal verilerden kurtulma
    with open(fad,"r",encoding="utf-8") as f:
        data = ''.join(i for i in f.read() if not i.isdigit())

    with open(fad, 'w+',encoding="utf-8") as f:
        f.write(data)
        
 
 
    liste = split_words(metin)
    print(liste)

    fad = "{}_words.txt".format(dosya)
    with open(fad,"w",encoding="utf8") as f:
        for w in liste:
            print("{}".format(w),file=f)
    
    
    #liste2 = split_sentences(metin)
    #print(liste)
    #fad2 = "{}_cumleler.txt".format(dosya)
    #with open(fad2,"w",encoding="utf8") as f:
        #for w in liste:
            #print("{}".format(w),file=f)