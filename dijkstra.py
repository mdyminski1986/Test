#-*- coding: iso-8859-2 -*-
import pqueue

class Graph:
	"""
	Klasa reprezentująca grafy, w których można przeprowadzić przeszukiwanie 
	Dijkstra
	"""
	
	def __init__(self):
		"""
		Konstruktor
		nodes - Słownik, w którym kluczem jest wierzchołek, a wartością lista krotek.
			W liście każda krotka, to wierzchołek docelowy oraz waga krawędzi.
		d - Słownik, w którym kluczem jest wierzchołek, a wartością koszt drogi
			pomiędzy wierzchołkiem "startowym" a tym. Słownik ten jest uzupełniany
			w trakcie działania metody dijkstra.
		p - Słownik, w którym kluczem jest wierzchołek, a wartością jego "rodzic"
			w metodzie dijkstra.
		pq - kolejka priorytetowa / obiekt klasy PriorityQueue. Jest wykorzystywana
			w metodzie dijkstra.
		"""
		
		self.nodes = {}
		self.d = {}
		self.p = {}
		self.pq = pqueue.PriorityQueue()
	
	def add_node(self, node):
		"""
		Metoda dodająca wierzchołki do grafu.
		node - nazwa wierzchołka. Może byc string lub int.
		"""
		
		if node not in self.nodes:
			self.nodes[node] = []
			
	def add_edge(self, edge):
		"""
		Metoda dodająca krawędzie w grafie skierowanym. 
		edge - krotka 3-elementowa zawierająca wierzchołek źródłowy, doecelowy oraz
			wagę krawędzi.
		"""
		
		source, target, weight = edge
		self.add_node(source)
		self.add_node(target)
		if source == target:
			raise ValueError("Petle sa zabronione")
		if (target, weight) not in self.nodes[source]:
			self.nodes[source].append((target, weight))
	
	def add_edge_undirected(self, edge):
		"""
		Metoda dodająca krawędzie w grafie nieskierowanym. W zasadzie wykorzystuje
			metode dodawania krawędzi w grafie skierowanym.
		edge - krotka 3-elementowa zawierająca wierzchołek źródłowy, doecelowy oraz
			wagę krawędzi.
		"""
		
		self.add_edge(edge)
		target, source, weight = edge
		self.add_edge((source, target, weight))
	
	def read_file(self, file):
		"""
		Metoda tworząca graf z danych podanych w pliku tekstowym.
		file - ścieżka do pliku.
		"""
		
		infile = open(file, "r")
		directed = int(infile.readline())
		
		if directed == 1:
			for line in infile:
				source, target, weight = line.split()
				weight = int(weight)
				
				if source.isdigit():
					source = int(source)
				
				if target.isdigit():
					target = int(target)
				
				self.add_edge((source, target, weight))
		else:
			for line in infile:
				source, target, weight = line.split()
				weight = int(weight)
				
				if source.isdigit():
					source = int(source)
				
				if target.isdigit():
					target = int(target)
				
				self.add_edge_undirected((source, target, weight))
	
	def initial(self, start):
		"""
		Metoda przygotowująca dane startowe, przed rozpocząciem przeszukiwania
		Dijkstra.
		start - wierzchołek startowy przeszukiwania Dijkstra.
		"""
		
		for node in self.nodes:
			self.d[node] = float("inf")
			self.p[node] = -1
		
		self.d[start] = 0
	
	def relax(self, source):
		"""
		Metoda relaksacyjna. Przeszukuje wszystkie krawędzie wierzchołka "source"
			sprawdzając, czy suma kosztu drogi do "source" i wagi danej krawędzi
			jest mniejsza od dotychczasowego kosztu drogi do wierzchołka docelowego
			tej krawędzi. Jeśli tak, to aktualizuje koszt drogi oraz rodzica.
		source - wierzchołek źródłowy, którego krawędzie są przeszukiwane.
		"""
		
		for target, weight in self.nodes[source]:	
			print "Droga z", source, "do", target, "kosztuje", weight
			tmp = self.d[source] + weight
			
			if self.d[target] > tmp:
				self.pq.insert(target, tmp)
				self.d[target] = tmp
				self.p[target] = source
				print "Aktualizacja, rodzicem", target, "jest", source
	
	def dijkstra(self, start):
		"""
		Metoda przeszukiwania grafu algorytmem Dijkstra.
		start - wierzchołek, od którego zaczynamy przeszukiwanie.
		"""
		
		self.initial(start)
		
		for key in self.d.keys():
			self.pq.insert(key, self.d[key])
		
		while not self.pq.is_empty():
			source = self.pq.remove()
			print
			print "Przeprowadzam relaksacje na:", source
			self.relax(source)
	
	def dijkstra_print(self, start, end):
		"""
		Metoda przeprowadzająca przeszukiwanie Dijkstra oraz wypisująca na ekranie
			komunikat o najkrótszej drodze pomiędzy wierzchołkami "start" i "end".
		start - wierzchołek, od którego rozpocznie się przeszukiwanie Dijkstra.
		end - wierzchołek docelowy.
		"""
		
		self.dijkstra(start)
		
		tmp = end
		L = []
		L.append(tmp)
		print
		print "Najkrotsza droga z", start, "do", end, "to:"
		
		while start != tmp:
			tmp = self.p[tmp]
			L.append(tmp)

		for item in range(len(L)-1):
			print L.pop(), "->",
		
		print L.pop()
		print "I wynosi:", self.d[end]
		print
	
	def dijkstra_write(self, file):
		"""
		Metoda wypisująca do pliku tekstowego wynik działania metody dijkstra.
		file - ścieżka do pliku.
		"""
		
		if self.d.keys():
			outfile = open(file, "a")
			
			for node in self.nodes.keys():
				outfile.write(str(node) + " " + str(self.d[node]) + " " + str(self.p[node]) + "\n")
			
			outfile.write("\n")
			outfile.close()
			return True
		else:
			print "Brak danych do zapisu!"
			return False

	def listnodes(self):
		"""Zwraca listę wierzchołków grafu."""
		return self.nodes.keys()

	def listedges(self):
		"""Zwraca listę krawędzi (krotek) grafu."""
		L = []
		for source in self.nodes:
			for (target, weight) in self.nodes[source]:
				L.append((source, target, weight))
		return L

	def print_graph(self):
		"""Wypisuje postać grafu na ekranie."""
		for source in self.nodes:
			print source, ":",
			for (target, weight) in self.nodes[source]:
				print "%s(%s)" % (target, weight),
			print
	
g = Graph()
g.read_file("in.txt")
g.dijkstra_print(1, 3)
g.dijkstra_write("out.txt")
raw_input("Kliknij, aby kontynuowac...")
g.dijkstra_print(3, 2)
g.dijkstra_write("out.txt")

raw_input("Kliknij, aby kontynuowac...")
polska = Graph()
polska.read_file("polska.txt")
polska.dijkstra_print("Rzeszow", "Szczecin")
polska.dijkstra_write("rzeszow.txt")