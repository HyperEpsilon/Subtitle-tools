import re
import os
from collections import defaultdict

ext = ['.xml']
dir_path = r"D:\Anime\Vinland Saga\Season 1\chapters\new_chapters"
sub_folder = r"\new_chapters"

def replace_titles():
	# A list of tuples to replace in the form (original, new)
	replace_ditc = [
		(r"<ChapterString>حقوق إستوديو ويت</ChapterString>", r"<ChapterString>Logo</ChapterString>"),
		(r"<ChapterString>الجزء الأول</ChapterString>", r"<ChapterString>Part 1</ChapterString>"),
		(r"<ChapterString>أغنية المقدمة</ChapterString>", r"<ChapterString>Opening</ChapterString>"),
		(r"<ChapterString>مشاهد الحلقة</ChapterString>", r"<ChapterString>Part 2</ChapterString>"),
		(r"<ChapterString>أغنية الخاتمة</ChapterString>", r"<ChapterString>Ending</ChapterString>")
	]

	os.chdir(dir_path)
	os.makedirs(dir_path+sub_folder, exist_ok=True) # Make \new_chapters\ if not exist

	for filename in os.listdir(dir_path):
		if filename[-4:] not in ext: continue  # Skip non-xml files
		
		with open(filename, 'r', encoding='utf8') as f:
			file_text = f.read()

		# replace all instances in the file text
		eng_tag = file_text
		for rep in replace_ditc:
			eng_tag = eng_tag.replace(rep[0], rep[1])

		# Change the language of the title to english
		no_und = re.sub(r">und<", ">eng<", eng_tag)

		with open("new_chapters\\"+filename, 'w', encoding="utf8") as f:
			f.write(no_und)



def list_titles():
	"""
	Get all chapter titles in each episode
	"""
	all_titles = set()
	episode_titles = defaultdict(list)

	os.chdir(dir_path)

	for filename in os.listdir(dir_path):
		if filename[-4:] not in ext: continue  # Skip non-xml files
		
		with open(filename, 'r', encoding='utf8') as f:
			file_text = f.read()

		# Get all chapter names and languages
		matches = re.findall(r"<ChapterString>(.*?)</ChapterString>\n.*?<ChapterLanguage>(.*?)</ChapterLanguage>", file_text)
		# print(matches)

		# Format the matches as "Chapter Title - Lang"
		for m in matches:
			f_match = f"{m[0]} - {m[1]}"
			all_titles.add(f_match)
			episode_titles[filename].append(f_match)


	with open('title_list.txt', 'w', encoding='utf8') as f:
		for title in all_titles:
			f.write(f"{title}\n")
		f.write("\n=============\n")

		# Join each episode with a newline and 3 spaces
		for ep, titles in episode_titles.items():
			joined_titles = '\n   '.join(titles)
			f.write(f"{ep}:\n   {joined_titles}\n")



if __name__ == '__main__':
	# replace_titles()
	list_titles()