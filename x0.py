namex = input("Введите имя игрока который будет играть с X: ")
name0 = input("Введите имя игрока который будет играть с 0: ")	
print('Поехали!\n')









numbers = '123456789'
uslovya = False
winx = False
win0 = False

def pasteX():
	global numbers
	global uslovya
	global winx 
	
	print(f"""	{numbers[0]} {numbers[1]} {numbers[2]}
	{numbers[3]} {numbers[4]} {numbers[5]}
	{numbers[6]} {numbers[7]} {numbers[8]}\n""")
	x = input("Куда вставить X = ")
	print('\n')
	if x == '':
		uslovya = True
	else:
		if x in '123456789': 
			x = int(x)
			if numbers[x-1] != 'x' and numbers[x-1] != '0':
				x = str(x)	
				numbers = numbers.replace(x, 'x')
				uslovya = False
			else:
				uslovya = True
		else:
			uslovya = True

		
	if ('xxx' == numbers[0:3]) or ('xxx' == numbers[3:6]) or ('xxx' == numbers[6:9]) or ('xxx' == numbers[0] + numbers[3] + numbers[6]) or ('xxx' == numbers[1] + numbers[4] + numbers[7])  or  ('xxx' == numbers[2] + numbers[5] + numbers[8]) or ('xxx' == numbers[0] + numbers[4] + numbers[8]) or ('xxx' == numbers[2] + numbers[4] + numbers[6]):
		winx = True
	

def paste0():
	global numbers
	global uslovya
	global win0
	
	print(f"""	{numbers[0]} {numbers[1]} {numbers[2]}
	{numbers[3]} {numbers[4]} {numbers[5]}
	{numbers[6]} {numbers[7]} {numbers[8]}\n""")
	y0 = input("Куда вставить 0 = ")
	print('\n')
	if y0 == '':
		uslovya = True
	else:
		if y0 in '123456789': 
			y0 = int(y0)
			if numbers[y0-1] != 'x' and numbers[y0-1] != '0':
				y0 = str(y0)	
				numbers = numbers.replace(y0, '0')
				uslovya = False
			else:
				uslovya = True
		else:
			uslovya = True
	
	if ('000' == numbers[0:3]) or ('000' == numbers[3:6]) or ('000' == numbers[6:9]) or ('000' == numbers[0] + numbers[3] + numbers[6]) or ('000' == numbers[1] + numbers[4] + numbers[7]) or  ('000' == numbers[2] + numbers[5] + numbers[8]) or ('000' == numbers[0] + numbers[4] + numbers[8]) or ('000' == numbers[2] + numbers[4] + numbers[6]):
		win0 = True

while winx == False or win0 == False:
	pasteX()
	while uslovya == True:
		print('Введите число и число должен быть на вашем экране. Попробуйте ещё раз.')
		pasteX()
	paste0()
	while uslovya == True:
		print('Введите число и число должен быть на вашем экране. Попробуйте ещё раз.')
		paste0()
	
	if winx == True and win0 == True:
		print(f"""	{numbers[0]} {numbers[1]} {numbers[2]}
	{numbers[3]} {numbers[4]} {numbers[5]}
	{numbers[6]} {numbers[7]} {numbers[8]}\n""")
		print('Ничья, поздравляем всех!')
		break
	elif winx == True:
		print(f"""	{numbers[0]} {numbers[1]} {numbers[2]}
	{numbers[3]} {numbers[4]} {numbers[5]}
	{numbers[6]} {numbers[7]} {numbers[8]}\n""")
		print(f'Выиграл {namex}! Поздравляю.')
		break
	elif win0 == True:
		print(f"""	{numbers[0]} {numbers[1]} {numbers[2]}
	{numbers[3]} {numbers[4]} {numbers[5]}
	{numbers[6]} {numbers[7]} {numbers[8]}\n""")
		print(f'Выиграл {name0}! Поздравляю.')
		break
