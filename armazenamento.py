def prever_armazenamento(inicial: float,taxa: float,anos: int) -> tuple:

    final = inicial * (1 + taxa / 100) ** anos

    if final < 500:
        status = "Seguro"

    elif final < 2000:
        status = "Monitorar"

    else:
        status = "Upgrade necessário"

    return final, status