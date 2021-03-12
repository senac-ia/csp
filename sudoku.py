from satisfacao_restricoes import Restricao, SatisfacaoRestricoes

class RestricaoDiferentes(Restricao):
    def __init__(self, x1, x2, x3, x4, x5, x6, x7, x8, x9):
        super().__init__([x1, x2, x3, x4, x5, x6, x7, x8, x9])
        self.variaveis = [x1, x2, x3, x4, x5, x6, x7, x8, x9]

    def esta_satisfeita(self, atribuicao):
        # Não analise se todos os estados estiverem atribu;idos
        if not all(variavel in atribuicao for variavel in self.variaveis):
          return True
        # cores de estados vizinhos não podem ser igual
        valores = [atribuicao[variavel] for variavel in self.variaveis]
        return len(set(valores)) == 9

if __name__ == "__main__":
    variaveis = ["X11", "X12", "X13", "X14", "X15", "X16", "X17", "X18", "X19",
                "X21", "X22", "X23", "X24", "X25", "X26", "X27", "X28", "X29",
                "X31", "X32", "X33", "X34", "X35", "X36", "X37", "X38", "X39",
                "X41", "X42", "X43", "X44", "X45", "X46", "X47", "X48", "X49",
                "X51", "X52", "X53", "X54", "X55", "X56", "X57", "X58", "X59",
                "X61", "X62", "X63", "X64", "X65", "X66", "X67", "X68", "X69",
                "X71", "X72", "X73", "X74", "X75", "X76", "X77", "X78", "X79",
                "X81", "X82", "X83", "X84", "X85", "X86", "X87", "X88", "X89",
                "X91", "X92", "X93", "X94", "X95", "X96", "X97", "X98", "X99"]      
    dominios = {}
    for variavel in variaveis:
      dominios[variavel] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    problema = SatisfacaoRestricoes(variaveis, dominios)

    # Linhas 
    problema.adicionar_restricao(RestricaoDiferentes("X11", "X12", "X13", "X14", "X15", "X16", "X17", "X18", "X19"))
    problema.adicionar_restricao(RestricaoDiferentes("X21", "X22", "X23", "X24", "X25", "X26", "X27", "X28", "X29"))
    problema.adicionar_restricao(RestricaoDiferentes("X31", "X32", "X33", "X34", "X35", "X36", "X37", "X38", "X39"))
    problema.adicionar_restricao(RestricaoDiferentes("X41", "X42", "X43", "X44", "X45", "X46", "X47", "X48", "X49"))
    problema.adicionar_restricao(RestricaoDiferentes("X51", "X52", "X53", "X54", "X55", "X56", "X57", "X58", "X59"))
    problema.adicionar_restricao(RestricaoDiferentes("X61", "X62", "X63", "X64", "X65", "X66", "X67", "X68", "X69"))
    problema.adicionar_restricao(RestricaoDiferentes("X71", "X72", "X73", "X74", "X75", "X76", "X77", "X78", "X79"))
    problema.adicionar_restricao(RestricaoDiferentes("X81", "X82", "X83", "X84", "X85", "X86", "X87", "X88", "X89"))
    problema.adicionar_restricao(RestricaoDiferentes("X91", "X92", "X93", "X94", "X95", "X96", "X97", "X98", "X99"))  

    # Colunas 
    problema.adicionar_restricao(RestricaoDiferentes("X11", "X21", "X31", "X41", "X51", "X61", "X71", "X81", "X91"))
    problema.adicionar_restricao(RestricaoDiferentes("X12", "X22", "X32", "X42", "X52", "X62", "X72", "X82", "X92"))
    problema.adicionar_restricao(RestricaoDiferentes("X13", "X23", "X33", "X43", "X53", "X63", "X73", "X83", "X93"))
    problema.adicionar_restricao(RestricaoDiferentes("X14", "X24", "X34", "X44", "X54", "X64", "X74", "X84", "X94"))
    problema.adicionar_restricao(RestricaoDiferentes("X15", "X25", "X35", "X45", "X55", "X65", "X75", "X85", "X95"))
    problema.adicionar_restricao(RestricaoDiferentes("X16", "X26", "X36", "X46", "X56", "X66", "X76", "X86", "X96"))
    problema.adicionar_restricao(RestricaoDiferentes("X17", "X27", "X37", "X47", "X57", "X67", "X77", "X87", "X97"))
    problema.adicionar_restricao(RestricaoDiferentes("X18", "X28", "X38", "X48", "X58", "X68", "X78", "X88", "X98"))
    problema.adicionar_restricao(RestricaoDiferentes("X19", "X29", "X39", "X49", "X59", "X69", "X79", "X89", "X99"))

    # Quadrados
    problema.adicionar_restricao(RestricaoDiferentes("X11", "X12", "X13", "X21", "X22", "X23", "X31", "X32", "X33"))
    problema.adicionar_restricao(RestricaoDiferentes("X14", "X15", "X16", "X24", "X25", "X26", "X34", "X35", "X36"))
    problema.adicionar_restricao(RestricaoDiferentes("X17", "X18", "X19", "X27", "X28", "X29", "X37", "X38", "X39"))
    problema.adicionar_restricao(RestricaoDiferentes("X41", "X42", "X43", "X51", "X52", "X53", "X61", "X62", "X63"))
    problema.adicionar_restricao(RestricaoDiferentes("X44", "X45", "X46", "X54", "X55", "X56", "X64", "X65", "X66"))
    problema.adicionar_restricao(RestricaoDiferentes("X47", "X48", "X49", "X57", "X58", "X59", "X67", "X68", "X69"))
    problema.adicionar_restricao(RestricaoDiferentes("X71", "X72", "X73", "X81", "X82", "X83", "X91", "X92", "X93"))
    problema.adicionar_restricao(RestricaoDiferentes("X77", "X78", "X79", "X87", "X88", "X89", "X97", "X98", "X99"))
    problema.adicionar_restricao(RestricaoDiferentes("X74", "X75", "X76", "X84", "X85", "X86", "X94", "X95", "X96"))


    resposta = problema.busca_backtracking(
      {
        "X11": 8, "X14": 4, "X16": 6, "X19": 7,
        "X27": 4,
        "X32": 1, "X37": 6, "X38": 5,
        "X41": 5, "X43": 9, "X45": 3, "X47": 7, "X48": 8,
        "X55": 7,
        "X62": 4, "X63": 8, "X65": 2, "X67": 1, "X69": 3,
        "X72": 5, "X73": 2, "X78": 9,
        "X83": 1,
        "X91": 3, "X94": 9, "X96": 2, "X99": 5
      }
    )
    if resposta is None:
        print("Nenhuma resposta encontrada")
    else:
        print(resposta)