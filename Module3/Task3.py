import re

text = """homEwork:

	tHis iz your homeWork, copy these Text to variable. 
	
	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
	
	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 
	
	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# Last words of each existing sentence
all_last_word = re.findall(r'\s(\w+)?\.', text)

# Adding new sentence to the end of this paragraph
full_text = text + ' '.join(all_last_word)

# Split message
normalized = re.split('(\.\s+)', full_text)

# Capitalize first letters of each sentence
capital_letters = [i.capitalize() for i in normalized]

# Union back into single message
capitalized_message = ''.join(capital_letters)

# Replacing 'iz' by 'is' where it is not a mistake
misspelling = capitalized_message.replace(' iz', ' is')
print(f'Corrected homework:\n{misspelling}')

# Calculate number of whitespace
count_whitespace = list(s for s in misspelling if s.isspace())
print(f'Number of whitespaces: {len(count_whitespace)}')
