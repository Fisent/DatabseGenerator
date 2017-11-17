import models
import randoms

print(models.get_dyzur())
print(models.get_pracownik())
print(models.get_pracownik_na_dyzurze())
print(models.get_karetka())

choroba = models.get_choroba()
print(choroba)
print(randoms.get_typ_schorzenia(choroba))
print(models.get_pracownik())

print(models.get_typy_schorzenia())
print(randoms.get_adres())

