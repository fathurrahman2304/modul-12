import pandas as pd
data = pd.read_csv('Negara.csv')

df = pd.DataFrame(data)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()
mean.to_csv('NegaraMean.csv')
std.to_csv('NegaraStandarDeviasi.csv')

print(df)
print(mean)
print(std)