## Pre-requisities: run 'pip install youtube-dl' to install the youtube-dl package.
## Specify your location of output videos and input json file.
import json
import os
from itertools import islice

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return dict(islice(iterable, n))

output_path = './dataset/videos'
json_path = './COIN.json'

if not os.path.exists(output_path):
	os.mkdir(output_path)

data = json.load(open(json_path, 'r'))['database']
youtube_ids = list(data.keys())

n_items = take(12, data.items())
data = n_items

for youtube_id in data:
	info = data[youtube_id]
	type = info['recipe_type']
	url = info['video_url']
	vid_loc = output_path + '/' + str(type)
	if not os.path.exists(vid_loc):
		os.mkdir(vid_loc)
	os.system('youtube-dl -o ' + vid_loc + '/' + youtube_id + '.mp4' + ' -f best ' + url)
	# break

	# To save disk space, you could download the best format available
	# 	but not better that 480p or any other qualities optinally
	# See https://askubuntu.com/questions/486297/how-to-select-video-quality-from-youtube-dl
