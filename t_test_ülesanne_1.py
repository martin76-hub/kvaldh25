#Andmestikeks on Venemaa ja USA sõjavägede aastased kulutused dollarites aastatel 1992-2024.

from scipy.stats import ttest_ind

venemaa_kulutused = (47565.8, 41580.9, 39308.2, 25863.3, 24420.9, 26698.7, 15877.5, 17632.3, 23790.0, 25709.9, 28481.2, 29863.6, 31213.9, 35471.7, 39261.8, 42736.6, 46957.9, 49267.7, 50269.3, 53649.2, 62160.8, 65190.1, 69865.8, 75301.2, 80726.1, 65414.1, 62949.4, 65771.0, 67316.2, 68649.8, 88877.4, 109203.6, 150534.0)
ameerika_kulutused = (705819.7, 668046.7, 633319.1, 591579.8, 559401.2, 556507.3, 543941.3, 545279.8, 566381.0, 570981.0, 641102.5, 729680.6, 795293.5, 831923.9, 843911.7, 866430.5, 929457.8, 1002596.4, 1031257.1, 1019045.9, 962443.2, 888413.2, 833765.0, 814831.4, 812331.0, 803961.2, 828158.3, 875217.4, 916416.6, 906594.3, 896121.2, 916014.7, 968381.6)

print("Venemaa kulutused:", venemaa_kulutused)
print("USA kulutused:", ameerika_kulutused)

vene_keskmine = sum(venemaa_kulutused) / len(venemaa_kulutused)
usa_keskmine = sum(ameerika_kulutused) / len(ameerika_kulutused)

print("Venemaa keskmine aastane kulutus:", vene_keskmine) 
print("USA keskmine aastane kulutus:", usa_keskmine) 

tulemus = ttest_ind(venemaa_kulutused, ameerika_kulutused) 
print("T-testi tulemus:", tulemus)

#T_testi tulemused näitavad, et erinevus ei ole juhuslik — see on äärmiselt tugev ja selge.
# USA kulutused on kordades suuremad kui Venemaa omad.

#T‑test on meetod kahe rühma keskmiste võrdlemiseks.
# See toimib hästi siis, kui andmed on ligikaudu normaalsed, rühmad sõltumatud ja valimid piisavalt suured.
# T‑test ei sobi väga väikeste valimite, tugevalt viltuste jaotuste, sõltuvate rühmade või kategooriliste andmete korral.