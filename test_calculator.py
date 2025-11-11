"""
Testes de Unidade para o módulo Calculator
"""

import pytest
from calculator import (
    somar, subtrair, multiplicar, dividir, 
    potencia, raiz_quadrada, fatorial
)


class TestOperacoesBasicas:
    """Testes para operações matemáticas básicas"""
    
    def test_somar_positivos(self):
        """Teste 1: Soma de números positivos"""
        assert somar(2, 3) == 5
        assert somar(10, 20) == 30
        assert somar(0, 5) == 5
    
    def test_subtrair(self):
        """Teste 2: Subtração de números"""
        assert subtrair(10, 5) == 5
        assert subtrair(5, 10) == -5
        assert subtrair(0, 0) == 0
        assert subtrair(100, 50) == 50
    
    def test_multiplicar(self):
        """Teste 3: Multiplicação de números"""
        assert multiplicar(3, 4) == 12
        assert multiplicar(-2, 5) == -10
        assert multiplicar(0, 100) == 0
        assert multiplicar(-3, -3) == 9
    
    def test_dividir_normal(self):
        """Teste 4: Divisão de números válidos"""
        assert dividir(10, 2) == 5
        assert dividir(9, 3) == 3
        assert dividir(7, 2) == 3.5
        assert dividir(-10, 2) == -5
    
    def test_dividir_por_zero(self):
        """Teste 5: Divisão por zero deve lançar exceção"""
        with pytest.raises(ValueError, match="Não é possível dividir por zero"):
            dividir(10, 0)


class TestOperacoesAvancadas:
    """Testes para operações matemáticas avançadas"""
    
    def test_potencia(self):
        """Teste 6: Potenciação"""
        assert potencia(2, 3) == 8
        assert potencia(5, 2) == 25
        assert potencia(10, 0) == 1
        assert potencia(2, -1) == 0.5
    
    def test_raiz_quadrada_positivos(self):
        """Teste 7: Raiz quadrada de números positivos"""
        assert raiz_quadrada(4) == 2
        assert raiz_quadrada(9) == 3
        assert raiz_quadrada(16) == 4
        assert raiz_quadrada(0) == 0
        assert abs(raiz_quadrada(2) - 1.414213) < 0.00001
    
    def test_raiz_quadrada_negativo(self):
        """Teste 8: Raiz quadrada de número negativo deve lançar exceção"""
        with pytest.raises(ValueError, match="Não é possível calcular raiz quadrada de número negativo"):
            raiz_quadrada(-4)
    
    def test_fatorial(self):
        """Teste 9: Fatorial de números inteiros"""
        assert fatorial(0) == 1
        assert fatorial(1) == 1
        assert fatorial(5) == 120
        assert fatorial(6) == 720
        assert fatorial(3) == 6
    
    def test_fatorial_invalido(self):
        """Teste 10: Fatorial de número inválido deve lançar exceção"""
        with pytest.raises(ValueError, match="O fatorial só é definido para inteiros não-negativos"):
            fatorial(-5)
        
        with pytest.raises(ValueError):
            fatorial(3.5)


class TestCasosMistos:
    """Testes com casos mistos e edge cases"""
    
    def test_operacoes_com_zero(self):
        """Teste 11: Operações com zero"""
        assert somar(0, 0) == 0
        assert multiplicar(5, 0) == 0
        assert subtrair(5, 5) == 0
    
    def test_operacoes_com_negativos(self):
        """Teste 12: Operações com números negativos"""
        assert somar(-5, -3) == -8
        assert multiplicar(-2, -4) == 8
        assert subtrair(-10, -5) == -5
    
    def test_operacoes_com_decimais(self):
        """Teste 13: Operações com números decimais"""
        assert abs(somar(1.5, 2.3) - 3.8) < 0.0001
        assert abs(multiplicar(2.5, 4) - 10.0) < 0.0001
        assert abs(dividir(5.5, 2) - 2.75) < 0.0001

