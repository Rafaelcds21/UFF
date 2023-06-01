import pandas as pd

oil_consumption = pd.read_excel("bp-stats-review-2022-all-data.xlsx", sheet_name='Oil - Proved reserves history')

df = pd.DataFrame(oil_consumption).rename(columns={'Unnamed: 1':'1980', 'Unnamed: 2':'1981', 'Unnamed: 3':'1982', 'Unnamed: 4':'1983', 'Unnamed: 5':'1984', 'Unnamed: 6':'1985', 'Unnamed: 7':'1986', 'Unnamed: 8':'1987', 'Unnamed: 9':'1988', 'Unnamed: 10':'1989', 'Unnamed: 11':'1990', 'Unnamed: 12':'1991', 'Unnamed: 13':'1992', 'Unnamed: 14':'1993', 'Unnamed: 15':'1994', 'Unnamed: 16':'1995', 'Unnamed: 17':'1996', 'Unnamed: 18':'1997', 'Unnamed: 19':'1998', 'Unnamed: 20':'1999', 'Unnamed: 21':'2000', 'Unnamed: 22':'2001', 'Unnamed: 23':'2002', 'Unnamed: 24':'2003', 'Unnamed: 25':'2004', 'Unnamed: 26':'2005','Unnamed: 27':'2006','Unnamed: 28':'2007', 'Unnamed: 29':'2008', 'Unnamed: 30':'2009', 'Unnamed: 31':'2010', 'Unnamed: 32':'2011', 'Unnamed: 33':'2012', 'Unnamed: 34':'2013', 'Unnamed: 35':'2014', 'Unnamed: 36':'2015', 'Unnamed: 37':'2016', 'Unnamed: 38':'2017', 'Unnamed: 39':'2018', 'Unnamed: 40':'2019', 'Unnamed: 41':'2020', 'Unnamed: 42':'Growth rate per annum - 2020', 'Unnamed: 43':'Growth rate per annum - 2009-2019', 'Unnamed: 44':'Share - 2020'})
df = df.drop(index=[0,1, 2, 6, 7, 16, 17, 24, 25, 33, 34, 45, 46, 60, 61, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])#, 17, 25, 34, 46, 61, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86])
df = df.reset_index()
df = df.drop('index', axis=1)

df_sem_taxas_de_crescimento = df.drop(['Growth rate per annum - 2020','Growth rate per annum - 2009-2019','Share - 2020'], axis=1)
df_ordenado_decrescente = df_sem_taxas_de_crescimento.sort_values(by=['2020'], ascending=False)

display(df_ordenado_decrescente.head(20).reset_index().drop('index', axis=1))
