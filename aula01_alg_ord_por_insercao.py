def Insercao(L, k):
  i = k
  while(i > 0 and L[i] < L[i-1]):
    Troca(L, i, i-1)
    i = i - 1

def Troca(L, i, j):
  aux = L[i]
  L[i] = L[j]
  L[j] = aux

def main():
  L = [8,10,27,42,20,5]
  N = len(L)
  for j in range(1, N):
    Insercao(L, j)
  
  print(L)
  
if __name__ == "__main__":
    main()