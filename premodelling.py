import pandas as pd

df = pd.read_csv('telecom_users.csv')
print(df.head(3))

df= df.drop(["Unnamed: 0","customerID","gender","PaymentMethod",'Contract','PaperlessBilling'],axis =1)
print(df.head(3))
print("\n", df.columns.values,"\n")
    #one technique of filtering out is this:-
trial = (df['Partner'] == 'Yes')
df.loc[trial,'Partner'] = 1
trial = (df['Partner'] =='No')
df.loc[trial,'Partner'] = 0

    #another way of filtering the values:-

df = df.applymap(lambda x: str(x).replace('Yes','1'))
df = df.applymap(lambda x: str(x).replace('No phone service', '-1'))
df = df.applymap(lambda x: str(x).replace('No internet service', '-1'))
df = df.applymap(lambda x: str(x).replace('DSL','1'))
df = df.applymap(lambda x: str(x).replace('Fiber optic','2'))#fiber optic is better than DSL
df = df.applymap(lambda x: str(x).replace('No', '0'))
df = df.applymap(lambda x: str(x).replace(' ', '0'))
df = df.applymap(lambda x: float(x))

df.to_csv('newTelecomData.csv', index=False)
print("\n",df.head(3),"\n")