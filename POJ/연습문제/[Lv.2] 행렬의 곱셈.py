# 걍 numpy 검색해서 도출함

import numpy as np

def solution(arr1, arr2):
    return np.dot(np.array(arr1), np.array(arr2)).tolist()