import numpy as np

def check_numpy(func):
    def inner_func(text1,text2):
        assert_np(text1)
        assert_np(text2)
        return func(text1,text2)
    return inner_func

def assert_np(vect):
    assert(type(vect)==np.ndarray)

@check_numpy
def l1(text1,text2):
    return np.linalg.norm((text1 - text2), ord=1)

@check_numpy
def l2(text1,text2):
    return np.linalg.norm((text1 - text2), ord=2)

@check_numpy
def l_inf(text1,text2):
    return np.linalg.norm((text1 - text2), ord=np.inf)

@check_numpy
def cos_metric(text1,text2):
    cs=np.dot(text1,text2)
    cs/=np.dot(text1,text1)*np.dot(text1,text1)
    return 1.0 - cs
