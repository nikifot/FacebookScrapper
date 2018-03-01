from urllib import request, error
import requests
import json

# file_path = 'C:\\Users\\nikfotei\\Downloads\\'
# file_name = 'ids.txt'
# thumbnails_path = 'C:\\Users\\nikfotei\\Downloads\\thumbnails\\'
#
# with open(file_path + file_name, 'r') as ids_file:
#     line = ids_file.readline().strip()
#     while line:
#         # print(line.strip()) # debug line
#         try:
#             request.urlretrieve('https://graph.facebook.com/{}/picture'.format(line), thumbnails_path + line + '.jpg')
#         except error.HTTPError:
#             print('Http error 400: {}'.format(line))
#         finally:
#             line = ids_file.readline().strip()

#region params
pageID = '177995872646'
access_token = 'EAACEdEose0cBAH4JFfOn4F5S9oI2TH9OSjCFU0zk5x0WQZAkx5zyhhDANZCVvQKm1sYI2EdqTAu7hrkXgnpQxQdZAImsimGb2PJHCXMZBkzNLb8lTHmMUWXIoSFGxdUprAFiNXbyr0t1T6ZBgrZAT2Dl0T5R6p7sh3ZAlx0HrfKHD106DzxTWNpzsQQvPW53FS2JBmyulJB4wZDZD'
type = 'photos'
file_path = 'C:\\Users\\nikfotei\\Documents\\GitHub\\FacbookVideoScrap\\Facebook Video\\'
page = 'https://www.facebook.com/pg/KFC.uk/videos/'
#endregion

req = requests.get('https://graph.facebook.com/v2.12/{0}/{1}?limit=250&access_token={2}&fields=id,source,description,comments.limit(1).summary(true),likes.limit(1).summary(true)'.format(pageID, type, access_token))

def scrapping(request):
    # print(json.dumps(request.json(), indent=4))

    for i, video in enumerate(request.json()['data']):
        # if i > 2:
        #     break
        photo_id = request.json()['data'][i]['id']

        metadata = {"description": request.json()['data'][i]["description"]
        if "decription" in request.json()['data'][i] else '',
                    "comments": request.json()['data'][i]["comments"]["summary"],
                    "likes": request.json()['data'][i]["likes"]["summary"]}

        with open('Facebook Pictures/{}.json'.format(photo_id), 'w') as jsonfile:
            json.dump(metadata, jsonfile, indent=4)

        # video = 'https://www.facebook.com/video.php?v=' + video_id
        # print('https://www.facebook.com/video.php?v=' + video_id)
        r = requests.get(request.json()['data'][i]["source"])
        with open('Facebook Pictures/{}.jpeg'.format(photo_id), 'wb') as imagefile:
            for chunk in r.iter_content(chunk_size=512):
                if chunk:
                    imagefile.write(chunk)
            imagefile.close()
    if "next" in request.json()['paging']:
        scrapping(requests.get(request.json()['paging']["next"]))

if __name__=="__main__":
    scrapping(req)
print('done')