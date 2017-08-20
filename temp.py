import os
import json

with open(os.path.join(os.getcwd(), 'Property.json')) as f:
    content = json.loads(f.read())

for i in content:
    print i
