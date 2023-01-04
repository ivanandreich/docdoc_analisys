import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import configparser as cp
import json


# def get_request_status(http):
#     r = requests.get(http)
#
#     return r
#
#
# def get_request(http):
#     return get_request_status(http).text


def read_config(file):
    config = cp.ConfigParser()  # создаём объекта парсера
    config.read(file)  # читаем конфиг

    return config

#
# def full_html(http):
#     return get_request(http)


def example_doctor_dict():
    doctor_dict = {'doctor_id': '',
                   'name': '',
                   'organization_id': [''],
                   'speciality': [''],
                   'rating': ''
                   }

    return doctor_dict

# def fill_doctors_list()


def fill_doctor_dict_list(doctors_json, index):

    doctor_dict_list = []
    for i in range(len(doctors_json["doctors"][index]['specialities'])):
        doctor_dict = example_doctor_dict()
        doctor_dict['speciality'] = doctors_json["doctors"][index]['specialities'][i]
        for j in range(len(list(doctors_json["doctors"][index]['clinics'].keys()))):
            doctor_dict['doctor_id'] = doctors_json["doctors"][index]['id']
            doctor_dict['name'] = doctors_json["doctors"][index]['name']
            if list(doctors_json["doctors"][index]['clinics'].keys()) == []:
                doctor_dict['organization_id'] = ""
            else:
                doctor_dict['organization_id'] = list(doctors_json["doctors"][index]['clinics'].keys())[j]
            # doctor_dict['speciality'] = doctors_json["doctors"][index]['specialities'][i]
            doctor_dict['rating'] = doctors_json["doctors"][index]['rating']['doctorRating']
            doctor_dict_list.append(doctor_dict)

    return doctor_dict_list


def save_doctors_json(doctors_json, id):
    file = open("doctors_jsons/" + str(id) + ".json", "w")
    file.write(doctors_json)
    file.close()


def doctors_html_to_json(doctors_page):
    soup = bs(doctors_page, "html.parser")
    doctors_tag = soup.find_all('doctor-list-page')
    doctors_json = str(doctors_tag[0])
    doctors_json = doctors_json[0:doctors_json.find('active-page-reception-type="clinic')]
    doctors_json = doctors_json[doctors_json.find("'"):len(doctors_json) - 1]
    doctors_json = '{"doctors": ' + doctors_json[1:doctors_json.find("' :filter-types='")] + '}'

    return doctors_json


def save_html(url):
    req = requests.get(url)
    with open("page.html", "w", encoding="utf-8") as file:
        file.write(req.text)
