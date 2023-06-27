import statistics
import streamlit as st

def main():
    st.title("Cálculo de Média, Desvio Padrão e Coeficiente de Variação de Gols")

    # Obtém os gols dos jogos
    gols_jogo_1_casa = st.number_input("Informe a quantidade de gols do jogo 1 (time da casa): ", min_value=0, step=1)
    gols_jogo_2_casa = st.number_input("Informe a quantidade de gols do jogo 2 (time da casa): ", min_value=0, step=1)
    gols_jogo_3_casa = st.number_input("Informe a quantidade de gols do jogo 3 (time da casa): ", min_value=0, step=1)
    gols_jogo_4_casa = st.number_input("Informe a quantidade de gols do jogo 4 (time da casa): ", min_value=0, step=1)
    gols_jogo_5_casa = st.number_input("Informe a quantidade de gols do jogo 5 (time da casa): ", min_value=0, step=1)

    gols_jogo_1_fora = st.number_input("Informe a quantidade de gols do jogo 1 (time de fora): ", min_value=0, step=1)
    gols_jogo_2_fora = st.number_input("Informe a quantidade de gols do jogo 2 (time de fora): ", min_value=0, step=1)
    gols_jogo_3_fora = st.number_input("Informe a quantidade de gols do jogo 3 (time de fora): ", min_value=0, step=1)
    gols_jogo_4_fora = st.number_input("Informe a quantidade de gols do jogo 4 (time de fora): ", min_value=0, step=1)
    gols_jogo_5_fora = st.number_input("Informe a quantidade de gols do jogo 5 (time de fora): ", min_value=0, step=1)

    # Calcula a média de gols
    media_casa = statistics.mean([gols_jogo_1_casa, gols_jogo_2_casa, gols_jogo_3_casa, gols_jogo_4_casa, gols_jogo_5_casa])
    media_fora = statistics.mean([gols_jogo_1_fora, gols_jogo_2_fora, gols_jogo_3_fora, gols_jogo_4_fora, gols_jogo_5_fora])

    # Calcula o desvio padrão de gols
    desvio_padrao_casa = statistics.stdev([gols_jogo_1_casa, gols_jogo_2_casa, gols_jogo_3_casa, gols_jogo_4_casa, gols_jogo_5_casa])
    desvio_padrao_fora = statistics.stdev([gols_jogo_1_fora, gols_jogo_2_fora, gols_jogo_3_fora, gols_jogo_4_fora, gols_jogo_5_fora])

    # Calcula o coeficiente de variação de gols
    coef_var_casa = (desvio_padrao_casa / media_casa) if media_casa != 0 else 0
    coef_var_fora = (desvio_padrao_fora / media_fora) if media_fora != 0 else 0

    # Formata o coeficiente de variação com duas casas decimais
    coef_var_casa_formatted = f'{coef_var_casa:.2f}'
    coef_var_fora_formatted = f'{coef_var_fora:.2f}'

    # Verifica a cor do coeficiente de variação
    coef_var_casa_color = 'green' if coef_var_casa < 0.70 else 'red'
    coef_var_fora_color = 'green' if coef_var_fora < 0.70 else 'red'

    # Cria a tabela com os resultados
    tabela = [
        ['Time', 'Média de Gols', 'Desvio Padrão', 'Coeficiente de Variação'],
        ['Casa', f'{media_casa:.2f}', f'{desvio_padrao_casa:.2f}', coef_var_casa_formatted],
        ['Fora', f'{media_fora:.2f}', f'{desvio_padrao_fora:.2f}', coef_var_fora_formatted]
    ]

 # Exibe a tabela
    st.table(tabela)

    # Exibe o crédito do desenvolvedor
    st.write("Desenvolvido por Lyssandro Silveira")

if __name__ == '__main__':
    main()
