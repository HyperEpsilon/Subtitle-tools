import re
import os
from collections import defaultdict

sub_ext = ['.ass']
dir_path = r"D:\_temp\vinland\subs"

def main():
	fonts = set()
	font_list = defaultdict(list)

	os.chdir(dir_path)
	for filename in os.listdir(dir_path):
		if filename[-4:] not in sub_ext: continue  # Skip non-subtitle files
		
		with open(filename, 'r', encoding='utf8') as f:
			file_text = f.read()

		style_matches = re.findall(r"(?<=\nStyle: ).*", file_text)
		embeded_matches = re.findall(r"(?<=\\fn).*?(?=\\)", file_text)
		# print(style_matches)
		# print(file_text)

		episode_fonts = set()

		# Font names are stored in the second element of the styles list
		for m in style_matches:
			episode_fonts.add(m.split(',')[1])
		for m in embeded_matches:
			episode_fonts.add(m)

		# Add the episode title to the list for each font
		for font in episode_fonts:
			font_list[font].append(filename)

		# Add all fonts to the master font list
		fonts.update(episode_fonts)

	with open('font_list.txt', 'w') as f:
		for font in fonts:
			f.write(f"{font}\n")
		f.write("\n=============\n")

		# Join each episode with a newline and 3 spaces
		for font, eps in font_list.items():
			joined_eps = '\n   '.join(sorted(eps))
			f.write(f"{font}:  [{len(eps)}]\n   {joined_eps}\n")




if __name__ == '__main__':
	main()