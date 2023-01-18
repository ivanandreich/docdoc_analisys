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

# r = requests.get('https://izh.docdoc.ru/clinic/ekomed')
save_html('https://izh.docdoc.ru/clinic/ekomed', 'ekomed.html')
# soup = bs(r.text, "html.parser")
# clinics_tag = soup.find_all('clinic-page')
#
# clinics_tag = str(clinics_tag[0])
#
# diag = clinics_tag[clinics_tag.find(':diagnostics-services=') + len(':diagnostics-services=') + 1:clinics_tag.find(':is-clinic-active="true"')-2]
# med = clinics_tag[clinics_tag.find(':med-services=') + len(':med-services=') + 1:clinics_tag.find(':total-reviews-count="35"')-2]
# full = diag[:len(diag)-1] + ',' + med[1:]
# print(full)
# # file = open("services.json", "w", encoding='cp1251')
# # l=json.loads(diag)
# # print(l)
# # json.dump(file, l)
# # file.write(json.dump(l, ensure_ascii=False))
# # file.close()
#
# services = json.loads(full)
# print(type(services))
#
# with open('services.json', 'w', encoding='utf-8') as fp:
#     json.dump(services, fp)

# print(services_dict)
# fill_doctors_json(doctors_url)
# fill_clinics_json(clinics_url)
# print(fill_specs_dict_list("doctors_json.json"))

# save_html(illness_url, 'illness_page.html')




