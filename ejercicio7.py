import csv

def lineasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter=";")

with open("data/trabajadores.csv") as midata:
	
	lista = list(filter(lambda x:len(list(x.items())[0][1].split("\t")[2])>10, lineasDiccionario(midata)))
	print(list(sorted(lista, key=lambda x:list(x.items())[0][1].split("\t")[1])))