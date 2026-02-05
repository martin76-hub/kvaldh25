lause1= "Kui Arno isaga koolimajja jõudis olid tunnid juba alanud. Arno roomas vargsi mööda klassitoa seinaäärt suure kapi juurde, kus õpetaja Laur maakaarte ja muid koolitarbeid hoidis ning puges kapi alla peitu."
lause2= "Mu isamaa mu õnn ja rõõm kui kaunis oled sa. Ei leia mina iial tääl see suure laia ilma peal, mis mul nii armas oleks ka kui sa mu isamaa"

#Leia T-testi abil, kes nende lausete sõnade keskmine pikkus erineb üldistavalt

sonad1=lause1.split()
sonad2=lause2.split()
print(sonad1)
print(sonad2)


pikkus1 = [len(sona) for sona in sonad1]
pikkus2 = [len(sona) for sona in sonad2]

print("Lause 1 sõnade pikkused:", pikkus1) 
print("Lause 2 sõnade pikkused:", pikkus2)

mitusona1 = len(sonad1)

lause1keskmine = sum(pikkus1) / mitusona1
print ("Esimese lause keskmine sõna pikkus on", lause1keskmine)

mitusona2 = len(sonad2)

lause2keskmine = sum(pikkus2) / mitusona2
print ("Teise lause keskmine sõna pikkus on", lause2keskmine)

