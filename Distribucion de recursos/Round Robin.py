
from collections import deque

class Proceso:
    nro : int
    bursts : []
    endisco = 0
    def __init__(self,nro,bursts):
        self.nro = nro
        self.bursts = bursts

class Burst:
    tipo: str
    tiempo: int
    def __init__(self,tipo,tiempo):
        self.tipo = tipo
        self.tiempo = tiempo



def main(procesos,q,ti):
    cola =  deque()
    reloj = 0
    while len(procesos) != 0:
        cola.append(procesos.pop())


    while len(cola) > 0:
        proceso = cola.popleft()
        if proceso.endisco == 0:
            burst = proceso.bursts.pop()
            if burst.tiempo > q:
                burst.tiempo -= q
                proceso.bursts.insert(0,burst)
                cola.append(proceso)
                reloj += q
            elif burst.tiempo <= q:
                reloj += burst.tiempo# ACA TENEMOS Q PONER EN 0 EL tiempo del proceso? lo saco a la mieda directamente
                if len(proceso.bursts) != 0:
                    burst = proceso.bursts.pop()
                    proceso.endisco = burst.tiempo + reloj
                if len(proceso.bursts) != 0:
                    cola.append(proceso)


        print(proceso.nro)




if __name__ == '__main__':
    burstsp1 = [Burst("cpu",40)] # ponele aca podes poner disco? se ej?
    proceso1 = Proceso(1,burstsp1)
    burstsp2 = [Burst("cpu",60)] # ponele aca podes poner disco? se ej?
    proceso2 = Proceso(2,burstsp2)
    q = 20
    ti = 10
    main([proceso1,proceso2],q,ti)