from google_images_search import GoogleImagesSearch

# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX

def my_progressbar(url, progress):
    print(f"{url} : {progress}%")
    
gis = GoogleImagesSearch('GOOGLE_API_KEY', 'PROJECT_CX_KEY', progressbar_fn=my_progressbar)

# define search params
# option for commonly used search param are shown below for easy reference.
# For param marked with '##':
#   - Multiselect is currently not feasible. Choose ONE option only
#   - This param can also be omitted from _search_params if you do not wish to define any value
_search_params = {
    'q': 'dream world',
    'num': 10,
    'fileType': 'jpg',
    'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived',
    'safe': 'active', ##
    # 'imgType': 'clipart|face|lineart|stock|photo|animated|imgTypeUndefined', ##
    # 'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge|imgSizeUndefined', ##
    # 'imgDominantColor': 'black|blue|brown|gray|green|orange|pink|purple|red|teal|white|yellow|imgDominantColorUndefined', ##
    # 'imgColorType': 'color|gray|mono|trans|imgColorTypeUndefined' ##
}

# # this will only search for images:
# gis.search(search_params=_search_params)

# # this will search and download:
# gis.search(search_params=_search_params, path_to_dir='/path/')

# this will search, download and resize:
gis.search(search_params=_search_params, path_to_dir='./images/dream_world', width=500, height=500, custom_image_name='dream_world')

# # search first, then download and resize afterwards:
# gis.search(search_params=_search_params)
# for image in gis.results():
#     image.url  # image direct url
#     image.referrer_url  # image referrer url (source) 
    
#     image.download('/path/')  # download image
#     image.resize(500, 500)  # resize downloaded image

#     image.path  # downloaded local file path