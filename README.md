# Aluna: Bruna Saturnino de Carvalho

# Projeto de CI/CD com GitHub Actions

Este projeto demonstra a implementação de testes automatizados com CI/CD usando GitHub Actions.

## 📋 Descrição

Programa Python com módulo de calculadora que inclui operações matemáticas básicas e avançadas, com testes de unidade automatizados executados em múltiplos sistemas operacionais e versões do Python.

## 🚀 Funcionalidades

O módulo `calculator.py` implementa as seguintes operações:

- **Operações Básicas:**
  - Soma
  - Subtração
  - Multiplicação
  - Divisão (com tratamento de divisão por zero)

- **Operações Avançadas:**
  - Potenciação
  - Raiz quadrada (com validação de números negativos)
  - Fatorial (com validação de entrada)

## 🧪 Testes

O projeto contém **13 testes de unidade** organizados em três classes:

1. **TestOperacoesBasicas**: 5 testes para operações básicas
2. **TestOperacoesAvancadas**: 5 testes para operações avançadas
3. **TestCasosMistos**: 3 testes para casos especiais e edge cases

### Executar Testes Localmente

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar todos os testes
pytest test_calculator.py -v

# Executar testes com cobertura
pytest test_calculator.py --cov=calculator --cov-report=term-missing
```

## 🔄 CI/CD com GitHub Actions

### Configuração

O workflow está configurado em `.github/workflows/tests.yml` e executa automaticamente a cada commit ou pull request.

### Matriz de Testes

Os testes são executados em uma matriz que combina:

**Sistemas Operacionais:**
- ✅ Ubuntu (latest)
- ✅ MacOS (latest)
- ✅ Windows (latest)

**Versões do Python:**
- ✅ Python 3.10
- ✅ Python 3.11
- ✅ Python 3.12

**Total: 9 combinações diferentes** (3 OS × 3 versões)



