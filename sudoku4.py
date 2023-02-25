from satisfacao_restricoes import Restricao, SatisfacaoRestricoes

class RestricaoDiferentes(Restricao):
  def __init__(self, x1, x2, x3, x4):
    super().__init__([x1, x2, x3, x4])
    self.variaveis = [x1, x2, x3, x4]

  def esta_satisfeita(self, atribuicao):
    # Não analise se todos os estados estiverem atribu;idos
    if not all(variavel in atribuicao for variavel in self.variaveis):
      return True
    # cores de estados vizinhos não podem ser igual
    valores = [atribuicao[variavel] for variavel in self.variaveis]
    return len(set(valores)) == 4 # pouco performático

def imprime(atribuicao):
  print("Sudoku:")
  for i in range(1, 5):
      for j in range(1, 5):
          print(atribuicao[f"X{i}{j}"], end=" ")
      print()

if __name__ == "__main__":
    variaveis = ["X11", "X12", "X13", "X14",
                "X21", "X22", "X23", "X24",
                "X31", "X32", "X33", "X34",
                "X41", "X42", "X43", "X44"]      
    dominios = {}
    for variavel in variaveis:
      dominios[variavel] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    problema = SatisfacaoRestricoes(variaveis, dominios)

    # Linhas 
    problema.adicionar_restricao(RestricaoDiferentes("X11", "X12", "X13", "X14"))
    problema.adicionar_restricao(RestricaoDiferentes("X21", "X22", "X23", "X24"))
    problema.adicionar_restricao(RestricaoDiferentes("X31", "X32", "X33", "X34"))
    problema.adicionar_restricao(RestricaoDiferentes("X41", "X42", "X43", "X44"))

    # Colunas 
    problema.adicionar_restricao(RestricaoDiferentes("X11", "X21", "X31", "X41"))
    problema.adicionar_restricao(RestricaoDiferentes("X12", "X22", "X32", "X42"))
    problema.adicionar_restricao(RestricaoDiferentes("X13", "X23", "X33", "X43"))
    problema.adicionar_restricao(RestricaoDiferentes("X14", "X24", "X34", "X44"))

    # Quadrados
    problema.adicionar_restricao(RestricaoDiferentes("X11", "X12", "X21", "X22"))
    problema.adicionar_restricao(RestricaoDiferentes("X13", "X14", "X23", "X24"))
    problema.adicionar_restricao(RestricaoDiferentes("X31", "X32", "X41", "X42"))
    problema.adicionar_restricao(RestricaoDiferentes("X33", "X34", "X43", "X44"))

		# No caso do Sudoku, já passamos algumas variáveis já preenchidas
    resposta = problema.busca_backtracking(
      {
        "X11": 3, "X12": 4, "X13": 1,
        "X22": 2,
        "X33": 2,
        "X42": 1, "X43": 4, "X44": 3,

      }
    )
    if resposta is None:
        print("Nenhuma resposta encontrada")
    else:
        print(imprime(resposta))