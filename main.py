import requests
from bs4 import BeautifulSoup as bs
import configparser as cp
import json
# pip install requests pandas configparser beautifulsoup4
# import time
# import lxml
# from functions import get_request, read_config, full_html, save_html, doctors_html_to_json, fill_doctors_json
#     get_request_status, example_doctor_dict
from functions import *

config = read_config("config.ini")

main_url = config["Url"]["main_url"]
doctors_url = config["Url"]["doctors_url"]
clinics_url = config["Url"]["clinics_url"]

r = requests.get('https://izh.docdoc.ru/clinic/lada_estet_na_karla_marksa')
soup = bs(r.text, "html.parser")
clinics_tag = soup.find_all('clinic-page')

clinics_json = str(clinics_tag[0])

diag = clinics_json[clinics_json.find(':diagnostics-services='):clinics_json.find('class="adaptive-clinic-page"')]
med = clinics_json[clinics_json.find(':med-services='):]
print(clinics_json)
services_dict = {'diag': diag
                 'med': med}

# fill_doctors_json(doctors_url)
# fill_clinics_json(clinics_url)
# print(fill_specs_dict_list("doctors_json.json"))

# save_html(illness_url, 'illness_page.html')




