"""
Equipe
- Giordano Diniz Serafini
- Victor Gabriel Eidt Bragagnolo
"""

import multiprocessing as mp
import time

def process(name: str, n: int, t: float,
            start_semaphore: mp.Semaphore, end_semaphores: list = None) -> None:
    print(f'Processo {name} aguardando\n')
    start_semaphore.acquire()
    print(f'Processo {name} iniciado\n')
    for i in range(1, n + 1):
        print(f'{name} - {i}\n')
        time.sleep(t)
    print(f'Processo {name} finalizado\n')
    if end_semaphores:
        for sem in end_semaphores:
            sem.release()

def main() -> None:
    range_count = int(input('Digite um valor para contagem: '))
    time_count = float(input('Digite um valor para a contagem: '))
    semaphore_a = mp.Semaphore(1)
    semaphore_b = mp.Semaphore(0)
    semaphore_c = mp.Semaphore(0)
    semaphore_d = mp.Semaphore(0)
    process_a = mp.Process(
        target=process,
        args=('Processo A', range_count, time_count, semaphore_a, [semaphore_b, semaphore_c])
    )
    process_b = mp.Process(
        target=process,
        args=('Processo B', range_count, time_count, semaphore_b, [semaphore_d])
    )
    process_c = mp.Process(
        target=process,
        args=('Processo C', range_count, time_count, semaphore_c, [semaphore_d])
    )
    process_d = mp.Process(
        target=process,
        args=('Processo D', range_count, time_count, semaphore_d)
    )
    process_a.start()
    process_b.start()
    process_c.start()
    process_d.start()
    process_a.join()
    process_b.join()
    process_c.join()
    process_d.join()

if __name__ == '__main__':
    main()
