<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=FCC009&height=180&section=header&animation=twinkling"/>

# 📊 BNDES Data Analytics  

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)   ![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-yellow?logo=pandas)  ![Plotly](https://img.shields.io/badge/Plotly-Visualização-orange?logo=plotly)  ![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)  ![Google Sheets](https://img.shields.io/badge/Google_Sheets-Dados-green?logo=googlesheets)  ![Looker Studio](https://img.shields.io/badge/Looker_Studio-Dashboard-blue?logo=looker)  ![Git](https://img.shields.io/badge/Git-Version_Control-lightgrey?logo=git)  

![License](https://img.shields.io/badge/license-MIT-green)

**Autor:** Gustavo Thyerris Nascimento Oliveira  
**Email:** gusthyerris@gmail.com  
**LinkedIn:** [https://www.linkedin.com/in/gustavo-thyerris/](https://www.linkedin.com/in/gustavo-thyerris/)  
**Celular:** +55 (11) 95655-1862  

## 🔹 Sobre o Projeto

Este projeto implementa um **pipeline de análise de dados** para explorar investimentos do **BNDES (Banco Nacional de Desenvolvimento Econômico e Social)**.  

O fluxo vai desde a **coleta e tratamento de dados (ETL)** até a criação de um **dashboard interativo** em **Streamlit**, permitindo identificar **insights estratégicos** como priorização setorial, distribuição regional e principais clientes beneficiados.  

## 🚀 Funcionalidades  
- **ETL completo**: extração, limpeza e transformação de dados em CSV/Excel.  
- **Filtros interativos**: seleção dinâmica de ano, setor e estado (UF).  
- **Visualizações ricas** com Plotly:  
  - Gráfico de barras → investimentos por setor.  
  - Linha temporal → evolução de investimentos por ano.  
  - Mapa coroplético → distribuição de investimentos por estados.  
- **Testes automatizados** para validar pipeline e gráficos.  
- **Dashboard intuitivo** em Streamlit.  

---

## 🗂️ Estrutura do Projeto  

```
├── data
│   └── bndes.csv              # Base de dados bruta
├── src
│   ├── data_loader.py         # Funções para carregar dados
│   ├── preprocess.py          # Limpeza e transformação (ETL)
│   ├── utils.py               # Funções auxiliares
│   └── visuals.py             # Gráficos com Plotly
├── tests
│   └── test_pipeline.py       # Testes de integração e gráficos
├── app.py                     # Aplicação principal em Streamlit
├── requirements.txt           # Dependências do projeto
└── README.md                  # Documentação
```

---

## ⚙️ Instalação  

Clone o repositório e instale as dependências:  

```bash
git clone https://github.com/seuusuario/bndes-data-analytics.git
cd bndes-data-analytics
pip install -r requirements.txt
```

---

## ▶️ Execução  

Inicie a aplicação Streamlit:  

```bash
streamlit run app.py
```

Acesse em [http://localhost:8501](http://localhost:8501).  

---

## ✅ Testes  

Para rodar os testes de pipeline e visualização:  

```bash
python -m tests.test_pipeline
```

---

## 💡 Exemplos de Insights  

- **Setores prioritários**: Indústria e Infraestrutura concentram maior volume de investimentos.  
- **Distribuição regional**: estados como MG, PR e PE aparecem em destaque, apontando oportunidades de balanceamento.  
- **Gestão de clientes**: identificação dos maiores beneficiários para acompanhamento estratégico.  

---

## 🛠️ Tecnologias  
- **Python** (Pandas, Plotly, Streamlit)  
- **Google Sheets & Looker Studio** (para dashboard exploratório inicial)  
- **Testes unitários** em Python  

---

## 📌 Próximos Passos  
- Integrar dados reais diretamente da API do BNDES (quando disponível).  
- Expandir visualizações (ex.: dispersão por cliente, séries preditivas).  
- Publicar aplicação em **Streamlit Cloud** ou **Heroku**.  

---

## 👨‍💻 Autor  
Desenvolvido por *Gustavo Thyerris* – apaixonado por transformar **dados em insights estratégicos** para impacto econômico e social.  
