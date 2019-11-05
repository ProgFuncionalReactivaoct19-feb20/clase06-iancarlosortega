import csv

def lineasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter=";")

with open("data/data-estudiantes.csv") as midata:
	#print(list(lineasDiccionario(midata)))
	print(list(map(lambda x:"%s - %s" % (list(x.items())[0][1].split(" ")[1],
		list(x.items())[1][1].strip(".com")), list(lineasDiccionario(midata)))))