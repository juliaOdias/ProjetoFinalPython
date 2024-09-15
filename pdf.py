from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font('Arial', 'B', 20)
pdf.cell(200, 10, 'Relatório de Análise da Desigualdade Educacional', ln=True, align='C')
pdf.image('c:\\archive\\capa.jpg', x=10, y=30, w=190)  # Ajuste o caminho e as dimensões conforme necessário


pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, 'Relatório de Análise da Desigualdade Educacional no Brasil', ln=True, align='C')

pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, '''

A educação no Brasil é marcada por desafios históricos que refletem as desigualdades sociais e econômicas do país. 
Desde o acesso inicial à educação infantil até o ensino superior, muitas barreiras limitam o desenvolvimento educacional de milhões de brasileiros.

Entre essas barreiras, a questão do acesso é um dos principais problemas enfrentados, especialmente em áreas rurais e regiões mais pobres. 
Além disso, questões como a desigualdade de gênero, onde certos cursos, especialmente na área de exatas, são dominados por um gênero, e a desigualdade racial, onde grupos étnicos minoritários enfrentam dificuldades de acesso e permanência, são fatores que agravam ainda mais a situação.

A análise apresentada neste relatório busca destacar essas desigualdades por meio de dados e gráficos que permitem uma compreensão mais profunda dos desafios enfrentados pela educação no Brasil. 
É uma tentativa de contribuir para a construção de políticas públicas mais eficazes e inclusivas, visando reduzir as disparidades e garantir uma educação de qualidade para todos.
''')
pdf.ln(10)


pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Distribuição de Vagas por Estado', ln=True)
pdf.image('C:\\archive\\distribuicao_vagas_estado.png', x=10, w=180)
pdf.ln(5)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, '''
Este gráfico mostra como as vagas são distribuídas por estado. Podemos observar que estados mais populosos como São Paulo, Rio de Janeiro e Minas Gerais concentram a maior parte das vagas, 
o que reflete a desigualdade de acesso educacional entre regiões mais e menos desenvolvidas do Brasil.
''')

pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Proporção de Inscritos por Modalidade', ln=True)
pdf.image('C:\\archive\\proporcao_inscritos_modalidade.png', x=10, w=180)
pdf.ln(5)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, '''
A análise por modalidade revela uma maior adesão ao ensino presencial em comparação com a educação a distância, embora a educação a distância esteja a cada ano crescendo mais. 
Podemos citar em conjunto, o gráfico anterior, pois as regiões menores e menos desenvolvidas podem optar pelo ensino a distância devido ao custo mais baixo, praticidade e pode ser única oportunidade disponível na localidade.
''')


pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Número de Matrículas por Faixa Etária', ln=True)
pdf.image('C:\\archive\\proporcao_matriculas_por_faixa_etaria.png', x=10, w=180)
pdf.ln(5)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, '''
Este gráfico indica que a maioria dos matriculados está na faixa etária dos 18 aos 24 anos, o que coincide com o período típico de ingresso no ensino superior. 
O gráfico vai dimunuindo conforme a idade aumenta, ao se perguntar o motivo, podemos incluir o aumento de responsabilidades e preconceitos enraizados.
''')

pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Ingressantes por Cor/Raça', ln=True)
pdf.image('C:\\archive\\proporcao_ingressantes_por_cor_raça.png', x=10, w=180)
pdf.ln(5)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, '''
A distribuição de ingressantes por cor/raça evidencia a maioria como brancos no ensino superior.
Apesar do crescimento de políticas afirmativas, como cotas raciais, os números mostram que ainda há um longo caminho para uma maior equidade racial no ensino superior.
''')

pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Ingressantes por Cor/Raça', ln=True)
pdf.image('C:\\archive\\distribuicao_genero_cursos_exatas.png', x=30, w=135)
pdf.ln(5)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, '''
O gráfico de barras mostra que, de maneira geral, ainda há uma predominância masculina nos cursos de exatas, com homens superando mulheres em praticamente todos os cursos analisados. 
Embora a participação feminina seja significativa em alguns cursos, como Engenharia e Química, a disparidade de gênero é evidente, especialmente em outras engenharias. 
Isso reflete uma realidade comum nas áreas de STEM (Ciência, Tecnologia, Engenharia e Matemática), onde os homens continuam a ser maioria.
No entanto, a crescente participação feminina em determinados cursos é um sinal positivo de avanço em termos de inclusão. 
Iniciativas que promovem a equidade de gênero nesse campo são fundamentais para continuar reduzindo essas diferenças e tornar o ambiente mais igualitário.
''')

pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Análise Geral', ln=True)
pdf.ln(5)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, '''
A análise dos dados educacionais no Brasil revela que regiões mais desenvolvidas possuem mais vagas, o que pode ser um reflexo das melhores oportunidades e infraestrutura dessas áreas. Em paralelo, embora a educação presencial continue predominante, a educação a distância está em expansão, oferecendo uma alternativa importante para estudantes em regiões com menos oportunidades.
Observou-se também que a faixa etária influencia o interesse e a oportunidade de iniciar os estudos, com uma tendência de diminuição do interesse conforme a idade aumenta. Este dado pode refletir a dificuldade em retornar aos estudos após um período prolongado fora do ambiente acadêmico ou a necessidade de priorizar outras responsabilidades.
No que tange à análise de gênero por curso de exatas, os dados mostram uma distribuição desigual entre os gêneros nas diferentes áreas. Cursos como Engenharia e Ciência da Computação tendem a ter uma maior predominância de ingressantes masculinos, enquanto áreas como Matemática e Química apresentam uma proporção mais equilibrada entre homens e mulheres. O gráfico de barras empilhadas ilustra claramente essas diferenças, evidenciando a necessidade de estratégias mais eficazes para promover a igualdade de gênero em cursos tradicionalmente dominados por um gênero específico.
Por fim, a análise da cor/raça revela que, mesmo com políticas de cotas raciais, a maioria dos estudantes em cursos de exatas ainda se identifica como branco. Este dado sugere que, apesar das políticas de inclusão, ainda existem desafios significativos a serem enfrentados para garantir uma representação mais equitativa de todas as raças e etnias no ensino superior.
Essas conclusões destacam a importância de continuar investindo em políticas educacionais que abordem as desigualdades regionais, de idade e de gênero, além de promover a inclusão racial para criar um ambiente acadêmico mais diversificado e igualitário.''')
pdf.output('C:\\archive\\relatorio_desigualdade_educacional.pdf')
