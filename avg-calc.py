bgn = 'bgn'
ro_ro = 'ro_ro'
loaded_ro = 'loaded_ro'
en_en = 'en_en'
loaded_en = 'loaded_en'

sterge = 1
ro = 2
mate = 3
alta = 4
gata = 5
optiuni = 6

clear = 7
thesis = 8
other = 9
quit = 10
options = 11
info = 12

#
#	OTHER TRANSLATIONS CAN BE SUBMITTED TO andrei.hent@gmail.com
#	DO NOT SUBMIT IF YOU DON'T KNOW HOW TO MODIFY THE CODE
#

# Language selection / Selectarea limbajului

print('')
print('Language selection:')
print('Selectarea limbajului:')
print('1 - English')
print('2 - Romanian')
print('')
print('Note: The A-F grading system is not yet implemented.')
print('Nota: Sistemul de notare A-F nu este implementat deocamdata.')
print('')
if bgn == 'bgn':
	lang_selection = int(input('Language (number): '))

#
#	ENGLISH CODE
#

if lang_selection == 1:
	if en_en == 'en_en':
		print('')
		print('Write "thesis" to calculate your average grade (with thesis).')
		print('Write "other" to calculate your average grade.')
		print('')
		print('Write "info" for more details about this script. (Version, contact etc.)')
		print('')
		print('Write "quit" to close the script.')
		print('Write "options" to display this menu again.')
		print('')
		print('Write "clear" to remove the text from the terminal.')
		print('')
		print('If you are lacking some of the grades write "0" when you are asked for them.')
		print('')

#       The script starts.

	while loaded_en == 'loaded_en':
		cmd = int(input("Command: "))
	
#		End of script.
	
		if cmd == quit:
			break
	
#		Calculation of the average grade (with the thesis).
	
		elif cmd == thesis:
			print('')
			print("What is the total of your grades? (Minimum 4; Maximum 6)")
			print('')
	
#			The user specifies his / her total number of grades.
	
			all_grds = int(input("Number of grades: "))
	
#			If the user doesn't have [[ at least ]] four (4) grades, the script restarts.
	
			if all_grds < 4:
				print('')
				print('> Error: Not enough grades.')
				print('')
				break
	
#			As of now, this script supports a maximum of six (6) grades. If the user 	specifies that (s)he has [[ more ]] than 6 grades, the script restarts.
	
			elif all_grds > 6:
				print('')
				print('> Error: Too many grades.')
				print('')
				break
	
#			The user has to specify his / her grades. The only ones considered will be the 	ones he specified (s)he has. For example, if the user said he has 4 grades, only the first 4 will be 	considered. Regardless of what the grades five (5) and 6 are, they will not be taken into consideration.
	
			thesis = float(input("Thesis:   "))
			grd1 = float(input("Grade #1: "))
			grd2 = float(input("Grade #2: "))
			grd3 = float(input("Grade #3: "))
			grd4 = float(input("Grade #4: "))
			grd5 = float(input("Grade #5: "))
			grd6 = float(input("Grade #6: "))
		
#			The average grade is calculated.
	
			if all_grds == 4:
				avg = str(((grd1 + grd2 + grd3 + grd4) / 4 * 3 + thesis) / 4)
			elif all_grds == 5:
				avg = str(((grd1 + grd2 + grd3 + grd4 + grd5) / 5 * 3 + thesis) / 4)
			elif all_grds == 6:
				avg = str(((grd1 + grd2 + grd3 + grd4 + grd5 + grd6) / 6 * 3 + thesis) / 4)
	
#			The average grade is shown and the script restarts.
		
			print('')
			print('Your average grade is: ' + avg)
			print('')

#		Calculation of the average grade (without the thesis).

		elif cmd == other:
			print('')
			print('What is the total of your grades? (Minimum 2; Maximum 6)')
			print('')
	
#			The user specifies his / her total number of grades.
	
			all_grds = int(input("Number of grades: "))
	
#			If the user doesn't have [[ at least ]] two (2) grades, the script restarts.
	
			if all_grds < 2:
				print('')
				print('> Error: Not enough grades.')
				print('')
				break
	
#			As of now, this script supports a maximum of six (6) grades. If the user specifies that (s)he has [[ more ]] than 6 grades, the script restarts.

			elif all_grds > 6:
				print('')
				print('> Error: Too many grades.')
				print('')
				break
	
#			The user has to specify his / her grades. The only ones considered will be the ones he specified (s)he has. For example, if the user said he has 2 grades, only the first 2 will be considered. Regardless of what the grades three (3), 4, 5 and 6 are, they will not be taken into consideration.

			grd1 = float(input("Grade #1: "))
			grd2 = float(input("Grade #2: "))
			grd3 = float(input("Grade #3: "))
			grd4 = float(input("Grade #4: "))
			grd5 = float(input("Grade #5: "))
			grd6 = float(input("Grade #6: "))
	
#			The average grade is calculated.
	
			if all_grds == 2:
				avg = str((grd1 + grd2) / 2)
			elif all_grds == 3:
				avg = str((grd1 + grd2 + grd3) / 3)
			elif all_grds == 4:
				avg = str((grd1 + grd2 + grd3 + grd4) / 4)
			elif all_grds == 5:
				avg = str((grd1 + grd2 + grd3 + grd4 + grd5) / 5)
			elif all_grds == 6:
				avg = str((grd1 + grd2 + grd3 + grd4 + grd5 + grd6) / 6)
	
#			The average grade is shown.
	
			print('')
			print('Your average grade is: ' + avg)
			print('')

#		Information about the script is shown.
	
		elif cmd == info:
			print('')
			print('Author:    Hent Andrei')
			print('Version:   2.0')
			print('E-mail:    andrei.hent@gmail.com')
			print('This script was written in Python 2.7.9. The distribution and modifica	tion of the source code is allowed. If you encountered any problems while using the script you can contact me through the e-mail provided above.')
			print('')
	
		elif cmd == options:
			print('')
			print('Write "thesis" to calculate your average grade (with thesis).')
			print('Write "other" to calculate your average grade.')
			print('')
			print('Write "info" for more details about this script. (Version, contact etc.)')
			print('')
			print('Write "quit" to close the script.')
			print('Write "options" to display this menu again.')
			print('')
			print('Write "clear" to remove the text from the terminal.')
			print('')
			print('If you are lacking some of the grades write "0" when you are asked for them.')
			print('')

		elif cmd == clear:
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')

	else:
		print('')
		print('> Invalid command.')
		print('')

#
#	ROMANIAN CODE
#

if lang_selection == 2:
	if ro_ro == 'ro_ro':
		print('')
		print('Optiuni:')
		print('')
		print('Scrie "ro" sau "mate" ca sa iti calculezi media la lb. Romana sau matematica.')
		print('Scrie "alta" ca sa iti calculezi media la alta materie.')
		print('')
		print('Scrie "info" pentru detalii despre acest script. (Versiune, contact etc.)')
		print('')
		print('Scrie "gata" ca sa inchizi scriptul.')
		print('Scrie "optiuni" pentru a vedea acest meniu din nou.')
		print('')
		print('Scrie "sterge" ca sa stergi tot textul de pe terminal.')
		print('')
		print('Daca nu ai anumite note, scrie "0" cand ele iti sunt cerute.')
		print('')
	
#	Incepe scriptul.

	while loaded_ro == 'loaded_ro':
		comanda = int(input("Comanda: "))
	
#		Terminarea scriptului.
	
		if comanda == gata:
			print('')
			break
	
#		Calcularea mediei la limba Romana sau matematica.
	
		elif comanda == ro or comanda == mate:
			print('')
			print("Cate note ai in total la materia respectiva? (Minim 4; Maxim 6)")
			print('')
	
#			Utilizatorul precizeaza notele sale.
	
			tot = int(input("Numar note: "))
	
#			Daca utilizatorul nu are [[ cel putin ]] patru (4) note, i se specifica acest lucru si reincepe scriptul.
	
			if tot < 4:
				print('')
				print('> Error: Prea putine note.')
				print('')
				break
	
#			Deocamdata [[ maximul de note ]] care pot fi precizate este de sase (6). Daca utilizatorul specifica ca are [[ mai mult ]] de 6 note reincepe scriptul.
	
			elif tot > 6:
				print('')
				print('> Error: Prea multe note.')
				print('')
				break
	
#			Utilizatorul trebuie sa isi introduca notele. Vor fi luate in considerare doar cate a precizat ca are. De exemplu, daca utilizatorul a precizat ca are 4 note doar primele 4 vor fi luate in considerare. Orice valoare ar avea notele cinci (5) si 6, ele nu vor fi luate in considerare cand se va calucla media.

			teza = float(input("Teza:    "))
			nr1 = float(input("Nota #1: "))
			nr2 = float(input("Nota #2: "))
			nr3 = float(input("Nota #3: "))
			nr4 = float(input("Nota #4: "))
			nr5 = float(input("Nota #5: "))
			nr6 = float(input("Nota #6: "))
	
#			Se calculeaza media in functie de cate note a precizat utilizatorul ca are.
	
			if tot == 4:
				medie = str(((nr1 + nr2 + nr3 + nr4) / 4 * 3 + teza) / 4)
			elif tot == 5:
				medie = str(((nr1 + nr2 + nr3 + nr4 + nr5) / 5 * 3 + teza) / 4)
			elif tot == 6:
				medie = str(((nr1 + nr2 + nr3 + nr4 + nr5 + nr6) / 6 * 3 + teza) / 4)
	
#			Se afiseaza media si reincepe scriptul.
	
			print('')
			print('Media ta este: ' + medie)
			print('')
	
#		Calcularea mediei la alte materii.
	
		elif comanda == alta:
			print('')
			print('Cate note ai in total la materia respectiva? (Minim 2; Maxim 6)')
			print('')
	
#			Utilizatorul precizeaza notele sale.
	
			tot = int(input("Numar note: "))
	
#			Daca utilizatorul nu are [[ cel putin ]] doua (2) note, i se specifica acest lucru si reincepe programul.
	
			if tot < 2:
				print('')
				print('> Error: Prea putine note.')
				print('')
				break
	
#			Deocamdata [[ maximul de note ]] care pot fi precizate este de 6. Daca utilizatorul specifica ca are [[ mai mult ]] de 6 note reincepe programul.

			elif tot > 6:
				print('')
				print('> Error: Prea multe note.')
				print('')
				break
	
#			Utilizatorul trebuie sa isi introduca notele. Vor fi luate in considerare doar cate a precizat ca are. De exemplu, daca utilizatorul a precizat ca are 2 note doar primele 2 vor fi luate in considerare. Orice valoare ar avea notele trei (3), 4, 5 si 6, ele nu vor fi luate in considerare cand se va calucla media.

			nr1 = float(input("Nota #1: "))
			nr2 = float(input("Nota #2: "))
			nr3 = float(input("Nota #3: "))
			nr4 = float(input("Nota #4: "))
			nr5 = float(input("Nota #5: "))
			nr6 = float(input("Nota #6: "))
	
#			Se calculeaza media in functie de cate note a precizat utilizatorul ca are.
	
			if tot == 2:
				medie = str((nr1 + nr2) / 2)
			elif tot == 3:
				medie = str((nr1 + nr2 + nr3) / 3)
			elif tot == 4:
				medie = str((nr1 + nr2 + nr3 + nr4) / 4)
			elif tot == 5:
				medie = str((nr1 + nr2 + nr3 + nr4 + nr5) / 5)
			elif tot == 6:
				medie = str((nr1 + nr2 + nr3 + nr4 + nr5 + nr6) / 6)
	
#			Se afiseaza media si reincepe scriptul.
	
			print('')
			print('Media ta este: ' + medie)
			print('')

#		Se afiseaza detalii despre acest program.
	
		elif comanda == info:
			print('')
			print('Autor:     Hent Andrei')
			print('Versiune:  2.0')
			print('E-mail:    andrei.hent@gmail.com')
			print('Acest script a fost scris in Python 2.7.9. Distribuirea si modificare codului sursa sunt permise. Daca ati avut parte de probleme in timpul folosirii acestui script, ma puteti contacta prin e-mailul furnizat mai sus.')
			print('')

		elif comanda == optiuni:
			print('')
			print('Optiuni:')
			print('')
			print('Scrie "ro" sau "mate" ca sa iti calculezi media la lb. Romana sau matematica.')
			print('Scrie "alta" ca sa iti calculezi media la alta materie.')
			print('')
			print('Scrie "info" pentru detalii despre acest script. (Versiune, contact etc.)')
			print('')
			print('Scrie "gata" ca sa inchizi scriptul.')
			print('')
			print('Scrie "sterge" ca sa stergi tot textul de pe terminal.')
			print('')
			print('Daca nu ai anumite note, scrie "0" cand ele iti sunt cerute.')
			print('')

		elif comanda == sterge:
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')
			print('')

		else:
			print('')
			print('> Comanda invalida.')
			print('')

#
#	OTHER TRANSLATIONS CAN BE SUBMITTED TO andrei.hent@gmail.com
#	DO NOT SUBMIT IF YOU DON'T KNOW HOW TO MODIFY THE CODE
#
