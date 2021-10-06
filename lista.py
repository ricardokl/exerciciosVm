import randVm as vm

k = 4

header = """\\documentclass[12pt,a4paper,titlepage]{article}
\\usepackage[brazil]{babel}
\\usepackage[utf8x]{inputenc}

\\RequirePackage{geometry}
\\geometry{lmargin=1.5cm,rmargin=1.5cm,top=0.5cm,bottom=0.5cm}

\\newcommand\\myVSpace[1][6pt]{\\rule[\\normalbaselineskip]{0pt}{#1}}

\\usepackage{color}
\\definecolor{rltred}{rgb}{0.75,0,0}
\\definecolor{rltgreen}{rgb}{0,0.5,0}
\\definecolor{rltblue}{rgb}{0,0,0.75}
\\definecolor{rltnova}{rgb}{0.30,0.60,0.20}

\\usepackage{graphicx}
\\usepackage{setspace}
\\usepackage{multirow}

\\selectlanguage{brazil}

\\begin{document}"""

cabecalho = """
\\def\\UERJ{\\textbf{Universidade do Estado do Rio de Janeiro}}
\\def\\cap{\\textbf{CAp/UERJ \\- Instituto de Aplicação Fernando Rodrigues da Silveira}}
\\def\\logo{\\includegraphics[width = 2.7cm]{/home/ricardo/Documents/cap/logouerj.png}}
\\def\\profs{PROFESSORES}
\\def\\ano{9º ano -- E.F.}
\\def\\titulo{\\textbf{Lista de Exercícios de Fixação}}

\\begin{center}
\\resizebox{\\linewidth}{!}{
\\begin{tabular}{|llc|}
\\hline
{\\myVSpace}
\\multirow{6}{*}{\\logo}	& \\multicolumn{2}{c|}{\\UERJ}\\\\
			& \\multicolumn{2}{c|}{\\cap}\\\\
[7pt]
			& \\textbf{Disciplina:} Física / \\ano		& \\textbf{Professores:} {\profs}\\\\
			& 						&\\\\
                & \\multicolumn{2}{c|}{\\titulo}\\\\
[7pt]
\\hline
\\end{tabular}}
\\end{center}
"""

footer = """
\\end{document}
"""

with open('lista.tex','w') as f:
    f.write(header + '\n')
    f.write(cabecalho + '\n')
    f.write('\\begin(itemize)\n')
    for i in range(k):
        f.write('\\item ')
        f.write(vm.exercicio())
    f.write('\\end(itemize)\n')
    f.write(footer)
