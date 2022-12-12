class Graph:
    def __init__(self):
        #constructor
        self._data = {}

    def addVertex(self, key):
        #menambah vertex
        if key not in self._data:
            self._data[key] = set()

    def vertex(self): #mencetak seluruh vertex
        
        print("\nSeluruh Node = ", end = "")
        # tulis kode Anda di bawah sini
        listkey = []
        for key, value in self._data.items():
            listkey.append(key)
        for i in listkey:
            print(i, end = " ")
        print()
    
    def edge(self): #mencetak seluruh edge
        print("Seluruh Edge = ", end = "")
        # tulis kode Anda di bawah sini
        listEdge = set()
        for key, value in self._data.items():
            for item in self._data[key]:
                if key+item not in listEdge and item+key not in listEdge:
                    listEdge.add(key+item)
        for item in listEdge:
            print(item, end= ' ')
        print()

    def addEdge(self, x, y):
        #menambah edge antara vertex x dan y
        if x in self._data and y in self._data:
            self._data[x].add(y)
            self._data[y].add(x) #hanya digunakan jika graph tidak berarah

    # untuk pembacaan traversing bfs graph
    def bfs(self, node):
        print("Traversing BFS = ", end = "")
        # silahkan tulis kode Anda di bawah ini 
        visited = []
        queue = []
        visited.append(node)
        queue.append(node)
        while queue:         
            m = queue.pop(0) 
            print (m, end = " ") 
            for i in self._data[m]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)
        print("\n")

# silahkan buat graph seperti pada soal
graph = Graph()
# misalnya 
# graph.addVertex('x')
# graph.addVertex('y')
# graph.addVertex('z')
# graph.addVertex('j')
# graph.addVertex('k')

# graph.addEdge('x', 'y')
# graph.addEdge('x','z')
# graph.addEdge('y', 'z')
# graph.addEdge('z', 'j')

graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')
graph.addVertex('e')
graph.addVertex('f')
graph.addVertex('g')
graph.addEdge('a', 'b')
graph.addEdge('b', 'c')
graph.addEdge('b', 'd')
graph.addEdge('d', 'e')
graph.addEdge('c', 'e')
graph.addEdge('c', 'g')
graph.addEdge('e', 'f')

# jangan ubah bagian di bawah 
graph.vertex()
graph.edge()
graph.bfs("a")