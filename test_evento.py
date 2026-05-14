from evento import gerar_id_evento


def test_gerar_id_evento():

    resultado = gerar_id_evento("server01","2025-05-13 10:00:00")

    esperado = ("ee7ee3bda51b5dd9e751db8446898e599b510222099fc21e75b8cb08ccf539be")

    assert resultado == esperado