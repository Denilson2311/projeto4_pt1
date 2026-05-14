import hashlib


def gerar_id_evento(nome_servidor: str, timestamp: str) -> str:

    texto = f"{nome_servidor}{timestamp}"

    id_evento = hashlib.sha256(
        texto.encode("utf-8")
    )

    return id_evento.hexdigest()