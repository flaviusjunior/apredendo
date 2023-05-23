
from datetime import date
ano = int(input("\nDidite o ano: ou '0' para ano atual. "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("\nEsse ano {} é Bissexto". format(ano))
else:
    print("Esse ano {} não é Bissexto!\n".format(ano))