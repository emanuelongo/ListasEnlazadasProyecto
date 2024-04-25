from Biblioteca import Biblioteca

class Finanzas:
    
    def __init__(self, historialLibrosAlquilados: Biblioteca):
        self.historialLibrosAlquilados = historialLibrosAlquilados
    
    def calcularIngresosTotalesPorAlquileres(self):
        
        ingresosTotales = 0
        for elemento in self.historialLibrosAlquilados:
            
            if self.historialLibrosAlquilados.length >= 2:
                ingresosTotales += (elemento.value.tarifaAlquiler - ((elemento.value.tarifaAlquiler) * 0.1))
            
            else:
                ingresosTotales += elemento.value.tarifaAlquiler
        
        return ingresosTotales