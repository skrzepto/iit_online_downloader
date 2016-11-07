import requests
import sys
try:
        import xml.etree.cElementTree as ET
except ImportError:
        import xml.etree.ElementTree as ET


# src: https://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    file_size = int(r.headers['content-length'])
    with open(local_filename, 'wb') as f:
        i = 0
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                i += 1
                print_percent_completed(file_size, i*1024)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename

def print_percent_completed(total, completed):
    progress = (completed/(total * 1.0)) * 100
    sys.stdout.write("Download progress: %d%%   \r" % (progress) )
    sys.stdout.flush()

def download_videos(base_url, video_paths):
    for vid in video_paths:
        full_path = base_url + vid
        print "Downloading Lecture: " + str(vid.split(".")[0])
        download_file(full_path)


def get_playlist(url):
    data = requests.get(str(url) + "/playlist.rss")
    return str(data.text)


def parse_playlist(xml_str):
    tree = ET.fromstring(xml_str)

    root = tree[0]
    res = {}
    for i in root:
        class_date = i[0].text
        description = i[1].text
        # thumbnail i[2]
        if description == 'Regular lecture':
           class_meta = {}
           # index 3 onwards is file quality 
           for idx in range(3, len(i)):
               video_res = i[idx].attrib['label']
               video_path = i[idx].attrib['file']
               class_meta[video_res] = video_path
           res[class_date] = class_meta
    # print res
    return res


def get_video_paths_for_res(base_url, resolution):
    playlist_xml = get_playlist(base_url)
    all_resolutions = parse_playlist(playlist_xml)

    res = []
    for k,v in all_resolutions.items():
        res.append(v[resolution])

    return res


def prompt_user_resolution():
    valid = ["720p", "480p", "360p"]
    inp = ''
    while inp not in valid:
        prompt = "Please enter a resolution to download. Valid options are " + str(valid) + "\n"
        inp = raw_input(prompt)
    return inp


def prompt_user_base_url():
    url = raw_input("Please enter base url of class \n")
    if url[-1] != "/":
        url += "/"
    inp = ''
    inp = raw_input("Is this base url correct? " + url + "\n")
    if inp.lower() not in ['y', 'yes', 't', 'true']:
        sys.exit()
    return url

def main():
    base_url = prompt_user_base_url()
    res = prompt_user_resolution()
    vid_paths = get_video_paths_for_res(base_url, res)
    # print(vid_paths)
    download_videos(base_url, vid_paths)


if __name__ == "__main__":
    main()
