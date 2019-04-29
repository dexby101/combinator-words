import random, codecs
random.seed()
list_word = []
print("Генератор всіх комбінацій слів.")
list_word = input("Напишіть через пробіл слова не повторюючи їх: ").split()
profile_gen = ' ' #input("Режим виводу результату, через що розділяти слова в рядку: ")
file_save = input("Зберегти результат у файл [Т/н]: ").strip().lower()
if file_save == 'т':
	file_save = True
else:
	file_save = False
list_word = list(map(lambda s: s.strip(), list_word))
ln = len(list_word)
if ln > 6:
	if input("Увага більше 6-ти слів, генерація займе кілька хвилин, згодні [Т/н]: ").strip().lower() == 'н':
		input("Ви відмінили генерацію комбінацій, Enter для виходу...")
		exit();
file_name = ''.join(list_word).lower()+'.txt'
print("Генеріція почалась...")
iter_koof = ln**(ln+1)
dic_filt = {}
list_res = []

for x in range(1, iter_koof):
	list_bufer = '_|_'.join(list_word).split('_|_')
	k = ''
	
	for xs in range(0,ln):
		w = random.choice(list_bufer)
		in_w = list_bufer.index(w)
		del list_bufer[in_w]
		k += ' '+w
		del w, in_w
		pass
	try:
		dic_filt[k] += 1
	except KeyError:
		dic_filt[k] = 1
ls = [k.strip() for k, v in dic_filt.items()]
res = []

for line in ls:
	res.append(line.split())
for r in res:
	print(profile_gen.join(r))

if file_save:
	with codecs.open(file_name, 'w', 'utf-8') as f:
		for r in res:
			f.write(profile_gen.join(r)+'\n')
	print(f'Файл з цим результатом {file_name} - створено!')

input("Кількість комбінацій: "+str(len(ls)))
		
