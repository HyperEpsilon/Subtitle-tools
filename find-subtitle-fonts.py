import re
import os

sub_ext = ['.ass']
dir_path = r"D:\Anime\Vinland Saga\Season 1\subs"

def main():
	fonts = set()

	os.chdir(dir_path)
	for filename in os.listdir(dir_path):
		if filename[-4:] not in sub_ext: continue  # Skip non-subtitle files
		
		with open(filename, 'r', encoding='utf8') as f:
			file_text = f.read()

		style_matches = re.findall(r"(?<=\nStyle: ).*", file_text)
		embeded_matches = re.findall(r"(?<=\\fn).*?(?=\\)", file_text)
		# print(style_matches)
		# print(file_text)

		for m in style_matches:
			fonts.add(m.split(',')[1])
		for m in embeded_matches:
			fonts.add(m)

	with open('font_list.txt', 'w') as f:
		for font in fonts:
			f.write(f"{font}\n")



if __name__ == '__main__':
	main()