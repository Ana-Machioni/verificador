import pytest 
from escola import verificador_media


def test_string_como_entrada():
    with pytest.raises(TypeError, match="Tipo invalido, a entrada deve ser numerica"):
        verificador_media("OITO")
