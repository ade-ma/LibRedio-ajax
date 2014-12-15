from pylab import *
import datetime
a = open("p?rrwg").read()
b = a.split('\n')
c = map(eval, b[0:-2])
c[0]
# OUT: (1417474394, [1, 2, 0, 9.7, 156.800003])
plot([datetime.datetime.fromtimestamp(x[0]) for x in c], [x[1][3] - 100 if x[1][3] > 80 else x[1][3] for x in c])
# OUT: [<matplotlib.lines.Line2D object at 0x35e5950>]
xlabel("Time")
# OUT: <matplotlib.text.Text object at 0x31b9210>
ylabel("Temp (degC)")
# OUT: <matplotlib.text.Text object at 0x31bf190>
savefig("data.png")
