import __pycache__.Plato_Menu as Plato_Menu

class Menu:
    def __init__(self):
        self.platos = []
        
    def agregar_plato(self, nombre, descripcion, precio):
        self.pedidos.append(Plato_Menu(nombre, descripcion, precio))
    
    def remover_plato(self, nombre):
        self.pedidos = [plato for plato in self.platos if plato.nombre != nombre]
        
    def mostrar_menu(self):
        for plato in self.platos:
            print(f"{plato.nombre}: {plato.descripcion} - ${plato.precio}")
    