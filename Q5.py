Algoritimo 01:

sum = 0;
2 for ( int i =0; i < n ; i ++) {
3 for ( int j =1; j <= n ; j ++) {
4 sum ++;
5 }
6 }

Respostas:
No primeiro algoritmo ele possui dois laços aninhados. o primeiro laço executa  n iterações, e o segundo laço também executa n iterações. Portanto, a complexidade de tempo é o(n ao quadrado).
                                                                                                                                                                                
                                                                                                                                                                                
Algoritimo 02:
                                                                                                                                                                                
sum = 0;
2 for ( int i =1; i < n ; i *=2) {
3 for ( int j =1; j <= n ; j ++) {
4 sum ++;
5 }
6 }


Respostas:

Já nesse segundo algoritmo, o primeiro laço executa O( Log n)  iterações, pois i dobra a cada iteração. O segundo laço executa n iterações. Portanto, a complexidade de tempo é O(n log de n).


Algoritimo 03:

sum = 0;
2 for ( int i =0; i < n ; i *=2) {
3 for ( int j =1; j <= n ; j += i ) {
4 sum ++;
5 }
6 }

Respostas:
No terceiro algoritmo, o primeiro laço nunca incrementa i, então ele permanece 0 para sempre. Como resultado, o segundo laço nunca avança, e o programa entra em um loop infinito. Portanto, este algoritmo 
não termina e não é possível realizar uma análise de complexidade de tempo significativa. Se o incremento de 
i for alterado para 1 i+1, o algoritmo será semelhante ao segundo algoritmo, e a complexidade seria O(n log n).
