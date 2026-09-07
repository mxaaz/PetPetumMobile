---
title: "ApkaŁapka 2.4.3: mapa klinik bez czekania"
date: 2026-09-07 10:00:00 +0200
categories: [changelog]
category_label: "Nowości"
cover_style: grad-a
emoji: "🏥"
read_time: 3
excerpt_text: "Mapa klinik weterynaryjnych to teraz jeden ekran, który pokazuje wyniki od razu. Do tego zdjęcia w galerii zostają na miejscu po aktualizacji iPhone'a."
description: "ApkaŁapka 2.4.3: jedna mapa klinik zamiast dwóch, koniec czekania na GPS, zdjęcia z galerii przeżywają aktualizację iPhone'a, pełne nazwy pól w edytorze karmy."
---

To wydanie w całości wzięło się ze zgłoszeń. Dwa przysłaliście nam wprost, resztę wyłapaliśmy z raportów o niespodziewanych zamknięciach aplikacji i z przeglądu ekranów na wąskich telefonach. 🐾

## Jedna mapa klinik zamiast dwóch

Do tej pory ta sama czynność wyglądała inaczej zależnie od tego, skąd otwierało się mapę. Z listy kontaktów weterynaryjnych dostawało się mapę do przeglądania okolicy, a przy zapisywaniu nowego kontaktu, osobną mapę, na której dało się tylko wskazać punkt. Dwa ekrany, dwa różne zestawy przycisków, ta sama baza klinik pod spodem.

Teraz jest jeden ekran. Przeglądasz na nim okolicę, a gdy wchodzisz na niego z formularza kontaktu, ten sam widok pozwala wybrać klinikę i wrócić z jej danymi.

## Koniec czekania na GPS

Mapa potrafiła zostać na komunikacie o ustalaniu położenia i nie pokazać niczego, mimo że kliniki były już pobrane. Zdarzało się to najczęściej w budynku, gdzie telefon długo szuka dokładnej pozycji.

Zmieniliśmy kolejność: aplikacja czeka na położenie najwyżej chwilę, zadowala się przybliżoną dokładnością, a jeśli i to nie przyjdzie na czas, korzysta z ostatniej znanej pozycji. Wyniki pojawiają się od razu.

## Zdjęcia w galerii zostają na miejscu

Na iPhonie każda aktualizacja systemu zmienia wewnętrzny adres, pod którym aplikacja trzyma swoje pliki. Zdjęcia dodane do galerii zapisywały ten adres na sztywno, więc po aktualizacji przestawały się wyświetlać, choć fizycznie nadal leżały w telefonie.

Poprawiliśmy sposób zapisu, a przy pierwszym uruchomieniu tej wersji przenosimy również starsze wpisy. Jedno zastrzeżenie: ratujemy zdjęcia, które nadal da się odnaleźć. Jeśli komuś zniknęły przy wcześniejszych aktualizacjach, te nie wrócą.

## Co jeszcze nowego

- Potwierdzenie posiłku z planu, do którego nie przypisano karmy, nie zamyka już aplikacji. Takie plany tworzy między innymi kreator przy dodawaniu pupila, więc dotyczyło to osób dopiero zaczynających.
- Przyciski w oknach z pytaniem („Anuluj", „Kontynuuj") nie zamykają aplikacji, nawet gdy w tle zmieni się stan konta.
- W edytorze karmy widać pełne nazwy pól zamiast „Popi…", „Wilg…" i „Fosf…". To samo poprawiliśmy w ustawieniach przypomnień i w oknie uzupełniania zapasu.
- Statystyki cyklu rui mają wreszcie polskie znaki.

<div class="callout vet">
Dane o zdrowiu w aplikacji to dziennik opieki, a nie diagnoza. W razie niepokojących objawów skonsultuj się z weterynarzem.
</div>

Aktualizacja pojawi się w sklepach w ciągu najbliższych dni. Nic nie trzeba robić, wystarczy pozwolić na automatyczną aktualizację.
