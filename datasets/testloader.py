"""Provides a simple interface to load test datasets"""

import os

import arff
import numpy as np
import pandas as pd
import sklearn.datasets as skdatasets


DIR_PATH = os.path.dirname(os.path.realpath(__file__)) + '/test/'


class Dataset():
    """Mimics the sklearn dataset interface"""

    def __init__(self, data, target):
        self.data = data
        self.target = target


def _load_local(which):
    """Load datasets from the local filesystem"""

    datafile = DIR_PATH + which + '/data.csv'
    labelfile = DIR_PATH + which + '/labels.csv'

    return Dataset(
        np.loadtxt(datafile, delimiter=',', dtype=np.int),
        np.loadtxt(labelfile, delimiter=',', dtype=np.int),
    )


# The loaders to be exposed ---------------------------------------------------

def load_fossil():
    """Fossil"""
    return _load_local('fossil')


def load_hartigan():
    """Hartigan 1975 (tiny)"""
    return _load_local('hartigan1975')


def load_iris():
    """Built-in Iris dataset"""
    return skdatasets.load_iris()


def load_iris_ccia():
    """To ensure using the exact same Iris data as Khan & Ahmad 2004"""

    datafile = DIR_PATH + '/iris_ccia/iris.arff'

    with open(datafile) as dfhandle:
        iris = np.array(arff.load(dfhandle)['data'])

    return Dataset(iris[:, 0:4].astype('float'), pd.factorize(iris[:, 4]))


def load_soy_small():
    """Soybean Small"""
    return _load_local('soy_small')


def load_wbco():
    """Wisconsin Breast Cancer"""
    return _load_local('wbco')


def load_wine():
    """Built-in Wine dataset"""
    return skdatasets.load_wine()