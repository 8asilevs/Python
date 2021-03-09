import json

with open('primer_7.txt', 'r') as file:
    dict_1 = {}
    while True:
        data = file.readline()
        if not data:
            break
        data = data.split(' ')
        nazvanie, forma_sobs, dohod, rasxod = data
        pribyl = int(dohod) - int(rasxod)
        dict_1.update({nazvanie: pribyl})

ch_firm, pribyl_all = 0, 0

for key in dict_1:
    if dict_1[key] > 0:
        pribyl_all += dict_1[key]
        ch_firm += 1

pribyl_sredn = pribyl_all / ch_firm

dict_2 = {'average_profit': pribyl_sredn}

rezultat = [dict_1, dict_2]

print(rezultat)

rezultat_json = json.dumps(rezultat)

with open('primer_7_json.txt', 'w') as file:
    file.write(rezultat_json)

#import os
#os.remove('primer_7_json.txt')

