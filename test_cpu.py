from cpu import avaliar_cpu

def test_avaliar_cpu_normal():
    assert avaliar_cpu(20) == 'normal'
    
def test_avaliar_cpu_alta():
    assert avaliar_cpu(50) == 'alta'
    
def test_avaliar_cpu_sobrecarga():
    assert avaliar_cpu(100) == 'sobrecarga'
    