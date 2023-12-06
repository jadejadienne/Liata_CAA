 # Primeira

 def Pesquisa1 (A , n ) :
 if n > 1:
 InspecioneNElementos = n * n * n # custo n^3
 Pesquisa1 (A , n // 3)

Resposta:

A função Pesquisa1 realiza uma chamada recursiva com n // 3. Portanto, a complexidade pode ser expressa como 
T(n)=T (3 n)+n 3. Pela análise mestra, a complexidade é O(N 3) pois a parte recursiva contribui menos do que 
a parte não-recursiva.

# Segunda

 def Pesquisa2 (A , n ) :
if n <= 1:
 return
 else :
 # obtenha o maior elemento entre os elementos
 # de alguma forma isso permite descartar 2/5 dos elementos e fazer
uma chamada recursiva no resto
 Pesquisa2 (A , 3 * n // 5)

Resposta:

A função Pesquisa2 realiza uma chamada recursiva com 
3/5 n. Portanto, a complexidade é T(n)= T(3/5 N) + 1. Pela análise mestra, a complexidade é 
O(logn), pois a parte recursiva diminui o tamanho do problema rapidamente.


# Terceira

 def Pesquisa3 (A , n ) :
 if n <= 1:
 return
 else :
 # ordena os elementos
# de alguma forma isso permite descartar 1/3 dos elementos e fazer
uma chamada recursiva no resto
 Pesquisa3 (A , 2 * n // 3)

Resposta:

A função Pesquisa3 realiza uma chamada recursiva com 2/3 n. Portanto, a complexidade é 
T(n)=T (2/3 n) +1.  Pela análise mestra, a complexidade é O(logn), pois a parte recursiva também diminui o tamanho
do problema rapidamente.



# Magica !!
 class Item :
 def __init__ ( self , Chave ) :
 self . Chave = Chave

 def Enigma2 (A , m , n , i , j ) :
 x = A [( i + j ) // 2]
 while True :
 while x . Chave > A [ i ]. Chave :


Resposta:

As funções Enigma1 e Enigma2 estão relacionadas ao algoritmo Quicksort. A complexidade média do Quicksort é 
O(nlogn) e no pior caso é O(n 2). Essas funções não alteram essas complexidades, pois são chamadas recursivas do Quicksort.

  
