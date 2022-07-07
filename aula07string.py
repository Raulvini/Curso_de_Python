#------testando a função uppper e lower-------#
curso = "Curso de python"

palavra ="Python" 

res = palavra.lower() in curso.lower()

print(res)

res = palavra.upper() in curso.upper()

print(res)
print(curso[9:15].upper())

#--------Usando o metodo format----------#
cidade = "belo Horizonte"
dia = 15 
mes ="Dezembro"
ano = 2019
data = "{},{} de {} de {}"

print(data.format(cidade,dia,mes,ano))

#-----------usando o print(f)--------------#

print(f"{cidade}, {dia} de {mes} de {ano}")