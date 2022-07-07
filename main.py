# use os.system() commands.getstatusoutput() and popen() to run binarys

from cgi import print_arguments
import os

# os.system() command to run binary
res = os.system("./GoBinary/main")
print(res)  

import subprocess

if os.path.exists("./GoBinary/main"):
    rs,out = subprocess.getstatusoutput("./GoBinary/main")
    print(rs)
    print(out)
else:
    print("binary not found")


# os.popen() command to run binary
p = os.popen("./GoBinary/main")
print(p.read())
p.close()


class GlobalWealth(object):
    def __init__(self):
        self._global_wealth = 10.0
        self._observers = []

    @property
    def global_wealth(self):
        return self._global_wealth

    @global_wealth.setter
    def global_wealth(self, value):
        self._global_wealth = value
        for callback in self._observers:
            print('announcing change')
            callback(self._global_wealth)

    def bind_to(self, callback):
        print('bound')
        self._observers.append(callback)


class Person(object):
    def __init__(self, data):
        self.wealth = 1.0
        self.data = data
        self.data.bind_to(self.update_how_happy)
        self.happiness = self.wealth / self.data.global_wealth

    def update_how_happy(self, global_wealth):
        self.happiness = self.wealth / global_wealth



if __name__ == '__main__':
    data = GlobalWealth()
    p = Person(data)
    print(p.happiness)
    data.global_wealth = 1.0
    print(p.happiness)