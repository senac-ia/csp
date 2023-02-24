from satisfacao_restricoes import Restricao, SatisfacaoRestricoes
import numpy as np

class RestricaoColoracaoMapa(Restricao):
  def __init__(self, estado1, estado2):
    super().__init__([estado1, estado2])
    self.estado1 = estado1
    self.estado2 = estado2

  def esta_satisfeita(self, atribuicao):
    # se nenhum dos estados está com cor atribuída, está satisfeito
    if self.estado1 not in atribuicao or self.estado2 not in atribuicao:
        return True
    # cores de estados vizinhos não podem ser igual 
    return atribuicao[self.estado1] != atribuicao[self.estado2]

if __name__ == "__main__":
  variaveis = np.array(["Maranhão", "Piauí", "Ceará", "Pernambuco", "Rio Grande do Norte", "Paraíba", "Alagoas", "Sergipe", "Bahia"])
  dominios = {}
  for variavel in variaveis:
    dominios[variavel] = np.array(["vermelho", "verde", "azul"])
  problema = SatisfacaoRestricoes(variaveis, dominios)
  problema.adicionar_restricao(RestricaoColoracaoMapa("Maranhão", "Piauí"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Piauí", "Maranhão"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Piauí", "Ceará"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Piauí", "Pernambuco"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Piauí", "Bahia"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Ceará", "Piauí"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Ceará", "Paraíba"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Ceará", "Pernambuco"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Ceará", "Rio Grande do Norte"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Rio Grande do Norte", "Ceará"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Rio Grande do Norte", "Paraíba"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Paraíba", "Rio Grande do Norte"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Paraíba", "Ceará"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Paraíba", "Pernambuco"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Pernambuco", "Ceará"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Pernambuco", "Paraíba"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Pernambuco", "Alagoas"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Pernambuco", "Bahia"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Alagoas", "Pernambuco"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Alagoas", "Sergipe"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Alagoas", "Bahia"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Sergipe", "Alagoas"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Sergipe", "Bahia"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Bahia", "Piauí"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Bahia", "Pernambuco"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Bahia", "Alagoas"))
  problema.adicionar_restricao(RestricaoColoracaoMapa("Bahia", "Sergipe"))

  resposta = problema.busca_backtracking()
  if resposta is None:
    print("Nenhuma resposta encontrada")
  else:
    print(resposta)