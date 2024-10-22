def Varredura(L, inicio, fim):
  for i in range(inicio, fim-1): # eh fim-1 pois vai sempre comparar um elemento com o proximo
    if(L[i] > L[i+1]):
      Troca(L, i, i+1)

def Troca(L, i, j):
  aux = L[i]
  L[i] = L[j]
  L[j] = aux


def main():
  L = [8,10,27,42,20,5]
  N = len(L)
  
  for j in range(N, 1, -1):
      Varredura(L, 0, j)
  print(L)

if __name__ == "__main__":
    main()