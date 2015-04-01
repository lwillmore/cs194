#!/usr/bin/env python

# import modules
from lxml import html
import requests
import requests.packages.urllib3.contrib.pyopenssl
requests.packages.urllib3.contrib.pyopenssl.inject_into_urllib3()
from bs4 import BeautifulSoup
import json


NUM_PAGES = 2#185

# build diagnosis dictionary
def get_diagnoses(key_soup):
	diags = {}
	j_key = json.loads(str(key_soup.find_all('p')[0])[3:-4])
	diag_facets = j_key['facet_collection']['diagnosis']['Facets']
	for facet in diag_facets.keys():
		diags[str(facet)] = diag_facets[str(facet)]['Text'].encode('ascii',errors='backslashreplace')
	return (diags)


# build list of pictures and diagnoses
def get_images(info_soup,diags):
	images = {}
	j = json.loads(str(info_soup.find_all('p')[0])[3:-4])
	results = j["Results"]
	for r in results:
		images[r["AssetId"]] = {"FileName" : r["FileName"], "diagnosis" : [diags[str(value['Id'])] for value in r["diagnosis"]]}
	return (images)

# download images with diagnosis
def download_images(images):
	for image in images:
	    image_name = image["FileName"]
	    url = 'https://www.dermquest.com/imagelibrary/thumb/'+image_name+'?height=110'
	    r = requests.get(url)
	    i = Image.open(StringIO(r.content))
	    i.save(image_name+image["diagnosis"])


if __name__ == '__main__':
	info_url = 'https://www.dermquest.com/Services/imageData.ashx?localization=107988|107987|107989|107990|107991|107992|107993|107994|107995|107996|107997|107998|107999|108000|108001|108002|108003|108004|108005|108006|108007|108008|108009|108010|108011|108012|108013|108025|108024|108026|108031|108032|108033|108034|108035|108027|108028|108029|108030|108036|108038|108037|108055|108054|108056|108057|108058|108059|108060|108061|108062|108063|108064|108065|108068|108066|108067|108053|108039|108052|108051|108047|108048|108049|108050|108042|108043|108044|108045|108046|108040|108041|108015|108014|108016|108017|108018|108019|108020|108021|108022|108023&page=1&perPage=128'
	info_page = requests.get(info_url)
	info_soup = BeautifulSoup(info_page.content)
	key_url = 'https://www.dermquest.com/Services/facetData.ashx'
	key_page = requests.get(key_url)
	key_soup = BeautifulSoup(key_page.content)
	diags = get_diagnoses(key_soup)
	for i in range(1,NUM_PAGES+1):
		images = get_images(info_soup)
		donload_images(images)

