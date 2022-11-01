import matplotlib.pyplot as plt

x = []
y = []

readFile = open('DS0.txt', 'r')
sepFile = readFile.read().split('\n')
readFile.close()

for plotPair in sepFile:
    xAndY = plotPair.split(' ')
    y.append(int(xAndY[0]))
    x.append(int(xAndY[1]))

px = 1/plt.rcParams['figure.dpi']
plt.subplots(figsize=(960*px, 540*px))
plt.scatter(x,y)
plt.savefig('LAB2.png')
plt.show()
