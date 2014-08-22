#!/usr/bin/python

from Cheetah.Template import Template
import re
import sys

header ='''
\\documentclass{letter}

\\usepackage[left=0in, right=0in, top=5.5in, bottom=0in]{geometry}
\\usepackage{anyfontsize}
\\usepackage{xcolor}
\\usepackage[T1]{fontenc}
\\usepackage{bookman}

\\begin{document}
'''

body = '''
\\vspace*{\\fill}
\\center{
\\makebox[0in][c]{
   \\makebox[6in]{
      \\fontencoding{T1}
      \\fontfamily{pbk}
      \\fontsize{80pt}{0pt}\selectfont
      \\color[RGB]{$color}
      {$table}}}
\\makebox[0in][c]{
   \\raisebox{18pt}{
      \\fontencoding{T1}
      \\fontfamily{pzc}
      \\fontsize{40pt}{0pt}\selectfont
      $name}}
\\vspace*{\\fill}
\\newpage
'''

footer = '''
\\end{document}
'''

tables = [
    'ONE',
    'TWO',
    'THREE',
    'FOUR',
    'FIVE',
    'SIX',
    'SEVEN',
    'EIGHT',
    'NINE',
    'TEN',
    'ELEVEN',
    'TWELVE'
]

for i in range(len(tables)):
    tables[i] = re.sub('(.)', '\hfill \g<1>\hfill ', tables[i])

infile = sys.argv[1];
outfile = sys.argv[2];

with open(infile) as f:
    fh = open(outfile, 'w');
    fh.write(str(Template(header)));
    for l in f:
        m = re.search('(.*), ([MCVS]), (\d+)', l);
        if not m:
            exit('you done fucked up');
        else:
            name = m.group(1);
            meal = m.group(2);
            table = m.group(3);
            if meal is 'M':
                color = '213,163,245'
            if meal is 'C':
                color = '249,214,112'
            if meal is 'V':
                color = '118,156,141'
            if meal is 'S':
                color = '158,119,27'
            fh.write(str(Template(body, searchList = [{'color' : color,
                                                       'name' : name,
                                                       'table' : tables[int(table) - 1]}])))

fh.write(str(Template(footer)))
fh.close()
