import pandas as pd
from statistics import mean
import seaborn as sns
import matplotlib.pyplot as plt
## assignment1
df = pd.read_csv("./LAKE/data.csv")
print(df.head(5))




## assignment2.1
female_customer = df[df['Gender']=="Female"]
Male_customer = df[df['Gender']=="Male"]

print("Average Age of Female Customer: {}".format(mean(female_customer['Age'])))
print("Average Age of Male Customer: {}".format(mean(Male_customer['Age'])))

rows = len(df.index)
print("Rows of the dataframe is : {}".format(rows))
columns = len(df.columns)
print("Columns of the dataframe is : {}".format(columns))



## assignmnt 3
## total purchage amount

TPA = sum(df['PurchaseAmount'])
print("Total Purchage amount is : {}".format(TPA))


product_sales = df.groupby(['ProductID'])['PurchaseAmount'].sum()
print(product_sales)
most_pur_product = product_sales.idxmax()
most_pur_product_sales = product_sales.max()
df2 = {
    "product":float(most_pur_product),
    "sales": float(most_pur_product_sales)
}
print(df2)

def age_group(age):
    if age>=18 and age <=25:
        return "18-25"
    elif age>=26 and age <=35:
        return "26-35"
    elif age>=36 and age <=45:
        return "36-45"
    else:
        return "Unknown"

df["Category"] = df['Age'].apply(age_group)

print(df)

sns.countplot(x='Category', hue='Gender', data=df, palette='coolwarm')
plt.title("Age Groups by Gender")
plt.xlabel("Age Group")
plt.ylabel("Count")
plt.legend(title="Gender")
plt.show()
plt.savefig("age_groups_by_gender.png", dpi=300, bbox_inches='tight') 