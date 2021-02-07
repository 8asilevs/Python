fullnumber = int(input('Введите количество секунд.'))

hours = fullnumber//3600
print(f'hours – {hours}')

fullnumber = fullnumber%3600
minutes = fullnumber//60
print(f'minutes – {minutes}')

fullnumber = fullnumber%60
seconds = fullnumber
print(f'seconds – {seconds}')

print(f'{hours}:{minutes}:{seconds}')