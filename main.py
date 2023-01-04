import requests
from bs4 import BeautifulSoup as bs
# import pandas as pd
import configparser as cp
import json
# pip install requests pandas configparser beautifulsoup4
# import time
# import lxml
# from functions import get_request, read_config, full_html, save_html, doctors_html_to_json,\
#     get_request_status, example_doctor_dict
from functions import *

config = read_config("config.ini")

main_url = config["Url"]["main_url"]
doctors_url = config["Url"]["doctors_url"]
i = 1
r = requests.get(doctors_url + str(i))
doctors_list = []
file = open("doctors_json.json", "w")

while r.ok:
    r = requests.get(doctors_url + str(i))
    print("request number " + str(i) + ': ' + str(r))
    doctors_json = doctors_html_to_json(r.text)
    doctors_json = json.loads(doctors_json)

    for index in range(len(doctors_json["doctors"])):
        doctor_dict_list = fill_doctor_dict_list(doctors_json, index)
        # print(doctor_dict)
        for k in range(len(doctor_dict_list)):
            doctors_list.append(doctor_dict_list[k])

    if i == 30:
        break
    i += 1
    r = requests.get(doctors_url + str(i))
doctors_list = json.dumps({'doctors': doctors_list}, ensure_ascii=False)
file.write(doctors_list)
# orgs_list =
# if not r.ok:
# file.write(']}')
file.close()

# print(doctors_list)


# «Id врача»
# «Имя»
# «Id специализации» (несколько) - если несколько, то дублируем
# «Id организации» - (несколько) - если несколько, то дублируем
# «Рейтинг врача»
