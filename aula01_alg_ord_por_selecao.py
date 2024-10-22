def posMaior(L, inicio, fim):
  M = L[inicio]
  posM = inicio
  for i in range(inicio + 1, fim):
    if(L[i] > M):
      M = L[i]
      posM = i
  return posM

def Troca(L, i, j):
  aux = L[i]
  L[i] = L[j]
  L[j] = aux

# k = posMaior(L, 1, N) --> encontra o maior da lista toda
# L = Troca(L, k, N) --> coloca o maior no fim da lista

# k = posMaior(L, 1, N-1) --> encontra o 2º maior indo de 1 até N-1, pois em N ja há o maior
# L = Troca(L, k, N-1) --> coloca o 2º maior na penúltima pos da lista

# ... e assim por diante, para isso, colocamos num loop


def main():
  L = [8,10,27,42,20,5]
  N = len(L)
  for j in range(N, 0, -1): #vai do N até o elemento de indice 1
      k = posMaior(L, 0, j) 
      Troca(L, k, j-1) #j-1 pq quando o j for igual a N, nao existirá elem na pos L[N]
  
  print(L)

if __name__ == "__main__":
    main()