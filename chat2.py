

#讀取
def read_file(filename):
	data = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: #讀input.txt
		for line in f:
			data.append(line.strip())
	return data


def convert(data):
	new = []
	person = None 
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0
	for line in data:
		s = line.split(' ') 
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
			 	for msg in s[2:]:
			 		allen_word_count += len(msg)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for msg in s[2:]:
					viki_word_count += len(msg)
	print('Allen說了', allen_word_count, '字，傳了', allen_sticker_count, '張貼圖、', allen_image_count, '張圖片')
	print('Viki說了', viki_word_count, '字，傳了', viki_sticker_count, '張貼圖、', viki_image_count, '張圖片')	
	
			
#寫入檔案
def write_file(filename, data):
	with open (filename, 'w', encoding='utf-8') as f:
		for line in data:
			f.write(line + '\n')


def main():
	data = read_file('LINE-Viki.txt')
	data = convert(data)
	#write_file('output.txt', data)

main()