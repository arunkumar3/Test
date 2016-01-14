__author__ = 'ArunKumar'
import urllib2
import json
import pprint
import csv
import requests
import pprint
import urllib
invalid_list =[]
def create_post_url(graph_url, APP_ID, APP_SECRET):
	#create authenticated post URL
	post_args = "/posts/?key=value&access_token=" + APP_ID + "|" + APP_SECRET
	post_url = graph_url + post_args
	return post_url


def render_to_json(graph_url):
    #render graph url call to JSON
    #print graph_url
    post_args = "/posts/?key=value&access_token=" + APP_ID + "|" + APP_SECRET
    post_url = graph_url + post_args
    #print post_url
    json_data =''
    try:
        web_response = urllib2.urlopen(post_url)
        readable_page = web_response.read()
        json_data = json.loads(readable_page)


    except:
        invalid_list.append(graph_url)
        print graph_url
    return json_data


if __name__ == "__main__":
    count =0
    list_companies =[]
    with open('E:\\Arun\\College Material\\3rd Sem\\Big Data\\Assignment 2\\BrandNetworkAttributes.csv', 'rb') as comments:
        read_data = csv.reader(comments,delimiter = ',', skipinitialspace=True)
        next(comments)
        for eachrow in read_data:
            #print eachrow

            list_companies.append(eachrow[1])
        print(list_companies)
    APP_SECRET = "21c6fe409b37a2b161413567123814e4"
    APP_ID = "416456465194313"
    graph_url = "https://graph.facebook.com/"
    for company in list_companies:
        print count + 1
        count = count + 1
        current_page = graph_url + company
        json_fbpage = render_to_json(current_page)
        ##pprint.pprint(json_fbpage)

    with open('E:\\Arun\\College Material\\3rd Sem\\Big Data\\Assignment 2\\Invalid_list.csv', 'wb') as csv_file:
        content_writer = csv.writer(csv_file,quoting = csv.QUOTE_NONNUMERIC)
        for eachrow in invalid_list:
            content_writer.writerow([unicode(eachrow).encode('utf8')])
