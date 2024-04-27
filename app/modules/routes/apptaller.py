from

from enum import Enum
from fastapi import APIRouter, HTTPException
from typing import Union


class MetodoDePago(Enum):
    TARJETA = "tarjeta"
    EFECTIVO = "efectivo"
    TRANSFERENCIA = "transferencia"


def obtener_procesador_de_pago(metodo_de_pago: MetodoDePago) -> ProcesadorDePago:
    if metodo_de_pago == MetodoDePago.TARJETA:
        return ProcesadorDeTarjeta()
    elif metodo_de_pago == MetodoDePago.EFECTIVO:
        return ProcesadorDeEfectivo()
    elif metodo_de_pago == MetodoDePago.TRANSFERENCIA:
        return ProcesadorDeTransferencia()
    else:
        raise HTTPException(status_code=400, detail="Método de pago inválido")


router = APIRouter()


@router.get("/procesar_pago")
def procesar_pago(monto: float, metodo_de_pago: MetodoDePago, procesador: ProcesadorDePago = Depends(obtener_procesador_de_pago)) -> bool:
    return procesador.procesar_pago(monto=monto)

@router.get("/procesador de pago")
class ProcesadorDePago:
    def procesar_pago(self, monto: float) -> bool:
        return metodo_de_pago.get_procesar_pago


class ProcesadorDeTarjeta(ProcesadorDePago):
    def procesar_pago(self, monto: float) -> bool:
        # Lógica para procesar el pago con tarjeta
        return True


class ProcesadorDeEfectivo(ProcesadorDePago):
    def procesar_pago(self, monto: float) -> bool:
        # Lógica para procesar el pago en efectivo
        return


class ProcesadorDeTransferencia(ProcesadorDePago):
    def procesar_pago(self, monto: float) -> bool:
        # Lógica para procesar el pago por transferencia
        return True
