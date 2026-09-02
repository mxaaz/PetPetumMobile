# ApkaLapka-legal: strona i blog

Jekyll na GitHub Pages, live pod **https://apkalapka.pl** (`CNAME`). Repo trzyma stronę, blog
i dokumenty prawne aplikacji ApkaŁapka. **Kodu aplikacji ani surowego materiału tu nie ma.**

🔴 **Push = publikacja.** Nie ma tu środowiska testowego: co wypchniesz, to za chwilę widzi świat,
razem z dokumentami prawnymi. **Push robi wyłącznie USER.** Ty commitujesz i mówisz, że gotowe.

## Skąd się tu bierze treść

Artykuły pisze skill `blog-content`, uruchamiany w repo marketingowym
(`/mnt/matrix/RRepos/MyRepos/ApkaLapka/ApkaLapkaMarketing/`). Tam też leży komplet zasad marki,
zakazów prawnych i rejestr contentu. Post wydaniowy (changelog) generuje skill `release-prep`
z repo aplikacji. **Sam z siebie nie wymyślaj tematów: sprawdź najpierw, co już jest w `_posts/`.**

## Drip: daty z przyszłości są celowe

- `_config.yml` ma `future: false`, więc **post z datą jutrzejszą jest niewidoczny do swojego dnia**.
- Strona buduje się na push, a datowane posty odsłania **codzienny rebuild**
  (`.github/workflows/scheduled-rebuild.yml`, 07:15 UTC).
- Rytm: **co dwa dni, godzina 09:00 +0200**. Nowy post dostaje pierwszą wolną datę w tym rytmie,
  licząc od najpóźniejszego pliku w `_posts/`. Nie wsadzaj postów wstecz.
- Nazwa pliku: `YYYY-MM-DD-slug.md`, slug myślnikami, bez polskich znaków. Data w nazwie i w
  `date:` musi się zgadzać, inaczej Jekyll opublikuje post w innym dniu, niż myślisz.

## Front matter (komplet, nic nie pomijaj)

```yaml
title: "…"                 # w cudzysłowie, bez em dash
date: 2026-10-02 09:00:00 +0200
categories: [porady]       # porady | zdrowie | changelog
category_label: "Porady"   # etykieta wyświetlana
cover_style: grad-a        # grad-a…grad-d, przeplataj między sąsiednimi postami
emoji: "🐾"
read_time: 5
excerpt_text: "…"          # 1-2 zdania na kartę wpisu, ma zachęcać, nie streszczać
description: "…"           # meta SEO, konkretne frazy, jedno zdanie
```

## Reguły treści (te same co w marketingu)

- **ZERO em dash (U+2014).** Dwukropek, przecinek, nawias, kropka.
- **Poprawne polskie znaki** wszędzie, także w `description` i `excerpt_text`.
- **NIE MA „AI".** Aplikacja jest algorytmiczna (planer liczy DER i kcal). Zero „sztucznej
  inteligencji" i „rekomendacji AI" w treści.
- **Linia „organizer, nie diagnoza".** Artykuł zdrowotny kończy się miękkim odesłaniem do
  weterynarza. Terminy, dawki i decyzje należą do weterynarza, nie do aplikacji ani do tekstu.
- **ZERO fabrykacji.** Żadnych wymyślonych liczb, norm, dawek, cen i telefonów. Jakościowo
  („zwiększone pragnienie"), nie ilościowo.
- **Kontrola redakcyjna przy tematach zdrowotnych i bezpieczeństwa** (kleszcze, zoonozy, zatrucia,
  pierwsza pomoc): lista twierdzeń do potwierdzenia idzie do usera PRZED commitem. Powód formalny:
  `/mnt/matrix/RRepos/MyRepos/ApkaLapka/PetPetumMobile/.claude/reference/ai-act.md`.
- Marka odmienia się: „w ApkaŁapce", „z ApkaŁapki". Nazwy techniczne (pakiet, repo) zostają.

## Czego NIE ruszaj bez wyraźnej prośby

- `privacy.html`, `privacy-pl.html`, `terms.html`, `terms-pl.html`, `account-deletion.html` -
  dokumenty prawne, do których odsyłają sklepy. Zmiana treści = zmiana zobowiązania wobec userów.
- `app-ads.txt` i `app-ads/` - identyfikator AdMob. Literówka wyłącza monetyzację.
- `CNAME` - jedna linia trzymająca domenę. Skasowanie zdejmuje stronę z `apkalapka.pl`.
- `_layouts/`, `_includes/`, `assets/` - szablon i style. Zmieniasz wygląd tylko na polecenie.

## Konwencje

- Commity po polsku, `<type>: <opis>`, **bez trailerów**. Dla wpisów: `content: <opis>`.
- Jeden commit na paczkę postów, nie na plik.
- Zdjęcia i grafiki do wpisów: tylko materiał od usera (`ApkaLapkaMarketing/Media/`), nigdy generowane.
