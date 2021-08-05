#!/usr/bin/python3
# This programme calculates some LC indicators
import string,re,sys,os,random
from math import sqrt,log
from lexicalrichness2 import LexicalRichness
import pandas as pd
entrada = 'data.csv'

standard=50

def sort_by_value(d):
    items=d.items()
    backitems=[ [v[1],v[0]] for v in items]
    backitems.sort()
    return [ backitems[i][1] for i in range(0,len(backitems))]

def getndwfirstz(z,lemmalist):
    ndwfirstztype={}
    for lemma in lemmalist[:z]:
        ndwfirstztype[lemma]=1
    return len(ndwfirstztype.keys())

def getndwerz(z,lemmalist):
    ndwerz=0
    for i in range(10):
        ndwerztype={}
        erzlemmalist=random.sample(lemmalist,z)
        for lemma in erzlemmalist:
            ndwerztype[lemma]=1
        ndwerz+=len(ndwerztype.keys())
    return ndwerz/10.0

def getndwesz(z,lemmalist):
    ndwesz=0
    for i in range(10):
        ndwesztype={}
        startword=random.randint(0,len(lemmalist)-z)
        eszlemmalist=lemmalist[startword:startword+z]
        for lemma in eszlemmalist:
            ndwesztype[lemma]=1
        ndwesz+=len(ndwesztype.keys())
    return ndwesz/10.0

def getmsttr(z,lemmalist):
    samples=0
    msttr=0.0
    while len(lemmalist)>=z:
        samples+=1
        msttrtype={}
        for lemma in lemmalist[:z]:
            msttrtype[lemma]=1
        msttr+=len(msttrtype.keys())/float(z)
        lemmalist=lemmalist[z:]
    return msttr/samples

def isLetterNumber(character):
    if character in string.printable and not character in string.punctuation:
        return 1
    return 0

def isSentence(line):
    for character in line:
        if isLetterNumber(character):
            return 1
    return 0

adjdict={}
verbdict={}
noundict={}
worddict={}
wordlistfile=open('corpesxxi','r')
wordlist=wordlistfile.readlines()
wordlistfile.close()
lexlist=''
for word in wordlist:
    wordinfo=word.strip()
    if not wordinfo or 'Total words' in wordinfo:
        continue
    infolist=wordinfo.split()
    lemma=infolist[0]
    pos=infolist[1]
    try:
        frequency=int(float(infolist[2]))
    except ValueError :
        print(f'Error on line: {wprd}')
    if pos=='NoP':
        worddict[lemma]=worddict.get(lemma,0)+frequency+2
    else:
        worddict[lemma]=worddict.get(lemma,0)+frequency
    if pos=='Adj':
        adjdict[lemma]=adjdict.get(lemma,0)+frequency
    elif pos=='Verb':
        verbdict[lemma]=verbdict.get(lemma,0)+frequency
    elif pos=='NoC':
        noundict[lemma]=noundict.get(lemma,0)+frequency
    elif pos=='NoP':
        noundict[lemma]=noundict.get(lemma,0)+frequency+2
wordranks=sort_by_value(worddict)
verbranks=sort_by_value(verbdict)

filename=sys.argv[1]
lemfile=open(filename,'r')
lemlines=lemfile.readlines()
lemfile.close()
filename=sys.argv[1].split('/')[-1]
basename = filename.split('.')[0]
group=basename.split('_')[0]
sample = basename.split('_',1)[1]

# process input file
wordtypes={}
wordtokens=0
swordtypes={}
swordtokens=0
lextypes={}
lextokens=0
slextypes={}
slextokens=0
verbtypes={}
verbtokens=0
sverbtypes={}
adjtypes={}
adjtokens=0
advtypes={}
advtokens=0
nountypes={}
nountokens=0
lemmaposlist=[]
lemmalist=[]
lexlemmaposlist=[]
lexlemmalist=[]


for lemline in lemlines:
    lemline=lemline.strip()
    lemline=lemline.lower()
    if not isSentence(lemline):
        continue
    lemmas=lemline.split()
    for lemma in lemmas:
        word=lemma.split('_')[0]
        pos=lemma.split('_')[-1]
        if (not pos in string.punctuation) and pos!='sent' and pos!='sym':
            lemmaposlist.append(lemma)
            lemmalist.append(word)
            wordtokens+=1
            wordtypes[word]=1
            if (not word in wordranks[-2000:]) and pos != 'cd' and pos != 'np':
                swordtypes[word]=1
                swordtokens+=1
            if pos =='nn':
                lextypes[word]=1
                nountypes[word]=1
                lextokens+=1
                nountokens+=1
                lexlemmaposlist.append(lemma)
                lexlemmalist.append(word)
                if not word in wordranks[-2000:]:
                    slextypes[word]=1
                    slextokens+=1
            elif pos == 'np':
                lextypes[word]=1
                nountypes[word]=1
                lextokens+=1
                nountokens+=1
                lexlemmaposlist.append(lemma)
                lexlemmalist.append(word)
            elif pos[0]=='j':
                lextypes[word]=1
                adjtypes[word]=1
                lextokens+=1
                adjtokens+=1
                lexlemmaposlist.append(lemma)
                lexlemmalist.append(word)
                if not word in wordranks[-2000:]:
                    slextypes[word]=1
                    slextokens+=1
            elif pos[0]=='r' and word in adjdict or (word[-5:]=='mente' and word[:-5] in adjdict):
                lextypes[word]=1
                advtypes[word]=1
                lextokens+=1
                advtokens+=1
                lexlemmaposlist.append(lemma)
                lexlemmalist.append(word)
                if not word in wordranks[-2000:]:
                    slextypes[word]=1
                    slextokens+=1
            elif pos[0]=='v' and not word in ['ser','haber','estar']:
                verbtypes[word]=1
                verbtokens+=1
                lextypes[word]=1
                lextokens+=1
                lexlemmaposlist.append(lemma)
                lexlemmalist.append(word)
                if not word in wordranks[-2000:]:
                    sverbtypes[word]=1
                    slextypes[word]=1
                    slextokens+=1

ld=float(lextokens)/wordtokens

ls1=slextokens/float(lextokens)
ls2=len(swordtypes.keys())/float(len(wordtypes.keys()))

vs1=len(sverbtypes.keys())/float(verbtokens)
vs2=(len(sverbtypes.keys())*len(sverbtypes.keys()))/float(verbtokens)
cvs1=len(sverbtypes.keys())/sqrt(2*verbtokens)
TTR=len(wordtypes.keys())/float(wordtokens)
CTTR=len(wordtypes.keys())/sqrt(2*wordtokens)
RTTR=len(wordtypes.keys())/sqrt(wordtokens)
LOGTTR=log(len(wordtypes.keys()))/log(wordtokens)
UBER=(log(wordtokens,10)*log(wordtokens,10))/log(wordtokens/float(len(wordtypes.keys())),10)
lex=LexicalRichness(lemmalist)
MAAS=float(lex.Maas)
try:
    HDD=lex.hdd(draws=42).astype(type('float', (float,), {}))
except RuntimeError:
    print(f'ERROR: {group}_{sample}.pole')
MTLD=lex.mtld(threshold=0.72)
output= [group, sample,
         len(wordtypes.keys()), len(swordtypes.keys()), len(lextypes.keys()),
         len(slextypes.keys()),
         wordtokens, swordtokens, lextokens, slextokens,
         ld,
         ls1, ls2, vs1, vs2, cvs1,
         TTR, CTTR, RTTR,
         MAAS, MTLD, HDD]

for index, measure in enumerate(output):
    if type(measure)==type(0.0):
        output[index] = measure='%.5f' % measure

df = pd.read_csv(entrada)
new_row = pd.Series(output, index = df.columns)
df = df.append(new_row, ignore_index=True)
df.to_csv(f'data.csv', mode='w', header=True, index=False)  

