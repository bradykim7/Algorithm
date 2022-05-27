import re

def solution(s):
	answer = s
	l = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'zero':0}

	for x, y in l.items():
		answer = re.sub(x, str(y), answer)
	return int(answer)


