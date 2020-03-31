#!/bin/bash
echo 'samplename,year,month,day,ninday,wordtypes,swordtypes,lextypes,slextypes,wordtokens,swordtokens,lextokens,slextokens,LD,LS1,LS2,VS1,VS2,CVS1,TTR,CTTR,RTTR,MAAS,MLTD,HD-D'>out.cvs
for i in *.txt ; do
	./poslem.py "$i" && lc.py "$i".pole >> out.cvs

