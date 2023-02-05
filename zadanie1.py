inflacja_styczen_2023 = 1.59282448436825
inflacja_luty_2023 = -0.453509101198007
inflacja_marzec_2023 = 2.32467171712441
inflacja_kwiecien_2023 = 1.26125440724877
inflacja_maj_2023 = 1.78252628571251
inflacja_czerwiec_2023 = 2.32938454145522
inflacja_lipiec_2023 = 1.50222984223283
inflacja_sierpien_2023 = 1.78252628571251
inflacja_wrzesien_2023 = 2.32884899407637
inflacja_pazdziernik_2023 = 0.616921348207244
inflacja_listopad_2023 = 2.35229588637833
inflacja_grudzien_2023 = 0.337779545187098
inflacja_styczen_2024 = 1.57703524727525
inflacja_luty_2024 = -0.292781442607648
inflacja_marzec_2024 = 2.48619659017508
inflacja_kwiecien_2024 = 0.267110317834564
inflacja_maj_2024 = 1.41795267229799
inflacja_czerwiec_2024 = 1.05424326726375
inflacja_lipiec_2024 = 1.4805201044812
inflacja_sierpien_2024 = 1.57703524727525
inflacja_wrzesien_2024 = -0.0774206903147018
inflacja_pazdziernik_2024 = 1.16573339872354
inflacja_listopad_2024 = -0.404186717638335
inflacja_grudzien_2024 = 1.49970852083123
wartosc_kredytu = float(input ("Wprowadź wartość kredytu: "))
oprocentowanie = float(input ("Wprowadź wartość oprocentowania: "))
stala_rata = float(input ("Wprowadź wartość stałej raty: "))
#styczeń23
poprzedni_miesiac = wartosc_kredytu
pozostala_kwota_styczen2023 = (1+((inflacja_styczen_2023+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_styczen2023 = poprzedni_miesiac - pozostala_kwota_styczen2023
print (f" Styczeń 2023: Twoja pozostała kwota kredytu to {pozostala_kwota_styczen2023}, to {round (roznica_kredytu_styczen2023, ndigits=2)} to mniej niż w poprzednim miesiącu")
#luty23
poprzedni_miesiac = pozostala_kwota_styczen2023
pozostala_kwota_luty2023 = (1+((inflacja_luty_2023+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_luty2023 = poprzedni_miesiac - pozostala_kwota_luty2023
print (f" Luty 2023: Twoja pozostała kwota kredytu to {pozostala_kwota_luty2023}, to {round (roznica_kredytu_luty2023, ndigits=2)} to mniej niż w poprzednim miesiącu")
#marzec23
poprzedni_miesiac = pozostala_kwota_luty2023
pozostala_kwota_marzec2023 = (1+((inflacja_marzec_2023+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_marzec2023 = poprzedni_miesiac - pozostala_kwota_marzec2023
print (f" Marzec 2023: Twoja pozostała kwota kredytu to {pozostala_kwota_marzec2023}, to {round (roznica_kredytu_marzec2023, ndigits=2)} to mniej niż w poprzednim miesiącu")
#kwiecień23
poprzedni_miesiac = pozostala_kwota_marzec2023
pozostala_kwota_kwiecien2023 = (1+((inflacja_kwiecien_2023+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_kwiecien2023 = poprzedni_miesiac - pozostala_kwota_kwiecien2023
print (f" Kwiecień 2023: Twoja pozostała kwota kredytu to {pozostala_kwota_kwiecien2023}, to {round (roznica_kredytu_kwiecien2023, ndigits=2)} to mniej niż w poprzednim miesiącu")
#maj23
poprzedni_miesiac = pozostala_kwota_kwiecien2023
pozostala_kwota_maj2023 = (1+((inflacja_maj_2023+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_maj2023 = poprzedni_miesiac - pozostala_kwota_maj2023
print (f" Maj 2023: Twoja pozostała kwota kredytu to {pozostala_kwota_maj2023}, to {round (roznica_kredytu_maj2023, ndigits=2)} to mniej niż w poprzednim miesiącu")
#czerwiec23
poprzedni_miesiac = pozostala_kwota_maj2023
pozostala_kwota_czerwiec2023 = (1+((inflacja_czerwiec_2023+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_czerwiec2023 = poprzedni_miesiac - pozostala_kwota_czerwiec2023
print (f" Czerwiec 2023: Twoja pozostała kwota kredytu to {pozostala_kwota_czerwiec2023}, to {round (roznica_kredytu_czerwiec2023, ndigits=2)} to mniej niż w poprzednim miesiącu")
#lipiec23
poprzedni_miesiac = pozostala_kwota_czerwiec2023
pozostala_kwota_lipiec2023 = (1+((inflacja_lipiec_2023+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_lipiec2023 = poprzedni_miesiac - pozostala_kwota_lipiec2023
print (f" Lipiec 2023: Twoja pozostała kwota kredytu to {pozostala_kwota_lipiec2023}, to {round (roznica_kredytu_lipiec2023, ndigits=2)} to mniej niż w poprzednim miesiącu")
#sierpien23
poprzedni_miesiac = pozostala_kwota_lipiec2023
pozostala_kwota_sierpien2023 = (1+((inflacja_sierpien_2023+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_sierpien2023 = poprzedni_miesiac - pozostala_kwota_sierpien2023
print (f" Sierpień 2023: Twoja pozostała kwota kredytu to {pozostala_kwota_sierpien2023}, to {round (roznica_kredytu_sierpien2023, ndigits=2)} to mniej niż w poprzednim miesiącu")
#wrzesien23
poprzedni_miesiac = pozostala_kwota_sierpien2023
pozostala_kwota_wrzesien2023 = (1+((inflacja_wrzesien_2023+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_wrzesien2023 = poprzedni_miesiac - pozostala_kwota_wrzesien2023
print (f" Wrzesień 2023: Twoja pozostała kwota kredytu to {pozostala_kwota_wrzesien2023}, to {round (roznica_kredytu_wrzesien2023, ndigits=2)} to mniej niż w poprzednim miesiącu")
#pazdziernik23
poprzedni_miesiac = pozostala_kwota_wrzesien2023
pozostala_kwota_pazdziernik2023 = (1+((inflacja_pazdziernik_2023+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_pazdziernik2023 = poprzedni_miesiac - pozostala_kwota_pazdziernik2023
print (f" Październik 2023: Twoja pozostała kwota kredytu to {pozostala_kwota_pazdziernik2023}, to {round (roznica_kredytu_pazdziernik2023, ndigits=2)} to mniej niż w poprzednim miesiącu")
#listopad23
poprzedni_miesiac = pozostala_kwota_pazdziernik2023
pozostala_kwota_listopad2023 = (1+((inflacja_listopad_2023+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_listopad2023 = poprzedni_miesiac - pozostala_kwota_listopad2023
print (f" Listopad 2023: Twoja pozostała kwota kredytu to {pozostala_kwota_listopad2023}, to {round (roznica_kredytu_listopad2023, ndigits=2)} to mniej niż w poprzednim miesiącu")
#grudzień23
poprzedni_miesiac = pozostala_kwota_listopad2023
pozostala_kwota_grudzien2023 = (1+((inflacja_grudzien_2023+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_grudzien2023 = poprzedni_miesiac - pozostala_kwota_grudzien2023
print (f" Grudzień 2023: Twoja pozostała kwota kredytu to {pozostala_kwota_grudzien2023}, to {round (roznica_kredytu_grudzien2023, ndigits=2)} to mniej niż w poprzednim miesiącu")
#styczeń24
poprzedni_miesiac = pozostala_kwota_grudzien2023
pozostala_kwota_styczen2024 = (1+((inflacja_styczen_2024+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_styczen2024 = poprzedni_miesiac - pozostala_kwota_styczen2024
print (f" Styczeń 2024: Twoja pozostała kwota kredytu to {pozostala_kwota_styczen2024}, to {round (roznica_kredytu_styczen2024, ndigits=2)} to mniej niż w poprzednim miesiącu")
#luty24
poprzedni_miesiac = pozostala_kwota_styczen2024
pozostala_kwota_luty2024 = (1+((inflacja_luty_2024+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_luty2024 = poprzedni_miesiac - pozostala_kwota_luty2024
print (f" Luty 2024: Twoja pozostała kwota kredytu to {pozostala_kwota_luty2024}, to {round (roznica_kredytu_luty2024, ndigits=2)} to mniej niż w poprzednim miesiącu")
#marzec24
poprzedni_miesiac = pozostala_kwota_luty2024
pozostala_kwota_marzec2024 = (1+((inflacja_marzec_2024+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_marzec2024 = poprzedni_miesiac - pozostala_kwota_marzec2024
print (f" Marzec 2024: Twoja pozostała kwota kredytu to {pozostala_kwota_marzec2024}, to {round (roznica_kredytu_marzec2024, ndigits=2)} to mniej niż w poprzednim miesiącu")
#kwiecień24
poprzedni_miesiac = pozostala_kwota_marzec2023
pozostala_kwota_kwiecien2024 = (1+((inflacja_kwiecien_2024+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_kwiecien2024 = poprzedni_miesiac - pozostala_kwota_kwiecien2024
print (f" Kwiecień 2024: Twoja pozostała kwota kredytu to {pozostala_kwota_kwiecien2024}, to {round (roznica_kredytu_kwiecien2024, ndigits=2)} to mniej niż w poprzednim miesiącu")
#maj24
poprzedni_miesiac = pozostala_kwota_kwiecien2024
pozostala_kwota_maj2024 = (1+((inflacja_maj_2024+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_maj2024 = poprzedni_miesiac - pozostala_kwota_maj2024
print (f" Maj 2024: Twoja pozostała kwota kredytu to {pozostala_kwota_maj2024}, to {round (roznica_kredytu_maj2024, ndigits=2)} to mniej niż w poprzednim miesiącu")
#czerwiec24
poprzedni_miesiac = pozostala_kwota_maj2024
pozostala_kwota_czerwiec2024 = (1+((inflacja_czerwiec_2024+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_czerwiec2024 = poprzedni_miesiac - pozostala_kwota_czerwiec2024
print (f" Czerwiec 2024: Twoja pozostała kwota kredytu to {pozostala_kwota_czerwiec2024}, to {round (roznica_kredytu_czerwiec2024, ndigits=2)} to mniej niż w poprzednim miesiącu")
#lipiec24
poprzedni_miesiac = pozostala_kwota_czerwiec2024
pozostala_kwota_lipiec2024 = (1+((inflacja_lipiec_2024+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_lipiec2024 = poprzedni_miesiac - pozostala_kwota_lipiec2024
print (f" Lipiec 2024: Twoja pozostała kwota kredytu to {pozostala_kwota_lipiec2024}, to {round (roznica_kredytu_lipiec2024, ndigits=2)} to mniej niż w poprzednim miesiącu")
#sierpien24
poprzedni_miesiac = pozostala_kwota_lipiec2024
pozostala_kwota_sierpien2024 = (1+((inflacja_sierpien_2024+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_sierpien2024 = poprzedni_miesiac - pozostala_kwota_sierpien2024
print (f" Sierpień 2024: Twoja pozostała kwota kredytu to {pozostala_kwota_sierpien2024}, to {round (roznica_kredytu_sierpien2024, ndigits=2)} to mniej niż w poprzednim miesiącu")
#wrzesien24
poprzedni_miesiac = pozostala_kwota_sierpien2024
pozostala_kwota_wrzesien2024 = (1+((inflacja_wrzesien_2024+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_wrzesien2024 = poprzedni_miesiac - pozostala_kwota_wrzesien2024
print (f" Wrzesień 2024: Twoja pozostała kwota kredytu to {pozostala_kwota_wrzesien2024}, to {round (roznica_kredytu_wrzesien2024, ndigits=2)} to mniej niż w poprzednim miesiącu")
#pazdziernik24
poprzedni_miesiac = pozostala_kwota_wrzesien2024
pozostala_kwota_pazdziernik2024 = (1+((inflacja_pazdziernik_2024+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_pazdziernik2024 = poprzedni_miesiac - pozostala_kwota_pazdziernik2024
print (f" Październik 2024: Twoja pozostała kwota kredytu to {pozostala_kwota_pazdziernik2024}, to {round (roznica_kredytu_pazdziernik2024, ndigits=2)} to mniej niż w poprzednim miesiącu")
#listopad24
poprzedni_miesiac = pozostala_kwota_pazdziernik2024
pozostala_kwota_listopad2024 = (1+((inflacja_listopad_2024+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_listopad2024 = poprzedni_miesiac - pozostala_kwota_listopad2024
print (f" Listopad 2024: Twoja pozostała kwota kredytu to {pozostala_kwota_listopad2024}, to {round (roznica_kredytu_listopad2024, ndigits=2)} to mniej niż w poprzednim miesiącu")
#grudzień24
poprzedni_miesiac = pozostala_kwota_listopad2024
pozostala_kwota_grudzien2024 = (1+((inflacja_grudzien_2024+oprocentowanie)/wartosc_kredytu)) * poprzedni_miesiac - stala_rata
roznica_kredytu_grudzien2024 = poprzedni_miesiac - pozostala_kwota_grudzien2024
print (f" Grudzień 2024: Twoja pozostała kwota kredytu to {pozostala_kwota_grudzien2024}, to {round (roznica_kredytu_grudzien2024, ndigits=2)} to mniej niż w poprzednim miesiącu")