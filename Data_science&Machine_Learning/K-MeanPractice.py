import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Sample data
X = np.array([[1,2],[1.5,1.8],[5,8],[8,8],[1,0.6],[9,11]])

# Scale the data - very important for KMeans
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow Method to find optimal K
wcss = []
for k in range(1, 8):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 8), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of clusters K')
plt.ylabel('WCSS')
plt.show()

# Train final model with optimal K
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

print("Cluster Labels  :", kmeans.labels_)
print("Centroids       :", kmeans.cluster_centers_)