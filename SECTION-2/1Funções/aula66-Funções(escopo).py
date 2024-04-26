"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

# x foi definido fora da função, tem escopo global, então da para ser acessado dentro da função. (má prática de programação)
x = 1

def escopo():
    # x está dentro do escopo da função, não da de acessar fora dela
    ## SE EU QUISER MODIFICAR A VARIÁVEL DE FORA (x), uso global x - (má prática de programação)
    #global x --- estaria modificando a variável de fora - (má prática de programação)
    x = 10 # definido um outro x dentro da função, ela prioriza esse.

    def outra_funcao():
        #x e y não pode ser acessado por nenhum outro lugar.
        x = 11
        y = 2
        print(x, y) # chama o x e y da função que ele está
    
    # eu chamo a função que está dentro da principal, para quando eu chamar ela, ela executa a "outra_funcao"
    outra_funcao()
    print(x) # chama o x da função que está (x = 10)

escopo()
print(x) # x da variável global (x = 1)
