#/bin/bash

(cd exercise1 && make && ./test.py) > /dev/null
(cd exercise2 && make && ./test.py) > /dev/null
(cd exercise3 && make && ./test.py) > /dev/null
(cd exercise4 && make && ./test.py) > /dev/null

