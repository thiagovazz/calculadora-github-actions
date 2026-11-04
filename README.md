# Calculadora — GitHub Actions

![CI](https://github.com/thiagovazz/calculadora-github-actions/actions/workflows/ci.yml/badge.svg)

Atividade de **GitHub Actions**: um pequeno programa em Python com testes de unidade executados automaticamente a cada commit em **3 sistemas operacionais** e **3 versões do Python**.

## O programa

Pacote `calculadora` (em `src/calculadora/`) com as operações:

| Função | Descrição |
|---|---|
| `somar`, `subtrair`, `multiplicar` | Operações aritméticas básicas |
| `dividir` | Divisão (lança `ZeroDivisionError` se o divisor for 0) |
| `fatorial(n)` | n! para inteiros não negativos |
| `eh_primo(n)` | Verifica se n é primo |
| `fibonacci(n)` | Lista com os n primeiros termos de Fibonacci |
| `media(valores)` | Média aritmética |

Também pode ser usado pela linha de comando:

```bash
python -m calculadora fatorial 5      # 120
python -m calculadora dividir 10 4    # 2.5
python -m calculadora media 1 2 3 4   # 2.5
```

## Testes

Os testes ficam em `tests/test_operacoes.py` (15 funções de teste, 30 casos com parametrização), usando **pytest**.

```bash
python -m pip install ".[test]"
python -m pytest
```

## Integração contínua (GitHub Actions)

O workflow `.github/workflows/ci.yml` roda a cada `push` e `pull_request` e usa uma matriz:

- **Sistemas operacionais:** `ubuntu-latest`, `macos-latest`, `windows-latest`
- **Versões do Python:** `3.11`, `3.12`, `3.13`

Total: **9 jobs** por commit. Cada job faz checkout, configura o Python, faz o build/instalação do pacote, executa os testes e roda o programa.
