import re

message = """homEwork:

	tHis iz your homeWork, copy these Text to variable. 
	
	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
	
	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 
	
	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# Last words of each existing sentence
all_last_word = re.findall(r'\s(\w+)?\.', message)


# Normalization and sentence with last words of each existing sentence
def normalization_text(regexp='(\.\s+)'):
    text = message + ', '.join(all_last_word)
    normalization_text = re.split(regexp, text)
    capital_letters = [i.capitalize() for i in normalization_text]
    return ''.join(capital_letters)


# Replacing 'iz' by 'is' where it is not a mistake
normalized = re.split('(\.\s+)', message)
capital_letters = [i.capitalize() for i in normalized]
capitalized_message = ''.join(capital_letters)
misspelling = capitalized_message.replace(' iz', ' is')


# Calculate number of whitespace characters in this text
def calculate_whitespace():
    return len(list(s for s in misspelling if s.isspace()))


normalization_text = normalization_text('(\.\s+)')

print(f'Corrected mistakes:\n{misspelling}')

print(f'Number of whitespaces: {calculate_whitespace()}')
