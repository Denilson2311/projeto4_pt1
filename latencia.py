def classificar_latencia(lat: float) -> str:

    if lat < 10:
        return "excelente"

    elif lat < 40:
        return "boa"

    elif lat < 100:
        return "regular"

    else:
        return "ruim"