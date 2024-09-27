name = ["Arthur", "Barnaby", "Rosie", "Will"]
verb = ["buys", "eats", "visits", "watches"]
noun = ["drills", "cheese", "museums", "Top Gun Maverick"]

from random import randint
def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    return words[num_picked]

print(pick(name), pick(verb), pick(noun))