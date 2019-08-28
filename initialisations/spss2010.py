"""
Pavan et al. 2011 Single Pass Sees Selection (SPSS) algorithm

See: Single pass seed selection algorithm for k-means (2010)
http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.165.8956 

and: Robust seed selection algorithm for k-means type algorithms (2011)
https://arxiv.org/abs/1202.1585
"""

import numpy as np

from initialisations.Initialisation import Initialisation
from kmeans import distance_table


class SPSS(Initialisation):
    
    
    def find_centers(self):
        """Main method"""
    
        Xh = self._find_hdp()
        centroids = np.array([Xh])
        
        # Remaining required centroids (exactly as per k-means++)
        while len(centroids) < self._K:

            distances = distance_table(self._data, centroids)
            probabilities = distances.min(1)**2 / np.sum(distances.min(1)**2)

            randindex = np.random.choice(self._num_samples, 
                                         replace=False, 
                                         p=probabilities)
            centroids = np.append(centroids, [self._data[randindex]], 0)
        
        return centroids
        
        
    def _find_hdp(self):
        """The highest density point"""
    
        Dist = distance_table(self._data, self._data)
        Sumv = np.sum(Dist, axis=1) # doesn't matter which axis
        h = np.argmin(Sumv)
        
        return self._data[h]
        
    
## -----------------------------------------------------------------------------


def generate(data, K, opts):
    """The common interface"""
    
    spss = SPSS(data, K, opts)
    return spss.find_centers()
    