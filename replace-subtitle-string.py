import re
import os

sub_ext = ['.ass']
dir_path = r"C:\Users\Alex\Downloads\qBittorrent\[Cerberus] Seishun Buta Yarou wa Bunny Girl Senpai no Yume wo Minai  + Movie [BD 1080p HEVC 10-bit OPUS]\subs"

# Note, only match the remaining section of a string and not everything before it, to preserve the timing and style details
string_match = r'T{\\c&HBF9105&}e{\\c&H952F0E&}.*$'
string_replace = r'R{\c&HBF9105&}a{\c&H952F0E&}s{\c&HBF9105&}c{\c&H952F0E&}a{\c&HBF9105&}l {\c&H952F0E&}D{\c&HBF9105&}o{\c&H952F0E&}e{\c&HBF9105&}s {\c&H952F0E&}N{\c&HBF9105&}o{\c&H952F0E&}t {\c&HBF9105&}D{\c&H952F0E&}r{\c&HBF9105&}e{\c&H952F0E&}a{\c&HBF9105&}m {\c&H952F0E&}o{\c&HBF9105&}f {\c&H952F0E&}B{\c&HBF9105&}u{\c&H952F0E&}n{\c&HBF9105&}n{\c&H952F0E&}y {\c&HBF9105&}G{\c&H952F0E&}i{\c&HBF9105&}r{\c&H952F0E&}l {\c&HBF9105&}S{\c&H952F0E&}e{\c&HBF9105&}n{\c&H952F0E&}p{\c&HBF9105&}a{\c&H952F0E&}i'


def main():
	os.chdir(dir_path)

	for filename in os.listdir(dir_path):
		if filename[-4:] not in sub_ext: continue  # Skip non-subtitle files

		with open(filename, 'r+', encoding='utf8') as f:
			file_text = f.read()
			new_text = re.sub(string_match, string_replace, file_text, re.S, re.MULTILINE)  # I don't know why I need the re.S flag, but I do
			f.seek(0)
			f.write(new_text)
			f.truncate()


if __name__ == '__main__':
	main()