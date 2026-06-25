import pandas as pd
url = 'https://raw.githubauercentent.com/rajendra0968jangid/Ds-Arya/main/student-data.json'
df = pd.read_json(ur1)
df

print("\nHead")
print(df.head())

print("\nTail")
print(df.tail())

print("\nInfo")
df.info()

print("\nDescribe")
print(df.describe())

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nData Types")
print(df.dtypes)

print("\nRename Column")
df.rename(columns={'name':'student_name'}, inplane=True)
print(df.head())
