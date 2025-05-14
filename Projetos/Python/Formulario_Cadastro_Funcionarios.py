import random

# CRIAR / RESETAR LISTAS
empresa = []
funcionario = []
matriculas_registradas = []
plano = []

# MODULARIZAR DADOS DE LEITURA: NOME
def lerNome():
  while True:
    try:
      nome = input('NOME: ')
      if(len(nome) < 2):
        print('ERRO: Escolha de novo')
      else:
        break
    except:
        print('ERRO: Escolha novamente')
  return nome

# MODULARIZAR DADOS DE LEITURA: CARGO
def lerCargo():
  while True:
    try:
      cargo = input('CARGO: ')
      if(len(cargo) < 2):
        print('ERRO: Escolha de novo')
      else:
        break
    except:
          print('ERRO: Escolha novamente')
  return cargo

# MODULARIZAR DADOS DE LEITURA: MATRÍCULA
import random

matriculas_registradas = set()

def lerMatricula():
  while True:
    try:
      opcao = input('DIGITE "S" PARA GERAR MATRÍCULA: ').strip().upper()
      if opcao != 'S':
        print('ERRO: Digite "S" para gerar a matrícula.')
      else:
        while True:
          id_matricula = random.randint(1000, 10000)
          if id_matricula not in matriculas_registradas:
            matriculas_registradas.add(id_matricula)
            print(f'Matrícula {id_matricula} gerada para esse funcionário.')
            return id_matricula
    except Exception as e:
      print('ERRO: Escolha de novo.', e)

# MODULARIZAR DADOS DE LEITURA: PLANO DE SAÚDE
def lerPlano():
  while True:
    try:
      plano = input('PLANO DE SAÚDE (S/N): ').strip().upper()
      if plano not in ('S', 'N'):
        print('ERRO: Escolha novamente diante a opção')
      else:
        break
    except:
      print('ERRO: Escolha novamente')
  return plano

# MODULARIZAR DADOS DE LEITURA: SALÁRIO
def lerSalario():
  while True:
    try:
      salario = float(input('INFORME O SALÁRIO R$: '))
      if salario < 1500:
        print('ERRO: Escolha novamente')
      else:
        break
    except:
      print('ERRO: Escolha novamente')
  return salario

# MENU: PROGRAMA PRINCIPAL (MAIN)
print('=' * 20)
print('MENU: FORMULÁRIO DE CADASTRO \n')
print('OPÇÃO 0 - CADASTRAR FUNCIONÁRIO')
print('QUALQUER TECLA NUMÉRICA - SAIR DO PROGRAMA')
print('=' * 20)
while True:
  try:
    opcao = int(input('DIGITE SUA OPÇÃO: '))
    if opcao != 0:
      print('VOCÊ ESCOLHEU SAIR \n')
      break
    else:
      # OPÇÃO 0 - CADASTRAR FUNCIONÁRIO
      print(f'INSERIR OS DADOS DO {len(empresa) + 1}º FUNCIONÁRIO: ')
      nome = lerNome()
      cargo = lerCargo()
      matricula = lerMatricula()
      plano = lerPlano()
      salario = lerSalario()
      funcionario = [nome, cargo, matricula, plano, salario]

      empresa.append(funcionario)
      empresa.append(plano)
      print('FUNCIONÁRIO CADASTRADO COM SUCESSO \n')
  except:
    print('FIM DO PROGRAMA \n')
    break
  
#   import math

# total_funcionarios = len(empresa)

# # A) TAXA DE ADESÃO e NÃO-ADESÃO
# nao_adesao_plano = [valor[3] for valor in empresa if valor[3] == 'N']
# adesao_plano = [valor[3] for valor in empresa if valor[3] == 'S']

# print('RELATÓRIO GERENCIAL: TAXA DE ADESÃO')
# print(f'ADESÃO DOS {total_funcionarios} FUNCIONÁRIOS (PLANO DE SAÚDE)')
# print(f'ADESÃO AO PLANO: {(len(adesao_plano) / total_funcionarios) * 100}% DOS FUNCIONÁRIOS')
# print(f'NÃO-ADESÃO AO PLANO: {(len(nao_adesao_plano) / total_funcionarios) * 100}% DOS FUNCIONÁRIOS \n')

# # B) NOMES DOS FUNCIONÁRIOS QUE POSSUEM PLANO
# nomes_com_plano = [valor[0] for valor in empresa if valor[3] == 'S']

# print('RELATÓRIO GERENCIAL: NOMES DOS FUNCIONÁRIOS (PLANO DE SAÚDE)')
# print('NOMES DOS FUNCIONÁRIOS COM PLANO DE SAÚDE')
# print(f'{nomes_com_plano} \n')

# # C) CARGOS DE FUNCIONÁRIOS ACIMA DA MÉDIA SALARIAL
# total_salario = [valor[4] for valor in empresa]

# if total_funcionarios > 0:
#     media_salario = sum(total_salario) / total_funcionarios

# print('RELATÓRIO GERENCIAL: CARGOS ACIMA DA MÉDIA SALARIAL')
# print(f'MÉDIA SALARIAL POR FUNCIONÁRIO: R${media_salario:.2f}')
# cargos_acima_media_salarial = [valor[1] for valor in empresa if valor[4] > media_salario]
# print(f'OS CARGOS ACIMA DA MÉDIA SALARIAL SÃO:')
# print(f'{cargos_acima_media_salarial} \n')

# # D) FOLHA DE PAGAMENTO
# total_bruto = sum([valor[4] for valor in empresa])  # Salários totais
# desconto_plano = 212.54
# total_descontos = sum([desconto_plano for valor in empresa if valor[3] == 'S'])
# total_liquido = total_bruto - total_descontos
# print('RELATÓRIO ADMNISTRATIVO: FOLHA DE PAGAMENTO')
# print(f'TOTAL DE FUNCIONÁRIOS: {total_funcionarios}')
# print(f'TOTAL BRUTO DA FOLHA: R${total_bruto:.2f}')
# print(f'DESCONTOS (PLANO DE SAÚDE): R${total_descontos:.2f}')
# print(f'TOTAL LIQUÍDO DA FOLHA: R${total_liquido:.2f}')