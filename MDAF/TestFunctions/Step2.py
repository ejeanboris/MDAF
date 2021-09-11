import math

def main(args):
    '''
    >>> (main([0,0])-0 )< 0.001
    True

    
    #_# dimmensions: 2
	#_# upper: 100
	#_# lower: -100
	#_# minimum: [0,0]
	#_# opti: 0
    
	#_# cm_angle: array([[1.75512600e+01],       [2.34210852e+00],       [1.71483517e+01],       [2.50786584e+00],       [1.61753509e+02],       [1.59072574e+01],       [2.57240076e-01],       [9.76587900e-02],       [0.00000000e+00],       [2.36000000e-01]])
	#_# cm_conv: array([[0.23076923],       [0.03846154],       [0.92307692],       [0.07692308],       [0.        ],       [0.107     ]])
	#_# cm_grad: array([[0.67816254],       [0.09775417],       [0.        ],       [0.203     ]])
	#_# ela_conv: array([[ 9.79000000e-01],       [ 0.00000000e+00],       [-2.05145940e+03],       [ 2.05327048e+03],       [ 1.00000000e+03],       [ 6.46000000e-01]])
	#_# ela_curv: array([[0.00000000e+00],       [0.00000000e+00],       [4.89000224e+02],       [0.00000000e+00],       [0.00000000e+00],       [9.72109612e+04],       [6.87376988e+03],       [0.00000000e+00],       [           nan],       [           nan],       [           nan],       [           nan],       [           nan],       [           nan],       [           nan],       [1.00000000e+00],       [1.24561010e+31],       [1.24561010e+31],       [8.68122601e+34],       [8.68122601e+34],       [1.73612064e+35],       [1.73612064e+35],       [1.22753460e+35],       [9.90000000e-01],       [6.01000000e+03],       [4.97100000e+00]])
	#_# ela_distr: array([[ 0.43860394],       [-0.49084682],       [ 1.        ],       [ 0.        ],       [ 1.202     ]])
	#_# ela_local: array([[9.00000000e+01],       [9.00000000e-01],       [1.07988034e-02],       [3.84798542e-01],       [1.00000000e-02],       [1.11235955e-02],       [1.00000000e-02],       [5.00000000e+00],       [5.00000000e+00],       [5.00000000e+00],       [5.00000000e+00],       [5.00000000e+00],       [5.00000000e+00],       [0.00000000e+00],       [5.90000000e+02],       [5.95000000e-01]])
	#_# ela_meta: array([[-5.59163331e-03],       [ 6.66553350e+03],       [ 7.98401523e-01],       [ 1.37733901e+00],       [ 1.72512071e+00],       [-6.31271941e-03],       [ 9.99871442e-01],       [ 1.00145301e+00],       [ 9.99870660e-01],       [ 0.00000000e+00],       [ 7.70000000e-02]])
	#_# basic: array([[ 2.0000e+00],       [ 5.0000e+02],       [-1.0000e+02],       [-1.0000e+02],       [ 1.0000e+02],       [ 1.0000e+02],       [ 4.0000e+01],       [ 1.9208e+04],       [ 6.0000e+00],       [ 6.0000e+00],       [ 3.6000e+01],       [ 3.6000e+01],       [ 1.0000e+00],       [ 0.0000e+00],       [ 1.0000e-03]])
	#_# disp: array([[  0.15385515],       [  0.23422366],       [  0.32112032],       [  0.4966564 ],       [  0.15756413],       [  0.23888297],       [  0.32384636],       [  0.49763056],       [-88.41565476],       [-80.0177606 ],       [-70.93772575],       [-52.59555028],       [-86.47503733],       [-78.12775499],       [-69.40636486],       [-51.56762415],       [  0.        ],       [  0.278     ]])
	#_# limo: array([[ 7.86427754e-01],       [ 1.98849138e-03],       [ 1.51526595e+02],       [ 5.45705991e+01],       [-5.22719614e-03],       [ 2.80081815e-03],       [ 2.58477109e+00],       [ 1.63257588e+00],       [ 1.00692690e+00],       [ 1.00336819e+00],       [ 1.15311134e+02],       [ 7.17134734e-01],       [ 0.00000000e+00],       [ 3.94000000e-01]])
	#_# nbc: array([[ 0.9837657 ],       [ 0.93415162],       [ 0.64779452],       [ 0.11588566],       [-0.24372765],       [ 0.        ],       [ 0.388     ]])
	#_# pca: array([[1.        ],       [1.        ],       [0.33333333],       [1.        ],       [0.51102453],       [0.51102427],       [0.99962042],       [0.34516086],       [0.        ],       [0.032     ]])
	#_# gcm: array([[1.        ],       [0.02777778],       [0.97222222],       [0.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [0.02777778],       [0.        ],       [0.056     ],       [1.        ],       [0.02777778],       [0.97222222],       [0.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [0.02777778],       [0.        ],       [0.221     ],       [1.        ],       [0.02777778],       [0.97222222],       [0.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [1.        ],       [       nan],       [1.        ],       [1.        ],       [0.02777778],       [0.        ],       [0.366     ]])
	#_# ic: array([[ 0.75546743],       [ 2.38738739],       [70.28244264],       [ 1.90690691],       [ 0.40361446],       [ 0.        ],       [ 2.644     ]])

	#_# Represented: 1

	'''
    floors = [(math.floor(a + 0.5))**2 for a in args]
    return sum(floors)

if __name__ == "__main__":
    import doctest
    doctest.testmod()