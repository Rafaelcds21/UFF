import pandas as pd
import matplotlib.pyplot as plt

preco_do_petroleo = pd.read_excel(r'"C:\Users\campo\Downloads\bp-stats-review-2022-all-data.xlsx"', sheet_name='Oil - Spot crude prices')
df_bruto = pd.DataFrame(preco_do_petroleo)
df_renomeado = df_bruto.rename(columns={'Oil: Spot crude prices': 'US dollars per barrels', 'Unnamed: 1': 'Dubai $/bbl *', 'Unnamed: 2': 'Brent $/bbl †', 'Unnamed: 3': 'Nigerian Forcados $/bbl', 'Unnamed: 4': 'West Texas Intermediate $/bbl ‡'})
df_sem_valores_nan = df_renomeado.drop(index=[0, 1, 2, 3, 54, 55, 56, 57])
df_sem_colunas_extras = df_sem_valores_nan.drop(['Unnamed: 5','Unnamed: 6','Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Contents'], axis=1)
df_final = df_sem_colunas_extras.replace('-', -1)

plt.plot()

plt.plot(df_final['US dollars per barrels'], df_final[['Dubai $/bbl *', 'Brent $/bbl †', 'Nigerian Forcados $/bbl', 'West Texas Intermediate $/bbl ‡']])
plt.grid()
plt.legend(df_final[['Dubai $/bbl *', 'Brent $/bbl †', 'Nigerian Forcados $/bbl', 'West Texas Intermediate $/bbl ‡']])

plt.show()
plt.savefig('Produção_de_petróleo.png', format='png')
