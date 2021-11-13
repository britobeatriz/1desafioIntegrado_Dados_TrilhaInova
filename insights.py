# -*- coding: utf-8 -*-
"""Desafio Integrado I.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p66Jw-VYn9cgCcwvVV4XA_ybMpYuwZKr

# Importando bibliotecas
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ranksums 
# %matplotlib inline

"""# Acessando dados"""

estadual = pd.read_csv('dados_rede_estadual.csv')

privada = pd.read_csv('dados_rede_privada.csv')

publica = pd.read_csv('dados_rede_publica.csv')

todos = pd.read_csv('dados_todas_as_redes.csv')

"""# Visualização Matrículas

## Selecionando o indicador 'Matrículas'
"""

total_estadual = estadual.loc[0]
total_privada = privada.loc[0]
total_municipal = publica.loc[0]

df1 = pd.DataFrame(total_estadual)
df2 = pd.DataFrame(total_privada)
df3 = pd.DataFrame(total_municipal)

frames = [df1, df2, df3]

resultado_1 = pd.concat(frames)

resultado_1.reset_index(level=0, inplace=True)

resultado_1 = resultado_1.drop(resultado_1.index[[0, 1, 4, 5, 8, 9]])

resultado_1 = resultado_1.rename(columns={0:'Valores', 'index':'Tipo_escola'})

resultado_1['Valores'] = resultado_1['Valores'].astype(int)

"""## Plotando os gráficos"""

ax = plt.figure(figsize=(12, 6))
fig_1 = sns.barplot(x='Tipo_escola', y='Valores', data=resultado_1.sort_values('Valores', ascending=False), ci=False)
for i in fig_1.patches:
  fig_1.annotate(i.get_height(), (i.get_x() + i.get_width() / 2, i.get_height())
  , ha='center', va='baseline', fontsize=12, color='black', xytext=(0,1), 
  textcoords='offset points')
fig_1.set_title('Total de inscritos', fontsize= 18)
ax=ax

fig_1.get_figure().savefig('Figura_1.png')

"""# Visualização distorção idade-série"""

dist_estadual = estadual.loc[1]
dist_municipal = publica.loc[1]
dist_privada = privada.loc[1]

df4 = pd.DataFrame(dist_estadual)
df5 = pd.DataFrame(dist_municipal)
df6 = pd.DataFrame(dist_privada)

frames_1 = [df4, df5, df6]
resultado_2 = pd.concat(frames_1)
resultado_2.reset_index(level=0, inplace=True)

resultado_2 = resultado_2.drop(resultado_2.index[[0, 1, 4, 5, 8, 9]])

resultado_2 = resultado_2.rename(columns={1:'Valores(%)', 'index':'Tipo_escola'})

def troca_sinal(num):
  num = num.replace('%','').replace(',','.')
  return num

resultado_2['Valores(%)'] = resultado_2['Valores(%)'].apply(troca_sinal)

resultado_2['Valores(%)'] = resultado_2['Valores(%)'].astype(float)

resultado_2.info()

"""## Plotando os gráficos"""

ax = plt.figure(figsize=(12, 6))
fig_2 = sns.barplot(x='Tipo_escola', y='Valores(%)', data=resultado_2.sort_values('Valores(%)', ascending=False), ci=False)
for i in fig_2.patches:
  fig_2.annotate(i.get_height(), (i.get_x() + i.get_width() / 2, i.get_height())
  , ha='center', va='baseline', fontsize=12, color='black', xytext=(0,1), 
  textcoords='offset points')
fig_2.set_title('Distorção Idade-Serie', fontsize= 18)
ax=ax

fig_2.get_figure().savefig('Figura_2.png')



"""# AFD (Adequação da formação docente) total"""

afd_estadual = estadual.loc[5]
afd_municipal = publica.loc[5]
afd_privada = privada.loc[5]

df7 = pd.DataFrame(afd_estadual)
df8 = pd.DataFrame(afd_municipal)
df9 = pd.DataFrame(afd_privada)

frames_2 = [df7, df8, df9]
resultado_3 = pd.concat(frames_2)
resultado_3.reset_index(level=0, inplace=True)

resultado_3 = resultado_3.drop(resultado_3.index[[0, 1, 4, 5, 8, 9]])

resultado_3 = resultado_3.rename(columns={5:'Valores(%)', 'index':'Tipo_escola'})
resultado_3['Valores(%)'] = resultado_3['Valores(%)'].apply(troca_sinal)
resultado_3['Valores(%)'] = resultado_3['Valores(%)'].astype(float)
resultado_3 = resultado_3.reset_index()
resultado_3

"""## Plotando os gráficos"""

ax = plt.figure(figsize=(12, 6))
fig_3 = sns.barplot(x='Tipo_escola', y='Valores(%)', data=resultado_3.sort_values('Valores(%)', ascending=False), ci=False)
for i in fig_3.patches:
  fig_3.annotate(i.get_height(), (i.get_x() + i.get_width() / 2, i.get_height())
  , ha='center', va='baseline', fontsize=12, color='black', xytext=(0,1), 
  textcoords='offset points')
fig_3.set_title('AFD Total', fontsize= 18)
ax=ax

fig_3.get_figure().savefig('Figura_3.png')

"""# Escolas com acesso a internet

## Para o Ensino
"""

internet_estadual = estadual.loc[19]
internet_municipal = publica.loc[16]
internet_privada = privada.loc[18]

df10 = pd.DataFrame(internet_estadual)
df11 = pd.DataFrame(internet_municipal)
df12 = pd.DataFrame(internet_privada)
df10 = df10.rename(columns={19:'Valores(%)'})
df11 = df11.rename(columns={16:'Valores(%)'})
df12 = df12.rename(columns={18:'Valores(%)'})

frames_3 = [df10, df11, df12]
resultado_4 = pd.concat(frames_3)
resultado_4.reset_index(level=0, inplace=True)
resultado_4 = resultado_4.drop(resultado_4.index[[0, 1, 4, 5, 8, 9]])

resultado_4

resultado_4 = resultado_4.rename(columns={'index':'Tipo_escola'})
resultado_4['Valores(%)'] = resultado_4['Valores(%)'].apply(troca_sinal)
resultado_4['Valores(%)'] = resultado_4['Valores(%)'].astype(float)
resultado_4 = resultado_4.reset_index()
resultado_4

ax = plt.figure(figsize=(12, 6))
fig_4 = sns.barplot(x='Tipo_escola', y='Valores(%)', data=resultado_4.sort_values('Valores(%)', ascending=False), ci=False)
for i in fig_4.patches:
  fig_4.annotate(i.get_height(), (i.get_x() + i.get_width() / 2, i.get_height())
  , ha='center', va='baseline', fontsize=12, color='black', xytext=(0,1), 
  textcoords='offset points')
fig_4.set_title('Escolas com acesso a internet', fontsize= 18)
ax=ax

fig_4.get_figure().savefig('Figura_4.png')

"""## Para os Alunos"""

aluno_estadual = estadual.loc[21]
aluno_municipal = publica.loc[18]
aluno_privada = privada.loc[20]

df13 = pd.DataFrame(internet_estadual)
df14 = pd.DataFrame(internet_municipal)
df15 = pd.DataFrame(internet_privada)
df13 = df13.rename(columns={21:'Valores(%)'})
df14 = df14.rename(columns={18:'Valores(%)'})
df15 = df15.rename(columns={20:'Valores(%)'})

df13

frames_4 = [df13, df14, df15]
resultado_5 = pd.concat(frames_4)
resultado_5.reset_index(level=0, inplace=True)
resultado_5 = resultado_5.drop(resultado_5.index[[0, 1, 4, 5, 8, 9]])

resultado_5 = resultado_5.rename(columns={'index':'Tipo_escola'})
resultado_5['Valores(%)'] = resultado_5['Valores(%)'].apply(troca_sinal)
resultado_5['Valores(%)'] = resultado_5['Valores(%)'].astype(float)
resultado_5 = resultado_5.reset_index()
resultado_5

ax = plt.figure(figsize=(12, 6))
fig_5 = sns.barplot(x='Tipo_escola', y='Valores(%)', data=resultado_5.sort_values('Valores(%)', ascending=False), ci=False)
for i in fig_5.patches:
  fig_5.annotate(i.get_height(), (i.get_x() + i.get_width() / 2, i.get_height())
  , ha='center', va='baseline', fontsize=12, color='black', xytext=(0,1), 
  textcoords='offset points')
fig_5.set_title('Escolas com acesso a internet para os alunos', fontsize= 18)
ax=ax

fig_5.get_figure().savefig('Figura_5.png')

"""# Ensino"""



"""## Multímídia """



"""## PC/Tablet

# Teste de Hipótese

## H<sup>null</sup>
**Estudantes de escolas particulares não têm menor distorção idade-série**

## H<sup>alt</sup>
**Estudantes de escolas particulares não têm menor distorção idade-série**
"""

resultado_2

"""## H<sup>null</sup>
**Escolas com maiores AFD têm menor distorção idade série**

## H<sup>alt</sup>
**Escolas com maiores AFD não têm menor distorção idade série**

"""

