import re
import os
from collections import defaultdict
import pymkv

ext = ['.mkv']
dir_path = r"D:\TV\WandaVision\Season 1"

def main():
	track_list = defaultdict(list)

	os.chdir(dir_path)
	for filename in os.listdir(dir_path):
		if filename[-4:] not in ext: continue
		print(f'Now checking: {filename}')

		mkv = pymkv.MKVFile(filename)
		tracks = mkv.get_track()

		tr_len = len(str(tracks[-1].track_id))
		for track in tracks:
			tr = f"{track.track_id:0{tr_len}}-{track.track_type} : {track.track_name} ({track.language})"
			# print(tr)
			track_list[filename].append(tr)

	
	with open('track_list.txt', 'w') as f:
		for ep, tracks in track_list.items():
			joined_tracks = '\n   '.join(tracks)
			f.write(f"{ep}:  [{len(tracks)}]\n   {joined_tracks}\n")




if __name__ == '__main__':
	main()