from certificado import validar_certificado


def test_certificado_expirado():

    resultado = validar_certificado("2020-01-01",1)

    assert resultado == "Certificado expirado"


def test_certificado_expira_em_breve():

    resultado = validar_certificado("2025-05-01",1)

    assert resultado == ("Certificado expirado")


def test_certificado_valido():

    resultado = validar_certificado("2025-01-01",5)

    assert resultado == ("Certificado válido")