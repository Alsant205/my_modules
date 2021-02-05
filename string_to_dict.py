"""Строку из файла, содержащую словарь, преобразуем в словарь для дальнейшей работы с ним"""
import json
s = ["{'Printers':[['Printer', 'HP', 'Black', 1], ['Printer', 'HP', 'Black', 2]]}"]
s1 = ''.join(s)
a = json.loads(s1.replace("'", '"'))
