#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import stanza


def ud2penn(argument):
    switcher = {
            'ADJ': 'JJ',        # adjective
            'ADP': 'IN',        # adposition
            'ADV': 'RB',        # adverb
            'AUX': 'MD',        # auxiliary
            'CCONJ': 'CC',      # coordinating conjunction
            'DET': 'DT',        # Determiner
            'INTJ': 'UH',       # interjection
            'NOUN': 'NN',       # noun
            'NUM': 'CD',        # nummeral
            'PART': 'RP',       # particle
            'PRON': 'PRP',     # pronoun
            'PROPN': 'NP',      # proper noun
            # 'PUNCT' : "",     # punctuation
            'SCONJ': 'IN',     # pron, subordinating conjunction
            'SYM': 'SYM',      # symbol
            'VERB': 'VB',       # verb
            'X': 'X'
    }
    if argument.lemma not in ["»", "«", "#", "$", "€", ".", ",", ":", "(", ")",
                              '"', "'", "“", "”", "‘", "’", ";", "—", "…",
                              "&", "¡", "!", "¿", "?", "–", "[", "]", "/",
                              "-", "..."]:
        return switcher.get(argument.pos)
    else:
        return argument.lemma


processor_dict = {
    'tokenize': 'ancora',
    'mwt': 'ancora',
    'pos': 'ancora',
    'lemma': 'ancora'
}                                                                               
                                                                                  
config = {
    'lang': 'es',
    'processors': processor_dict
}                              

try:
    entrada = sys.argv[1]
except Exception:
    entrada = "entrada"

nlp = stanza.Pipeline(**config)

f = open(entrada, "r")
texto = nlp(f.read())
f.close()

print(*[f'{word.lemma+"_"}{ud2penn(word)}'
        for sent in texto.sentences for word in sent.words],
      sep=' ', file=open(entrada+".pole", "w+"))
