class Restricao():
    def __init__(self, variaveis):
        self.variaveis = variaveis

    def esta_satisfeita(self, atribuicao):
      return True

class SatisfacaoRestricoes():
  def __init__(self, variaveis, dominios):
    self.variaveis = variaveis # Variáveis para serem restringidas
    self.dominios = dominios # Domínio de cada variável
    self.restricoes = {}
    for variavel in self.variaveis:
        self.restricoes[variavel] = []
        if variavel not in self.dominios:
            raise LookupError("Cada variávei precisa de um domínio")

  def adicionar_restricao(self, restricao):
    for variavel in restricao.variaveis:
      if variavel not in self.variaveis:
        raise LookupError("Variável não definida previamente")
      else:
        self.restricoes[variavel].append(restricao)

  def esta_consistente(self, variavel, atribuicao):
    for restricoes in self.restricoes[variavel]:
      if not restricoes.esta_satisfeita(atribuicao):
        return False
    return True
  
  def busca_backtracking(self, atribuicao = {}):
    # atribuicao is complete if every variavel is assigned (our base case)
    if len(atribuicao) == len(self.variaveis):
      return atribuicao

    # get all variaveis in the CSP but not in the atribuicao
    variavel_nao_atribuida  = [v for v in self.variaveis if v not in atribuicao]

    primeira_variavel = variavel_nao_atribuida[0]
    for valor in self.dominios[primeira_variavel]:
      atribuicao_local = atribuicao.copy()
      atribuicao_local[primeira_variavel] = valor
      # if we're still consistent, we recurse (continue)
      if self.esta_consistente(primeira_variavel, atribuicao_local):
        resultado  = self.busca_backtracking(atribuicao_local)
        # if we didn't find the resultado, we will end up backtracking
        if resultado is not None:
          return resultado
    return None