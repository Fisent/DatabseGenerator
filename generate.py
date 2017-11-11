import models
import randoms

print(models.get_dyzur())
print(models.get_pracownik())
print(models.get_pracownik_na_dyzurze())
print(models.get_karetka())

choroba = models.get_schorzenie()
print(choroba)
print(randoms.get_typ_schorzenia(choroba))
print(models.get_pracownik())

