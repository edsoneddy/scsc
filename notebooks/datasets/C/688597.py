import heapq

def main():
    monton_max = []
    recuento_entrada = 0

    while True:
        try:
            comando = input().strip()
            if comando == 'T':
                break

            cmd_partes = comando.split()
            if cmd_partes[0] == 'S':
                x = int(cmd_partes[1])
                heapq.heappush(monton_max, -x)
                recuento_entrada += 1
            elif cmd_partes[0] == 'A':
                if recuento_entrada == 0:
                    print("Error")
                else:
                    print(-monton_max[0])
            elif cmd_partes[0] == 'R':
                if recuento_entrada == 0:
                    print("Error")
                else:
                    heapq.heappop(monton_max)
                    recuento_entrada -= 1
            elif cmd_partes[0] == 'I':
                if recuento_entrada == 0:
                    print("Error")
                else:
                    incremento = int(cmd_partes[1])
                    max_elemento = -heapq.heappop(monton_max)
                    max_elemento += incremento
                    heapq.heappush(monton_max, -max_elemento)
            elif cmd_partes[0] == 'D':
                if recuento_entrada == 0:
                    print("Error")
                else:
                    decrement = int(cmd_partes[1])
                    max_elemento = -heapq.heappop(monton_max)
                    max_elemento -= decrement
                    heapq.heappush(monton_max, -max_elemento)
        except EOFError:
            break

if __name__ == "__main__":
    main()
