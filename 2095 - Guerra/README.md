# Guerra
*Questão 2095 | Beecrowd*   
*[Link para o problema](https://www.beecrowd.com.br/judge/pt/problems/view/2095)*

### Descrição

Guerra, um evento digno apenas de aparecer na literatura, filmes ou talvez programação de concursos, veio a atingir o império Nogloniano, que está enfrentando o império vizinho de Quadradônia. Protocolos de guerra combinados por ambas as partes indicam que a guerra será travada em sucessivas batalhas, em cada uma das quais um soldado diferente de cada império vai enfrentar outro, de modo que cada soldado irá participar em exatamente uma batalha. O império que ganhar mais batalhas ganha a guerra. Cada império tem um exército formado por S soldados, e cada soldado tem uma certa habilidade de combate. Em cada batalha entre dois soldados, aquele com maior habilidade de combate ganha a batalha. Se ambos os soldados têm as mesmas habilidades de combate, a batalha é declarada como empate e tecnicamente nenhum lado é vitorioso. Os espiões de Noglônia tiveram que interceptar informações secretas relativas às habilidades de combate de cada soldado do exército de Quadradônia, por isso a rainha de Noglônia requer a sua assistência, a fim de calcular o número máximo de batalhas que podem ganhar durante a guerra se os seus soldados forem enviados na ordem apropriada.

### Entrada

A primeira linha contém um número inteiro S que representa o número de soldados em cada exército (1 ≤ S ≤ 10^5). A segunda linha contém S números inteiros, onde Qi representa as habilidades de combate dos diferentes soldados do exército de Quadradônia, na ordem em que as batalhas irão acontecer (1 ≤ Qi ≤ 10^9 para i = 1, ..., S). A terceira linha contém S números inteiros, onde Ni representando as habilidades de combate dos diferentes soldados do exército de Noglônia, em uma ordem arbitrária (1 ≤ Ni ≤ 10^9 para i = 1, ..., S).

### Saída

Imprima uma linha contendo um único número inteiro que representa o número máximo de batalhas que Noglônia pode ganhar durante a guerra.

| **Exemplo de Entrada** | **Exemplo de Saída** |
|-----------|-----------|
|3<br>2 1 1000000000<br>1 1 2|1|

| **Exemplo de Entrada** | **Exemplo de Saída** |
|-----------|-----------|
|4<br>6 3 1 4<br>2 7 4 3|3|

### Resultado

![image](https://user-images.githubusercontent.com/63034102/212785555-6d5b52f8-c0b0-4712-8da4-a2f1557c9fb7.png)
