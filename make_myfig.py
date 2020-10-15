import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0,10,1)

y= x**2

plt.figure()

plt.plot(x,y)
plt.ylabel('widgets')
plt.xlabel('time')
plt.title('Big Shmancy title')
plt.savefig('/Users/coakley/Desktop/SWBC2020/git_hackhour/hello-git/myfig.png')
