import pandas as pd
import numpy as np

np.random.seed(42)


cgpa = np.round(np.random.uniform(6.0, 10.0, 1000), 2)

# for genrate package
noise = np.random.normal(0, 1.0, 1000)
package = np.round(cgpa * 1.5 + noise, 2)
package = np.clip(package, 2.0, 30.0)  

# Create DataFrame
df = pd.DataFrame({
    "CGPA": cgpa,
    "Package (LPA)": package
})

df.head(1000)

df.isnull()

x =df[["CGPA"]]
y=df["Package (LPA)"]

import seaborn as sns
import matplotlib as plt
from sklearn.model_selection import train_test_split

sns.scatterplot(x="CGPA",y="Package (LPA)",data=df)

 x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.25,random_state=30)

  karthik.fit(x_train,y_train)

karthik.predict([[7.9]])
