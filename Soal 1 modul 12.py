import pandas
data = pandas.read_csv('Negara.csv')

df = pandas.DataFrame(data)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()
print(df)
print(f'Rata-ratanya adalah: {mean}')
print(std)