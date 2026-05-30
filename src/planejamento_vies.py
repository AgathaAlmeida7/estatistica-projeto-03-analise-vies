import pandas as pd

dados={
    "Pergunta enviesada":[
        "Você acha importante estudar muito todos os dias?",
        "Você concorda que exercicios melhoram totalmente a saude?",
        "Você acredita que pessoas organizadas têm mais sucesso?",
        "Você acha errado não praticar atividades físicas?"
    ],
    "Problema identificado":[
        "Induz resposta positiva",
        "Pergunta tendenciosa",
        "Associação subjetiva",
        "Pressão moral na resposta"
    ],
    "Impacto estatistico":[
        "Pode induzir respostas socialmente aceitas",
        "Compromete a neutralidade  da pesquisa",
        "Gera interpretação subjetiva dos dados",
        "Pressiona emocionalmente o entrevistado"
    ]
    
}

#Perguntas enviesadas influenciam respostas
#Isso compromete a neutralidade estatistica
#Pesquisas precisam ser objetivas e imparciais


#TRANSFORMANDO EM DATAFRAME

df=pd.DataFrame(dados)
#transformando o dicionario em tabela estatistica estruturada
#dataframe é padrao profissional em dados

#MOSTRANDO A TABELA CRIADA

print(df.to_string(index=False))


#EXPORTANDO O DATAFRAME PARA A PASTA: DATA/PROCESSED->dados tratados


df.to_csv(
    "data/processed/analise_vies.csv",
    index=False
)

#df.to_csv()-> transforma o dataframe em arquivo csv

#Exportando a analise estatistica para um arquivo csv
#csv é  um formato padrao utilizado em analise de dados
#isso permite reutilizacao dos dados em outras ferramentas

