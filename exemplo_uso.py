"""
Exemplo de uso do módulo Calculator
Execute: python exemplo_uso.py
"""

from calculator import (
    somar, subtrair, multiplicar, dividir,
    potencia, raiz_quadrada, fatorial
)


def main():
    print("=" * 50)
    print("DEMONSTRAÇÃO DO MÓDULO CALCULATOR")
    print("=" * 50)
    
    # Operações básicas
    print("\nOPERACOES BASICAS:")
    print(f"10 + 5 = {somar(10, 5)}")
    print(f"10 - 5 = {subtrair(10, 5)}")
    print(f"10 x 5 = {multiplicar(10, 5)}")
    print(f"10 / 5 = {dividir(10, 5)}")
    
    # Operações avançadas
    print("\nOPERACOES AVANCADAS:")
    print(f"2^3 = {potencia(2, 3)}")
    print(f"raiz(16) = {raiz_quadrada(16)}")
    print(f"5! = {fatorial(5)}")
    
    # Tratamento de erros
    print("\nTRATAMENTO DE ERROS:")
    try:
        dividir(10, 0)
    except ValueError as e:
        print(f"Erro ao dividir por zero: {e}")
    
    try:
        raiz_quadrada(-4)
    except ValueError as e:
        print(f"Erro ao calcular raiz de negativo: {e}")
    
    try:
        fatorial(-5)
    except ValueError as e:
        print(f"Erro ao calcular fatorial: {e}")
    
    print("\n" + "=" * 50)
    print("Todos os exemplos executados com sucesso!")
    print("=" * 50)


if __name__ == "__main__":
    main()

