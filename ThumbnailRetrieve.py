from urllib import request, error

file_path = 'C:\\Users\\nikfotei\\Downloads\\'
file_name = 'ids.txt'
thumbnails_path = 'C:\\Users\\nikfotei\\Downloads\\thumbnails\\'

with open(file_path + file_name, 'r') as ids_file:
    line = ids_file.readline().strip()
    while line:
        # print(line.strip()) # debug line
        try:
            request.urlretrieve('https://graph.facebook.com/{}/picture'.format(line), thumbnails_path + line + '.jpg')
        except error.HTTPError:
            print('Http error 400: {}'.format(line))
        finally:
            line = ids_file.readline().strip()
