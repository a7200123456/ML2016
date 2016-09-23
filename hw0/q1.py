import sys
import numpy as np

matrix = np.loadtxt(sys.argv[2])
ans1 = np.sort(matrix[:,int(sys.argv[1])])
ans1 = np.reshape(ans1,(1,ans1.shape[0]))
np.savetxt('ans1.txt',ans1,delimiter = ',',fmt='%.3f')