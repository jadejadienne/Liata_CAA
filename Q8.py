Codico 01:

def bubble_sort2 (A , n ) :
troca = True
while troca :
troca = False
for i in range ( n - 1) :
if A [ i ] > A [ i + 1]:
aux = A [ i ]
A [ i ] = A [ i + 1]
A [ i + 1] = aux
troca = True

Resposta:

Pior caso: O pior caso ocorre quando o array está reversamente ordenado. sendo que a complexidade é O(n^2)
devido aos loops aninhados.

Melhor caso: O melhor caso ocorre quando o array já está ordenado, resultando em uma complexidade de O(n), 
pois o algoritmo pode detectar que nenhum swap é necessário na primeira passagem.

Caso médio: No caso médio, a complexidade também é O(n^2).

Codico 02:

def AlgumaCoisa ( n ) :
 x = 0
 for i in range (1 , n ):
 for j in range ( i + 1 , n + 1) :
 for k in range (1 , j + 1) :
 x = x + 1

Resposta:

Pior caso: A complexidade no pior caso é O(n^3), pois há três loops aninhados.

Melhor caso: Não há um melhor caso distinto, pois todos os loops sempre serão executados.

Caso médio: No caso médio, a complexidade é O(n^3).

Codico 03:

def AlgumaCoisa2 ( n ) :
 x = 0
 for i in range (1 , n + 1) :
 for j in range ( i + 1 , n ) :
 for k in range (1 , j + 1) :
 x = x + 1
  
Resposta:

Pior caso: A complexidade no pior caso é O(n^3), semelhante à função AlgumaCoisa.

Melhor caso: Não há um melhor caso distinto.

Caso médio: A complexidade no caso médio é O(n^3).
