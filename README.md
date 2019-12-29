***1- Copyright information***

These programmes are free software; you can redistribute them and/or modify them under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

These programmes are distributed in the hope that they will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA


***About***

**2.1. poslem.py**

Tokeniser, lemmatiser and PoS-tagger script using the StanfordNLP Python library (https://stanfordnlp.github.io/stanfordnlp/). This is a frontend for StanfordCoreNLP (https://stanfordnlp.github.io/CoreNLP/#about ), therefore, a full installation this toolkit with the Spanish models is required.

*Usage:*

./sposle.py filename
The output will be filename.pole


**2.2. lc.py**

The script to analyse the lemmatised PoS-tagged and calculates some indicators for Lexical Sophistication and Lexical Diversity.
This code is a modified version of LCA (lexical complexity analyzer of  Lu (http://www.personal.psu.edu/xxl13/downloads/lca.html). It just substitutes the BNC corpus for CORPES XXI (Corpus del español del siglo XXI) lemmmata frequency list. Some adaptations in the code regarding adverbial morphemes and auxiliary verbs were done. Apart from that, there are some minor syntax corrections to port it to Python 3. HD-D, MTLD and MAAS are calculated with routines of a modified version of Shen Yan Sun's library lexicalrichnes https://github.com/LSYS/lexicalrichness that disables its tokeniser.

*Usage:*

All input files must be POS-tagged and lemmatised with UD tagset in the form lemma_pos. The file should contain a minumum of 50 words. The filename is expected to include the year, month, day, and  number of sample within the day. in the 
form samplename.YYYY.mm.dd.nn[.txt] 

./lc.py filename

It prints to stdout the following comma-sepatrated fields:

samplename,year,month,day,ninday,wordtypes,swordtypes,lextypes,slextypes,wordtokens,swordtokens,lextokens,slextokens,LD,LS1,LS2,VS1,VS2,CVS1,CTTR,RTTR,MAAS,MLTD,HD-D


**3. Example**

./poslem.py quetratadela.2019.12.28.1.txt

./lc.py quetratadela.2019.12.28.1.txt.pole
