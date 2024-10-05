# tests/test_app.py
from app import calcular_imc, classificar_imc
import pytest

def test_calcular_imc():
    assert calcular_imc(70, 1.75) == pytest.approx(22.86, rel=1e-2)  # Compara com tolerância

def test_classificar_imc():
    assert classificar_imc(22.86) == "Peso normal"
    assert classificar_imc(17.0) == "Abaixo do peso"
    assert classificar_imc(26.0) == "Sobrepeso"
    assert classificar_imc(30.0) == "Obesidade"
