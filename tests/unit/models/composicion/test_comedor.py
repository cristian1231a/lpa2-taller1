import pytest
from src.models.composicion.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla

class TestComedor:
    @pytest.fixture
    def comedor_basico(self):
        mesa = Mesa("Mesa Comedor", "Roble", "Beige", 216)
        sillas = [Silla("Silla Comedor", "Roble", "Roble", 50) for _ in range(6)]
        return Comedor("Comedor Familiar", mesa, sillas)
    
    def test_composicion_correcta(self, comedor_basico):
        assert comedor_basico.mesa is not None
        assert len(comedor_basico.sillas) == 6
        assert isinstance(comedor_basico.mesa, Mesa)
        assert all(isinstance(silla, Silla) for silla in comedor_basico.sillas)
    
    def test_calcular_precio_total(self, comedor_basico):
        print(comedor_basico)
        precio_total = comedor_basico.calcular_precio_total()
        precio_esperado = 200 + (6 * 50)  # Mesa + 6 sillas
        assert precio_total == precio_esperado