import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Currículo", layout="centered")

file_path = "arquivos/fortune1000.xlsx"

pages = st.sidebar.selectbox("Escolha:", [
    "📌 Apresentação",
    "🎓 Formação e Experiência",
    "🎯 Soft e Hard Skills",
    "📈 Apresentação dos Dados",
    "🔎 Análise Inicial dos Dados",
    "📉 Distribuições Probabilísticas"
])

if pages == "📌 Apresentação":
    st.header("Beatriz Silva Pinheiro Rocha")
    st.image("arquivos/foto.jpeg", width=400)
    st.write("São Paulo - SP")
    st.markdown("Visite meu LinkedIn: www.linkedin.com/in/beatriz-sp-rocha")
    st.write(
        "Estudante de Engenharia de Software apaixonada pelo potencial da tecnologia e comprometida em transformar ideias em soluções que impactem positivamente o mundo. Tenho experiência prática em testes de novas versões de aplicativos e produtos, benchmarking, suporte ao cliente e interação com fornecedores internacionais, incluindo a China. "
        "Possuo competências técnicas em Python, HTML, CSS, JavaScript, Design Thinking, Metodologia Scrum, Cisco Packet Tracer e Arquitetura de Redes. "
        "Tenho estado em busca de oportunidades para aplicar e expandir meus conhecimentos, especialmente em análise de dados e metodologias ágeis. Sempre disponível para novos aprendizados e desafios. "
        "Estou motivada e pronta para contribuir com as empresas na criação de soluções inovadoras e no desenvolvimento de projeto que tragam impacto positivo para o mercado e para a sociedade."
    )

elif pages == "🎓 Formação e Experiência":
    st.title("Histórico Profissional")
    st.markdown(
        """
        Assistente Administrativo: 02/2022 - 05/2023. \n
        Multilaser Industrial S.A. - Extrema - MG. \n 
        - Testes de novas versões de aplicativos (GPS, drone, rádio, smartwatch, mini impressora, caixa de som); 
        - Benchmarking de aplicativos e produtos (drones, smartwatchs e caixas de som); 
        - Interação e suporte ao cliente para esclarecimento de dúvidas; 
        - Contato com a China para esclarecimento de dúvidas em relação ao produto.
        """, unsafe_allow_html=True
    )
    st.markdown("<hr>", unsafe_allow_html=True)
    st.title("Formação Acadêmica")
    st.markdown(
        """
        Bacharelado em Engenharia de Software: 08/2023 - 07/2027 \n
        Faculdade de Informática e Administração Paulista (FIAP): São Paulo, SP
        """
    )
    st.markdown("<hr>", unsafe_allow_html=True)
    st.title("Idiomas")
    st.markdown(
        """
        Inglês - Avançado; \n
        Imersão de 4 semanas em inglês avançado, com foco em comunicação profissional e cultural, NESE - Boston/USA (Julho 2024)
        """
    )

elif pages == "🎯 Soft e Hard Skills":
    st.title("Soft Skills")
    st.markdown(
        """
        - Boa comunicação oral e escrita; 
        - Criatividade; 
        - Colaboração e trabalho em equipe; 
        - Organização; 
        - Capacidade de planejamento; 
        - Organização para o cumprimento de prazos; 
        - Determinação e persistência para o alcance de metas; 
        - Produtividade. 
        """
    )
    st.markdown("<hr>", unsafe_allow_html=True)
    st.title("Hard Skills")
    st.markdown(
        """
        **Front-End:**
        - HTML; 
        - CSS; 
        - JavaScript; 
        - SASS. 

        **Back-End:**
        - Java; 
        - Python; 
        - SQL. 

        **Outros:** 
        - Ferramenta de Design (Figma); 
        - Design Thinking; 
        - Metodologia Scrum; 
        - Design Thinking; 
        - Metodologia Scrum.
        """
    )

elif pages == "📈 Apresentação dos Dados":
    st.title("As 1000 Maiores Empresas do Mundo")

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown(
        """
        **Explicação sobre o conjunto de dados utilizado:** \n
        Resolvi utilizar esse dataset a fim de mostrar as empresas com o maior número de funcionários. O dataset foi pego em um github público.
        """
    )

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown(
        """
        **Perguntas:**
        - Qual a probabilidade de uma empresa ter um lucro acima de 7 bilhões?
        - Em quais cenários seria mais adequado usar a distribuição binomial em vez da normal?
        - Qual a probabilidade de exatamente 5 delas serem lucrativas?
        """
    )

    st.markdown("<hr>", unsafe_allow_html=True)

    df = pd.read_excel(file_path, engine="openpyxl")
    st.write(df)

    st.markdown(
        """
        **Identificação do tipo de variáveis:**
        - **Rank:** Ordinal;
        - **Company:** Nominal;
        - **Sector:** Nominal;
        - **Industry:** Nominal;
        - **Revenue:** Ordinal;
        - **Profits:** Contínua;
        - **Employees:** Discreta.
        """
    )

elif pages == "🔎 Análise Inicial dos Dados":

    df = pd.read_excel(file_path, engine="openpyxl")

    st.subheader("Média")
    # --- EXPLICAÇÃO ---
    st.markdown(
        """
        A média é calculada somando todos os valores e dividindo o resultado pelo número total de elementos. Com base nisso, podemos concluir que as empresas possuem aproximadamente:
        - **Receita (Revenue)** de $48.213 milhões;
        - **Lucro (Profits)** de $2.409 milhões;
        - **Número de Funcionários (Employees)** de 86.000.
        """
    )
    if isinstance(df.iloc[0, 0], str) and "," in df.iloc[0, 0]:  
        st.write("Os dados parecem estar mal formatados. Corrigindo...")
        df = df.iloc[:, 0].str.split(",", expand=True)
        df.columns = df.iloc[0]
        df = df[1:].reset_index(drop=True)
    numeric_columns = ["Revenue", "Profits", "Employees"]
    existing_numeric_cols = [col for col in numeric_columns if col in df.columns]
    for col in existing_numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    mean_values = df[existing_numeric_cols].mean()
    grafico, media = plt.subplots()
    mean_values.plot(kind="bar", ax=media, color=["yellow", "red", "blue"])
    media.set_title("Média")
    media.set_ylabel("Valor médio")
    media.set_xlabel("Variáveis")
    st.pyplot(grafico)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.subheader("Mediana")
    # --- EXPLICAÇÃO ---
    st.markdown(
        """
        A mediana é o valor que está no meio dos dados ordenados. Com isso, concluimos que:
        - **Receita (Revenue)** de $28.118 milhões;
        - **Lucro (Profits)** de $1 milhão;
        - **Número de Funcionários (Employees)** de 26.000. 
        """
    )
    median_values = df[existing_numeric_cols].median()
    grafico2, mediana = plt.subplots()
    median_values.plot(kind="bar", ax=mediana, color=["green", "blue", "purple"])
    mediana.set_title("Mediana")
    mediana.set_ylabel("Valor da mediana")
    mediana.set_xlabel("Variáveis")
    st.pyplot(grafico2)
    
    st.markdown("<hr>", unsafe_allow_html=True)

    st.subheader("Moda")
    # --- EXPLICAÇÃO ---
    st.markdown(
        """
        A moda é o valor que aparece com mais frequência nos dados. Com isso, podemos concluir que a moda possui os mesmo valores que a mediana:
        - **Receita (Revenue)** de $28.118 milhões;
        - **Lucro (Profits)** de $1 milhão;
        - **Número de Funcionários (Employees)** de 26.000.
        """
    )
    mode_values = df[existing_numeric_cols].mode().iloc[0]
    grafico3, moda = plt.subplots()
    mode_values.plot(kind="bar", ax=moda, color=["orange", "pink", "cyan"])
    moda.set_title("Moda")
    moda.set_ylabel("Valor da moda")
    moda.set_xlabel("Variáveis")
    st.pyplot(grafico3)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.subheader("Desvio Padrão e Variância")

    std_values = df[existing_numeric_cols].std()
    var_values = df[existing_numeric_cols].var()

    # --- EXPLICAÇÃO ---
    st.markdown(
        """
        O desvio padrão mede a dispersão padrão e a dispersão dos dados. Com isso, pode ser observado que:
        - **Receita (Revenue)** de $60 milhões;
        - **Lucro (Profits)** de $5 milhões;
        - **Número de Funcionários (Employees)** de 120.000.
        """
    )
    grafico4, desvio = plt.subplots()
    std_values.plot(kind="bar", ax=desvio, color=["yellow", "purple", "orange"])
    desvio.set_title("Desvio Padrão")
    desvio.set_ylabel("Valor do Desvio Padrão")
    desvio.set_xlabel("Variáveis")
    st.pyplot(grafico4)

    # --- EXPLICAÇÃO ---
    st.markdown(
        """
        A variância é o quadrado do desvio padrão, e é que nem o desvio padrão que mede a dispersão dos dados. Com isso, é possível apresentar:
        - **Receita (Revenue)** de $3,6 bilhões;
        - **Lucro (Profits)** de $25 milhões;
        - **Número de Funcionários (Employees)** de 14,4 milhões.
        """
    )
    grafico5, variancia = plt.subplots()
    var_values.plot(kind="bar", ax=variancia, color=["magenta", "red", "blue"])
    variancia.set_title("Variância")
    variancia.set_ylabel("Valor da Variância")
    variancia.set_xlabel("Variáveis")
    st.pyplot(grafico5)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.subheader("Identificação de Possíveis Correlações Entre Variáveis")
    # --- EXPLICAÇÃO ---
    st.markdown(
        """
        A matriz de correlação mostra a relação linear entre as variáveis. Com isso, é possível termos os seguintes resultados:
        - **Revenue e Profits** 0.75, onde empresas com maior receita possuem maiores lucros;
        - **Revenue e Employess** 0.6, empresas com maior receitas possuem mais funcionários;
        - **Profits e Employees** 0.45, empresas com maiores lucros possuem mais funcionários.
        """
    )
    for col in existing_numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    correlation_matrix = df[existing_numeric_cols].corr()
    grafico6, correlacao = plt.subplots(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=correlacao, vmin=-1, vmax=1)
    correlacao.set_title("Matriz de Correlação")
    st.pyplot(grafico6)

elif pages == "📉 Distribuições Probabilísticas":  
    df = pd.read_excel(file_path, engine="openpyxl")
    st.title("📉 Análise Estatística: Distribuições Normal e Binomial")
    limite_lucro = 10_000
    df["Employees"] = pd.to_numeric(df["Employees"], errors="coerce").fillna(0)
    df["Profits"] = pd.to_numeric(df["Profits"], errors="coerce").fillna(0)
    df["n"] = df["Employees"]
    df["k"] = df.apply(lambda row: row["Employees"] if row["Profits"] > limite_lucro else 0, axis=1) 
    df["p"] = np.where(df["n"] > 0, df["k"] / df["n"], 0)

    # --- ANÁLISE DA DISTRIBUIÇÃO BINOMIAL ---
    st.subheader("📊 Análise da Distribuição Binomial")
    st.latex(r"P(X = k) = \binom{n}{k} p^k (1 - p)^{n-k}")
    if "Company" in df.columns:
        df = pd.read_excel(file_path, engine="openpyxl")
    numeric_columns = ["Revenue", "Profits", "Employees"]
    existing_numeric_cols = [col for col in numeric_columns if col in df.columns]
    for col in existing_numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    n = 10 
    p = 0.5  
    for col in existing_numeric_cols:
        media_col = df[col].mean()
        binomial = np.random.binomial(n, p, 1000)
    grafico7, distribuicao_binomial = plt.subplots()
    distribuicao_binomial.hist(binomial, bins=10, density=True, alpha=0.6, color="blue")
    distribuicao_binomial.set_title(f"Distribuição Binomial - {col}")
    distribuicao_binomial.set_ylabel("Frequência")
    distribuicao_binomial.set_xlabel("Número de Sucessos")
    st.pyplot(grafico7)
    # --- EXPLICAÇÃO ---
    st.subheader("Explicação:")
    st.write(
        """
        A **distribuição binomial** é usada para modelar situações onde temos um número fixo de tentativa, tendo apenas sucesso e fracasso como resultados. Com isso nisso, podemos observar que 
        o **Revenue** e **Profits** possuem uma distribuição normal com certa dispersão, e a **quantidade de Employees** pode seguir padrões diferentes dependendo da variabilidade dos dados.
        """
    )

    st.markdown("<hr>", unsafe_allow_html=True)

    # --- ANÁLISE DA DISTRUIBUIÇÃO NORMAL ---
    st.subheader("📊 Análise da Distribuição Normal")
    st.latex(r"f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}")
    variavel = st.selectbox("Escolha a variável:", ["Revenue", "Profits", "Employees"])
    media = df[variavel].mean()
    desvio_padrao = df[variavel].std()
    st.write(f"**Média ({variavel}):** {media:.2f}")
    st.write(f"**Desvio Padrão ({variavel}):** {desvio_padrao:.2f}")
    x = np.linspace(media - 4 * desvio_padrao, media + 4 * desvio_padrao, 1000)
    y = stats.norm.pdf(x, media, desvio_padrao)
    grafico8, distribuicao_normal = plt.subplots()
    distribuicao_normal.plot(x, y, color="orange", label="Distribuição Normal")
    distribuicao_normal.axvline(media, color="red", linestyle="--", label="Média")
    distribuicao_normal.fill_between(x, y, alpha=0.3, color="blue")
    distribuicao_normal.set_title(f"Distribuição Normal de {variavel}")
    distribuicao_normal.set_xlabel(variavel)
    distribuicao_normal.set_ylabel("Densidade de Probabilidade")
    distribuicao_normal.legend()
    st.pyplot(grafico8)
    # --- EXPLICAÇÃO ---
    st.subheader("Explicação:")
    st.write(
        """
        - A **distribuição normal** é uma distribuição que descreve o comportamento aleatório de fenômenos naturais, mostrando que as mesmas seguem um padrão típico. O pico da curva representa a média dos dados, e a forma simétrica indica que a maioria dos valores está concentrada em torno dessa média.   
        - No gráfico, como no caso do **Revenue**, a curva mostra que a maioria das empresas possui receitas próximas à média, enquanto poucas apresentam valores extremamente altos ou baixos."Revenue", a curva mostra que a maioria das empresas tem receitas próximas à média, enquanto poucas empresas têm receitas extremamente altas ou baixas.
        """
        f"A variável **{variavel}** segue aproximadamente uma distribuição normal, com uma média de **{media:.2f}** e desvio padrão de **{desvio_padrao:.2f}**. Indicando que a maior parte dos dados se encontra dentro de uma a duas vezes o desvio padrão em relação à média.  "
    )