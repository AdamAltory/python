colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m']
for i in range(10):
 print(colors[i % 4] + "python is magic!")
print('\033[0m') # reset colors 