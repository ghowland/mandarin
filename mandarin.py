#!/usr/bin/end python

"""
Mandarin
"""


import yaml
import glob
import os


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
            
            data[reverse_key][english] = mandarin
    
    return data


def Main():
    data = LoadData()


if __name__ == '__main__':
    Main()


