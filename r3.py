data = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		data.append(line.strip())
for line in data:
	s = line.split(' ')
	time = s[0][:5] #S0字串的前五個字 (0,1,2,3,4)
	name = s[0][5:] #S0字串的5開始一直到結尾 (0,1,2,3,4,5)
	print('名字：', name)
