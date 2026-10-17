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
- Rytm siedzi w `_config.yml` (`drip_interval_days`, `drip_time`), obecnie **co 4 dni, 09:00 +0200**
  (decyzja usera 2026-09-21, bo tematy się kończyły). Nowy post dostaje pierwszą wolną datę w tym
  rytmie, licząc od najpóźniejszego pliku w `_posts/`. Zmiana rytmu: popraw `_config.yml` i puść
  `python3 scripts/reschedule_posts.py --apply` (przelicza kolejkę, pomija `changelog` i `spolecznosc`). Nie wsadzaj postów wstecz.
- Nazwa pliku: `YYYY-MM-DD-slug.md`, slug myślnikami, bez polskich znaków. Data w nazwie i w
  `date:` musi się zgadzać, inaczej Jekyll opublikuje post w innym dniu, niż myślisz.

## Front matter (komplet, nic nie pomijaj)

```yaml
title: "…"                 # w cudzysłowie, bez em dash
date: 2026-10-02 09:00:00 +0200
categories: [porady]       # porady | zdrowie | changelog | spolecznosc
category_label: "Porady"   # etykieta wyświetlana ("Poznajcie pupili" dla spolecznosc)
cover_style: grad-a        # grad-a…grad-d, przeplataj między sąsiednimi postami
emoji: "🐾"
read_time: 5
excerpt_text: "…"          # 1-2 zdania na kartę wpisu, ma zachęcać, nie streszczać
description: "…"           # meta SEO, konkretne frazy, jedno zdanie
```

**Kategoria `spolecznosc` („Poznajcie pupili")** to wpisy o pupilach, których opiekunowie korzystają
z ApkaŁapki. Ma własną zakładkę `/poznajcie-pupili/` w nawigacji i stopce. Pisze się je własnymi
słowami na podstawie faktów od opiekuna, bez kopiowania ich opisów z Instagrama, i **bez słowa
„współpraca"**: pupil korzysta z ApkaŁapki (decyzja usera 2026-09-11).

## Ton strony: ApkaŁapka + Ty (decyzja usera 2026-09-02)

Strona ma dwie strefy i dwa głosy. Granica: czy po drugiej stronie stoi narzędzie, czy człowiek
z firmy.

**Strefa produktowa** (`index.html`, listingi bloga i changelogu): podmiotem czynności jest
**ApkaŁapka**, adresatem **Ty**.

- ✅ „ApkaŁapka porządkuje terminy, przypomina w porę i pokazuje trendy w zdrowiu pupila."
- ✅ „ApkaŁapka pomaga pilnować tego, co ważne, między wizytami u weterynarza."
- ✅ „ApkaŁapka nie sprzedaje Twoich danych."
- ❌ „Pomożemy", „zadbamy", „pilnujemy za Ciebie", „z nami", „nasza aplikacja".

Powód: nazwa marki wybrzmiewa, zamiast znikać w „my"; obietnica dotyczy narzędzia, nie opieki, więc
trzyma linię „organizer, nie diagnoza"; ton zostaje uprzejmy, bez skracania dystansu.

**Strefa firmowa** (`faq.html`, dokumenty prawne, kontakt, treść wpisów): „my" jest tu na miejscu,
bo odzywa się firma do człowieka. „Zbieramy wyłącznie dane, które sam/a wprowadzasz", „Staramy się
odpowiadać w ciągu 24 godzin".

**Emoji: nie w nagłówkach.** Zero emoji w `h1`, `h2` i w eyebrow. Wolno w kaflach, tagach, chipach
i na okładkach wpisów, bo tam niosą lekkość, a nie nadają tonu.

**Zmieniasz copy? Zmień OBIE wersje językowe.** `index.html` trzyma PL i EN w jednym pliku
(`<span class="pl">` / `<span class="en">`), a `faq.html` w dwóch osobnych sekcjach `#lang-en`
i `#lang-pl`. Zgubiona para zostawia polskie zdanie na angielskiej wersji strony.

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
- `hero.jpg` - generowana półfotorealistyczna ilustracja psa i kota z 15.06.2026. **Nie jest już
  używana** i nie podpinaj jej z powrotem: hero ma akwarelowy pas `assets/hero-bg.webp`. Fotorealizm
  odpada zawsze, patrz `ai-act.md`.
- `hero2.jpeg` - źródło akwareli, z niego wycięty jest `assets/hero-bg.webp`. Nie podpinaj źródła
  bezpośrednio w CSS: nie ma wygaszonej góry i waży 15 razy więcej.
- `assets/hero-pattern.svg` - wzór wektorowy z podejścia sprzed 2026-09-03, nieużywany przez nic.

## Hero na stronie głównej

**Hero jest jasny** (decyzja usera 2026-09-03): papier `#EAEAE3`, tekst `--green-dark`, nav nad hero
ciemny bez cienia. Nie ma trybu ciemnego na stronie i nie było - jeśli ktoś raportuje, że tło się
nie zmienia po przełączeniu motywu, to wtyczka w przeglądarce, nie błąd.

Tło to akwarelowy pas `assets/hero-bg.webp` (kot i pies, gałązki, łapki, serce z kreski) przyklejony
do dołu w pełnej szerokości, nad nim dwa miękkie mycia w CSS. Źródło ma proporcję 5,28:1, więc
**świadomie nie ma tu `cover`**: kadrowanie do wysokości hero (815 px przy 1920 i 1440) pokazałoby
tylko środkowe 45% szerokości i ucięłoby kota i psa przy lewej krawędzi. `100% auto` pokazuje całą
szerokość zawsze, a przy 1920 px pas renderuje się jako 1920x364, czyli w pomniejszeniu - ostro.

Górna krawędź grafiki jest **wygaszona w alfie** (gradient na 150 px z 448), dlatego pas przechodzi
w papier bez widocznej linii cięcia. Stąd WebP z przezroczystością zamiast JPEG-a i stąd brak
fallbacku PNG: ten sam plik w PNG waży 1,3 MB wobec 37 KB.

Trzy szerokości, trzy zachowania: powyżej 880 px `100% auto` na dole; 520-880 px `auto 190px`, bo
makieta telefonu schodzi pod tekst i pas musi być niższy niż ona; poniżej 520 px `300% auto` z
kotwicą `left bottom`, żeby w wąskim kadrze zostali kot i pies. W obu wariantach mobilnych hero ma
`padding-bottom: 168px` - bez tego telefon przykrywa zwierzaki.

Zmieniasz to? **Sprawdzaj zrzutem przy 1920, 1440, 768, 560 i 390 px.** Zwierzaki mają być widoczne
i nieprzykryte na każdej z nich, a przejście pasa w papier niewidoczne.

## Tło reszty strony

Poniżej hero `body` ma krem `--bg` plus `assets/page-paws.webp`: kafel 520 px z 20 akwarelowymi
łapkami **wyciętymi z `hero2.jpeg`**, czyli z tej samej grafiki co hero.

**Łapki widać tylko przy lewej i prawej krawędzi okna.** Na wzór nałożona jest zasłona w kolorze
kremu, `linear-gradient(to right, ...)` z pełnym kryciem między 23% a 77% szerokości. W środkowym
pasie, gdzie stoi treść, wzór gaśnie do zera. Bez tej zasłony łapki szły pod tekst i całość robiła
się nieczytelna (zgłoszenie usera 2026-09-03).

**Same procenty nie wystarczą** (poprawka 2026-09-23): przy 390 px zasłona 23–77% zostawiała po
~90 px wzoru z każdej strony, dokładnie pod tekstem wpisu. Dlatego stopy są liczone przez
`min(23%, calc(50% - 400px))` i `max(77%, calc(50% + 400px))` (analogicznie 7%/93% z ±500 px):
pełne krycie nigdy nie jest węższe niż 800 px wokół środka. Poniżej ~800 px zasłona kryje całą
szerokość, powyżej ~1480 px działają same procenty, więc desktop wygląda jak wcześniej. Ten sam
blok siedzi w `index.html` i `assets/css/blog.css`: zmieniasz jeden, zmień drugi.

**Nie rysuj tu łapki wektorowo.** Próbowaliśmy (SVG z czterech kółek i owalu, krycie 0,02, potem
0,30) i za każdym razem gryzło się z hero: akwarela ma wydłużone paluchy, nieregularną poduszkę
i rozmyte krawędzie, geometryczny odpowiednik wygląda przy niej jak z innej strony. Za mocne
krycie to nie był problem samego krycia, tylko kształtu (obserwacja usera 2026-09-03).

Jak odtworzyć kafel: wytnij łapkę z `hero2.jpeg`, zrób alfę z jasności (`-colorspace gray
-negate -level 9%,24%`), **dociśnij resztkę alfy do zera** (`-channel A -level 14%,100%`) i dopiero
wtedy obracaj. Bez tego ostatniego kroku papier zostaje na 11% krycia i po obrocie widać wokół
każdej łapki prostokątną poświatę. Łapki rozrzucone losowo z minimalnym odstępem 92 px i
marginesem od krawędzi kafla, więc kafel klei się bez szwu; siatka rzędów wychodzi widoczna,
jeśli rozmieszczać je równomiernie.

Wzór widać tylko między sekcjami, bo hero, pasek zaufania, karty i stopka mają własne
nieprzezroczyste tła.

Stronę domyka `.page-foot-art` tuż nad stopką: `assets/page-foot.webp`, czyli ta sama akwarela co
w hero, ale **z dolnych 340 px źródła** i odbita w poziomie (`-flop`), więc kot i pies siedzą po
prawej. Wycinek jest węższy niż w hero, bo pełne 448 px zostawiało nad pasem szeroki jałowy pas
papieru i user zgłosił to jako dziurę w układzie (2026-09-03). Z tego samego powodu sekcja
`#download` ma `padding-bottom: 18px` zamiast domyślnych 78 px.

**Wygaszenie górnej krawędzi rozciągnij na 200 px z 340.** Papier w grafice jest zieleńszy od kremu
strony, więc przy krótkim wygaszeniu (próbowaliśmy 100 px) różnica tonu układa się w poziomą
krawędź przez całą szerokość okna. Przy 200 px rozkłada się niepostrzeżenie.

`aspect-ratio: 2365/340` trzyma wysokość elementu równą renderowanej wysokości grafiki, dzięki
czemu wygaszona górna krawędź nigdy nie zostaje ucięta. Poniżej 880 px stała wysokość 150 px, bo
przy proporcji pas schodziłby do kilkudziesięciu pikseli.

Blog, changelog i FAQ jadą na `assets/css/blog.css`, który ma ten sam blok `background`
przeniesiony z `index.html` (od commitu „łapki w tle na blogu i changelogu"), więc wzór łapek
jest tam już spójny ze stroną główną - nic nie trzeba migrować.

## Zrzuty aplikacji i ikony

- Strona ładuje `screens/*.webp` (600x1300, około 25 KB sztuka). `screens/*.jpg` (944x2046) to źródła:
  nowy zrzut wrzucasz jako JPG i robisz z niego WebP
  (`magick X.jpg -resize 600x -strip -quality 80 -define webp:method=6 X.webp`).
- `report`, `bloodtests`, `health` i `cardio` mają jeden plik bez prefiksu języka, bo wersje
  PL i EN były identyczne (oba po polsku). Angielski zrzut podmienia się jako `en-<nazwa>.webp`.
- Każdy `<img>` zrzutu ma `width`/`height` i `loading="lazy"`, oprócz polskiego zrzutu w hero
  (`fetchpriority="high"`). Bez lazy przeglądarka ściągała też ukryte makiety i drugi język.
- `icon.png` (512 px) zostaje do logo w JSON-LD. **`og:image` to `assets/og-image.jpg`** (1200x630,
  akwarela z hero, od 2026-10-17): domyślne dla wszystkich stron przez `defaults` w `_config.yml`,
  na stronie głównej wpisane ręcznie w `<head>`. Odtwarzasz skryptem `scripts/og_image.py`.
  Wpis może mieć własne `image:` w front matter i wtedy ono wygrywa. Na stronie wisi `icon-180.png`
  (nawigacja, hero, apple-touch) i `icon-64.png` (favicona, stopka).

## Konwencje

- Commity po polsku, `<type>: <opis>`, **bez trailerów**. Dla wpisów: `content: <opis>`.
- Jeden commit na paczkę postów, nie na plik.
- Zdjęcia i grafiki do wpisów: tylko materiał od usera (`ApkaLapkaMarketing/Media/`), nigdy generowane.

## Strona główna: układ od 2026-10-11

Kolejność: hero → pasek → **Sytuacje** (`#sytuacje`, 4 pytania opiekuna i odpowiedź aplikacji) →
**Co jest w środku** (`#features`, 12 kafli + telefon) → **Opinie** (`#opinie`) → **Od twórcy**
(`#od-tworcy`) → cennik → FAQ → blog → CTA. Wycięte: „Znasz to uczucie?”, „I wiele więcej”,
„Konkrety na wizytę”, „Choroba przewlekła”, „Dlaczego ApkaŁapka” (decyzja usera: krótsza strona,
mniej ogólników). Przebudowa po pojawieniu się konkurenta lapaapp.pl: z niego wolno brać tylko
układ, **nigdy tekstów ani grafik**.

- **Słowa „PDF” nie używamy** w treści strony (user 2026-10-11): „raport dla weterynarza”.
- **Copy Sytuacji bez straszenia i bez obiecywania tego, czego aplikacja nie widzi** (user
  2026-10-12): aplikacja nie wie, czy kot był w kuwecie, wie tylko to, co wpiszesz, więc odpowiedź
  zaczyna się od wpisu. Nie eksponować alertów o krwi: lepiej „z Twoich wpisów liczy normę i daje
  znać, gdy coś odbiega”. Bez wydumanych słów („worek”, „składa raport”), pisz tak, jak mówi opiekun.
- **Sytuacje:** każde zdanie sprawdzone w `PetPetumMobile/.claude/features/` (komentarz w HTML
  podaje pliki). Zmieniasz zdanie albo aplikacja zmieniła działanie → sprawdź ponownie.
- **Kafle:** plakietka Premium tylko przy tym, co jest w `kPremiumFeatures` (`premium_screen.dart`).
  Opis kafla mówi, co konkretnie zrobisz i co zobaczysz, z listą rzeczy wziętą z aplikacji (np. Pulpit
  wymienia kafle do wyboru z `quick_access_customize_screen.dart`). Bez oczywistości w rodzaju „działa
  po restarcie telefonu” (user 2026-10-12). Kafel nazywa się „Pulpit”, jak zakładka w aplikacji.
  Na desktopie telefon sam przechodzi po kaflach (pasek postępu pod aktywnym), dopóki kursor nie
  wejdzie na siatkę. Na telefonie dotknięcie kafla rozwija jego zrzut.
- **Opinie:** wyłącznie prawdziwe, cytowane dosłownie ze sklepów, z datą „Stan z”. **Nigdy opinii
  z konta twórcy** (MxaaZx w App Store). Oceny 5,0 / 4,9 są statyczne: aktualizuj je razem z datą
  (też w linii pod przyciskami w hero). Bez `aggregateRating` w JSON-LD.
- **Od twórcy:** jedyny głos „ja” na stronie głównej (stąd „Napisz do mnie”, nie „do nas”). Tekst
  podyktowany przez usera 2026-10-12. Zdjęcia przenikają się co 3,5 s od kociaka do dziś
  (`#founder-photos`, rusza dopiero w kadrze, przy `prefers-reduced-motion` stoi obecne):
  `czesia-kociak-1` z `mrugacz.jpeg` (wycięta broda człowieka u góry), `-2` z `spi_z_lapkami.jpeg`,
  `-3` z `głodzilla.jpeg` (wycięty klapek z logo FILA), na koniec `czesia.webp` z `Czesia_profil.jpeg`.
- **„Też w środku”:** eksport i usuwanie danych (RODO) zdjęte 2026-10-12, bo żyją w FAQ. Doszły SOS,
  wydatki, pielęgnacja i ubezpieczenie. Pielęgnacja dostanie własny kafel po przebudowie funkcji
  (backlog aplikacji).
- **Tropy łapek** (`.paw-trail`): `assets/paw.webp` to pojedyncza łapka wycięta z `hero2.jpeg`
  przepisem z sekcji o tle. W hero idą od kota i psa w prawo, w CTA w górę. Poniżej 880 px ukryte,
  bo w jednej kolumnie weszłyby pod telefon. Przy `prefers-reduced-motion` stoją.
- **Tropy wzdłuż strony** (`.side-trails`, od 2026-10-12, prośba usera „więcej łapek, też niżej”):
  skrypt rysuje dla każdej sekcji `main` (bez `#download`) trop schodzący w dół lewym marginesem
  i drugi, z opóźnieniem, prawym. Odcinki się stykają, więc trop idzie przez całą stronę. Działa tylko przy
  marginesie ≥ 110 px (z prawej liczonym bez paska ikon), czyli od ok. 1180 px szerokości.
  **Zagęszczenie i rozmiary** (user 2026-10-12): margines dzieli się na pasy po ok. 170 px, najwyżej
  dwa na stronę (przy 1920 px po dwa z każdej, przy 1440 px po jednym), krok co 60 px. Łapki mają trzy
  rozmiary (42, 32, 24 px) **wymieszane w obrębie każdego tropu** (losowanie z ziarnem, stały układ po
  resize). Pierwsza wersja miała do trzech pasów, każdy z łapką jednego rozmiaru: user ocenił, że za
  gęsto i że „ślaczek małych, ślaczek średnich, ślaczek dużych” wygląda słabo.
  Trop jest pocięty na odcinki po 8 kroków i każdy rusza sam, gdy wjedzie w kadr (a stoi poza kadrem):
  wcześniej cały odcinek sekcji startował od jej góry i w środku długiej sekcji długo nie było nic.
  **W hero** te same tropy (`.hero-trails`, rysuje je ten sam skrypt) chodzą po pustym tle nad akwarelą:
  jednym tropem między nawigacją a ikoną (w prawo, do telefonu) i bokami w dół, kończąc nad akwarelowym pasem.
  Stare statyczne tropy przy kocie i psie zostały.
  **Tam, gdzie są tropy, stały wzór `page-paws.webp` na stronie głównej znika** (`body.has-trails`):
  ta sama akwarela w obu warstwach zlewała się i animacji nie było widać. Węższe okna mają wzór
  jak dawniej.
  **Na podstronach** (blog, wpisy, Nowości, Poznajcie pupili, FAQ, 404, od 2026-10-13, zgłoszenie
  usera „na blogu łapki stoją”) te same tropy rysuje `assets/js/paw-trails.js`, podpięty w
  `_layouts/default.html`, a style siedzą w `assets/css/blog.css`. Margines liczony od kolumny
  1080 px (`.wrap`, `.related`), więc tropy ruszają od ok. 1260 px szerokości; we wpisie startują
  pod kolorową okładką. Skrypt jest kopią logiki z `index.html`: zmieniasz jeden, zmień drugi.
- **Telefon w hero** przewija 6 ekranów co 3,2 s (kropki pod spodem), stoi pod kursorem i przy
  `prefers-reduced-motion`.
- **Zrzuty 2026-10-11** (z `ApkaLapkaMarketing/Media/Aplikacja/nowe/`): nowe `pl-today`, `pl-calendar`,
  `pl-weight`, `pl-litter`, `pl-hydration`. Kuweta i nawodnienie nie mają wersji EN, więc angielska
  strona pokazuje polski zrzut. 2026-10-12 doszedł nowy `pl-supplies` z markami karm (Animonda,
  Bozita) w kadrze: user kazał wrzucić bez kadrowania. `en-supplies` zostaje stary, po angielsku.
  Planer i przypomnienia nadal stare (nowe też pokazują marki, decyzja usera).
- Lokalny `jekyll build` nie działa (2026-10-11: brak gemu `eventmachine` po aktualizacji Ruby).
  Podgląd: kopia `index.html` bez bloku Liquid bloga, otwarta z `file://`.
