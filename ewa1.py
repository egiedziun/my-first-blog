print('Hello, Django girls!')
if 3>2:
	pass
	print('To działa!')
if 5>2:
	print('5 jest jednak większe od 2')
else:
	print('5 nie jest większe od 2')

name = 'Sonja'
if name == 'Ola':
	print('Hej Ola!')
elif name == 'Sonja':
	print('Hej Ewa!')
else:
	print('Hej nieznajoma!')

glosnosc = 57
if glosnosc < 20:
	print("prawie nic nie słychać.")
elif 20 <= glosnosc < 40:
	print("0, muzyka leci w tle.")
elif 40 <= glosnosc < 60:
	print("Idealnie, mogę usłyszeć wszystkie detale")
elif 60 <= glosnosc < 80:
	print("Troszeczkę za głośno!")
else:
	print("Ojoj! Moje uszy! :(")



def hej(imie):
	if imie == 'Ola':
		print('Hej Ola!')
	elif imie == 'Sonja':
		print('Hej Sonja')
	else:
		print('Hej nieznajoma!')

hej("Ola")

	
def hej(imie):
		print('Hej ' + imie + '!')
hej("Rachel")

dziewczyny = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Ty']
for imie in dziewczyny:
	hej(imie)
	print('Kolejna dziewczyna')

for i in range(1, 6):
	print(i)
	