#!/usr/bin/env python

"""
Mandarin
"""


import yaml
import glob
import os
import pprint
import random


DATA_PATH_GLOB = 'data/*.yaml'


# Assertion
SENTENCE_STRUCTURES_1 = '%(subject) shir4 %(object)s'
# Negative Assertion
SENTENCE_STRUCTURES_2 = '%(subject) bu2_shir4 %(object)s'

# Action sentence
SENTENCE_STRUCTURES_3 = '%(subject) %(action)s %(object)s'

# Description sentence
SENTENCE_STRUCTURES_4 = '%(subject) %(adjective)s'


def LoadData(with_reverse=True):
    """Returns a dict with the name of the file as the first key, and the reverse as 'reverse_*' and name"""
    data = {}
    
    paths = glob.glob(DATA_PATH_GLOB)
    
    for path in paths:
        key = os.path.basename(path).split('.')[0]
        reverse_key = 'reverse_%s' % key
        
        data[key] = {}
        
        if with_reverse:
            data[reverse_key] = {}
        
        path_data = yaml.load(open(path))
        
        for (mandarin, english) in path_data.items():
            data[key][mandarin] = english
            
            if with_reverse:
                if type(english) in (str, unicode):
                    data[reverse_key][english] = mandarin
                elif type(english) in (int, float):
                    data[reverse_key][english] = str(mandarin)
                else:
                    # print '%s:    %s = %s' % (key, mandarin, english)
                    
                    for item in english:
                        if type(item) in (int, float):
                            data[reverse_key][str(item)] = mandarin
                            
                        elif not item.startswith('*NOTE*') and not item.startswith('*NOUN*') and not item.startswith('*VERB*') and not item.startswith('*ADJ*'):
                            data[reverse_key][item] = mandarin
        
    return data


def Match(source, target):
    source = str(source)
    target = str(target)

    source = source.lower().replace('_', ' ').replace(' ', '').replace('?', '').replace("'", '')
    target = target.lower().replace('_', ' ').replace(' ', '').replace('?', '').replace("'", '')

    return source == target


def QuizOneItem(data, key_list=None):
    """Ask the user one question, does not construct a sentence, basic term checking.    key_list will limit which questions are asked"""
    keys = data.keys()
    keys.sort()
    key_count = len(keys)
    
    key_selected = random.randint(0, key_count-1)

    print '\n\n'

    #print 'Key Count: %s    Key selected: %s' % (key_count, key_selected)

    key = keys[key_selected]
    
    items = data[key]
    
    item_count = len(items)
    item_keys = items.keys()
    item_keys.sort()

    item_selected = random.randint(0, item_count-1)
    
    #print '%s -- Item Count: %s    Item selected: %s' % (key, item_count, item_selected)

    source = item_keys[item_selected]
    target = items[item_keys[item_selected]]
    
    print 'Translate: %s  (%s)' % (source, key)

    answer = raw_input('Answer: ')


    # Assume no match, and override
    success = False

    if Match(answer, target):
        print 'CORRECT:    Target was: %s' % target
        success = True

    elif type(target) == list:

        for target_item in target:
            if Match(answer, target_item):
                print 'CORRECT:    Target was: %s' % target
                success = True

    if not success and answer != '':
        print 'WRONG:    Target was: %s' % target
    if not success and answer == '':
        print 'NOANSWER:  Target was: %s' % target

    return (source, target, answer, success)


def Main():
    data = LoadData(with_reverse=False)
    
    #pprint.pprint(data)

    correct = 0
    wrong = 0
    noanswer = 0

    noanswer_sources = []
    wrong_sources = []

    try:
        while True:
            (source, target, answer, success) = QuizOneItem(data)

            if success:
                correct += 1

            else:
                if answer == '':
                    noanswer += 1

                    if source not in noanswer_sources:
                        noanswer_sources.append(source)

                else:
                    wrong += 1

                    if source not in wrong_sources:
                        wrong_sources.append(source)

    except KeyboardInterrupt, e:
        pass

    print '\n\nCorrect: %s\nWrong: %s\nNo Answer: %s\n' % (correct, wrong, noanswer)

    print 'No Answer: %s\n' % ', '.join(noanswer_sources)
    print 'Wrong: %s\n' % ', '.join(wrong_sources)



if __name__ == '__main__':
    Main()


