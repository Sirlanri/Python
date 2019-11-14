import matplotlib.pyplot as plt
import numpy
import matplotlib
def nine_one():
	x=numpy.linspace(0,15,100)
    #下面两步完全没有代码补全提示！吓人
	y=numpy.cos(2*numpy.pi*x)*numpy.exp(-x)+0.8
	plt.plot(x,y,'k',color='r',linewidth=3,linestyle='-')
	plt.show()

def nine_two():
	plt.plot()