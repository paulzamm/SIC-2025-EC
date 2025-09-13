from random import randint

# Resolución de ejercicios del quiz

# Q 22-01
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        """Agrega un elemento a la pila."""
        self.stack.append(item)
    
    def pop(self):
        """Elimina y devuelve el elemento superior de la pila."""
        return self.stack.pop()
    
    def is_empty(self):
        """Verifica si la pila está vacía."""
        return len(self.stack) == 0
    
    def peek(self):
        """Devuelve el elemento superior de la pila sin eliminarlo."""
        return self.stack[-1]

stack = Stack()
stack.push("Banana")
stack.push("Apple")
stack.push("Tomato")
stack.pop()
stack.push("Strawberry")
stack.push("Grapes")
stack.pop()
print(stack.stack)

# Q 22-02
stack_2 = Stack()
items = [10 * i for i in range(1, 10)]
for item in items:
    stack_2.push(item)
    if (item // 10) % 2 == 0:
        stack_2.pop()

print(stack_2.stack)

# Q 23-01
class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        """Agrega un elemento al final de la cola."""
        self.queue.append(item)
        
    def dequeue(self):
        """Elimina y devuelve el primer elemento de la cola."""
        return self.queue.pop(0)

    def is_empty(self):
        """Verifica si la cola está vacía."""
        return len(self.queue) == 0
    
    def peek(self):
        """Devuelve el primer elemento de la cola sin eliminarlo."""
        return self.queue[0]
    
    def size(self):
        """Devuelve la cantidad de elementos de la cola."""
        return len(self.queue)

queue = Queue()
queue.enqueue("Banana")
queue.enqueue("Apple")
queue.enqueue("Tomato")
queue.dequeue()
queue.enqueue("Strawberry")
queue.enqueue("Grapes")
queue.dequeue()
print(queue.queue)

# Q 23-02
queue_2 = Queue()
items_2 = [10 * i for i in range(1, 10)]
for item in items_2:
    queue_2.enqueue(item)
    if (item // 10) % 2 == 0:
        queue_2.dequeue()

print(queue_2.queue)

# Q 24-01
def find_two(nums):
    x = y = 0
    for i in range(1, len(nums)):
        if nums[x] < nums[i]:
            x = i
        elif nums[y] > nums[i]:
            y = i
        print(f"Iteración: {i}, x: {nums[x]}, y: {nums[y]}")
    return (x, y)

nums = [11, 37, 45, 26, 59, 28, 17, 53]
i, j = find_two(nums)
print(nums[i], nums[j])

# Q 25-01
maximo = int(input("Ingrese el número maximo: "))
numero = int(input("Ingrese tu intento de adivinar el numero: "))
low, high = 1, maximo
count = 0
while low < high:
    count += 1
    mid = (low + high) // 2
    if mid == numero:
        print(f"El número es {numero}")
        break
    elif mid > numero:
        high = mid - 1
    else:
        low  = mid + 1

print(f"Total {count} veces fue buscado.")

# Q 25-02
class TablaHash:
    def __init__(self, tamaño=8):
        """
        Constructor de la tabla hash
        """
        self.tamaño = tamaño
        # Creamos una lista con "tamaño" buckets vacíos
        self.tabla = [[] for _ in range(tamaño)]  

    def funcion_hash(self, clave):
        """
        Convierte la clave (string) en un número.
        """
        return sum(ord(c) for c in clave) % self.tamaño

    def put(self, clave, valor):
        """
        Inserta un par (clave, valor) en la tabla.
        """
        indice = self.funcion_hash(clave)
        
        # Recorremos el bucket en ese índice para ver si ya existe la clave
        for i, (k, v) in enumerate(self.tabla[indice]):
            if k == clave:
                # Si encontramos la misma clave → actualizamos el valor
                self.tabla[indice][i] = (clave, valor)  
                return
        
        # Si no encontramos la clave, la agregamos al bucket
        # (aunque haya ya otras claves en ese mismo índice)
        self.tabla[indice].append((clave, valor))

    def get(self, clave):
        """
        Busca un valor asociado a una clave.
        """
        indice = self.funcion_hash(clave)
        for k, v in self.tabla[indice]:
            if k == clave:
                return v
        return None  # la clave no existe en la tabla

    def __str__(self):
        """
        Representación de la tabla hash en forma de texto.
        """
        resultado = []
        for i, bucket in enumerate(self.tabla):
            resultado.append(f"{i}: {bucket}")
        return "\n".join(resultado)

table = TablaHash(8)
book = "Alice in Wonderland"
key = sum(map(ord, book))
print("key: ",key, "Hash: ",table.funcion_hash(book))

# Q 26-02
table_2 = TablaHash(10)
books = [
    "The Little Prince",
    "The Old Man and the Sea",
    "The Little Memaid",
    "Beauty and the Beast",
    "The Last Leaf",
    "Alice in Wonderland",
]

for book in books:
    table_2.put(book, book)

for valor, bucket in enumerate(table_2.tabla):
    if bucket:
        print(f"Bucket {valor}: {bucket}")