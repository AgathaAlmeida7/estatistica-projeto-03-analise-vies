#modulo de correção metodologica da pesquisa
import pandas as pd

#comparando pergunta rumi e pergunta corrigida

dados={
    "Pergunta enviesada":[
        "Você acha importante estudar muito todos os dias?",
        "Você concorda que exercicios melhoram totalmente a saude?",
        "Você acredita que pessoas organizadas têm mais sucesso?",
        "Você acha errado não praticar atividades físicas?"
    
    ],
    "Pergunta corrigida":[
        "Quantas horas você estuda por dia?",
        "Com que frequencia voce pratica exercicios fisicos?",
        "Quais fatores voce considera importantes para o sucesso profissional?",
        "Voce pratica atividades fisicas regularmente"
    ],
    "Melhoria metodologica":[
        "Remove inducao e julgamento de valor",
        "Reduz tendenciosidade da pergunta",
        "Evita associacoes subjetivas",
        "Remove pressao emocional sobre o entrevistado"
    ]

}

#Perguntas corrigidas buscam neutralidade estatistica
#O objetivo e reduzir influencia sobre o entrevistado
#Perguntas neutras produzem dados mais confiaveis

# Perguntas neutras ajudam a produzir dados mais confiaveis
# Reduzir vies melhora a qualidade estatistica da pesquisa
# perguntas imparciais diminuem distorcoes nas respostas



#CRIANDO O DATAFRAME DESSE DICIONARIO

df=pd.DataFrame(dados)

#MOSTRANDO ESSA TABELA

print(df.to_string(index=False))

df.to_csv(
    "data/processed/correcao_vies.csv",
    index=False
)

# Exportando a analise corrigida para csv
# csv e um formato padrao em analise de dados
# isso permite reutilizacao da analise em outras ferramentas
