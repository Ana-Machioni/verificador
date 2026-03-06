import pytest
from escola import verificador_media

def test_verificador_aprovado(): 
    assert verificador_media(8) == "Aprovado"

def test_verificador_reprovado():
    assert verificador_media(4) == "Reprovado"

def test_verificar_recuperacao():
    assert verificador_media(6) == "Recuperação"