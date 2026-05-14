from armazenamento import prever_armazenamento


def test_armazenamento_seguro():

    resultado = prever_armazenamento(
        100, 10, 2
    )

    assert resultado == (
        +     121.00000000000001,
        "Seguro"
    )


def test_armazenamento_monitorar():

    resultado = prever_armazenamento(
        600, 20, 1
    )

    assert resultado == (
        720.0,
        "Monitorar"
    )


def test_upgrade_necessario():

    resultado = prever_armazenamento(
        1800, 20, 1
    )

    assert resultado == (
        2160.0,
        "Upgrade necessário"
    )