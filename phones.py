import bs4 as bs
import urllib.request
from phone import Phone
import csv
import pandas as pd

db_base_url = 'https://strefa-zakupowa.pl/rankingi/sprzet-telefoniczny/smartfon/'

telephone_rank_content = urllib.request.urlopen(db_base_url).read()

#print(telephone_rank_content)

telephone_rank_soup = bs.BeautifulSoup(telephone_rank_content, 'lxml')

# print(telephone_rank_soup.prettify())


telephones_odd = telephone_rank_soup.findAll(class_ = 'odd_rows')
telephones_even = telephone_rank_soup.findAll(class_ = 'even_rows')

phonesList = []
#
# for i, v in enumerate(telephones_odd):
#     phonesList.append(str(telephones_odd[i]).split("CPU: "))
# print(phonesList)


for telephone in telephones_even:
    tel_name = telephone.find('td', {'class' : 'prod_tab_def_tele'}).text
    ranking = telephone.find('div', {'class' : 'table_poz'}).text
    profitability = telephone.find('td', {'class' : 'oplacalnosc_def'}).text
    parameters = telephone.find('td', {'class' : 'param_def_tele'}).text
    price = telephone.find('div', {'class' : 'cena_tab'}).text


    CPU=str(parameters).split("CPU: ")[1].split("Pamięć RAM: ")[0]
    RAM=str(parameters).split("Pamięć RAM: ")[1].split("Wbudowana: ")[0]
    Wbudowana=str(parameters).split("Wbudowana: ")[1].split("Wyświetlacz: ")[0]
    Wyswietlacz=str(parameters).split("Wyświetlacz: ")[1].split("System: ")[0]
    System=str(parameters).split("System: ")[1].split("Aparat (tył): ")[0]
    Aparat=str(parameters).split("Aparat (tył): ")[1].split("Akumulator: ")[0]
    Akumulator=str(parameters).split("Akumulator: ")[1]


    print(tel_name)
    print(ranking)
    print(profitability)
    print(CPU)
    print(RAM)
    print(Wbudowana)
    print(Wyswietlacz)
    print(System)
    print(Aparat)
    print(Akumulator)
    print(price)


    phone=Phone(tel_name, ranking, profitability, CPU, RAM, Wbudowana, Wyswietlacz, System, Aparat, Akumulator, price)

    phonesList.append(vars(phone).values())

# print(phonesList)
# print(vars(phonesList))

with open('ranking_phones', 'w+', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(phonesList)
csvfile.close()

df = pd.read_csv('ranking_phones')