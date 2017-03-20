#!/usr/bin/env python

"""
Mandarin
"""


import yaml
import glob
import os
import pprint


DATA_PATH_GLOB = 'data/*.yaml'

# NOUNS = yaml.load(open('data/conjunction.yaml'))
# VERBS = yaml.load(open('data/conjunction.yaml'))
# ADJECTIVES = yaml.load(open('data/adjective.yaml'))
# QUESTIONS = yaml.load(open('data/question.yaml'))
# NUMBERS = yaml.load(open('data/conjunction.yaml'))
# COUNTER = yaml.load(open('data/conjunction.yaml'))
# CONJUNCTIONS = yaml.load(open('data/conjunction.yaml'))
# SPECIAL = yaml.load(open('data/special.yaml'))


# Assertion
SENTENCE_STRUCTURES_1 = '%(subject) shir4 %(object)s'
# Negative Assertion
SENTENCE_STRUCTURES_2 = '%(subject) bu2_shir4 %(object)s'

# Action sentence
SENTENCE_STRUCTURES_3 = '%(subject) %(action)s %(object)s'

# Description sentence
SENTENCE_STRUCTURES_4 = '%(subject) %(adjective)s'


def LoadData():
    """Returns a dict with the name of the file as the first key, and the reverse as 'reverse_*' and name"""
    data = {}
    
    paths = glob.glob(DATA_PATH_GLOB)
    
    for path in paths:
        key = os.path.basename(path).split('.')[0]
        reverse_key = 'reverse_%s' % key
        
        data[key] = {}
        data[reverse_key] = {}
        
        path_data = yaml.load(open(path))
        
        for (mandarin, english) in path_data.items():
            data[key][mandarin] = english
            
            if type(english) in (str, unicode):
                data[reverse_key][english] = mandarin
            elif type(english) in (int, float):
                data[reverse_key][english] = str(mandarin)
            else:
                # print '%s:  %s = %s' % (key, mandarin, english)
                
                for item in english:
                    if type(item) in (int, float):
                        data[reverse_key][str(item)] = mandarin
                        
                    elif not item.startswith('*NOTE*') and not item.startswith('*NOUN*') and not item.startswith('*VERB*') and not item.startswith('*ADJ*'):
                        data[reverse_key][item] = mandarin
    
    return data


def Main():
    data = LoadData()
    
    pprint.pprint(data)


if __name__ == '__main__':
    Main()


