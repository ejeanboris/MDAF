def main(args):
    '''
    >>> (main([0,0]) - 0)<0.001
    True

    
    #_# dimmensions: 2
	#_# upper: 100
	#_# lower: -100
	#_# minimum: [0,0]
	#_# opti: 0
    
	#_# cm_angle: array([[1.72215494e+01],       [2.59186558e+00],       [1.73080840e+01],       [2.32553416e+00],       [1.55317224e+02],       [1.54411724e+01],       [2.63099825e-01],       [1.01400943e-01],       [0.00000000e+00],       [3.36000000e-01]])
	#_# cm_conv: array([[0.23076923],       [0.01923077],       [0.92307692],       [0.07692308],       [0.        ],       [0.158     ]])
	#_# cm_grad: array([[0.66203256],       [0.08653427],       [0.        ],       [0.291     ]])
	#_# ela_conv: array([[ 1.00000000e+00],       [ 0.00000000e+00],       [-2.25864698e+03],       [ 2.25864698e+03],       [ 1.00000000e+03],       [ 9.57000000e-01]])
	#_# ela_curv: array([[1.66265566e+01],       [1.14451325e+02],       [1.55060539e+02],       [1.63087623e+02],       [1.96213591e+02],       [2.73023876e+02],       [5.68415849e+01],       [0.00000000e+00],       [1.01060763e+00],       [1.42768440e+00],       [1.44939345e+01],       [2.01740454e+00],       [4.44927588e+00],       [1.33798016e+03],       [9.73375169e+01],       [0.00000000e+00],       [1.00000005e+00],       [1.00000147e+00],       [3.07924737e+01],       [1.00000273e+00],       [1.00000731e+00],       [5.95879834e+03],       [4.21279716e+02],       [0.00000000e+00],       [8.40000000e+03],       [6.46800000e+00]])
	#_# ela_distr: array([[ 0.4595509 ],       [-0.39456146],       [ 2.        ],       [ 0.        ],       [ 0.144     ]])
	#_# ela_local: array([[9.00000000e+01],       [9.00000000e-01],       [2.89705664e-03],       [2.28020182e-01],       [1.00000000e-02],       [1.11235955e-02],       [1.00000000e-02],       [2.00000000e+01],       [2.00000000e+01],       [2.20500000e+01],       [2.00000000e+01],       [2.50000000e+01],       [2.50000000e+01],       [2.47155535e+00],       [2.29500000e+03],       [1.97300000e+00]])
	#_# ela_meta: array([[-5.88921156e-03],       [ 6.66594695e+03],       [ 3.45283009e-01],       [ 9.35344958e-01],       [ 2.70892264e+00],       [-5.51001031e-03],       [ 1.00000000e+00],       [ 1.00000000e+00],       [ 1.00000000e+00],       [ 0.00000000e+00],       [ 6.30000000e-02]])
	#_# basic: array([[ 2.00000000e+00],       [ 5.00000000e+02],       [-1.00000000e+02],       [-1.00000000e+02],       [ 1.00000000e+02],       [ 1.00000000e+02],       [ 1.12775826e+00],       [ 1.86355093e+04],       [ 6.00000000e+00],       [ 6.00000000e+00],       [ 3.60000000e+01],       [ 3.60000000e+01],       [ 1.00000000e+00],       [ 0.00000000e+00],       [ 1.00000000e-03]])
	#_# disp: array([[  0.15269879],       [  0.23271735],       [  0.32156902],       [  0.50335822],       [  0.14758667],       [  0.23489903],       [  0.32051915],       [  0.50259174],       [-88.55743104],       [-80.19412662],       [-70.90761106],       [-51.90753826],       [-87.61726606],       [-78.64266382],       [-69.84200313],       [-51.12725292],       [  0.        ],       [  0.744     ]])
	#_# limo: array([[ 3.28306369e-01],       [ 3.80487807e-03],       [ 1.51562625e+02],       [ 5.50106121e+01],       [-1.46339879e-03],       [ 8.32396327e-04],       [ 2.53047996e+00],       [ 1.59095599e+00],       [ 1.00147226e+00],       [ 1.00051589e+00],       [ 1.15441744e+02],       [ 7.17131951e-01],       [ 0.00000000e+00],       [ 3.95000000e-01]])
	#_# nbc: array([[ 0.99836061],       [ 0.93284167],       [ 0.67967868],       [ 0.11387608],       [-0.24321922],       [ 0.        ],       [ 0.319     ]])
	#_# pca: array([[1.        ],       [1.        ],       [0.33333333],       [1.        ],       [0.5096517 ],       [0.5096517 ],       [0.99961314],       [0.34195362],       [0.        ],       [0.01      ]])
	#_# gcm: array([[1.        ],       [0.02777778],       [0.97222222],       [0.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [0.02777778],       [0.        ],       [0.135     ],       [1.        ],       [0.02777778],       [0.97222222],       [0.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [0.02777778],       [0.        ],       [0.285     ],       [1.        ],       [0.02777778],       [0.97222222],       [0.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [0.02777778],       [0.        ],       [0.298     ]])
	#_# ic: array([[ 0.74639553],       [ 2.36736737],       [64.09244019],       [ 1.94694695],       [ 0.37951807],       [ 0.        ],       [ 2.627     ]])

	#_# Represented: 1

	'''
    vals = [x**2 for x in args]
    return sum(vals)

if __name__ == "__main__":
    import doctest
    doctest.testmod()