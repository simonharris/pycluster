"""
Principle Component Analysis-based algorithm from Onoda 2012
"""

from sklearn.decomposition import PCA

from initialisations.onoda2012 import Onoda


class OnodaPCA(Onoda):

    @staticmethod
    def _find_components(data, num_components):
        """Run Pricipal Component Analysis"""

        pca = PCA(n_components=num_components)
        pca.fit(data)
        return pca.components_


def generate(data, num_clusters):
    """Provide consistent interface"""

    onoda = OnodaPCA(data, num_clusters)
    return onoda.find_centers(data, num_clusters)
