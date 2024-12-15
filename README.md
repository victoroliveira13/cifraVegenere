# Cifra de Vigenère

Este repositório apresenta um código em Python para realizar o processo completo de cifragem e decifragem utilizando a **Cifra de Vigenère**. O código imprime os cálculos intermediários, detalhando como cada caractere da mensagem (msg) é combinado com a chave (key).

## Funcionamento

O programa realiza duas etapas principais:

### Etapa 1: Cifrar (Função `enc`)

**Entrada:**
- **Mensagem (msg):** `senha`
- **Chave (key):** `chave`

#### Cálculos detalhados:
```
Mensagem + Chave:
S ( 18 ) + C ( 2 ) = 20 -> U
E ( 4 ) + H ( 7 ) = 11 -> L
N ( 13 ) + A ( 0 ) = 13 -> N
H ( 7 ) + V ( 21 ) = 2 -> C
A ( 0 ) + E ( 4 ) = 4 -> E

Resultado:
ULNCE
```
- `S (18)` indica que o caractere `S` (posição 18 no alfabeto) é somado ao caractere `C` (posição 2). A soma é `(18 + 2) % 26 = 20`, que corresponde a `U`.
- Esse processo é repetido para cada caractere da mensagem com os caracteres correspondentes da chave.
- Quando a chave é menor que a mensagem, ela se repete.

**Texto cifrado:** `ULNCE`

### Etapa 2: Decifrar (Função `dec`)

**Entrada:**
- **Mensagem cifrada (msg):** `ULNCE`
- **Chave (key):** `chave`

#### Cálculos detalhados:
```
Mensagem - Chave:
U ( 20 ) - C ( 2 ) = 18 -> S
L ( 11 ) - H ( 7 ) = 4 -> E
N ( 13 ) - A ( 0 ) = 13 -> N
C ( 2 ) - V ( 21 ) = 7 -> H
E ( 4 ) - E ( 4 ) = 0 -> A

Resultado:
SENHA
```
- `U (20)` indica que o caractere `U` (posição 20 no alfabeto) é subtraído do caractere `C` (posição 2). O resultado é `(20 - 2) % 26 = 18`, que corresponde a `S`.
- Esse processo é repetido para cada caractere da mensagem cifrada, utilizando os caracteres da chave.

**Texto decifrado:** `SENHA`

## Resumo da Saída

### Cifragem:
```
Mensagem + Chave:
S ( 18 ) + C ( 2 ) = 20 -> U
E ( 4 ) + H ( 7 ) = 11 -> L
N ( 13 ) + A ( 0 ) = 13 -> N
H ( 7 ) + V ( 21 ) = 2 -> C
A ( 0 ) + E ( 4 ) = 4 -> E

Resultado:
ULNCE
```

### Decifragem:
```
Mensagem - Chave:
U ( 20 ) - C ( 2 ) = 18 -> S
L ( 11 ) - H ( 7 ) = 4 -> E
N ( 13 ) - A ( 0 ) = 13 -> N
C ( 2 ) - V ( 21 ) = 7 -> H
E ( 4 ) - E ( 4 ) = 0 -> A

Resultado:
SENHA
```

## Conclusão

O código funciona corretamente para cifrar e decifrar utilizando a cifra de Vigenère. Ele também fornece um detalhamento passo a passo dos cálculos realizados em cada etapa, permitindo o acompanhamento completo do processo.

Para testar com outras mensagens ou chaves, basta ajustar os valores de `txt1` (mensagem) e `txt2` (chave) no código.

---

Explore, modifique e aproveite para aprender mais sobre criptografia! 😊

