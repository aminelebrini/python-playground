import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

data_csv = pd.read_csv("project1_df.csv")

df = pd.DataFrame(data_csv)

print("Nombre de lignes :", df.shape[0])
print("Nombre de colonnes :", df.shape[1])

print("------<<data frame after drop null values and nan>>------")
print(df.isnull().sum())

# print("\n<<analysis of Product Category>>")

# pg_count = df["Product Category"].value_counts()
# print(pg_count)

# print("\n<<analysis of Purchase Method>>")

# pm_count = df["Purchase Method"].value_counts()
# print(pm_count)

# print("\n<<avrage amount of Transactions>>")

# amm = df["Net Amount"].mean()
# print(amm)

# print("\n<<total of n Transactions>>")

# n_t = df["Net Amount"].value_counts()

# print("\n<<total amount>>")

# amt = df["Net Amount"].sum()
# print(amt)

# print("\n<<avrage of Discount Amount (INR)>>")

# ada = df["Discount Amount (INR)"].mean()
# print(ada)

# print("\n<<number of transaction per category>>")

# n_tc = df["Product Category"].value_counts()
# print(n_tc)

# print("\n<<seles per category>>")

# sales_percategory = df.groupby("Product Category")["Net Amount"].sum()
# print(sales_percategory)

# print("\n<<avrage sales per category>>")
# avrage_sales_per_category = df.groupby("Product Category")["Net Amount"].mean()
# print(avrage_sales_per_category)


# #data Visualisation With Matplotlib

# #using countplot

# plt.figure(figsize=(8, 5))

# sbn.countplot(data=df, x="Purchase Method")

# plt.xlabel("Purchase Method")
# plt.ylabel("Number of Transactions")
# plt.xticks(rotation=45)

# plt.tight_layout()
# plt.savefig("countplot.png", dpi=300, bbox_inches="tight")
# plt.show()

# #using boxplot

# sbn.boxplot(data=df, x="Gender", y="Net Amount")
# plt.xlabel("Genre")
# plt.ylabel("Transacation")
# plt.tight_layout()
# plt.savefig("boxplot_1.png", dpi=300, bbox_inches="tight")
# plt.show()

# sbn.boxplot(data=df, x="Product Category", y="Net Amount")
# plt.xlabel("Genre")
# plt.ylabel("Transacation")
# plt.tight_layout()
# plt.savefig("boxplot_2.png", dpi=300, bbox_inches="tight")
# plt.show()

# #using scatterplot


# sbn.scatterplot(data=df, x="Gross Amount", y="Discount Amount")
# plt.xlabel("")
