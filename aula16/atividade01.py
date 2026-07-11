import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Obter dados

try:
    print("Obtendo dados...")

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # delimitando as variáveis
    df_lesao = df_ocorrencias[['cisp', 'lesao_corp_dolosa', 'lesao_corp_morte']]
    
    # agrupar por cisp
    df_lesao = df_lesao.groupby('cisp', as_index=False)[['lesao_corp_dolosa', 'lesao_corp_morte']].sum()
    
    print(df_lesao)
    print("\nDados obtidos com sucesso!")

except Exception as e:
    print(f"Erro ao obter dados: {e}")

    # Calculando Correlação entre Roubos e Recuperação de Veículos
try:
    print("\nCalculando correlação entre roubos e recuperação de veículos...")

    # Calcular a correlação
    # correlacao = np.corrcoef(df_veiculos['roubo_veiculo'], df_veiculos['recuperacao_veiculos'])
    correlacao = np.corrcoef(df_lesao['lesao_corp_dolosa'], df_lesao['lesao_corp_morte'])[0, 1]
    
    print(f"Correlação: {correlacao}") 
    print(f'''
          A correlação entre lesão corporal dolosa e lesão corporal com morte é de {correlacao} o que indica uma correlação positiva forte entre as variáveis, 
          ou seja, conforme a lesão corporal dolosa aumenta, também aumenta a lesão corporal com morte.
          ''')
    # a correlação ela tenta comparar todas as variáveis varias vezes, em matriz, a gente tem lesao_corp_dolosa e lesao_corp_morte,
    # então ela vai comparar essas duas variáveis e vai retornar um valor entre -1 e 1, onde -1 é uma correlação negativa perfeita, 
    # 0 é nenhuma correlação e 1 é uma correlação positiva perfeita.
    # Se o valor estiver entre 0,70 e 1,00 ou entre -0,70 e -1,00, podemos considerar que há uma correlação forte entre as variáveis.
    # Se o valor estiver entre 0,30 e 0,70 ou entre -0,30 e -0,70, podemos considerar que há uma correlação moderada entre as variáveis.
    # Se o valor estiver entre 0,00 e 0,30 ou entre -0,00 e -0,30, podemos considerar que há uma correlação fraca entre as variáveis.

    # Plotando o gráfico de dispersão
    plt.scatter(df_lesao['lesao_corp_dolosa'], df_lesao['lesao_corp_morte'])
    plt.title('Correlação entre Lesão Corporal Dolosa e Lesão Corporal com Morte')
    plt.xlabel('Lesão Corporal Dolosa')
    plt.ylabel('Lesão Corporal com Morte')
    plt.show()


except Exception as e:
    print(f"Erro ao calcular correlação: {e}")
