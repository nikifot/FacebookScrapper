# finds all video ids from given facebook page and saves .mp4 files on local disk
import requests
import youtube_dl
import json


#region params
pageID = '114581942646'
access_token = 'EAACEdEose0cBAKHlOg8w9ZCpDUnxEOqay4UMW34GgTykPxXVIe3oSmpa9108m13r08iKD2e0bzV3u8I92DMtAX8kOQfIuzSNBSzEWnt9ZB8bkUZBFMtcrcXFWKUmt7ok4pRjpXZAXZBZAdkb5jL80HdpGTXR188ifoKf2PbUqFzz4P3webz00qEcLFAbYZAAUOoRprDhTuaiQZDZD'
type = 'videos'
file_path = 'C:\\Users\\nikfotei\\Documents\\GitHub\\FacbookVideoScrap\\Facebook Video\\'
page = 'https://www.facebook.com/pg/KFC.uk/videos/'
#endregion

req = requests.get('https://graph.facebook.com/v2.12/{0}/{1}?limit=250&access_token={2}&fields=id,description,comments.limit(1).summary(true),likes.limit(1).summary(true)'.format(pageID, type, access_token))

def scrapping(request):
    # print(request.json()["paging"])

    for i, video in enumerate(request.json()['data']):
        # if i > 2:
        #     break
        video_id = request.json()['data'][i]['id']

        metadata = {"description": request.json()['data'][i]["description"],
                    "comments": request.json()['data'][i]["comments"]["summary"],
                    "likes": request.json()['data'][i]["likes"]["summary"]}

        with open('Facebook Video/{}.json'.format(video_id), 'w') as jsonfile:
            json.dump(metadata, jsonfile, indent=4)

        video = 'https://www.facebook.com/video.php?v=' + video_id
        print('https://www.facebook.com/video.php?v=' + video_id)
        try:
            ydl_opts = {"outtmpl": "Facebook Video/{}.mp4".format(video_id)}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video])
        except Exception as e:
            print(e)

    if "next" in request.json()['paging']:
        scrapping(requests.get(request.json()['paging']["next"]))

if __name__=="__main__":
    scrapping(req)
print('done')