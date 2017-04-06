#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint
import uuid

files_num = 200

for i in xrange(files_num):
    with open(str(uuid.uuid4())[:8] + '.py', 'w+') as _file:
        for j in xrange(randint(10, 100)):
            if randint(1, 4) == 1:
                _file.write('\n')
            else:
                _file.write(str(uuid.uuid4()).replace('-', '')[:randint(1, 32)] + '\n')
