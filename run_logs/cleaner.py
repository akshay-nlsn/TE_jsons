bad_words = ['INFO']

with open('out.txt') as oldfile, open('out_clean.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)
