def main(args):
    '''
	>>> (main([-10,0]) - 0)<0.001
	True


    #_# dimmensions: 2
	#_# upper: [-5, 3]
	#_# lower: [-15, -3]
	#_# minimum: [-10,0]
	#_# opti: 0
    
	
	#_# cm_angle: array([[3.46336319e-01],       [1.11596448e-01],       [3.32688632e-01],       [1.10567852e-01],       [1.26709762e+02],       [3.96040507e+01],       [1.47616482e-01],       [9.06041269e-02],       [0.00000000e+00],       [7.90000000e-02]])
	#_# cm_conv: array([[0.23809524],       [0.19642857],       [0.67857143],       [0.32142857],       [0.        ],       [0.033     ]])
	#_# cm_grad: array([[0.81854428],       [0.1192788 ],       [0.        ],       [0.052     ]])
	#_# ela_conv: array([[ 1.00000000e+00],       [ 0.00000000e+00],       [-1.06441804e+02],       [ 1.06441804e+02],       [ 1.00000000e+03],       [ 1.04000000e-01]])
	#_# ela_curv: array([[3.20384285e+00],       [1.59352986e+02],       [3.11716056e+02],       [3.16753438e+02],       [4.75852875e+02],       [5.98482830e+02],       [1.80339798e+02],       [0.00000000e+00],       [3.20382725e+02],       [1.59352986e+04],       [3.11716055e+04],       [3.16753436e+04],       [4.75852869e+04],       [5.98482828e+04],       [1.80339798e+04],       [0.00000000e+00],       [5.31778742e+06],       [4.94191117e+07],       [1.07037935e+36],       [3.96591773e+08],       [6.61335123e+12],       [1.60389805e+38],       [1.16318553e+37],       [0.00000000e+00],       [8.40000000e+03],       [9.98000000e-01]])
	#_# ela_distr: array([[ 0.63700187],       [-0.86671884],       [ 2.        ],       [ 0.        ],       [ 0.024     ]])
	#_# ela_local: array([[9.00000000e+01],       [9.00000000e-01],       [1.00000000e+00],       [1.64410646e-01],       [1.00000000e-01],       [1.01123596e-02],       [1.00000000e-02],       [4.50000000e+01],       [8.00000000e+01],       [8.93000000e+01],       [9.00000000e+01],       [1.00000000e+02],       [1.35000000e+02],       [1.65758130e+01],       [9.02000000e+03],       [7.07000000e-01]])
	#_# ela_meta: array([[-6.03426790e-03],       [ 3.06569525e+02],       [ 2.05064239e-02],       [ 6.61146864e-01],       [ 3.22409635e+01],       [-7.94339775e-03],       [ 1.00000000e+00],       [ 5.33390671e+04],       [ 1.00000000e+00],       [ 0.00000000e+00],       [ 1.40000000e-02]])
	#_# basic: array([[ 2.00000000e+00],       [ 5.00000000e+02],       [-1.50000000e+01],       [-3.00000000e+00],       [-5.00000000e+00],       [ 3.00000000e+00],       [ 8.36446791e-03],       [ 8.95463288e+02],       [ 1.00000000e+01],       [ 1.00000000e+01],       [ 1.00000000e+02],       [ 1.00000000e+02],       [ 1.00000000e+00],       [ 0.00000000e+00],       [ 1.00000000e-03]])
	#_# disp: array([[ 0.90387646],       [ 0.87562005],       [ 0.80237804],       [ 0.81384686],       [ 0.90019544],       [ 0.85330973],       [ 0.74450389],       [ 0.74867028],       [-0.40830656],       [-0.52833206],       [-0.83944411],       [-0.79072771],       [-0.40329912],       [-0.59275905],       [-1.03243135],       [-1.01559546],       [ 0.        ],       [ 0.011     ]])
	#_# limo: array([[4.17880614e-01],       [4.99806181e-03],       [2.99599766e+02],       [1.70588576e+02],       [6.54778826e-02],       [5.20933692e-03],       [9.01491863e+02],       [3.18988622e+03],       [9.03063909e+01],       [3.88297785e+01],       [1.74942209e+02],       [5.15283205e-01],       [0.00000000e+00],       [1.12000000e-01]])
	#_# nbc: array([[ 0.19285636],       [ 0.84080448],       [ 0.11842373],       [ 0.17016598],       [-0.30584099],       [ 0.        ],       [ 0.034     ]])
	#_# pca: array([[1.        ],       [1.        ],       [0.33333333],       [1.        ],       [0.73538694],       [0.50398941],       [0.99984257],       [0.33688393],       [0.        ],       [0.003     ]])
	#_# gcm: array([[5.        ],       [0.05      ],       [0.95      ],       [0.93      ],       [0.16376097],       [0.2       ],       [0.18658697],       [0.26119064],       [0.03940216],       [0.01      ],       [0.014     ],       [0.01      ],       [0.02      ],       [0.00547723],       [0.07      ],       [0.08      ],       [0.2       ],       [0.21      ],       [0.32      ],       [0.10024969],       [1.        ],       [0.21551545],       [0.01      ],       [0.        ],       [0.091     ],       [4.        ],       [0.04      ],       [0.96      ],       [0.9       ],       [0.10082007],       [0.25      ],       [0.19083529],       [0.51750934],       [0.18364899],       [0.01      ],       [0.025     ],       [0.015     ],       [0.06      ],       [0.02380476],       [0.1       ],       [0.05      ],       [0.25      ],       [0.18      ],       [0.59      ],       [0.23537205],       [1.        ],       [0.17734396],       [0.01      ],       [0.        ],       [0.094     ],       [4.        ],       [0.04      ],       [0.96      ],       [0.88      ],       [0.15058257],       [0.25      ],       [0.22415964],       [0.40109815],       [0.10875386],       [0.01      ],       [0.03      ],       [0.025     ],       [0.06      ],       [0.0244949 ],       [0.12      ],       [0.14      ],       [0.25      ],       [0.22      ],       [0.42      ],       [0.13241349],       [1.        ],       [0.40109815],       [0.01      ],       [0.        ],       [0.095     ]])
	#_# ic: array([[  0.56692136],       [  2.74774775],       [116.69898186],       [  2.36736737],       [  0.27710843],       [  0.        ],       [  0.228     ]])

	#_# Represented: 1

	'''
    return 100*args[1]**2+0.01*abs(args[0]+10)


if __name__ == "__main__":
    import doctest
    doctest.testmod()