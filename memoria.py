def avaliar_memoria(mem: float) -> str:

    if mem < 50:
        return "Confortavel"

    elif mem < 85:
        return "Monitorar"

    else:
        return "Critica"