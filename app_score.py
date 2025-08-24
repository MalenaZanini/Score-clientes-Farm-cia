import streamlit as st
import pandas as pd

# Lendo a planilha
base = pd.read_excel("base.xlsx")  # coloque o caminho correto do seu arquivo


# Função de resumo com score e dias de atraso
def resumo_cliente(row):
    # Definindo a cor do score
    if row['PONTUACAO'] >= 70:
        cor = "green"
    elif row['PONTUACAO'] >= 40:
        cor = "yellow"
    else:
        cor = "red"
    
    return (f"### Cliente: {row['razao_social']}\n"
            f"- 💰 Dívida: **R$ {row['valor_divida']:.2f}**\n"
            f"- 🛒 Última compra: **{row['dias_desde_ultima_compra']} dias atrás**\n"
            f"- 📆 Tempo como cliente: **{row['anos_como_cliente']:.1f} anos**\n"
            f"- 📊 Valor total já gasto: **R$ {row['valor_pago_total']:.2f}**\n"
            f"- ⏳ Proporcao atrasos/pag realizados: **{row['proporcao_atrasos_formatado']}**\n\n"
            f"- 📈 Score: <span style='color:{cor}; font-weight:bold; font-size:24px'>{row['PONTUACAO']}</span>\n")
            

st.title("📌 Sistema de Pontos")

# Inputs opcionais
id_cliente_input = st.text_input("Digite o ID do cliente (opcional):")
razao_social_input = st.text_input("Ou digite a Razão Social do cliente (opcional):")

# Inicializa cliente_row como vazio
cliente_row = pd.DataFrame()

# Filtra pelo que foi preenchido
if id_cliente_input:
    try:
        id_cliente_input = int(id_cliente_input)
        cliente_row = base[base["id_cliente"] == id_cliente_input]
    except ValueError:
        st.warning("Digite um número válido para o ID.")
elif razao_social_input:
    cliente_row = base[base["razao_social"].str.contains(razao_social_input, case=False, na=False)]

# Mostra o resumo
if not cliente_row.empty:
    row = cliente_row.iloc[0]
    st.markdown(resumo_cliente(row), unsafe_allow_html=True)
elif id_cliente_input or razao_social_input:
    st.warning("Cliente não encontrado.")
