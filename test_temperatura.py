from temperatura import avaliar_temperatura

def test_avaliar_temperatura_frio():
    assert avaliar_temperatura(10) == 'Frio'

def test_avaliar_temperatura_ideal():
    assert avaliar_temperatura(30) == 'Ideal'
    
def test_avaliar_temperatura_alerta():
    assert avaliar_temperatura(50) == 'Alerta'
    
def test_avaliar_temperatura_risco_critico():
    assert avaliar_temperatura(90) == 'Risco Critico'