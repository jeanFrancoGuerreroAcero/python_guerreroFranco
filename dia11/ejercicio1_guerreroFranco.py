import json

#!/usr/bin/python
 # -*- coding: utf-8 -*-

with open("dia11/large-file.json", encoding= "utf-8") as openfile:
    mijson= json.load(openfile)

print((mijson[0]))
