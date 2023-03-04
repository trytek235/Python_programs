import random
import urllib.request

def web_download_page(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

web_download_page("https://www.southernliving.com/thmb/JOV1II4ho49bEI50Drk4RDtDK1Y=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/How_To_Soften_Butter_013-2000-61e8b4e1ad9c431887472483ae714dbb.jpg")