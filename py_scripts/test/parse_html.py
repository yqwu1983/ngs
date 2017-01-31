# -*- coding:utf8 -*-

from BeautifulSoup import BeautifulSoup

html = """ 
<html>
	<table>
		<tr>
			<td class="one">Some SOme</td>
			<td>SomeSOme</td>
		</tr>

		<tr>
			<td class="one">S omeSOme</td>
			<td>SomeSOme</td>
		</tr>

		<tr>
			<td class="one">SomeSO me</td>
			<td>SomeSOme</td>
		</tr>

		<tr>
			<td>SomeSOme</td>
			<td>другое последнее</td>
		</tr>
	</table>
</html>
"""

# parsed_html = BeautifulSoup(html)
# for tr in parsed_html.findAll('tr'):
# 	td = tr.find('td', { 'class': 'one' })
# 	if td:
# 		td.extract()

# print str(parsed_html)

def parse_html(filename):
	f = open(filename, 'r')
	parsed = BeautifulSoup(f.read())
	f.close()
	return parsed

def fetch_tables(html):
	tables = html.findAll('table')
	return tables[1:len(tables)]

def fetch_tds(tr, lshift):
	tds = tr.findAll('td')
	return tds[lshift:len(tds)]

def find_row(table, tr, lshfift):
	tds = fetch_tds(tr, lshfift)
	for table_tr in table.findAll('tr'):
		if fetch_tds(table_tr, lshfift) == tds:
			return True
	return False

def handle_tables(table_1, table_2, lshift):
	trs = table_1.findAll('tr')
	trs = trs[2:len(trs)]

	for tr in trs:
		if find_row(table_2, tr, lshift):
			tr.extract()
			# tr['style'] = 'background-color: red;'
	return 0

html_1 = '/home/anna/bioinformatics/outdirs/mut9/BL21-Ecoli-mut9/breseq_out/output/index.html'
html_2 = '/home/anna/bioinformatics/outdirs/mut6/BL21-Ecoli-mut6/breseq_out_BL21-mut6/output/index.html'

html_1 = parse_html(html_1)
html_2 = parse_html(html_2)

tables_1 = fetch_tables(html_1)
tables_2 = fetch_tables(html_2)

handle_tables(tables_1[0], tables_2[0], 1)
handle_tables(tables_1[1], tables_2[1], 3)
handle_tables(tables_1[2], tables_2[2], 3)

f = open('/home/anna/bioinformatics/outdirs/mut9/BL21-Ecoli-mut9/breseq_out/output/index_compare.html', 'w')
f.write(str(html_1))
f.close()




