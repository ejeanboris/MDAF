def main(args):
    '''
    >>> (main([0,0]) - 0)<0.001
    True

    
    #_# dimmensions: 2
	#_# upper: 10
	#_# lower: -10
	#_# minimum: [0,0]
	#_# opti: 0
    
	#_# cm_angle: array([[  1.74423906],       [  0.27293964],       [  1.76075806],       [  0.29531509],       [143.02933717],       [ 24.06675059],       [  0.29793996],       [  0.16731295],       [  0.        ],       [  0.285     ]])
	#_# cm_conv: array([[0.30769231],       [0.19230769],       [0.73076923],       [0.26923077],       [0.        ],       [0.086     ]])
	#_# cm_grad: array([[0.6992867 ],       [0.09123779],       [0.        ],       [0.23      ]])
	#_# ela_conv: array([[ 1.00000000e+00],       [ 0.00000000e+00],       [-1.09269603e+01],       [ 1.09269603e+01],       [ 1.00000000e+03],       [ 8.33000000e-01]])
	#_# ela_curv: array([[1.13629627e-01],       [5.50553497e+00],       [1.07430400e+01],       [1.07578815e+01],       [1.60831070e+01],       [1.99616202e+01],       [5.83772714e+00],       [0.00000000e+00],       [           nan],       [           nan],       [           nan],       [           nan],       [           nan],       [           nan],       [           nan],       [1.00000000e+00],       [3.10673872e+29],       [7.79028149e+31],       [7.25379887e+43],       [4.08761262e+32],       [5.95115785e+33],       [1.41618495e+46],       [1.00156955e+45],       [0.00000000e+00],       [7.20000000e+03],       [9.35600000e+00]])
	#_# ela_distr: array([[ 0.63731058],       [-0.86516682],       [ 2.        ],       [ 0.        ],       [ 0.242     ]])
	#_# ela_local: array([[9.00000000e+01],       [9.00000000e-01],       [8.99156632e-25],       [2.86476224e-01],       [1.00000000e-02],       [1.11235955e-02],       [1.00000000e-02],       [2.00000000e+01],       [2.00000000e+01],       [2.23000000e+01],       [2.00000000e+01],       [2.50000000e+01],       [2.50000000e+01],       [2.50454133e+00],       [2.32000000e+03],       [2.61900000e+00]])
	#_# ela_meta: array([[-5.95672965e-03],       [ 3.33348862e+01],       [ 1.84396704e-03],       [ 5.83364265e-02],       [ 3.16363715e+01],       [-7.99188239e-03],       [ 1.00000000e+00],       [ 7.50815513e+17],       [ 1.00000000e+00],       [ 0.00000000e+00],       [ 1.04000000e-01]])
	#_# basic: array([[ 2.00000000e+00],       [ 5.00000000e+02],       [-1.00000000e+01],       [-1.00000000e+01],       [ 1.00000000e+01],       [ 1.00000000e+01],       [ 1.93346220e-04],       [ 9.99336729e+01],       [ 6.00000000e+00],       [ 6.00000000e+00],       [ 3.60000000e+01],       [ 3.60000000e+01],       [ 1.00000000e+00],       [ 0.00000000e+00],       [ 0.00000000e+00]])
	#_# disp: array([[ 0.66775335],       [ 0.64309839],       [ 0.66537207],       [ 0.69438354],       [ 0.63502799],       [ 0.57661317],       [ 0.5877032 ],       [ 0.61742602],       [-3.47196596],       [-3.72960941],       [-3.49685024],       [-3.19368145],       [-3.7429486 ],       [-4.34201828],       [-4.22828516],       [-3.92346456],       [ 0.        ],       [ 0.309     ]])
	#_# limo: array([[2.87816403e-02],       [7.59592794e-04],       [9.97657005e+00],       [5.51600215e+00],       [1.28722457e-01],       [1.60375448e-01],       [1.74841570e+02],       [2.84743848e+02],       [7.79501361e+01],       [4.26928609e+01],       [5.83540750e+00],       [5.18827787e-01],       [0.00000000e+00],       [3.39000000e-01]])
	#_# nbc: array([[ 0.23737592],       [ 0.88748311],       [ 0.15958744],       [ 0.14163924],       [-0.21953669],       [ 0.        ],       [ 0.413     ]])
	#_# pca: array([[1.        ],       [1.        ],       [0.33333333],       [1.        ],       [0.50446366],       [0.50446296],       [0.93024089],       [0.33809051],       [0.        ],       [0.027     ]])
	#_# gcm: array([[2.        ],       [0.05555556],       [0.94444444],       [0.61111111],       [0.28656214],       [0.5       ],       [0.5       ],       [0.71343786],       [0.30184672],       [0.02777778],       [0.19444444],       [0.19444444],       [0.36111111],       [0.23570226],       [0.38888889],       [0.33333333],       [0.5       ],       [0.5       ],       [0.66666667],       [0.23570226],       [1.        ],       [0.71343786],       [0.02777778],       [0.        ],       [0.287     ],       [2.        ],       [0.05555556],       [0.94444444],       [0.58333333],       [0.42569148],       [0.5       ],       [0.5       ],       [0.57430852],       [0.10508812],       [0.13888889],       [0.20833333],       [0.20833333],       [0.27777778],       [0.09820928],       [0.41666667],       [0.5       ],       [0.5       ],       [0.5       ],       [0.5       ],       [0.        ],       [1.        ],       [0.57430852],       [0.02777778],       [0.        ],       [0.174     ],       [2.        ],       [0.05555556],       [0.94444444],       [0.69444444],       [0.49752284],       [0.5       ],       [0.5       ],       [0.50247716],       [0.00350324],       [0.08333333],       [0.15277778],       [0.15277778],       [0.22222222],       [0.09820928],       [0.30555556],       [0.5       ],       [0.5       ],       [0.5       ],       [0.5       ],       [0.        ],       [1.        ],       [0.50247716],       [0.02777778],       [0.        ],       [0.23      ]])
	#_# ic: array([[0.65337406],       [1.26626627],       [3.35371015],       [0.68568569],       [0.35542169],       [0.        ],       [1.627     ]])

	#_# Represented: 1

	'''
    vals = [i*x**2 for i,x in enumerate(args)]
    return sum(vals)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
