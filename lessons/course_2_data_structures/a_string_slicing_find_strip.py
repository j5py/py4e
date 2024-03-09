
# Using find() and string slicing to extract 0.8475

text = 'X-DSPAM-Confidence:    0.8475'

print( float(text[text.find(':') + 1:].strip()) )


# Enter the following to output all string methods:

    # >>> print(dir(''))
