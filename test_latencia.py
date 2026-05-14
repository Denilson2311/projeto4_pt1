from latencia import classificar_latencia

def test_classificar_latencia_excelente():
    assert classificar_latencia(5) == 'excelente'
    
def test_classificar_latencia_boa():
    assert classificar_latencia(20) == 'boa'
    
def test_classificar_latencia_regular():
    assert classificar_latencia(70) == 'regular'
    
def test_classificar_latencia_ruim():
    assert classificar_latencia(200) == 'ruim'