import sys
sys.path.append('src/')
from identifier import identifier

class TestesIdentifier:

    def testeId1(self):
        assert identifier("") == "Invalido"
    
    def testeId2(self):
        assert identifier("b") == "Valido"
    
    def testeId3(self):
        assert identifier("b45862") == "Valido"

    def testeId4(self):
        assert identifier("b45862317") == "Invalido"

    def testeId5(self):
        assert identifier("2") == "Invalido"

    def testeId6(self):
        assert identifier("Z$82") == "Invalido"