from memoria import avaliar_memoria
    
def test_avaliar_memoria_confortavel():
    assert avaliar_memoria (30) =='Confortavel'
    
def test_avaliar_memoria_monitorar():
    assert avaliar_memoria (70) =='Monitorar'
    
def test_avaliar_memoria_critica():
    assert avaliar_memoria (100) =='Critica'