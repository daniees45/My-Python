
prompts = ["Enter a name: ", "Enter a pronoun(he): ", "Enter an adjective: ", "Enter a verb ending in -ing: ",  "Enter a animal name: ", "Enter an adverb ending with -ly"]
inputs = []
for prompt in prompts:
  word = input(prompt) # Get the user input
  inputs.append(word) # Add the input to the list


noun, pronoun, adjective, verb,  noun_animal, adverb = inputs

# Print the story with the user inputs
print(f"""
Once upon a time, in a bustling city, there lived a curious cat named {noun}. {noun} was known for his {adjective} spirit and insatiable curiosity. 
One day, as {noun} roamed the streets {adverb}, he stumbled upon a mysterious alleyway. Intrigued, {pronoun} cautiously ventured inside. 
The alleyway was dimly lit, and shadows danced eerily along the walls. {noun}' heart raced with excitement as he explored every nook and cranny. 
Suddenly, {pronoun} heard a faint rustling sound behind him. {noun} turned around {adverb}, his whiskers {verb} with anticipation. 
To his surprise, {pronoun} found a small, trembling {noun_animal} cowering in the corner. 
The {noun_animal} looked up at {noun} with wide, fearful eyes. 
Without hesitation, {noun} approached the {noun_animal} {adverb}, his tail swaying {adverb} with each step.
 "Don't be afraid," he said {adverb}, "I won't harm you." 
 The {noun_animal} gazed at {noun} {adverb}, his fear {adverb} dissipating. 
 Together, they embarked on an unexpected friendship, exploring the hidden wonders of the city and sharing countless adventures along the way.
""")
