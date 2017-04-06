#!/usr/bin/python
# -*- coding: utf-8 -*-
import uuid

print str(uuid.uuid4())[:8]

for i in xrange(30):
    with open(str(uuid.uuid4())[:8] + '.py', 'w+') as _file:
        pass
