from translate import Translator

translator = Translator(to_lang="russian")

file_r = open('primer_4_r.txt', 'r')
file_w = open('primer_4_w.txt', 'w')

while True:
    data = file_r.readline()
    if not data:
        break
    slovo, dash, nomer = data.split(' ')
    slovo = translator.translate(slovo)
    data = [slovo, dash, nomer]
    file_w.write(' '.join(data))

file_r.close()
file_w.close()

#import os
#os.remove('primer_4_w.txt')
