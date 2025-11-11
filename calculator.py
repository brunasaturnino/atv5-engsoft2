"""
Módulo de Calculadora - Programa simples para demonstração de CI/CD
Este módulo contém funções básicas de operações matemáticas.
"""


def somar(a, b):
    """
    Retorna a soma de dois números.
    
    Args:
        a: Primeiro número
        b: Segundo número
    
    Returns:
        A soma de a e b
    """
    return a + b


def subtrair(a, b):
    """
    Retorna a subtração de dois números.
    
    Args:
        a: Primeiro número
        b: Segundo número
    
    Returns:
        A subtração de b de a
    """
    return a - b


def multiplicar(a, b):
    """
    Retorna a multiplicação de dois números.
    
    Args:
        a: Primeiro número
        b: Segundo número
    
    Returns:
        O produto de a e b
    """
    return a * b


def dividir(a, b):
    """
    Retorna a divisão de dois números.
    
    Args:
        a: Numerador
        b: Denominador
    
    Returns:
        O resultado da divisão de a por b
    
    Raises:
        ValueError: Se b for zero
    """
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b


def potencia(base, expoente):
    """
    Retorna a potência de um número.
    
    Args:
        base: Número base
        expoente: Expoente
    
    Returns:
        base elevado ao expoente
    """
    return base ** expoente


def raiz_quadrada(numero):
    """
    Retorna a raiz quadrada de um número.
    
    Args:
        numero: Número para calcular a raiz
    
    Returns:
        A raiz quadrada do número
    
    Raises:
        ValueError: Se o número for negativo
    """
    if numero < 0:
        raise ValueError("Não é possível calcular raiz quadrada de número negativo")
    return numero ** 0.5


def fatorial(n):
    """
    Retorna o fatorial de um número.
    
    Args:
        n: Número inteiro não-negativo
    
    Returns:
        O fatorial de n
    
    Raises:
        ValueError: Se n for negativo ou não inteiro
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("O fatorial só é definido para inteiros não-negativos")
    
    if n == 0 or n == 1:
        return 1
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

