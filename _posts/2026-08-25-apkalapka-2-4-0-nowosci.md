---
title: "ApkaŁapka 2.4.0: klinika pod ręką, zaległości w jednym miejscu"
date: 2026-08-25 10:00:00 +0200
categories: [changelog]
category_label: "Nowości"
cover_style: grad-a
emoji: "🗺️"
read_time: 4
excerpt_text: "Klinikę z mapy zapiszesz jako kontakt jednym tapnięciem, zaległe wpisy odhaczysz na jednym ekranie, a powiadomień jest mniej, nie więcej."
description: "ApkaŁapka 2.4.0: mapa klinik weterynaryjnych z zapisem kontaktu, wyszukiwanie po nazwie, ekran Do potwierdzenia, mniej powiadomień, kreator pupila, diety weterynaryjne i poprawki synchronizacji."
---

Poprzednia duża aktualizacja przebudowała przypomnienia. Ta zajmuje się tym, co dzieje się wokół nich: szukaniem kliniki, nadrabianiem zaległości i wyciszaniem tego, co nie musi się odzywać. 🐾

## Klinikę z mapy zapisujesz, zamiast ją przepisywać

Mapa klinik weterynaryjnych dostała to, czego brakowało jej od początku: znalezioną lecznicę zapisujesz jako swój kontakt jednym tapnięciem. Nazwa, adres, telefon i mail przenoszą się same, godziny otwarcia i strona lądują w notatce. Wcześniej mapa była wyłącznie przeglądarką, więc dane trzeba było przepisać ręcznie do formularza.

Przy okazji naprawiliśmy błąd, przez który ekran mapy potrafił pokazać czarne tło z uciętym w połowie arkuszem zamiast mapy. Pinezki są teraz takie same jak w wyborze lokalizacji, czyli łapki, a nie krzyże, więc obie mapy w aplikacji wyglądają spójnie.

## Wyszukiwanie po nazwie, nie tylko w promieniu

Do tej pory jedynym sposobem znalezienia kliniki było przeszukanie okolicy wokół siebie. To działa, dopóki jesteś w domu. Teraz wpisujesz nazwę i znajdujesz lecznicę także wtedy, gdy jesteś w innym mieście albo dopiero się tam wybierasz.

Wyniki są rozdzielone na dwie sekcje: kliniki i miejsca. To nie jest kosmetyka. Wyszukiwanie miejsc opiera się na geokoderze, który potrafi na zapytanie „weterynarz Lublin" oddać wynik oddalony o sto pięćdziesiąt kilometrów, więc mieszanie obu list w jedną wprowadzałoby w błąd.

Samo szukanie jest też wyraźnie szybsze. Aplikacja odpytuje teraz serwery map równolegle zamiast po kolei, więc jeden wolny serwer nie zjada całego czasu oczekiwania. A gdy naprawdę nie uda się nic pobrać, zobaczysz „Nie udało się pobrać klinik" z możliwością ponowienia, a nie mylące „Brak klinik weterynaryjnych" w mieście pełnym lecznic.

## Adres otwiera się w Twoich mapach

Tapnięcie w adres kliniki prowadzi teraz do map systemowych: na iPhonie do Map Apple, na Androidzie do systemowego wyboru aplikacji. Jeśli nie masz zainstalowanych Map Google, nadal trafisz tam, gdzie trzeba.

## Wszystko, co czeka na odhaczenie, na jednym ekranie

Nowy ekran „Do potwierdzenia" zbiera w jednym miejscu karmienia, dawki i wpisy, które minęły bez potwierdzenia. Wchodzisz tam stałym wejściem z paska na panelu głównym, a nie tylko z powiadomienia.

Dwie rzeczy, które wychodzą z codziennego używania: przy odhaczaniu poprawisz godzinę, jeśli posiłek odbył się wcześniej, niż go zapisujesz, a przy karmieniu doszło „Pomiń dziś" na dni, w których po prostu nie było jak. Tapnięcie w treść powiadomienia otwiera właściwy ekran wraz z oknem potwierdzenia, co wcześniej nie działało dla części typów przypomnień.

## Powiadomień jest mniej

To jest zmiana, której nie widać na liście funkcji, a robi największą różnicę w tym, czy aplikację da się wytrzymać dłużej niż kilka dni.

Dopytki milkną same, gdy przestajesz na nie odpowiadać, i wracają, gdy znów coś potwierdzisz. Doszedł dobowy limit powiadomień na pupila, więc żaden dzień nie zamienia się w serię przypomnień. Zniknęło codzienne powiadomienie o 20:00, które każdego wieczoru mówiło to samo, a jego miejsce zajęła krótka informacja o tym, czego dziś faktycznie brakuje, doklejona do wieczornego podsumowania. O nawodnieniu aplikacja odzywa się teraz raz, a nie trzy razy w jeden wieczór.

Zadbaliśmy też o coś odwrotnego: przypomnienia o kuwecie i badaniu serca wracają po wyczyszczeniu kolejki powiadomień, zamiast milczeć aż do kolejnego wpisu.

## Krótki kreator po dodaniu pupila

Po dodaniu zwierzaka aplikacja przeprowadza Cię przez pięć kroków, które ustawiają pory karmienia i przypomnienia od razu. Zapis następuje raz, na końcu, więc przerwanie w połowie niczego nie zostawia w połowie. W zapasach, lekach i wydatkach doszły krótkie checklisty „jak to działa" dla tych, którzy nie wiedzą, od czego zacząć.

## Karma, zapasy i diety weterynaryjne

Własną karmę, dodaną spoza bazy, oznaczysz teraz jako dietę weterynaryjną. W sekcji odżywczej doszły sód i wapń oraz przeliczenie na suchą masę, dzięki czemu porównanie dwóch karm o różnej wilgotności ma sens.

Cena karmy kupowanej w opakowaniu zbiorczym jest przeliczana na pojedynczą sztukę, więc koszt dzienny się zgadza. Karma dodawana z linku zaciąga komplet danych, a nie ich fragment.

<div class="callout vet">Dane o żywieniu i zdrowiu w aplikacji to dziennik opieki, a nie diagnoza. Dobór diety weterynaryjnej skonsultuj z weterynarzem.</div>

## Skasowane naprawdę znika

Ta poprawka dotyczy każdego, kto używa aplikacji na koncie chmurowym, i była najtrudniejsza do zauważenia. Jeśli wyczyściłeś notatkę przy ważeniu, numer chipa w profilu albo instrukcję przy leku, pole znikało na tym telefonie, ale wracało na drugim urządzeniu i po ponownej instalacji aplikacji. Przyczyna siedziała w sposobie wysyłania zmian do chmury: puste pole po prostu nie było wysyłane, więc chmura trzymała starą wartość.

Objęliśmy tym dwadzieścia trzy rodzaje wpisów, od leków i wizyt przez kontakty weterynaryjne po wydatki i zapasy. Przy okazji wyszło, że cofnięcie odhaczenia wizyty jako odbytej też nie docierało do drugiego urządzenia, więc wizyta zostawała tam zamknięta na zawsze.

## Nawodnienie czytelniej

W panelu choroby przewlekłej karta nawodnienia przestała pokazywać „0 ml" i czerwony pasek komuś, kto codziennie zapisuje picie jakościowo, bez odmierzania mililitrów. Zamiast tego streszcza dni z wpisem i rozkład poziomów. Doszedł filtr zakresu dat na liście wpisów, a pod ikoną aplikacji skrót do szybkiego zapisania wody.

## Co jeszcze nowego

- Pusty ekran kontaktów weterynaryjnych ma teraz dwa wyjścia zamiast samego napisu: dodanie kontaktu i znalezienie kliniki na mapie.
- Mail weryfikacyjny przy zakładaniu konta przychodzi w języku aplikacji, a nie zawsze po polsku.
- Nazwa ApkaŁapka i adresy stron są spójne wszędzie tam, gdzie widzi je użytkownik.
- Na Androidzie aplikacja korzysta z pełnej wysokości ekranu zgodnie z bieżącymi zaleceniami sklepu.
- Na iPhonie aplikacja nie prosi już o dostęp do lokalizacji w tle, bo do niczego go nie potrzebuje.
