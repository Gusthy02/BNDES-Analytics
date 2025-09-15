import pandas as pd
from src.preprocess import clean_bndes_data
from src.visuals import plot_by_sector, plot_over_time, plot_by_state

def run_tests():
    # 1. Criar datasets fake em memória
    data = {
        'ano': [2020, 2020, 2021, 2021, 2022],
        'setor': ['Energia', 'Infraestrutura', 'Energia', 'Agronegócio', 'Infraestrutura'],
        'uf': ['SP', 'RJ', 'SP', 'MG', 'RJ'],
        'valor': [1000000, 500000, 1200000, 800000, 700000] 
    }

    df = pd.DataFrame(data)

    # 2. Limpeza
    df_clean = clean_bndes_data(df)
    print(f'✅ DataFrame limpo:\n{df_clean}')

    # 3. Testar gráficos
    fig1 = plot_by_sector(df_clean)
    fig2 = plot_over_time(df_clean)
    fig3 = plot_by_state(df_clean)

    assert fig1 is not None, '❌ plot_by_sector falhou'
    assert fig2 is not None, '❌ plot_over_time falhou'
    assert fig3 is not None, '❌ plot_by_state falhou'

    print('🎉 Todos os testes passaram!')

if __name__ == '__main__':
    run_tests()