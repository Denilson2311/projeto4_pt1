def avaliar_cpu(
    uso: float
) -> str:

    if uso < 40:
        return "normal"

    elif uso <= 80:
        return "alta"

    else:
        return "sobrecarga"