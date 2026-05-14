from servidor import avaliar_datacenter


def test_servidor_critico():
    assert avaliar_datacenter(80, 50, 40, 20, 50) == "Servidor crítico"


def test_servidor_alerta():
    assert avaliar_datacenter(50, 40, 30, 20, 50) == "Servidor em alerta"


def test_servidor_estavel():
    assert avaliar_datacenter(30, 40, 30, 20, 50) == "Servidor estável"