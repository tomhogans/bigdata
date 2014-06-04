from sklearn.datasets import load_boston
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
import pandas
import matplotlib.pyplot as plt

dataset = load_boston()
data = dataset['data']
feature_names = list(dataset['feature_names'])
target = dataset['target']

# Scale data
data = scale(data)
# Load into DataFrame
data = pandas.DataFrame(data)
# Assign column names
feature_names.remove('MEDV')
data.columns = feature_names

pca = PCA(n_components=.90)
pca.fit(data)

results = []
for i in range(len(data.columns)):
    dimensions = i + 1
    pca = PCA(n_components=dimensions)
    pca.fit(data)
    results.append((dimensions, sum(pca.explained_variance_ratio_)))
x, y = zip(*results)

plt.plot(x, y)
plt.xlabel('Components')
plt.ylabel('Explained Variance')
plt.show()
# We can see from the plot that we can reduce the dimensions to 7 and still
# retain features that represent almost 90% of the variance in the data.  This
# shows that almost half of the data accords for almost 90% of the variance,
# allowing us to reduce the data we're processing in half without losing much
# accuracy in our predictions.
