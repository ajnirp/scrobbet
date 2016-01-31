# a script to dump idv3 tags to a file

import taglib
import os
import utils

# get relevant data from a tags dict
def get_data(tags):
    artist = tags['ARTIST'][0]
    tracknumber = tags['TRACKNUMBER'][0]
    title = tags['TITLE'][0]
    album = tags['ALBUM'][0]
    return (artist, tracknumber, title, album)

if __name__ == '__main__':
    curr_dir = os.getcwd()
    with open('tags.txt', 'w') as f:
        for i in os.listdir(curr_dir):
            if utils.is_audio_file(i):
                tag_obj = taglib.File(i)
                data = get_data(tag_obj.tags)
                f.write(str(data))
                f.write('\n')