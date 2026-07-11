# importar pandas, numpy e matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Obter dados

try:
    print("Obtendo dados...")

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # delimitando as variáveis
    df_veiculos = df_ocorrencias[['cisp', 'roubo_veiculo', 'recuperacao_veiculos']]
    
    # agrupar por cisp
    df_veiculos = df_veiculos.groupby('cisp', as_index=False)[['roubo_veiculo', 'recuperacao_veiculos']].sum()
    
    print(df_veiculos)
    print("\nDados obtidos com sucesso!")

except Exception as e:
    print(f"Erro ao obter dados: {e}")


# Calculando Correlação entre Roubos e Recuperação de Veículos
try:
    print("\nCalculando correlação entre roubos e recuperação de veículos...")

    # Calcular a correlação
    # correlacao = np.corrcoef(df_veiculos['roubo_veiculo'], df_veiculos['recuperacao_veiculos'])
    correlacao = np.corrcoef(df_veiculos['roubo_veiculo'], df_veiculos['recuperacao_veiculos'])[0, 1]
    
    print(f"Correlação: {correlacao}") # a correlação ela tenta comparar todas as variáveis varias vezes, em matriz, a gente tem roubo_veiculo e recuperacao_veiculos, então ela vai comparar essas duas variáveis e vai retornar um valor entre -1 e 1, onde -1 é uma correlação negativa perfeita, 0 é nenhuma correlação e 1 é uma correlação positiva perfeita.

    # Plotando o gráfico de dispersão
    plt.scatter(df_veiculos['roubo_veiculo'], df_veiculos['recuperacao_veiculos'])
    plt.title('Correlação entre Roubos e Recuperação de Veículos')
    plt.xlabel('Roubos de Veículos')
    plt.ylabel('Recuperação de Veículos')
    plt.show()


except Exception as e:
    print(f"Erro ao calcular correlação: {e}")