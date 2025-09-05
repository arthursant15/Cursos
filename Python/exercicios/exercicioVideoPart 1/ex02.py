print("=== CALCULADORA DE MEDIA ===")

def media():
    n = 0
    nf = 0
    media = 0
    for i in range(3):
        i +=1
        print(i)
        n = int(input("digite algum numero: "))
        nf += n
    media = nf / i
    print(media)
    
media()