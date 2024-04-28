from abc import ABC, abstractmethod


class ProcesadorStrategy(ABC):
    @abstractmethod
    def get_descuento(self, monto: float, porcentaje: float) -> float:
        pass




class TarjetaStrategy(ProcesadorStrategy):
   def get_descuento(self, monto: float, porcentaje: float) -> float:
        return monto * (porcentaje/100)

class TransferenciaStrategy(ProcesadorStrategy):
    def get_descuento(self, monto: float, porcentaje: float) -> float:
        return 0


class EfectivoStrategy(ProcesadorStrategy):
   def get_descuento(self, monto: float, porcentaje: float) -> float:

         descuento = monto * (porcentaje/100)

         descuento_total = descuento + (descuento *(porcentaje/100))

         return  descuento_total