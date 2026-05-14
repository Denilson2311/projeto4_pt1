def avaliar_datacenter(temp: float,cpu: float,mem: float,lat: float,disco: float) -> str:

    if (temp > 70 or cpu > 90 or mem > 90 or disco < 10):
        return "Servidor crítico"

    elif (lat > 100 or temp > 40):
        return "Servidor em alerta"

    else:
        return "Servidor estável"