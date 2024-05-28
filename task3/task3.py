# Формирование файла report.json с заполненными полями value для структуры tests.json на основании values.json
# В качестве аргументов принимает три файла в след. порядке: файл с тестами, файл с результатами и файл отчета

import json

def create_report(tests, values, report):

    with open(tests, 'r') as t:
        data_tests = json.load(t)

    with open(values, 'r') as v:
        data_values = json.load(v)

    for el in data_values["values"]:
        for el_1 in data_tests["tests"]:
            if el_1["id"] == el["id"]:
                el_1["value"] = el["value"]
            if "values" in el_1:
                for el_2 in el_1["values"]:
                    if el_2["id"] == el["id"]:
                        el_2["value"] = el["value"]
                    if "values" in el_2:
                        for el_3 in el_2["values"]:
                            if el_3["id"] == el["id"]:
                                el_3["value"] = el["value"]
                            if "values" in el_3:
                                for el_4 in el_3["values"]:
                                    if el_4["id"] == el["id"]:
                                        el_4["value"] = el["value"]

    with open(report, 'w') as r:
        json.dump(data_tests, r, ensure_ascii=False, indent=2)


create_report(input(), input(), input())