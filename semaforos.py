import threading
from time import sleep


class Pilha:
    def __init__(self, value=0):
        self._value = value
        self._value_lock = threading.Lock()

    def inc(self, value):
        with self._value_lock:
            self._value += value

    def dec(self, value):
        with self._value_lock:
            self._value -= value

    def getValue(self):
        with self._value_lock:
            return self._value


def th_produtor(valor):
    PILHA.inc(valor)
    sleep(valor) if valor != 0 else sleep(1)


def produtor(valor):
    return threading.Thread(target=th_produtor, args=(valor,))


def th_consumidor(valor):
    PILHA.dec(valor)
    sleep(valor) if valor != 0 else sleep(1)


def consumidor(valor):
    return threading.Thread(target=th_consumidor, args=(valor,))


if __name__ == '__main__':
    matricula = input('Digite o número da matricula \n')

    PILHA = Pilha()
    vetor = [int(m) for m in matricula]
    threads = []

    for i, m in enumerate(vetor):
        if i % 2 == 0:
            t = produtor(m)
        else:
            t = consumidor(m)
        threads.append(t)

    for t in threads:
        t.start()

    sleep(10)

    for t in threads:
        t.join()

    print(f'O valor é: {PILHA.getValue()}')

# matricula 201910004319
