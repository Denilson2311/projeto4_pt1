def avaliar_disco(espaco_livre: float) -> str:

    if espaco_livre >= 40:
        return "seguro"

    elif espaco_livre >= 20:
        return "atencao"

    else:
        return "critico"