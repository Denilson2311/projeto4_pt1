from so import identificar_so


def test_identificar_so():
    resultado = identificar_so()

    sistemas_validos = ["Windows","Linux/Unix","Outro sistema"]

    assert resultado in sistemas_validos