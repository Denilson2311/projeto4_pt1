def avaliar_temperatura(
    temp: float
) -> str:

    if temp < 20:
        return "Frio"

    elif temp < 40:
        return "Ideal"

    elif temp < 70:
        return "Alerta"

    else:
        return "Risco Critico"