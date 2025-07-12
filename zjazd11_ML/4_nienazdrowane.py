from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

digits = load_digits()
# print(digits['images'])
#
# plt.matshow(digits.images[9], cmap="gray")
# plt.show()
X = digits.data
y = digits.target

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

kmeans = KMeans(n_clusters=10)
clusters = kmeans.fit_predict(X)

plt.figure(figsize=(10, 7))
sns.scatterplot(x=X_pca[:,0], y=X_pca[:,1], hue=clusters, palette='tab10', legend='full')
plt.title('Klasteryzacja cyfr odręcznych')
plt.xlabel('Główna składowa 1')
plt.xlabel('Główna składowa 2')
plt.legend(title='Klaster')
plt.grid(True)
plt.show()


