# tests/test_app.py
from app import calcular_imc, classificar_imc
def test_calcular_imc():
    assert calcular_imc(70, 1.75) == 22.86 # IMC esperado para peso 70kg e altura 1.75m
def test_classificar_imc():
    assert classificar_imc(22.86) == 'Peso normal'
    assert classificar_imc(17.0) == 'Abaixo do peso'
    assert classificar_imc(26.0) == 'Sobrepeso'
    assert classificar_imc(30.0) == 'Obesidade'