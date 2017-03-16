import yaml

NOUNS = yaml.load(open('data/conjunction.yaml'))
VERBS = yaml.load(open('data/conjunction.yaml'))
ADJECTIVES = yaml.load(open('data/adjective.yaml'))
QUESTIONS = yaml.load(open('data/question.yaml'))
NUMBERS = yaml.load(open('data/conjunction.yaml'))
COUNTER = yaml.load(open('data/conjunction.yaml'))
CONJUNCTIONS = yaml.load(open('data/conjunction.yaml'))
SPECIAL = yaml.load(open('data/special.yaml'))


# Assertion
SENTENCE_STRUCTURES_1 = '%(subject) shir4 %(object)s'
# Negative Assertion
SENTENCE_STRUCTURES_2 = '%(subject) bu2_shir4 %(object)s'

# Action sentence
SENTENCE_STRUCTURES_3 = '%(subject) %(action)s %(object)s'

# Description sentence
SENTENCE_STRUCTURES_4 = '%(subject) %(adjective)s'




def Main():
    pass


if __name__ == '__main__':
    Main()