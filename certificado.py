from datetime import datetime


def validar_certificado(
    data_emissao: str,
    anos: int
) -> str:

    emissao = datetime.strptime(
        data_emissao,
        "%Y-%m-%d"
    )

    validade = emissao.replace(
        year=emissao.year + anos
    )

    hoje = datetime.today()

    dias_restantes = (
        validade - hoje
    ).days

    if dias_restantes < 0:
        return "Certificado expirado"

    elif dias_restantes <= 30:
        return (
            "Certificado expira em breve"
        )

    else:
        return "Certificado válido"