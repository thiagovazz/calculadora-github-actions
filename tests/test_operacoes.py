import pytest

from calculadora import (
    dividir,
    eh_primo,
    fatorial,
    fibonacci,
    media,
    multiplicar,
    somar,
    subtrair,
)
from calculadora.__main__ import main


def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0


def test_subtrair():
    assert subtrair(10, 4) == 6
    assert subtrair(0, 5) == -5


def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(-2, 5) == -10


def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(1, 4) == pytest.approx(0.25)


def test_dividir_por_zero_lanca_erro():
    with pytest.raises(ZeroDivisionError):
        dividir(1, 0)


@pytest.mark.parametrize("n, esperado", [(0, 1), (1, 1), (5, 120), (10, 3628800)])
def test_fatorial(n, esperado):
    assert fatorial(n) == esperado


def test_fatorial_negativo_lanca_erro():
    with pytest.raises(ValueError):
        fatorial(-1)


def test_fatorial_tipo_invalido_lanca_erro():
    with pytest.raises(TypeError):
        fatorial(2.5)


@pytest.mark.parametrize("n", [2, 3, 5, 7, 13, 97, 7919])
def test_eh_primo_verdadeiro(n):
    assert eh_primo(n)


@pytest.mark.parametrize("n", [-7, 0, 1, 4, 9, 15, 100])
def test_eh_primo_falso(n):
    assert not eh_primo(n)


def test_fibonacci():
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_media():
    assert media([1, 2, 3, 4]) == pytest.approx(2.5)


def test_media_vazia_lanca_erro():
    with pytest.raises(ValueError):
        media([])


def test_cli_somar(capsys):
    assert main(["somar", "2", "3"]) == 0
    assert capsys.readouterr().out.strip() == "5.0"


def test_cli_erro_divisao_por_zero(capsys):
    assert main(["dividir", "1", "0"]) == 2
    assert "Erro" in capsys.readouterr().out
