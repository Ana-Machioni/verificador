import pytest
from escola import verificador_media

def test_verificar_aprovado():
    assert verificador_media(8) == "Aprovado(a)"