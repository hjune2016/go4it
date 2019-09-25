from bs4 import BeautifulSoup
import urllib.request as req
import csv

input_file = "/Users/Surface/Desktop/go4it/total.csv"
output_file = "/Users/Surface/Desktop/go4it/total2.csv"

def url_fun(row_list_output):
    for html1 in row_list_output:
         url = "https://store.naver.com/restaurants/detail?entry=pll&id={}".format(str(html1))
         return url

def place_info(url):
    try:
        html = req.urlopen(url).read()
    except req.HTTPError:
        print('HTTPError exception 발생')

    soup = BeautifulSoup(html, "html.parser", from_encoding='utf-8')
    place=[]
    menu=[]
    price=[]
    time=[]
    imgUrl=[]

    for p_name in soup.find('div', {'class': 'biz_name_area'}).findAll("strong", {"name": ""}):
        place.append(p_name.text)

    for m_name in soup.findAll('span', {'class': 'name'}):
        menu.append(m_name.text)

    for m_price in soup.findAll('em', {'class': 'price'}):
        price.append(m_price.text)

    for clock in soup.find('span', {'class': 'time'}):

        time.append(clock.text)

    for img in soup.findAll('div', class_='thumb'):
        imgUrl.append(img.find("img")["src"])

    group = [place,menu,price,time,imgUrl]
    return group

selected_column= [0]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        freader = csv.reader(csv_in_file)
        fwirter = csv.writer(csv_out_file)
        next(freader)
        for row_list in freader:
            row_list_output =[]
            for index_value in selected_column:
                row_list_output.append(row_list[index_value])
                fwirter.writerow(place_info(url_fun(row_list_output)))
    csv_out_file.close()
csv_in_file.close()
