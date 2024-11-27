import threading
import time
import random

# Função de contagem das threads
def contar(thread_id, resultado, lock, posicao):
    for i in range(1, 21):
        
        # Thread dorme 0.25 seg padrão
        sleep = 0.25

        # Se a contagem finalizou, impede as outras threads de 
        # alterar o array de posição e adiciona o id da sua thread
        if i == 20:
            with lock:
                posicao.append(thread_id)

        # Imprime a contagem das Threads e seu ID
        print(f"Thread {thread_id} - Contagem: {i}")

        # Adiciona uma chance de 0.35 da Thread dormir 0.4 seg a mais
        if random.random() < 0.35:
            sleep += 0.4
        
        # Armazena a contagem de cada Thread no dicionário de resultado
        resultado[thread_id].append(i)

        # Aguarda o tempo de sleep antes de continuar
        time.sleep(sleep)

# Número de Threads que serão criadas 
num_threads = 8

# Lista relacionadas as Threads
threads = []
# Dicionário para armazenar a contagem de cada thread
resultado = {i: [] for i in range(1, num_threads + 1)}
# Array de posições 
posicao = []
# Variável que "trava" o uso das outras Threads
lock = threading.Lock()

# Mostra onde as Threads vão atuar e os argumentos da função contar
for i in range(num_threads):
    thread = threading.Thread(target=contar, args=(i + 1, resultado, lock, posicao))
    threads.append(thread)
    thread.start()

# Espera todas as threads terminarem
for thread in threads:
    thread.join()

print("\nOrdem de finalização das threads:")
for thread_id in posicao:
    print(f"Thread {thread_id}")
