# Avaliação Prática - Arquitetura de Computadores 
Universidade Federal do Ceará 

 
## descrição geral: 
Projetar uma microarquitetura, implementar o respectivo emulador e permitir que sejam executados programas quaisquer para ela escritos. Deverá, portanto, projetar um conjunto de instruções para serem executadas pela sua microarquitetura (definindo uma macroarquitetura), implementando-o através do microprograma de controle. deve-se implementar um montador (assembler) para uma linguagem de montagem (assembly) que traduza para a linguagem de máquina da macroarquitetura criada.
### Parte 1 - Emulador:
---
Tomar como base o emulador escrito em aula ou construir do zero.
- Criar uma nova microarquitetura.
- Melhorar a microarquitetura proposta em sala.
- Manter a microarquitetura inalterada.
- Criar um novo microprograma de controle, disponibilizando um novo conjunto de instruções (nova macroarquitetura).
- Melhorar o microprograma, tanto tornando mais eficientes as implementações das instruções já apresentadas, quanto adicionando novas instruções ao conjunto.
- Manter o microprograma inalterado.

O emulador deve poder receber arquivos binários com programas em linguagem de máquina da sua arquitetura e executá-los.
### Parte 2 - Assembler:
---
O assembler deve montar programas escritos no assembly que foram projetados na linguagem de máquina da arquitetura. O assembly deve cobrir todo o conjunto de instruções criados em sua arquitetura bem como disponibilizar pseudo-instruções para escrita direta de bytes ou words no processo de montagem. Um assembler para a arquitetura apresentada em sala de aula foi disponibilizado e, portanto, é possível:
- Utilizar o mesmo assembler sem qualquer alteração.
- Alterar o assembler disponibilizado para dar conta do novo conjunto de instruçõe.
- Construir um novo assembler do zero.


### Parte 3 - Programando para sua máquina:
--- 
Foi disponibilizados quatro problemas para os quais deve-se escrever programas que computem suas soluções, executando tais programas em seu emulador. Você deverá, portanto, escrever esses programas com sua linguagem assembly, usar o seu assembler para gerar o código binário e, finalmente, colocar para rodar no emulador
#### Problemas disponibilizados:
---
![problemas](<imgs/Captura de tela de 2023-06-25 11-19-44.png>)
## Dupla:
---
| Estudante | Github |
| --- | --- |
| Gabriel Carmo | [ArtroxGabriel](https://github.com/ArtroxGabriel)
| Tobias Nóbrega | [Tobnobre](https://github.com/Tobnobre)
