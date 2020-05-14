

#讀取
def read_file(filename):
	data = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: #讀input.txt
		for line in f:
			data.append(line.strip())
	return data

def convert(data):
	new = []
	person = None #值還沒出現，先宣告這個變數 (其他語言叫Null)
	for line in data:
		if line == 'Allen':
			person = 'Allen'
			continue #跳過 line20 不然會變成 'Allen:Allen' ，進入下一迴 '哈囉'
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: #如果person有值(allen or tom)就運行new.append
			new.append(person + ':' + line)
	return new #把運行結果存回data


			
#寫入檔案
def write_file(filename, data):
	with open (filename, 'w', encoding='utf-8') as f:
		for line in data:
			f.write(line + '\n')

def main():
	data = read_file('input.txt')
	data = convert(data)
	write_file('output.txt', data)

main()