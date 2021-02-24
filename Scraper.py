import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 RuxitSynthetic/1.0 v8404650969 t38550 ath9b965f92 altpub cvcv=2"}

url = "https://www.swiggy.com/"
response_city = requests.get(url, headers=headers)
print(response_city)
content_city = response_city.content
soup_city = BeautifulSoup(content_city, "html.parser")

name_city = soup_city.find_all('ul', class_="_1w9D3")
html_code = "<html><body>" + str(name_city) + "</body></html>"
soup = BeautifulSoup(html_code, "html.parser")

# Content from swiggy homepage and saving all the city name listed there
url_city = []
cities = []

for u in soup.find_all('a'):
    # print(u)
    url_city.append(u.get('href'))
    cities.append(u.string)

city_name = input("Enter the city name ")
cities = ['hyderabad', 'chennai', 'vijayawada', 'bangalore', 'mumbai']
for city_name in cities:
    city_name = city_name.lower()
    if city_name in cities:
        cur_url = url + url_city[cities.index(city_name)][1:] + "/top-rated-collection"
        # "https://www.swiggy.com/"+city_name+"/top-rated-collection"
        print("The site will be: ", cur_url)
    else:
        print("Swiggy currently not operating in ", city_name)

    response = requests.get(cur_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    restaurants = soup.find_all("div", class_="_3XX_A")
    html_code = "<html><body>" + str(restaurants) + "</body></html>"
    soup_res = BeautifulSoup(html_code, "html.parser")

    # print("Something here",soup_res.find('div',attrs={"class":"_1gURR"}).text)

    list_tr = []
    for i in range(0, len(restaurants)):
        list_tr.append(restaurants[i].find_all("div", class_="_3Ztcd"))

    list_rest = []
    for tr in list_tr:
        # print(tr)
        html_code = "<html><body>" + str(tr) + "</body></html>"
        soup_tr = BeautifulSoup(html_code, "html.parser")
        dataframe = {}
        dataframe["rest_name"] = (soup_tr.find("div", attrs={"class": "nA6kb"})).text.replace('\n', ' ')
        dataframe["cuisine_type"] = (soup_tr.find("div", attrs={"class": "_1gURR"})).text.replace('\n', ' ')
        list_rest.append(dataframe)

    # find the restaurant links in that area
    rest_divs = []
    rest_urls = []
    rest_divs.extend(soup_res.find_all('a', class_="_1j_Yo"))
    # print(rest_divs)
    for div in rest_divs:
        html_code = "<html><body>" + str(div) + "</body></html>"
        soup_url = BeautifulSoup(html_code, "html.parser")
        rest_urls.append(soup_url.a.get('href'))
    print("RestURLs", rest_urls)
    pcLink = "https://www.swiggy.com/" + city_name + "/top-rated-collection"
    print("For Top rated restaurants  in your current city: ", pcLink)
    # Now we are going to each restaurant and collect their menu
    rest_names = []
    cuisines = []
    for i in list_rest:
        rest_names.append(i['rest_name'])
        cuisines.append(str(i['cuisine_type'].split(',')[:1][0]))
    links = {'CityName': city_name, 'CityLink': pcLink, 'RestaurantName': rest_names, 'Cuisines': cuisines,
             'Restaurant links': rest_urls
             }
    df = pd.DataFrame.from_dict(links)
    df.to_csv("CitiesData.csv", mode='a', index=False)
