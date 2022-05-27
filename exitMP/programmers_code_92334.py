def solution(id_list, report, k):
    answer = []
    index = {}
    res = {}
	ans = set()
    for x in id_list:
        index[x] = []
		res[x] = 0
    for x in report:
        who = x.split()[0]
        target = x.split()[1]
		if target in index[who]: 
			continue
		else:
			index[who].append(target)
			res[target] = res[target] + 1
			if res[target] >= k:
				ans.add(target)
	for key, value in index.items():
		answer.append(len(set(value) & ans))
	return answer
