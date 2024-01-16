# Random Story

import random

print('Hello reader')
rname = input('What is your name: ')
print('Welcome ' + rname)

names = ['Varun', 'Divyansh', 'Rohan']
char = ['Sher', 'Helios', 'Killer']
ele = ['Pen', 'Book', 'Phone']
things = ['Table', 'Duster', 'Chair']

randname = random.choice(names)
randchar = random.choice(char)
randele = random.choice(ele)
randthings = random.choice(things)

story = (
    f"Once upon a time, in a mystical forest, there was a legendary hero named {rname},
    known far and wide as '{randchar} the Brave'. "
    f"{rname} possessed a magical {randele} that
    could unlock the secrets of ancient books. "
    f"But there was a catch - {rname}'s trusty {randthings}
    was cursed, and it had a habit of disappearing at the most inconvenient times. "
    f"One day, {rname}, a curious traveler, stumbled upon {rname}'s
    camp while searching for a lost treasure map. "
    f"{rname} and {randname} decided to embark on a daring adventure to
    break the curse of the {randthings} and uncover the hidden treasures of the forest. "
    f"Little did they know that their journey would lead them to encounter
    magical creatures, solve riddles, and forge a friendship that would last a lifetime."
)

print(story)
