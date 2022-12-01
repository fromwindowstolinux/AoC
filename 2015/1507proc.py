#!/usr/bin/env python
from pprint import pprint
import functools
import sys

nodes = []

with open('1507input.txt') as indata:
    for line in indata:
        node = None

        # extract line with 2 inputs
        for optype in ['AND','OR','RSHIFT','LSHIFT']:
            if optype in line:
                in1, op, in2, _, out = line.split()
                node = {
                    'in': [in1, in2],
                    'op': op,
                    'out': out
                }
                nodes.append(node)
                break

        if node is not None:
            continue

        # extract for not
        if 'NOT' in line:
            op, in1, _, out = line.split()
            node = {
                'in': [in1],
                'op': op,
                'out': out
            }
            nodes.append(node)
            continue

        # extract for noop
        in1, _, out = line.split()
        node = {
            'in': [in1],
            'op': None,
            'out': out
        }
        nodes.append(node)

# convert numbers to int
for node in nodes:
    inputs = []
    for item in node['in']:
        try:
            item = int(item)
        except ValueError:
            pass
        inputs.append(item)
    node['in'] = inputs


index = {}
for node in nodes:
    index[node['out']] = node

@functools.cache
def resolve(var):
    if type(var) == int:
        return var

    node = index[var]
    if node['op'] == 'AND':
        res = resolve(node['in'][0]) & resolve(node['in'][1])
    elif node['op'] == 'OR':
        res = resolve(node['in'][0]) | resolve(node['in'][1])
    elif node['op'] == 'RSHIFT':
        res = resolve(node['in'][0]) >> resolve(node['in'][1])
    elif node['op'] == 'LSHIFT':
        res = resolve(node['in'][0]) << resolve(node['in'][1])
    elif  node['op'] == 'NOT':
        res = ~ resolve(node['in'][0])
    else:
        res = resolve(node['in'][0])

    return res


if len(sys.argv) == 1:
    print('Usage: %s [VAR]' % sys.argv[0])
    sys.exit(1)

for i in sys.argv[1:]:
    if i not in index.keys():
        print('Unknown variable %s' % i, file=sys.stderr)
    else:
        print(resolve(i))
