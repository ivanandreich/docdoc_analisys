import requests
from bs4 import BeautifulSoup as bs
# import pandas as pd
import configparser as cp
import json


def save_html(url, name):
    req = requests.get(url)
    with open(name, "w", encoding="utf-8") as file:
        file.write(req.text)


def read_config(file):
    config = cp.ConfigParser()  # создаём объекта парсера
    config.read(file)  # читаем конфиг

    return config


def example_doctor_dict():
    doctor_dict = {'doctor_id': '',
                   'name': '',
                   'organization_id': [''],
                   'speciality': [''],
                   'rating': ''
                   }

    return doctor_dict


def example_clinic_dict():
    clinic_dict = {'clinic_id': '',
                   'name': '',
                   'rating': ''
                   }

    return clinic_dict


def example_spec_dict():
    spec_dict = {'spec_id': '',
                 'name': '',
                 'clinic_id': ''
                 }

    return spec_dict


def example_service_dict():
    service_dict = {'service_id': '',
                    'name': '',
                    'price': '',
                    'clinic_id': ''
                    }

    return service_dict


def save_doctors_json(doctors_json, id):
    file = open("doctors_jsons/" + str(id) + ".json", "w")
    file.write(doctors_json)
    file.close()


def save_clinics_json(clinics_json, id):
    file = open("clinics_jsons/" + str(id) + ".json", "w")
    file.write(clinics_json)
    file.close()


def doctors_html_to_json(doctors_page):
    soup = bs(doctors_page, "html.parser")
    doctors_tag = soup.find_all('doctor-list-page')
    doctors_json = str(doctors_tag[0])
    doctors_json = doctors_json[0:doctors_json.find('active-page-reception-type="clinic')]
    doctors_json = doctors_json[doctors_json.find("'"):len(doctors_json) - 1]
    doctors_json = '{"doctors": ' + doctors_json[1:doctors_json.find("' :filter-types='")] + '}'

    return doctors_json


def clinics_html_to_json(clinics_page):
    soup = bs(clinics_page, "html.parser")
    clinics_tag = soup.find_all('clinic-list-page')
    clinics_json = str(clinics_tag[0])
    clinics_json = clinics_json[clinics_json.find(':clinics-list='):clinics_json.find(":has-bottom-content")]
    clinics_json = clinics_json[clinics_json.find("'"):len(clinics_json) - 1]
    clinics_json = clinics_json[1:len(clinics_json) - 1]
    clinics_json = '{"clinics": ' + clinics_json + '}'

    return clinics_json


def services_html_to_json(services_page):
    soup = bs(services_page, "html.parser")


def fill_clinics_dict_list(clinics_json, index):
    clinics_dict_list = []
    for index in range(len(clinics_json['clinics'])):
        clinic_dict = example_clinic_dict()
        clinic_dict['clinic_id'] = clinics_json['clinics'][index]['id']
        clinic_dict['name'] = clinics_json['clinics'][index]['name']
        clinic_dict['rating'] = clinics_json['clinics'][index]['reviews']['rating']
        clinics_dict_list.append(clinic_dict)

    return clinics_dict_list


def fill_specs_dict_list(file):
    data = open(file)
    str_data = data.read()
    doctors_json = json.loads(str_data)
    specs_dict_list = []
    print(len(doctors_json["doctors"]))
    for index in range(len(doctors_json["doctors"])):
        spec_dict = example_spec_dict()
        spec_dict['spec_id'] = doctors_json["doctors"][index]["speciality"]["id"]
        spec_dict['name'] = doctors_json["doctors"][index]["speciality"]["name"]
        spec_dict['clinic_id'] = doctors_json["doctors"][index]["organization_id"]
        specs_dict_list.append(spec_dict)
    data.close()

    return specs_dict_list


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


def fill_doctors_json(url):
    print("Введите ограничения на кол-во запросов врачей (0, если ограничений нет)")
    requests_limit = int(input())
    i = 1
    r = requests.get(url + str(i))
    doctors_list = []
    file = open("doctors_json.json", "w")

    while r.ok:
        r = requests.get(url + str(i))
        print("doctors request number " + str(i) + ': ' + str(r))
        doctors_json = doctors_html_to_json(r.text)
        doctors_json = json.loads(doctors_json)

        for index in range(len(doctors_json["doctors"])):
            doctor_dict_list = fill_doctor_dict_list(doctors_json, index)
            # print(doctor_dict)
            for k in range(len(doctor_dict_list)):
                doctors_list.append(doctor_dict_list[k])

        if i == requests_limit and requests_limit != 0:
            break
        i += 1
        r = requests.get(url + str(i))
    doctors_list = json.dumps({'doctors': doctors_list}, ensure_ascii=False)
    file.write(doctors_list)

    file.close()


def fill_clinics_json(url):
    print("Введите ограничения на кол-во запросов клиник (0, если ограничений нет)")
    requests_limit = int(input())
    i = 1
    r = requests.get(url + str(i))
    clinics_list = []
    file = open("clinics_json.json", "w")

    while r.ok:
        r = requests.get(url + str(i))
        print("clinics request number " + str(i) + ': ' + str(r))
        clinics_json = clinics_html_to_json(r.text)
        clinics_json = json.loads(clinics_json)

        for index in range(len(clinics_json["clinics"])):
            clinics_dict_list = fill_clinics_dict_list(clinics_json, index)
            for k in range(len(clinics_dict_list)):
                clinics_list.append(clinics_dict_list[k])

        if i == requests_limit and requests_limit != 0:
            break
        i += 1
        r = requests.get(url + str(i))
    # print(clinics_list)
    clinics_json = json.dumps({'clinics': clinics_list}, ensure_ascii=False)
    file.write(clinics_json)

    file.close()
