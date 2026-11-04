"""Operações matemáticas simples."""

from __future__ import annotations

from typing import Iterable


def somar(a: float, b: float) -> float:
    """Retorna a soma de a e b."""
    return a + b


def subtrair(a: float, b: float) -> float:
    """Retorna a diferença entre a e b."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Retorna o produto de a e b."""
    return a * b


def dividir(a: float, b: float) -> float:
    """Retorna a divisão de a por b. Lança ZeroDivisionError se b for zero."""
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b


def fatorial(n: int) -> int:
    """Retorna n! para n inteiro não negativo."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n deve ser um inteiro.")
    if n < 0:
        raise ValueError("n deve ser não negativo.")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def eh_primo(n: int) -> bool:
    """Indica se n é um número primo."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def fibonacci(n: int) -> list[int]:
    """Retorna os n primeiros termos da sequência de Fibonacci."""
    if n < 0:
        raise ValueError("n deve ser não negativo.")
    termos: list[int] = []
    a, b = 0, 1
    for _ in range(n):
        termos.append(a)
        a, b = b, a + b
    return termos


def media(valores: Iterable[float]) -> float:
    """Retorna a média aritmética dos valores. Lança ValueError se estiver vazio."""
    lista = list(valores)
    if not lista:
        raise ValueError("A lista de valores não pode ser vazia.")
    return sum(lista) / len(lista)
