import pandas

############################
## Part A
## Read data and scale to interval [0, 1]
############################
from sklearn.preprocessing import MinMaxScaler

data = pandas.read_csv('./segmentation_data/segmentation_data.txt', header=None)
labels = pandas.read_csv('./segmentation_data/segmentation_classes.txt', sep='\t', header=None)
labels = labels[1]  # Only need the IDs

min_max_scaler = MinMaxScaler()
data = min_max_scaler.fit_transform(data)

data = pandas.DataFrame(data)
column_names = open('./segmentation_data/segmentation_names.txt').read().splitlines()

print("(A) Scaled %d rows of data to interval [0, 1]" % len(data))


############################
## Part B
## Run KMeans on the image data
############################
from sklearn.cluster import KMeans
from sklearn import metrics

# Use number of classes as desired number of clusters
kmeans = KMeans(n_clusters=7)
x = kmeans.fit(data)

print("(B) K-means: Homogeneity %.4f, Completeness: %.4f" % (
    metrics.homogeneity_score(labels, kmeans.labels_),
    metrics.completeness_score(labels, kmeans.labels_)))


############################
## Part C
## Run PCA on data to reduce dimensionality, keeping enough components to
## capture 95% of the variance in the data
############################
from sklearn.decomposition import PCA

# We can pass a fractional value to n_components argument, which does a lot of work for us.
# The long way around would be to initially pass n_components=columns and call pca.fit(data),
# which would allow us to examine pca.explained_variance_ratio_ to see which components explain
# (proportionally) the variance in the data, sort that list, and the top N items from list so that
# their sum is >= .95.  Then call PCA again with n_components=N and use fit_transform().
pca = PCA(n_components=.95)
reduced_data = pca.fit_transform(data)

print("(C) Reduced dimensions to %d components, accounting for %.1f%% of the data variance" %
     (len(pca.explained_variance_ratio_), sum(pca.explained_variance_ratio_) * 100))


############################
## Part D
## Run KMeans again on reduced dimensionality data
############################
# Use number of classes as desired number of clusters
kmeans = KMeans(n_clusters=7)
x = kmeans.fit(reduced_data)

print("(D) K-means after PCA: Homogeneity %.4f, Completeness: %.4f" % (
    metrics.homogeneity_score(labels, kmeans.labels_),
    metrics.completeness_score(labels, kmeans.labels_)))
