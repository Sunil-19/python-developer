l=[{'name': 'affirm', 'confidence': 0.9448149204254},
   {'name': 'affirm', 'confidence': 0.944814920425415},
   {'name': 'inform', 'confidence': 0.9842240810394287},
   {'name': 'inform', 'confidence': 0.9842240810394287}]

seen = set()
new = []
for d in l:
    t = tuple(d.items())
    if t not in seen:
        seen.add(t)
        new.append(d)

print (new)
