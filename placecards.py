#!/usr/bin/python

from Cheetah.Template import Template
import re
import sys

header ='''
\\documentclass{letter}

\\usepackage[total={11in,11in}, left=0in, right=0in, top=6in, bottom=0.5in]{geometry}
\\usepackage{anyfontsize}
\\usepackage{xcolor}
\\usepackage[T1]{fontenc}
\\usepackage{bookman}

\\begin{document}
\\pagenumbering{gobble}
'''

body = '''
\\vspace*{\\fill}
\\center{
\\makebox[0in][c]{
   \\makebox[8.25in]{
      \\fontencoding{T1}
      \\fontfamily{pbk}
      \\fontsize{130pt}{0pt}\selectfont
      \\color[RGB]{$color}
      {$table}}}
\\makebox[0in][c]{
   \\raisebox{27pt}{
      \\fontencoding{T1}
      \\fontfamily{pzc}
      \\fontsize{70pt}{0pt}\selectfont
      \\textbf{$name}}}
\\vspace*{\\fill}
\\newpage
'''

footer = '''
\\end{document}
'''

tables = [
    'ZERO',
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

table_count = [0] * 13;
meat = 0;
veggie = 0;
chicken = 0;
other = 0;

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
            table = int(m.group(3));
            table_count[table] += 1
            if meal is 'M':
                color = '213,163,245'
                meat += 1;
            if meal is 'C':
                color = '245, 204, 146'
                chicken += 1;
            if meal is 'V':
                color = '99,226,74'
                veggie += 1;
            if meal is 'S':
                color = '249,247,133'
                other += 1
            fh.write(str(Template(body, searchList = [{'color' : color,
                                                       'name' : name,
                                                       'table' : tables[table]}])))

fh.write(str(Template(footer)))
fh.close()

for t in range(len(table_count)):
    print 'Table' + str(t) + ':' +  str(table_count[t])

print 'Chicken: ' + str(chicken);
print 'Beef: ' + str(meat);
print 'Veggie: ' + str(veggie);
print 'other: ' + str(other)
