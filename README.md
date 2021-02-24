# Web-Scraping-

Web scraping for food trend Insights
								By A. Mounika Durga
The purpose of this research is to discuss web scraping as a method for extracting large amounts of data from online sources. We scraped data from online food delivery websites to analyze food trends. 
The basic idea of analyzing the Swiggy dataset is to get a fair idea about the factors affecting the establishment of different types of restaurants at different places in Bengaluru. This Zomato data aims at analyzing demography of the location. Most importantly it will help new restaurants in deciding their theme, menus, cuisine, cost, etc for a particular location. It also aims at finding similarity between neighborhoods of Bengaluru on the basis of food.

Information extracted from the site
●	Cities in which Swiggy is currently operating
●	Popular restaurants in those cities
●	Links to the restaurants
●	Types of cuisines available in those restaurants
●	Ratings of the restaurants
Software Requirements
1.	Python 
2.	Requests library (for connecting to the website)
3.	Beautiful soup library (for web scraping)
4.	Pandas library (for data analysis) in our local machine
Why should we scrape the web?
Python to help automate the repetitive parts of your job search. Automated web scraping can be a solution to speed up the data collection process. You write your code once and it will get the information you want many times and from many pages. Manual web scraping can take a lot of time and repetition.
API can be an alternative to web scraping, but it much harder to inspect the structure of an API by yourself if the provided documentation is lacking in quality.
So, for the scraping of Swiggy website, we are using Beautiful Soup and Python.
Part 1: Inspecting our data source
●	First, we have to visit the website which we want to scrape and make a note of the elements where the data is present which you want to scrape.
●	You’ll need to understand the website structure to extract the information you’re interested in it.

Decipher the URLs
Understanding how URLs are modifying when we move forward from one page to another
In every URL there are two parts 1. Base URL and 2. Query parameters 
Whenever we move from one page to another the base url will remain same and the next will change accordingly.
Inspecting the data elements 
By using developer tools in web browser, we can interactively explore the website DOM. When we click on the inspect in browser, we can see the clickable html elements and we can understand the hierarchy of the DOM tree and also understand with what CSS elements we are working on.
Part 2: Scrape and parse HTML content from a page with Beautiful Soup

When we click inspect element in the browser as mentioned we will see html codes and can find the class names on the elements that we are interested.
We can make use of them with the help of beautiful soup
Extract Text from HTML Elements
Find Elements by Class Name and Text Content
Pass a function to a Beautiful Soup Method
Extract Attributes from HTML Elements
Example:
response_city = requests.get(url, headers=headers)
content_city = response_city.content
soup_city = BeautifulSoup(content_city, "html.parser")
name_city = soup_city.find_all('ul', class_="_1w9D3")
After doing all these steps we will save our results to python lists and we can create a Pandas dataframe and later save it in csv file format.
We did all these steps to collect the data from 5 south Indian cities and saved the information as a .csv file.
df = pd.DataFrame(dict) 
# saving the dataframe 
df.to_csv('CitiesData.csv')
Pandas allows user for fast analysis, data cleaning and preparation of data efficiently.
Part 3: Analysing the obtained csv file
For this we need few python libraries
●	Pandas
●	Seaborn
●	Matplotlib
df = pd.read_csv('CitiesData.csv')
The columns we have in the csv file are CityName, CityLink, RestaurantNames, Cuisine Types, Restaurant links for further scraping.
Exploratory Data Analysis:
The below graph gives trends of popular cuisines in five major cities.  

We carried out an in-depth analysis on Bengaluru city 
 
 
Most of the restaurants are rated between 4.1 to 4.3 ratings. Very few restaurants are rated low due to low quality.
 
The top ten cuisines traded in Swiggy are listed in the above graph.
 North Indian, Desserts and Chinese foods tops the table.
 
The cost of food varies between 100 to 800 Rs/two per person. This shows Bengalureans are interested in the both local and high value restaurants foods
Conclusion
In this study, we have discussed how to extract data using web scrapping techniques. As explained about basic explanatory data analysis techniques to derive food trends and insights. 

