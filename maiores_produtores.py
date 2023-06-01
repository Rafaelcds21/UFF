import pandas as pd

oil_consumption = pd.read_excel("bp-stats-review-2022-all-data.xlsx", sheet_name='Oil Consumption - Barrels')

df = pd.DataFrame(oil_consumption).rename(columns={'Oil: Trade movements':'Thousand barrels daily', 'Unnamed: 1':'1965', 'Unnamed: 2':'1966', 'Unnamed: 3':'1967', 'Unnamed: 4':'1968', 'Unnamed: 5':'1969', 'Unnamed: 6':'1970', 'Unnamed: 7':'1971', 'Unnamed: 8':'1972', 'Unnamed: 9':'1973', 'Unnamed: 10':'1974', 'Unnamed: 11':'1975', 'Unnamed: 12':'1976', 'Unnamed: 13':'1977', 'Unnamed: 14':'1978', 'Unnamed: 15':'1979', 'Unnamed: 16':'1980', 'Unnamed: 17':'1981', 'Unnamed: 18':'1982', 'Unnamed: 19':'1983', 'Unnamed: 20':'1984', 'Unnamed: 21':'1985', 'Unnamed: 22':'1986', 'Unnamed: 23':'1987', 'Unnamed: 24':'1988', 'Unnamed: 25':'1989', 'Unnamed: 26':'1990','Unnamed: 27':'1991','Unnamed: 28':'1992', 'Unnamed: 29':'1993', 'Unnamed: 30':'1994', 'Unnamed: 31':'1995', 'Unnamed: 32':'1996', 'Unnamed: 33':'1997', 'Unnamed: 34':'1998', 'Unnamed: 35':'1999', 'Unnamed: 36':'2000', 'Unnamed: 37':'2001', 'Unnamed: 38':'2002', 'Unnamed: 39':'2003', 'Unnamed: 40':'2004', 'Unnamed: 41':'2005', 'Unnamed: 42':'2006', 'Unnamed: 43':'2007', 'Unnamed: 44':'2008', 'Unnamed: 45':'2009', 'Unnamed: 46':'2010', 'Unnamed: 47':'2011', 'Unnamed: 48':'2012', 'Unnamed: 49':'2013', 'Unnamed: 50':'2014', 'Unnamed: 51':'2015', 'Unnamed: 52':'2016', 'Unnamed: 53':'2017', 'Unnamed: 54':'2018', 'Unnamed: 55':'2019', 'Unnamed: 56':'2020', 'Unnamed: 57':'2021', 'Unnamed: 58':'Growth rate per annum - 2021', 'Unnamed: 59':'Growth rate per annum - 2011-2021', 'Unnamed: 60':'Share - 2021'})
df = df.drop(index=[0, 1, 2, 6, 7, 19, 20, 55, 56, 65, 66, 76, 77, 87, 88, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120])
df = df.reset_index()
df = df.drop('index', axis=1)

df_sem_taxas_de_crescimento = df.drop(['Growth rate per annum - 2021','Growth rate per annum - 2011-2021','Share - 2021'], axis=1)
df_ordenado_decrescente = df_sem_taxas_de_crescimento.sort_values(by=['2021'], ascending=False)

display(df_ordenado_decrescente.head(20).reset_index().drop('index', axis=1))
