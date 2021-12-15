user = input('Would you like to play a Mad Lib?  ').lower()
if user == 'yes':
    verb1 = input('Please pick a verb:  ').capitalize()
    noun1 = input('Please pick a noun:  ')
    noun2 = input('Please pick a noun:  ').capitalize()
    plural_noun1 = input('Please pick a plural noun:  ')
    plural_noun2 = input('Please pick a plural noun:  ')
    plural_noun3 = input('Please pick a plural noun...again:  ').capitalize()
    verb2 = input('Please pick a verb: ')
    plural_noun4 = input('Please pick another plural noun:  ')
    verb3 = input('Please pick a verb:  ')
    story = verb1 + ' your ' + noun1 + '! ' + verb1 + ' your ' + noun1 + '! ' 'Sons of ' + noun2 + '! ' + 'Of Rohan! My ' + plural_noun1 + '.' + ' I see in your ' + plural_noun2 + ' the same fear that would take the heart of me. A day may come when the courage of ' + plural_noun3 + ' fails, when we forsake our friends and ' + verb2 + ' all bonds of fellowship, but it is not this day. An hour of ' + plural_noun4 + ' and shattered shields when the Age of ' + plural_noun3 + ' comes crashing down, but it is not this day! This day we ' + verb3 + '!' + ' By all that you hold dear on this good earth, I bid you stand, ' + plural_noun3 + ' of the West!'
    print(story)
else:
    print('Well, maybe next time!')
