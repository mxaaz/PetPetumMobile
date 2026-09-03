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

## Ton strony: ApkaŁapka + Ty (decyzja usera 2026-09-02)

Strona ma dwie strefy i dwa głosy. Granica: czy po drugiej stronie stoi narzędzie, czy człowiek
z firmy.

**Strefa produktowa** (`index.html`, listingi bloga i changelogu): podmiotem czynności jest
**ApkaŁapka**, adresatem **Ty**.

- ✅ „ApkaŁapka porządkuje terminy, przypomina w porę i pokazuje trendy w zdrowiu pupila."
- ✅ „ApkaŁapka pilnuje tego, co ważne, między wizytami u weterynarza."
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

Poniżej hero `body` ma krem `--bg` plus wzór `assets/page-pattern.svg`: łapki i drobne listki
zielonym tuszem `--green`, jedna warstwa, kafel 260 px. **Krycie 0,30 dla łapek i 0,22 dla
listków** (decyzja usera 2026-09-03). Wcześniejsze podejścia na 0,032 i 0,020 były praktycznie
niewidoczne, user chciał wzoru, który widać. Okręgów nie ma, czytały się jak bąble.

Ceną za to krycie jest to, że nagłówki sekcji i linia rozwiązania stoją wprost na łapkach.
Jeśli kiedyś to zacznie przeszkadzać, są dwa wyjścia: zejść z kryciem do 0,20-0,22 albo dołożyć
kremową poświatę pod te dwa bloki tekstu, zamiast ruszać wzór.

Wzór widać tylko między sekcjami, bo hero, pasek zaufania, karty i stopka mają własne
nieprzezroczyste tła.

Stronę domyka `.page-foot-art` tuż nad stopką: `assets/page-foot.webp`, czyli ta sama akwarela co
w hero odbita w poziomie (`-flop`), więc kot i pies siedzą po prawej. `aspect-ratio: 2365/448`
trzyma wysokość elementu równą renderowanej wysokości grafiki, dzięki czemu wygaszona górna
krawędź nigdy nie zostaje ucięta. Poniżej 880 px stała wysokość 150 px, bo przy proporcji pas
schodziłby do kilkudziesięciu pikseli.

Blog i changelog jadą na `assets/css/blog.css` i tego wzoru **nie mają**. Jak będziesz to
ujednolicał, przenieś tam ten sam blok `background` z `index.html`.

## Konwencje

- Commity po polsku, `<type>: <opis>`, **bez trailerów**. Dla wpisów: `content: <opis>`.
- Jeden commit na paczkę postów, nie na plik.
- Zdjęcia i grafiki do wpisów: tylko materiał od usera (`ApkaLapkaMarketing/Media/`), nigdy generowane.
