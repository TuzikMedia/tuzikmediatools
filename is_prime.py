# Copyright RimMirK (rimmirk) 2023 | https://t.me/RimMirK | GPLv3 license

def is_prime(*nums):
	r = []
	for x in (nums):
		if x > 1:
			b = True
			for i in range(2,(x//2)+1): 
				if x % i == 0: b = False
			r.append(b)
		else: r.append(False)
	if len(r) == 1: return r[0]
	return tuple(r)


