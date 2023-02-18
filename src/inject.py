#!/usr/bin/env python3

with open('critical.css') as file:
    css = file.read()

replacements = {'styletag':'style', 'stylecontent': css}

lines = []
with open('index.html') as file:
    for line in file:
        for src, target in replacements.items():
            line = line.replace(src, target)
        lines.append(line)

with open('index.html', 'w') as file:
    for line in lines:
        file.write(line)

