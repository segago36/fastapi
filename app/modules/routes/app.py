from app.modules.routes.strategytaller import EfectivoStrategy, ProcesadorStrategy, TarjetaStrategy, TransferenciaStrategy
from fastapi import APIRouter, Depends, HTTPException
from .strategy import CarRoute, BikeRoute, RouteStrategy, MotorcycleRoute
from enum import Enum


class Vehicle(Enum):
    CAR = "car"
    BIKE = "bike"
    MOTORCYCLE = "motorcycle"

class MetodoDePago(Enum):
    TARJETA = "tarjeta"
    EFECTIVO = "efectivo"
    TRANSFERENCIA = "transferencia"


def get_strategy(vehicle: Vehicle) -> RouteStrategy:
    if vehicle == Vehicle.CAR:
        return CarRoute()
    elif vehicle == Vehicle.BIKE:
        return BikeRoute()
    elif vehicle == Vehicle.MOTORCYCLE:
        return MotorcycleRoute()
    else:
        raise HTTPException(status_code=400, detail="Invalid vehicle")

def get_strategy_descuento(metodo_de_pago: ProcesadorStrategy) -> ProcesadorStrategy:
    if metodo_de_pago == MetodoDePago.TARJETA:
        return TarjetaStrategy()
    elif metodo_de_pago == MetodoDePago.EFECTIVO:
        return EfectivoStrategy()
    elif metodo_de_pago == MetodoDePago.TRANSFERENCIA:
        return TransferenciaStrategy()
    else:
        raise HTTPException(status_code=400, detail="Método de pago inválido")



router = APIRouter()


@router.get("/best_route")
def best_route(origin: int, destination: int, vehicle: RouteStrategy = Depends(get_strategy)) -> dict:
    return vehicle.get_best_route(origin=origin, destination=destination)


@router.get("/cost")
def cost(origin: int, destination: int, vehicle: RouteStrategy = Depends(get_strategy)) -> float:
    return vehicle.get_cost(origin=origin, destination=destination)


@router.get("/time")
def time(origin: int, destination: int, vehicle: RouteStrategy = Depends(get_strategy)) -> float:
    return vehicle.get_time(origin=origin, destination=destination)


@router.get("/descuento")
def descuento(monto: float, porcentaje: float, procesador: ProcesadorStrategy = Depends(get_strategy_descuento)) -> float:
    return procesador.get_descuento(monto=monto,porcentaje=porcentaje)