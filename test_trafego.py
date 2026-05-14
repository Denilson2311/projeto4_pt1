from trafego import analisar_trafego

def test_analisar_trafego_baixo_trafego():
    resultado = analisar_trafego (20, 30, 40)
    assert resultado[1] == 'baixo trafego'
    
def test_analisar_trafego_trafego_moderado():
    resultado = analisar_trafego (220, 350, 470)
    assert resultado[1] == 'trafego moderado'
    
def test_analisar_trafego_trafego_alto():
    resultado = analisar_trafego (650, 760, 900)
    assert resultado[1] == 'trafego alto'