"""
Para desarrollar el problema del inventario.

"""

from MDPs import MDP, iteracion_valor

class Inventario(MDP):
    """
    Clase que representa un MDP para el problema del camión mágico.
    
    Si caminas, avanzas 1 con coso 1
    Si usas el camion, con probabilidad rho avanzas el doble de donde estabas
    y con probabilidad 1-rho te quedas en el mismo lugar. Todo con costo 2.
    
    El objetivo es llegar a la meta en el menor costo posible
    
    """    
    
    def __init__(self, gama,lambda_): 
        self.gamma = gama
        self.lambda_ = lambda_
        self.capacidad = 20
        self.inventario_min = -10
        self.precio_venta=150
        self.costo_compra=80
        self.costo_fijo=40
        self.costo_almacen=5
        self.costo_backlog=15
        self.estados = tuple(range(inventario_min,capacidad+1))
        
    
    def acciones_legales(self, s):
        return range(self.capacidad -s + 1)
    
    def recompensa(self, s, a, s_):
        demanda = (s+a)-s_
        venta = min(demanda, s+a)
        ganancia = venta * self.precio_venta 
        costo = a*self.costo_compra
        if a > 0:
            costo += self.costo_fijo
        if s_ > 0:
            costo += s_ * self.costo_almacen
        if s_ < 0:
            costo += abs(s_) * self.costo_backlog
        return ganancia - costo
        
    def prob_transicion(self, s, a, s_):
        demanda = (s+a)-s_
        if demanda < 0:
            return 0
        return (self.lambda_**demanda * np.exp(-self.lambda_)) / np.math.factorial(demanda)
                
    def es_terminal(self, s):
        return False 


if __name__ == "__main__":

    inventario = Inventario(0.9, 0.5, ...)  #TODO: Agregar lo que se requiera

    pi_star, V = iteracion_valor(inventario, ...) #TODO: Agregar lo que se requiera

    print("-" * 60)
    print("Estado".center(20) + "Acción".center(20) + "Valor".center(20))
    print("-" * 60 )
    for s in pi_star:
        print(f"{s:^20}{pi_star[s]:^20}{V[s]:^20.2f}")
    print("-" * 60)


"""
Contesta las preguntas aquí mismo (has espacio entre las preguntas):

1. ¿Cómo se comporta las transiciones y las ganancias para casos específicos de $s$ y $a$? 
2. ¿Qué psa si hay mucho almacen? 
3. ¿Que pasa si hay muy poco o estamos sin almacen? 
4. ¿Existe un punto donde la ganancia sea máxima?  
---
5. ¿Cómo se ve la política óptima? ¿Tiene sentido?
6. ¿Como se comporta la función de valor de estado V(s)?
7. ¿Cómo cambiaría la política si la variabilidad de la demanda (lambda) aumenta de 4 a 8?

"""