#with open('iris.data', 'r') as f:
#	print(f.readlines())

# with open('iris.data', 'r') as f:
# 	for linha in f.readlines():
# 		print(linha)


# with open('iris.data', 'r') as f:
# 	conteudo = f.read()
# 	print(conteudo)


with open('iris.data', 'r') as f:
	lista = f.read().splitlines()


print(len(lista))

print(lista[2])


print(lista[-10:])

