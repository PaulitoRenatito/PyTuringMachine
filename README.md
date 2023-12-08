This work was done for the discipline of Formal Languages and Automata under the mentoring of teacher [Andrei Rimsa](https://github.com/rimsa)

[English](#eng-us)
- [Description](#description)
- [Instructions](#instructions)
- [Examples](#examples)
  - [Definition](#definition)
  - [Diagram](#diagram)
  - [Input/Output](#inputoutput)

[Português](#pt-br)
- [Descrição](#descrição)
- [Instruções](#instruções)
- [Exemplos](#exemplos)
  - [Definição](#definição)
  - [Diagrama](#diagrama)
  - [Entradas/Saídas](#entradassaídas)

# Eng - US
## Description
This program implements a multiple tape turing machine based on the instructions provided in a JSON file. It accepts a specific input and performs the operations defined in the instruction file.

## Instructions
To run the program you must use command lines in the CMD as follows:
```bash
python main.py tests/01/mt.json "001100001"
```
Where `main.py` is the main script,` tests/01/mt.json` are the instructions for the Turing machine and the third argument `"001100001"` is the entrance of the Turing machine.

## Examples
In the **tests** folder, you will find examples of programs that can be resolved by the script. Each example folder contains three files:

### Definition
**mt.json**: This file contains the definition of the Turing machine.

```json
{ "mt": [
  n,
  E,
  al,
  af,
  x,
  y,
  [
    [e1,e2,[[a1,b1,c1], ..., [ak,bk,ck]]]
  ],
  ei,
  [ef]
]}
```

Where:
- **n:** Quantity of tapes
- **E:** Set of states
- **al:** Language Alphabet
- **af:** Tape Alphabet
- **x:** Start symbol of the tape
- **y:** Empty cell symbol
- Transitional function
  - **e1:** Current state
  - **e2:** Next state
  - **a1:** Symbol read on the tape
  - **b1:** Symbol written on the tape
  - **c1:** Direction of movement of the head, it can be
    - **'>':** Right
    - **'<':** Left
    - **'|':** Unmoved
- **ei:** Initial state
- **ef:** Final state

### Diagram
**mt.pdf**: A visual diagram representing the machine.

### Input/Output
**mt.txt**: A file that contains input pairs and their corresponding test answers in the format _input:answers_ (_Sim_ means Yes and _Não_ means No).

Dentro do arquivo **mt.txt**, os pares de entrada e saída são representados da seguinte maneira:
```
:Sim
0:Não
1:Não
00:Não
01:Não
10:Não
11:Não
000:Sim
001:Não
010:Não
011:Não
100:Não
101:Não
110:Não
111:Sim
```
Where each line consists of an input followed by colon and a response correspondent. Here, "Sim" means that a turing machine accepts the input, and "Não" means that an entry is rejected.

# Pt - BR
## Descrição
Este programa implementa uma Máquina de Turing de multiplas fitas com base nas instruções fornecidas em um arquivo JSON. Ele aceita uma entrada específica e executa as operações definidas no arquivo de instruções.

## Instruções
Para rodar o programa deve-se usar linhas de comando no cmd da seguinte forma:
```bash
python main.py tests/01/mt.json "001100001"
```
Onde `main.py` é o script principal, `tests/01/mt.json` são as instruções para a maquina de turing e o terceiro argumento `"001100001"` é a entrada da Maquina de Turing.

## Exemplos
Na pasta **tests**, você encontrará exemplos de programas que podem ser resolvidos pelo script. Cada pasta de exemplo contém três arquivos:

### Definição
**mt.json**: Este arquivo contém a definição da máquina de Turing.

```json
{ "mt": [
  n,
  E,
  al,
  af,
  x,
  y,
  [
    [e1,e2,[[a1,b1,c1], ..., [ak,bk,ck]]]
  ],
  ei,
  [ef]
]}
```

Onde:
- **n:** Quantidade de fitas
- **E:** Conjunto de estados
- **al:** Alfabeto da linguagem
- **af:** Alfabeto da fita
- **x:** Simbolo de inicio da fita
- **y:** Simbolo de celulas vazias
- Função de transição
  - **e1:** Estado atual
  - **e2:** Proxímo estado
  - **a1:** Simbolo lido na fita
  - **b1:** Simbolo escrito na fita
  - **c1:** Direção de movimento do cabeçote, podendo ser
    - **'>':** Direita
    - **'<':** Esquerda
    - **'|':** Imovél
- **ei:** Estado inicial
- **ef:** Estado final

### Diagrama
**mt.pdf**: Um diagrama visual representando a máquina.

### Entradas/Saídas
**mt.txt**: Um arquivo que contém pares de entrada e suas respostas correspondentes para testes no formato _'entrada:saída'_.

Dentro do arquivo **mt.txt**, os pares de entrada e saída são representados da seguinte maneira:
```
:Sim
0:Não
1:Não
00:Não
01:Não
10:Não
11:Não
000:Sim
001:Não
010:Não
011:Não
100:Não
101:Não
110:Não
111:Sim
```
Onde cada linha consiste em uma entrada seguida por dois pontos e a resposta correspondente. Aqui, "Sim" significa que a máquina de Turing aceita a entrada, e "Não" significa que a entrada é rejeitada.