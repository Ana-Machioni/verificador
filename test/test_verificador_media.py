import pytest
from escola import verificador_media

def test_verificar_aprovado():
    assert verificador_media(8) == "Aprovado"

def test_verificar_reprovado():
    assert verificador_media(3) == "Reprovado"

def test_verificar_recuperacao():
    assert verificador_media(6) == "Recuperação"