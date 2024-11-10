
"""
Equipe
- Giordano Diniz Serafini
- Victor Gabriel Eidt Bragagnolo
"""

import multiprocessing as mp
import time
from multiprocessing.synchronize import Semaphore

RANGE_COUNT = 5
TIME_COUNT = 1

def process(name: str, n: int, t: int,
            actual_semaphore: Semaphore, next_semaphore: Semaphore) -> None:
    print(f'Processo {name} aguardando')
    actual_semaphore.acquire()
    print(f'Processo {name} iniciado')
    for i in range(1,n+1):
        print(f'{name} - {i}')
        time.sleep(t)
    print(f'Processo {name} finalizado')
    next_semaphore.release()

def main() -> None:
    range_count = int(input('Digite um valor inteiro para contagem: '))
    time_count = int(input('Digite um valor para o tempo de contagem: '))
    semaphore1 = mp.Semaphore(0)
    semaphore2 = mp.Semaphore(0)
    semaphore3 = mp.Semaphore(0)
    semaphore4 = mp.Semaphore(0)
    process1 = mp.Process(
        target=process,
        args=('Processo 1', range_count, time_count,
              semaphore1, semaphore2
        )
    )
    process2 = mp.Process(
        target=process,
        args=('Processo 2', range_count, time_count,
              semaphore2, semaphore3
        )
    )
    process3 = mp.Process(
        target=process,
        args=('Processo 3', range_count, time_count,
              semaphore3, semaphore4
        )
    )
    process4 = mp.Process(
        target=process,
        args=('Processo 4', range_count, time_count,
              semaphore4, semaphore1
        )
    )
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    time.sleep(TIME_COUNT)
    semaphore1.release()
    process1.join()
    process2.join()
    process3.join()
    process4.join()

if __name__ == '__main__':
    main()