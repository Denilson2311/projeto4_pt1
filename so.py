import os


def identificar_so() -> str:
    if os.name == "nt":
        return "Windows"

    elif os.name == "posix":
        return "Linux/Unix"

    else:
        return "Outro sistema"