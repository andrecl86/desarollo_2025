class Producto:

    def __init__(self, id, nombre, precio, cantidad):
        self._id = id
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio

    def get_cantidad(self):
        return self._cantidad

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_precio(self, precio):
        self._precio = precio

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad