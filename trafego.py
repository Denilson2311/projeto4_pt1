def analisar_trafego(r1, r2, r3) -> tuple:

    media = (r1 + r2 + r3) / 3

    if media < 100:
        status = "baixo trafego"

    elif media < 500:
        status = "trafego moderado"

    else:
        status = "trafego alto"

    return media, status