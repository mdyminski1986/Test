#-*- coding: iso-8859-2 -*-

class PriorityQueue:
	"""
	Klasa reprezentująca kolejkę priorytetową, wykorzystywaną w algorytmie dijkstra.
	"""

	def __init__(self):
		"""
		Konstruktor
		d - Słownik, w którym kluczem jest wierzchołek, a wartością koszt drogi
			pomiędzy wierzchołkiem "startowym" a tym. Słownik ten jest uzupełniany
			w trakcie działania metody dijkstra.
		"""
		
		self.d = {}

	def __str__(self):   # podglądamy kolejkę
		return str(self.d)

	def is_empty(self):
		"""
		Metoda zwraca "True" jeśli kolejka pusta i "False" jeśli nie jest pusta.
		"""
		
		return not self.d

	def insert(self, key, value):
		"""
		Metoda dodaje element do kolejki.
		"""
		
		self.d[key] = value
		print "d[" + str(key) + "] = " + str(value)

	def remove(self):
		"""
		Metoda zwraca i usuwa najmniejszy element z kolejki.
		"""
		
		L = self.d.keys()
		mini = L[0]
		
		for key in self.d.keys():
			if self.d[key] < self.d[mini]:
				mini = key
				print "Aktualnie indeks minimalny w kolejce to:", mini
		self.d.pop(mini)
		return mini