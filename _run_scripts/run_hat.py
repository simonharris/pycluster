"""Temp bootstrap file to run B&F"""
import pathhack

from sklearn.cluster import KMeans

from datasets import testloader
from initialisations import hatamlou2012 as alg

# dataset = testloader.load_iris()
# num_clusters = 3

# dataset = testloader.load_hartigan()
# num_clusters = 3

# dataset = testloader.load_soy_small()
# num_clusters = 4

# Hopefully will fail...
dataset = testloader._load_local('20_1000_1000_u_1_005')
num_clusters = 20

data = dataset.data

centroids = alg.generate(data, num_clusters)

# est = KMeans(n_clusters=num_clusters, init=centroids, n_init=1)
# est.fit(dataset.data)

# print("Final centres:\n", est.cluster_centers_)
