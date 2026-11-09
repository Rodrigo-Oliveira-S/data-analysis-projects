## Video Game Sales - Análise de Negócio

Fiz uma análise para entender quais são os gêneros e jogos mais vendidos, e também qual região mais consome esse produto.

## Ferramentas:

- PostgreSQL
- Excel
- Power Query

## O que analisei

1. Top 10 jogos mais vendidos no mundo
2. Top 10 Jogos com as melhores notas
3. Quantos jogos não possuem notas
4. Regiões que mais vendem
5. Empresa que mais vendeu
6. Qual gênero lidera em cada região
7. Jogo fora do Top 10 notas, mas no Top 10 vendas

## Principais descobertas

1. Top 10 jogos mais vendidos no mundo

   - Grand Theft Auto V lidera com 48.43 milhões de cópias.
   - Call of Duty domina o ranking com 7 dos 10 jogos mais vendidos.
   - Rockstar Games tem apenas 2 títulos no top 10, mas ambos com vendas massivas.

2. Top 10 jogos com as melhores notas

   - Grand Theft Auto IV e Red Dead Redemption: Undead Nightmare empatam com nota 10.0.
   - Rockstar Games concentra metade dos jogos com as maiores notas do Metacritic.
   - Nota alta não garante vendas: Undead Nightmare (nota 10) vendeu 2.29M, enquanto GTA IV (nota 10) vendeu 21.66M.

3. Quantos jogos não possuem notas

   - O dataset contém 64.016 registros, mas apenas 10,4% (6.678) possuem nota do Metacritic.
   - As análises que envolvem nota consideram apenas esse subconjunto.

4. Regiões que mais vendem

   - América do Norte lidera com 3.345 milhões de cópias, quase o dobro da Europa/África (1.916M).
   - Japão (687M) e Resto do Mundo (651M) têm volumes bem menores.

5. Empresa que mais vendeu

   - Activision lidera com 722.77 milhões de cópias, impulsionada pelo catálogo extenso (685 títulos diferentes).
   - Rockstar Games ficou em 7º lugar (239.67M) porque tem apenas 70 títulos — mas seus jogos vendem mais por unidade.

6. Qual gênero lidera em cada região

   - América do Norte e Resto do Mundo: Sports lidera.
   - Japão: Role-Playing é o gênero dominante.
   - Europa/África: Action vence por margem apertada sobre Sports.

7. Jogo fora do Top 10 notas, mas no Top 10 vendas

   - Sim. Call of Duty: Ghosts e Black Ops 3 têm notas abaixo de 8.5, mas estão entre os 5 mais vendidos.
   - Undertale (nota 9.7) e The Walking Dead (nota 9.7) estão no top 10 notas, mas venderam menos de 1 milhão de cópias cada.
   - Nota alta não é garantia de sucesso comercial.

## Estrutura

- `dados/` — CSVs extraídos das consultas SQL
- `queries/` — Consultas SQL usadas na análise
- `dashboard/` — Planilha com capa, dados brutos, análises de apoio e dashboard final
