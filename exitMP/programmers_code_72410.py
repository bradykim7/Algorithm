def solution(new_id):
    answer = ''
    # step 1
    answer = new_id.lower()
    #step 2
    for i in new_id:
        if ord(i) < 48 or (ord(i) > 57 and ord(i) < 97) or ord(i) > 122 :
            # exclude "-", "_", "."
            if ord(i) in [45,46,95] :
                continue
            answer = answer.replace(i,'')
    #step 3
    p = '.'
    for i in answer:
        temp = i
        if i == '.' and i == p:
            answer = answer.replace(i,'',1)
        p = temp
    print(answer)
    #step 4
    answer = answer.rstrip('.')
    answer = answer.lstrip('.')

    #step 5
    if answer == '':
        return 'aaa'
    #step 6
    if len(answer) >= 16 : answer = answer[:15]
	
	x = 0
	while answer[-1] == '.':
		answer = answer[:15-x]
		x += 1

    #step 7
    while len(answer) <=2 :
        answer+=answer[-1]
    return answer
