#!/usr/bin/python3
# Usage: poslem.py inputfile

import sys
import stanfordnlp


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


# An explicit definition to the path of each model mey be necessary
# unless DEFAULT_MODEL_DIR is correctly set in
# /[path_to]/dist-package/path_to/stanfordnlp/utils/resources.py
# In this case, justt 'lang':'es' is enough.
config = {
    "processors": "tokenize,mwt,pos,lemma", "lang": "es",
    "use_gpu": True
}   # Language code for the language
# 'tokenize_model_path': 'pathto/es_ancora_tokenizer.pt',
# 'mwt_model_path': 'pathto/es_ancora_mwt_expander.pt',
# 'pos_model_path': '../es_ancora_tagger.pt',
# 'pos_pretrain_path': '../es_ancora.pretrain.pt',
# 'lemma_model_path': '../es_ancora_lemmatizer.pt',
# 'depparse_model_path': '../es_ancora_parser.pt',
# 'depparse_pretrain_path': '../es_ancora.pretrain.pt'

try:
    entrada = sys.argv[1]
except Exception:
    entrada = "entrada"

nlp = stanfordnlp.Pipeline(**config)

f = open(entrada, "r")
texto = nlp(f.read())
f.close()


print(*[f'{word.lemma+"_"}{ud2penn(word)}'
        for sent in texto.sentences for word in sent.words],
      sep=' ', file=open(entrada+".pole", "w+"))
