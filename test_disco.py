from disco import avaliar_disco

def test_avaliar_disco_seguro():
    assert avaliar_disco(50) == 'seguro'

def test_avaliar_disco_atencao():
    assert avaliar_disco(30) == 'atencao'
    
def test_avaliar_disco_critico():
    assert avaliar_disco(10) == 'critico'