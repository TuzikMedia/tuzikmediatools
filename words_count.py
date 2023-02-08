# Copyright RimMirK (rimmirk) 2023 | https://t.me/RimMirK | GPLv3 license

def words_count(*texts):
	r = []
	for text in texts:
		words = text.split(' ')
		try: 
			while True: words.remove("")
		except ValueError: pass
		r.append(len(words))
	if len(r) == 1: return r[0]
	return tuple(r)