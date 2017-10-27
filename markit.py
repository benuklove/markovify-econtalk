""" Markovify EconTalk transcripts. """

import markovify

# Get raw text as string.
with open("data/corpus.txt") as fin:
    text = fin.read()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
# for i in range(5):
#     print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 140 characters
for i in range(3):
    print(text_model.make_short_sentence(140))

# make sentence with start
# print(text_model.make_sentence_with_start("Can"))
