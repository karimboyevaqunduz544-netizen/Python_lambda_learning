def daraja(n):
	return lambda x : x** n
kvadrat = daraja(2)
kub = daraja(3)
print(f" 3ning kvadrati {kvadrat(3)}ga , kubi {kub(3)}ga teng")
#3ning kvadrati 9ga , kubi 27ga teng
