# 🤖 Robby -- O Robo Cata Lixo
 Projeto desenvolvido para ajudar um robo chamado robby a limpar seu planeta. 
 É utilizado meta-heurística Algoritmo Genético para encontrar a melhor solução

## 📄RELATÓRIO
## 📄Portfólio - Ed. 3 - Metaheurística - Robô

---

                                                       CENTRO UNIVERSITÁRIO

                                                     GOVERNADOR OZANAM COELHO

                                                       CIÊNCIA DA COMPUTAÇÃO


                                                                                 Robert Ferreira
                                                                       Autores : 
                                                                                 Taylor Ambrósio                                    


                                                               Ubá
                                                      Minas Gerais – Brasil
                                                            Junho / 2022

---

# ***Avaliação:***

- [x]  (1) Apresentação do código com os resultados alcançados.
- [x]  (2) Entrega do relatório constando passo a passo da configuração do Algoritmo Genético implementado.
- [x]  (3) No relatório deverão ser especificados os resultados alcançados, como foram desenvolvidos os testes até encontrar a melhor estratégia.
- [x]  (4) Apresente também o a configuração da máquina utilizada, linguagem de programação escolhida e o sistema operacional utilizado para rodar os testes.
- [x]  (5) Aponte situações que levaram ao resultado.
- [x]  (6) Conclusão.
- [x]  (7) Referência.

---

 # ***Relatório Passo a Passo Configuração Algoritmo Genético***

- Para o inicio do desenvolvimento do algoritmo, primeiramente separamos em partes todos os dados e indicações que o nosso “cliente” solicitou para o projeto como.: 

  - O tamanho do local que Robby se movimenta, os objetos presentes no local, movimentos que ele pode fazer, regras do jogo, passos e ações.

  - Foi montado então inicialmente uma matriz com a representação numérica do mundo de Robby, com os locais e designados pelo texto do cliente.

- Utilizamos inicialmente um programa e conteúdo para entender melhor o funcionamento do Robby -> **[Demonstração tutorial de redes neurais e algoritmos genéticos (muni.cz)](https://is.muni.cz/www/kabath/genetic_algorithms.html)**

- Também buscamos ideias e conhecimentos sobre algoritmos geneticos em outras fontes como por exemplo: 

- [Implementação de Algoritmo Genético - Problema da mochila - Python *YOUTUBE*](https://youtu.be/fC4mDO3RGQ8)   

- [Algoritmos Genéticos - Seleção *YOUTUBE*](https://youtu.be/dFboBO_oGIU)   

---
# ⚙️ Especificações :

A Linguagem de programação escolhida pela equipe para desenvolver o projeto foi “PYTHON” por ser uma linguagem de alto nível, com varias extensões com uma IA e um enquadramento de testes que facilitaram o desenvolvimento do software e o sistema operacional “Windows 11 64 bits”.

### 🖥️ Computador Teste Robert 

- Processador: Ryzen 5 5600x
- Placa de video: GTX: 1660
- Placa Mãe: Aours B550m elite
- Memoria Ram: 2x8 DDR4 36000MHz XPG D60G
- Versão Sistema Operacional: Windows 11 21h2
- Linguagem de programação: Python 3.10.4 - 32 Bits

### 💻 Computador Teste Taylor


- Processador: Intel(R) Core(TM) i5-10210U
- Placa de video: MX 250
- Placa Mãe: Doc_WC
- Memoria Ram: 1x8 DDR4 36000MHz XPG D60G
- Versão Sistema Operacional: Windows 10 (Ultima Att) 
- Linguagem de programação: Python 3.10.4 - 32 Bits

---

# ***Resultados & Conclusão*** 

## Abaixo apresentamos como foi feita a Função de evolução da população : 


![image](https://user-images.githubusercontent.com/88808709/173194657-ed771b7e-580e-456c-ab2a-1f37507d1975.png)


## Abaixo apresentamos como foi feita a Função de seleção para a roleta: 

![image](https://user-images.githubusercontent.com/88808709/173194745-f0248c1c-7bce-44fd-9ae5-2e2a32f11495.jpeg)

## Abaixo apresentamos como foi feita a Função do método da roleta: 

![image](https://user-images.githubusercontent.com/88808709/173194791-636556fb-4083-47b6-b1ef-194fb04e427e.jpeg)

## Abaixo apresentamos como foi feita a Função de mutação:

![image](https://user-images.githubusercontent.com/88808709/173194815-2f2cea2f-37af-403b-968d-bc736e007c51.jpeg)

---

## A seguir temos um exemplo de resultados e as respectivas configurações: 

- Tamanho da população: 20

- Numero de gerações: 20

- Taxa de mutação: 0.13

- Numero de ações individuais: 200


![image](https://user-images.githubusercontent.com/88808709/173194867-1e926287-fa75-444a-b44e-211321be1716.png)

Print do Resultado acima !

---
## A seguir temos um exemplo de resultados e as respectivas configurações:  

- Tamanho da população: 10

- Numero de gerações: 10

- Taxa de mutação: 0.10

- Numero de ações individuais: 150


![image](https://user-images.githubusercontent.com/88808709/173196110-a8fa1baf-4b8d-429d-bd03-02c99a19267b.png)

Print do Resultado acima !

---
## A seguir temos um exemplo de resultados e as respectivas configurações:  

- Tamanho da população: 15

- Numero de gerações: 15

- Taxa de mutação: 0.08

- Numero de ações individuais: 125

![image](https://user-images.githubusercontent.com/88808709/173196254-45e68dff-c703-4180-8e92-08d6adfeae12.png)

Print do Resultado acima !

---
# ***Referências*** 

 - BENDER Frederico **Implementação de Algoritmo Genético - Problema da mochila - Python** Março 2021 **<Acessado em 05/2022> [^1].**
 
 - TAVARES Ander **Algoritmos Genéticos** Março 2022 **<Acessado em 05/2022> [^2].**
 
 - **GENETICOS Lork Algoritmos Geneticos** Março 2016 **<Acessado em 05/2022> [^3].**
 
 - KABÁTH David **Algoritmos genéticos**. Site Postado Yahoo. Internet: 2010. **<Acessado em 05/2022> [^4].**

 - LUCA C. Diogo **Apostilia de Introdução a Algoritmos Geneticos: Principios e Aplicações.** Março 2002 **<Acessado em 05/2022> [^5].** 

[^1]: ( [(326) Implementação de Algoritmo   Genético - Problema da mochila - Python - YouTube](https://www.youtube.com/watch?v=fC4mDO3RGQ8) ) 

[^2]: ( [(326) Algoritmos Genéticos - Seleção - YouTube](https://www.youtube.com/watch?v=dFboBO_oGIU) )

[^3]: ( [https://sites.icmc.usp.br/andre/research/genetic/#:~:text=Um método de seleção muito,ao seu índice de aptidão](https://sites.icmc.usp.br/andre/research/genetic/#:~:text=Um%20m%C3%A9todo%20de%20sele%C3%A7%C3%A3o%20muito,ao%20seu%20%C3%ADndice%20de%20aptid%C3%A3o) )

[^4]: ( [Genetic algorithms](https://is.muni.cz/www/kabath/genetic_algorithms.html) )

[^5]: ( [Algoritmos Genéticos: uma Introdução](https://www.muriloleal.com.br/visao/repositorio/centec/eai/ia//ALGORITMOS%20GEN%C3%89TICOS%20-%20APOSTILA.pdf) )
