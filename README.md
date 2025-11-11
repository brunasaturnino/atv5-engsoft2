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

### O que o Workflow Faz

1. Faz checkout do código do repositório
2. Configura a versão específica do Python
3. Instala as dependências do projeto
4. Executa todos os testes com pytest
5. Gera relatório de cobertura de código

## 📦 Como Usar Este Projeto

### 1. Criar Repositório no GitHub

```bash
# Inicializar repositório local
git init
git add .
git commit -m "Initial commit: Calculator with CI/CD"

# Conectar ao repositório remoto
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPO.git
git branch -M main
git push -u origin main
```

### 2. Verificar Execução dos Testes

Após fazer push para o GitHub:

1. Vá até a aba **Actions** no seu repositório
2. Você verá o workflow "Testes CI/CD" em execução
3. Clique no workflow para ver os detalhes de cada combinação de OS/Python
4. Os testes serão executados automaticamente em todas as 9 combinações

### 3. Badge de Status (Opcional)

Adicione ao README para mostrar o status dos testes:

```markdown
![Tests](https://github.com/SEU_USUARIO/NOME_DO_REPO/actions/workflows/tests.yml/badge.svg)
```

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação
- **pytest**: Framework de testes
- **pytest-cov**: Plugin para cobertura de código
- **GitHub Actions**: Plataforma de CI/CD

## 📁 Estrutura do Projeto

```
github-actions-ci/
├── .github/
│   └── workflows/
│       └── tests.yml          # Configuração do GitHub Actions
├── calculator.py              # Módulo principal com funções
├── test_calculator.py         # Testes de unidade
├── requirements.txt           # Dependências do projeto
└── README.md                  # Este arquivo
```

## ✅ Requisitos Atendidos

- ✅ Repositório criado no GitHub
- ✅ Programa implementado em Python
- ✅ Pelo menos 5 testes de unidade (13 testes implementados)
- ✅ GitHub Actions executando testes automaticamente
- ✅ Testes em 3 sistemas operacionais (Ubuntu, MacOS, Windows)
- ✅ Testes em múltiplas versões da linguagem (Python 3.10, 3.11, 3.12)

## 📝 Exemplo de Uso do Programa

```python
from calculator import somar, multiplicar, fatorial

# Operações básicas
resultado = somar(10, 5)          # 15
produto = multiplicar(3, 4)       # 12

# Operações avançadas
fat = fatorial(5)                 # 120
```

## 🤝 Contribuindo

1. Faça fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

Os testes serão executados automaticamente no seu PR!

## 📄 Licença

Este projeto é livre para uso educacional.

## 👨‍💻 Autor

Criado como projeto de Engenharia de Software II - Demonstração de CI/CD com GitHub Actions.

