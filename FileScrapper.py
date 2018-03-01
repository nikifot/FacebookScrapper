# reads facebook video ids from file and saves .mp4 in local folder
import youtube_dl

video_url = 'https://www.facebook.com/video.php?v='

with open('videos.csv', 'r') as file:
    videos = file.readlines()

del videos[0]
videos = [x.strip() for x in videos]

video_id = []
for video in videos:
    url_array = video.split('/')
    while '' in url_array:
        url_array.remove('')
    video_id.append(url_array[len(url_array) - 1])

for video in video_id:
    #print(video_url + video)
    try:
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url + video])
    except Exception:
        print(video + ' failed')

print('done')