import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

filename = 'mushrooms/agaricus-lepiota.data.txt'
df = pd.read_table(filename, sep=',', header=None)

# Convert to numeric values
for col in df.columns:
    df[col] = df[col].replace(dict(zip(df[col].unique(),
                              range(len(df[col].unique())))))
# Assign positive/negative value to label column
df[0] = df[0].apply(lambda x: 2 if x == 1 else -2)

X_training = df[:5000]
y_training = X_training.pop(0)
X_test = df[5000:]
y_target = X_test.pop(0)

model = LinearRegression()
model.fit(X_training, y_training)
predictions = model.predict(X_test)

print('Predicted %d poisonous, %d possibly poisonous, %d definitely edible' % (
    len([x for x in predictions if x <= -2]),
    len([x for x in predictions if x > -2 and x < 2]),
    len([x for x in predictions if x >= 2])))
print('Data says %d poisonous, %d edible' % (
    len([x for x in y_target if x == -2]),
    len([x for x in y_target if x == 2])))

# The mean square error
print ("Residual sum of squares: %.2f" % np.mean((predictions - y_target) ** 2))
# Explained variance score: 1 is perfect prediction
print ('Variance score: %.2f' % model.score(X_test, y_target))

# Blue values for mushrooms above "2" on poisonous scale are definitely safe,
# in the "red zone" is possibly poisonous, and below -2 is definitely poisonous
plt.plot(range(len(predictions)), predictions, color='blue')
plt.plot(range(len(predictions)), y_target, color='red')
plt.xlabel('Mushroom from test set')
plt.ylabel('Poisonousness')
plt.show()
