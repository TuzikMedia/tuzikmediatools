# Copyright RimMirK (rimmirk) 2023 | https://t.me/RimMirK | GPLv3 license

from random import randint

def get_result(lenght, category, symbols_pack=None, numbers_range=None):
	result = ''
	if category == 'numbers':
		for _ in range(lenght):
			result += str(randint(numbers_range[0], numbers_range[1]))
		return result

	elif category == 'bool':
		result = []
		for i in range(lenght):
			b = randint(0, 1)
			if b == 1:
				x = True
			else: x = False
			result += x
			return result
	else:
		for _ in range(lenght):
			result += str(symbols_pack[randint(0, len(symbols_pack)-1)])
		return result

def generate(lenght, 
			 symbols='1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+-=[]{};\':",./<>?/\\|№', 
			 numbers_range=(0, 9),
			 case=None):
	if symbols == 'numbers': return get_result(lenght, 'numbers', numbers_range=numbers_range)
	elif symbols == 'a-z':
		if case == 'low': return get_result(lenght, 'symbols', symbols_pack='qwertyuiopasdfghjklzxcvbnm')
		elif case == 'up': return get_result(lenght, 'symbols', symbols_pack='QWERTYUIOPASDFGHJKLZXCVBNM')
		else: return get_result(lenght, 'symbols', symbols_pack='qwertyuiopasdfghjklxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
	
	elif symbols == 'bool': return get_result(lenght, 'bool')
	else: return get_result(lenght, 'symbols', symbols_pack=symbols)

