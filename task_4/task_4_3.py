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
def normalization_text(text_to_normalize):
    text_to_normalize = text_to_normalize.lower()
    normalized = re.split('(\.\s+)', text_to_normalize)
    normalized_with_capitals = [i.capitalize() for i in normalized]
    capitalized = ''.join(normalized_with_capitals)
    normalized = capitalized.replace(' iz', ' is')
    return ''.join(normalized)


# Calculate number of whitespace characters in this text
def calculate_whitespace(text):
    return len(list(s for s in text if s.isspace()))


normalized_text = normalization_text(message)

print(f'Corrected mistakes:\n{normalized_text}')

print(f'Number of whitespaces: {calculate_whitespace(normalized_text)}')
