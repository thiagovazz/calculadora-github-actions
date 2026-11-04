"""Interface de linha de comando: python -m calculadora <operacao> <args...>"""

import sys

from . import operacoes

USO = (
    "Uso: python -m calculadora <operacao> <args...>\n"
    "Operações: somar a b | subtrair a b | multiplicar a b | dividir a b |\n"
    "           fatorial n | eh_primo n | fibonacci n | media v1 v2 ..."
)


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if not args:
        print(USO)
        return 1
    op, *params = args
    try:
        if op in {"somar", "subtrair", "multiplicar", "dividir"}:
            a, b = map(float, params)
            print(getattr(operacoes, op)(a, b))
        elif op in {"fatorial", "eh_primo", "fibonacci"}:
            (n,) = map(int, params)
            print(getattr(operacoes, op)(n))
        elif op == "media":
            print(operacoes.media(map(float, params)))
        else:
            print(USO)
            return 1
    except (ValueError, TypeError, ZeroDivisionError) as erro:
        print(f"Erro: {erro}")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
