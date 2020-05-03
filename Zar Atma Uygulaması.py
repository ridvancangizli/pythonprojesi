import time
import random

print("-----------------------------")
print("Zar Uygulamamıza Hoşgeldiniz")
print("-----------------------------")


i= 1

while True:
    zar_1 = random.randint(1,3)
    zar_2 = random.randint(1,3)
    zar_3 = random.randint(1,3)
    
    if zar_1 == 3 and zar_2 == 3 and zar_3 == 3:
        time.sleep(2)
        print("Zarınız {} Denemede Bulundu ({},{},{})".format(i,zar_1,zar_2,zar_3))
        break
    
    print("Deneme {}: ({},{},{})".format(i,zar_1,zar_2,zar_3))
    i +=1
    time.sleep(0.5)
        
    




    




    
        

