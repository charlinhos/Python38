import threading
import time

contador = 0
max_for = 10000000
paralelo = True

lock = threading.Lock()

def somar():
    global contador
    for i in range(0, max_for):
        lock.acquire()
        contador+=1
        lock.release()

start_time = time.time()
if paralelo:
    t1 = threading.Thread(target=somar)
    t2 = threading.Thread(target=somar)

    t1.start()
    t2.start() 

    t1.join()
    t2.join()

else:   
    somar()
    somar()
end_time = time.time() - start_time

print(end_time)
print(contador)
# assert contador == max_for * 2


# Tempo Serial
# 3.9357450008392334, 3.73392653465271, 3.9095046520233154

# Tempo Paralelo
# 3.685208559036255, 3.930535078048706, 3.9139645099639893
