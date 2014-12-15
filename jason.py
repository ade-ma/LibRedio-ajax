import datetime
import json


def norm(x):
    if x[3] > 80:
        x[3] -= 100
    return x

def to_json(x):
    return {'date': str(x[0]), 'uuid': sum(x[1][:3]), 'temp': x[1][3], 'humidity': x[1][4]}


a = open("p?rrwg").read()
b = a.split('\n')
c = map(eval, b[0:-2])
c[0]
data = [to_json((datetime.datetime.fromtimestamp(x[0]), norm(x[1]))) for x in c]
f = open('serialized', 'a')

for i in data:
    f.write(json.dumps(i))
    f.write('\n')
f.close()
