import csv

def lineasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter=";")

with open("data/trabajadores.csv") as midata:
	lista = list(filter(lambda x:len(x[2][1])>10, lineasDiccionario(midata)))

	print(lista)
