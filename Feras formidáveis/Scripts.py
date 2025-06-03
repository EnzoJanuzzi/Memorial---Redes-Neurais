import random

###############################################################################
#                               Operadores                                    #
###############################################################################

def selecao_torneio_min(populacao, fitness, tamanho_torneio):
    """Faz a seleção de uma população usando torneio.

    Nota: da forma que está implementada, só funciona em problemas de
    minimização.

    Args:
      populacao: lista contendo os individuos do problema
      fitness: lista contendo os valores computados da funcao objetivo
      tamanho_torneio: quantidade de invíduos que batalham entre si

    """
    selecionados = []

    for _ in range(len(populacao)):
        sorteados = random.sample(populacao, tamanho_torneio)

        fitness_sorteados = []
        for individuo in sorteados:
            indice_individuo = populacao.index(individuo)
            fitness_sorteados.append(fitness[indice_individuo])

        min_fitness = min(fitness_sorteados)
        indice_min_fitness = fitness_sorteados.index(min_fitness)
        individuo_selecionado = sorteados[indice_min_fitness]

        selecionados.append(individuo_selecionado)

    return selecionados

def selecao_torneio_max(populacao, fitness, tamanho_torneio):
    """Faz a seleção de uma população usando torneio.

    Nota: da forma que está implementada, só funciona em problemas de
    maximização.

    Args:
      populacao: lista contendo os individuos do problema
      fitness: lista contendo os valores computados da funcao objetivo
      tamanho_torneio: quantidade de invíduos que batalham entre si

    """
    selecionados = []

    for _ in range(len(populacao)):
        sorteados = random.sample(populacao, tamanho_torneio)

        fitness_sorteados = []
        for individuo in sorteados:
            indice_individuo = populacao.index(individuo)
            fitness_sorteados.append(fitness[indice_individuo])

        min_fitness = max(fitness_sorteados)
        indice_min_fitness = fitness_sorteados.index(min_fitness)
        individuo_selecionado = sorteados[indice_min_fitness]

        selecionados.append(individuo_selecionado)

    return selecionados

def cruzamento_uniforme(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento uniforme

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        filho1 = []
        filho2 = []

        for gene_pai, gene_mae in zip(pai, mae):
            if random.choice([True, False]):
                filho1.append(gene_pai)
                filho2.append(gene_mae)
            else:
                filho1.append(gene_mae)
                filho2.append(gene_pai)

        return filho1, filho2
    else:
        return pai, mae

def cruzamento_ordenado(pai, mae, chance_de_cruzamento):
    """Cruzamento ordenado entre dois individuos

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        tamanho_individuo = len(mae)

        # pontos de corte
        corte1 = random.randint(0, tamanho_individuo - 2)
        corte2 = random.randint(corte1 + 1, tamanho_individuo)

        # filho1
        filho1 = [None] * tamanho_individuo
        filho1[corte1:corte2] = mae[corte1:corte2]
        pai_ = pai[corte2:] + pai[:corte2]
        posicao = corte2 % tamanho_individuo
        for valor in pai_:
            if valor not in filho1:
                filho1[posicao] = valor
                posicao += 1
                posicao %= tamanho_individuo

        # filho2
        filho2 = [None] * tamanho_individuo
        filho2[corte1:corte2] = pai[corte1:corte2]
        mae_ = mae[corte2:] + mae[:corte2]
        posicao = corte2 % tamanho_individuo
        for valor in mae_:
            if valor not in filho2:
                filho2[posicao] = valor
                posicao += 1
                posicao %= tamanho_individuo

        return filho1, filho2
    else:
        return pai, mae

def mutacao_simples(populacao, chance_de_mutacao, valores_possiveis):
    """Realiza mutação simples

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      valores_possiveis: lista com todos os valores possíveis dos genes

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.randint(0, len(individuo) - 1)
            valor_gene = individuo[gene]
            valores_sorteio = set(valores_possiveis) - set([valor_gene])
            individuo[gene] = random.choice(list(valores_sorteio))

def mutacao_salto(populacao, chance_de_mutacao, valores_possiveis):
    """Realiza mutação de salto

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      valores_possiveis: lista com todos os valores possíveis dos genes

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.randint(0, len(individuo) - 1)
            valor_gene = individuo[gene]
            indice_letra = valores_possiveis.index(valor_gene)
            indice_letra += random.choice([1, -1])
            indice_letra %= len(valores_possiveis)
            individuo[gene] = valores_possiveis[indice_letra]

def mutacao_salto_tamanho(populacao, chance_de_mutacao, valores_possiveis):
    """Realiza mutação de salto de tamanho

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      valores_possiveis: lista com todos os valores possíveis dos genes

    """
    for individuo in populacao:
      if random.random() < chance_de_mutacao:
        # condições de contorno
        if len(individuo) == 1:
          individuo.insert(0,random.choice(valores_possiveis))
        elif len(individuo) == 30:
          individuo.pop(-1)

        else:
          gene = random.randint(0, len(individuo) - 1)
          # sorteia se vai adicionar ou remover o gene
          fator_transicao = random.choice([-1, 1])
          if fator_transicao == -1:
            individuo.pop(gene)
          else:
            individuo.insert(gene,random.choice(valores_possiveis))

def mutacao_elemento(populacao, chance_de_mutacao, valores_possiveis):
    """Realiza mutação dos elementos no problema da liga

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      valores_possiveis: lista com todos os valores possíveis dos genes

    """
    
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.randint(0, len(individuo) - 1)
            valores_sorteio = set(valores_possiveis) - set(individuo)
            individuo[gene] = random.choice(list(valores_sorteio))

###############################################################################
#                               Senha Aleatória                               #
###############################################################################

def gene_senha(letras_possiveis):
    """Sorteia uma letra.

    Args:
      letras: letras possíveis de serem sorteadas.

    """
    letra = random.choice(letras_possiveis)
    return letra

def cria_candidato_senha_size(letras_possiveis):
    """Cria um candidato para o problema da senha com tamanho aleatório

    Args:
      letras_possiveis: letras possíveis de serem sorteadas.

    """
    candidato = []

    for _ in range(random.randint(1,30)):
        candidato.append(gene_senha(letras_possiveis))

    return candidato

def populacao_senha_size(tamanho_populacao, letras_possiveis):
    """Cria população inicial no problema da senha no problema da senha com tamanho aleatório

    Args
      tamanho_populacao: tamanho da população.
      letras_possiveis: letras possíveis de serem sorteadas.

    """
    populacao = []

    for _ in range(tamanho_populacao):
        populacao.append(cria_candidato_senha_size(letras_possiveis))

    return populacao

def funcao_objetivo_senha_size(candidato, senha_verdadeira):
    """Computa a funcao objetivo de um candidato no problema da senha

    Args:
      candidato: um palpite para a senha que você quer descobrir
      senha_verdadeira: a senha que você está tentando descobrir

    """
    distancia = 0

    for letra_candidato, letra_senha in zip(candidato, senha_verdadeira):
        num_letra_candidato = ord(letra_candidato)
        num_letra_senha = ord(letra_senha) # converte letra para número
        distancia += abs(num_letra_candidato - num_letra_senha)
    distancia += abs(len(candidato) - len(senha_verdadeira))*75

    return distancia

def funcao_objetivo_pop_senha_size(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.

    Args:
      populacao: lista contendo os individuos do problema
      senha_verdadeira: a senha que você está tentando descobrir

    """
    fitness = []

    for individuo in populacao:
        fitness.append(funcao_objetivo_senha_size(individuo, senha_verdadeira))

    return fitness

###############################################################################
#                               Ligas ternárias                               #
###############################################################################

def cria_candidato_liga(tamanho_liga, elementos_possiveis):
    """Cria um candidato para o problema da liga

    Args:
      tamanho_liga: inteiro representando o tamanho da liga.
      elementos_possiveis: elementos possíveis de serem sorteadas.

    """
    
    candidato = []
       
    for _ in range(tamanho_liga):
      valores_sorteio = set(elementos_possiveis) - set(candidato)
      elemento = random.choice(list(valores_sorteio))
      candidato.append(elemento)

    return candidato

def populacao_liga(tamanho_pop, tamanho_liga, elementos_possiveis):
  """Cria uma população para o problema das ligas ternárias.

  Args:
    tamanho: tamanho da população
    tamanho_liga: inteiro representando o tamanho da liga.
    elementos_possiveis: elementos possíveis de serem sorteados.

  """
  populacao = []
  for _ in range(tamanho_pop):
      populacao.append(cria_candidato_liga(tamanho_liga, elementos_possiveis))
  return populacao
  
def funcao_objetivo_liga(candidato, elementos_possiveis, dic_precos, xyz):
    preco = 0

    for elemento, qtd in zip(candidato, xyz):
      preco += dic_precos[elemento] * qtd

    return preco

def funcao_objetivo_pop_liga(populacao, elementos_possiveis, dic_precos, xyz):
    fitness = []
    
    for individuo in populacao:
        fitness.append(funcao_objetivo_liga(individuo, elementos_possiveis, dic_precos, xyz))
        
    return fitness

###############################################################################
#                           Ligas ternárias leves                             #
###############################################################################

def funcao_objetivo_liga_leve(candidato, elementos_possiveis, dic_precos, dic_pesos, xyz):
    densidade_valor = 0
 
    for elemento, qtd in zip(candidato, xyz):
      densidade_valor += (dic_precos[elemento]/dic_pesos[elemento]) * qtd
 
    return densidade_valor
 
def funcao_objetivo_pop_liga_leve(populacao, elementos_possiveis, dic_precos, dic_pesos, xyz):
    fitness = []
   
    for individuo in populacao:
        fitness.append(funcao_objetivo_liga_leve(individuo, elementos_possiveis, dic_precos, dic_pesos, xyz))
       
    return fitness  
