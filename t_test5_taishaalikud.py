from scipy.stats import ttest_ind
lause1= "Kui Arno isaga koolimajja jõudis olid tunnid juba alanud. Arno roomas vargsi mööda klassitoa seinaäärt suure kapi juurde, kus õpetaja Laur maakaarte ja muid koolitarbeid hoidis ning puges kapi alla peitu."
lause2= "Mu isamaa mu õnn ja rõõm kui kaunis oled sa. Ei leia mina iial tääl see suure laia ilma peal, mis mul nii armas oleks ka kui sa mu isamaa"

th="aeiouõäöü"
print(lause1.lower())
print(len([t for t in lause2 if t in th]))

def t_arv(sona):
    return len([t for t in sona if t in th])


print(t_arv("kalamaja"))
arvud1=[t_arv(sona) for sona in lause1.lower().split()]
print(arvud1)

arvud2=[t_arv(sona) for sona in lause2.lower().split()]
print(arvud2)

print(ttest_ind(arvud1, arvud2))

def keskmine(m):
    return sum(m)/len(m)

print(keskmine(arvud1), keskmine(arvud2))
