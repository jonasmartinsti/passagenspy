tentativas = ['A>C','A>C','A>C','B>D','B>D','B>D','B>D','B>D','A>B','A>B','A>B','A>B','B>C','B>C','B>C','B>C','B>C','A>D','A>D','A>D','A>D','A>D','A>D','A>D','A>D','A>D','C>D','C>D','C>D','C>D','C>D','C>D','C>D','C>D','B>D','B>D','B>D','B>D','B>C','B>C','B>C','A>C','A>B','A>B','B>C','B>C','B>C','A>C','C>D','C>D','C>D','C>D','C>D','C>D','C>D','B>D','B>D','B>D','B>D','A>B','A>B','A>B','A>B','A>B','A>B','A>B','A>B','A>B','A>B','A>B','A>C','A>C','A>C','A>C','A>C','A>C','A>C','A>C','A>C','A>C','A>D','C>D','C>D','C>D','C>D','B>D','B>D','B>D','B>D','B>D','A>B','A>B','A>C','A>C','A>C','C>D','C>D','A>B','A>B','A>D']

ab = []
bc = []
cd = []

poltronas = 45

i = 0

for tentativa in tentativas:

	i = i + 1

	if (tentativa == 'A>B' and len(ab) < poltronas): 
		ab += [i]

	if (tentativa == 'A>C' and len(ab) < poltronas and len(bc) < poltronas):
		ab += [i]
		bc += [i]

	if (tentativa == 'A>D' and len(ab) < poltronas and len(bc) < poltronas and len(cd) < poltronas):
		ab += [i] 
		bc += [i]
		cd += [i]

	if (tentativa == 'B>C' and len(bc) < poltronas):
		bc += [i]

	if (tentativa == 'B>D' and len(bc) < poltronas and len(cd) < poltronas):
		bc += [i]
		cd += [i]

	if (tentativa == 'C>D' and len(cd) < poltronas):
		cd += [i]

	if (i in ab or i in bc or i in cd):
		print (i , ' - ', tentativa , ' - VENDER')
	else:
		print (i , ' - ', tentativa , ' - NAO VENDER')