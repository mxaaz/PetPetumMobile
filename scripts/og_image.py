"""Grafika do udostępniania (og:image) 1200x630: assets/og-image.jpg.

Akwarela z hero (assets/hero-bg.webp), ikona i fonty strony. Uruchom z katalogu repo:
  uv run --no-project --with fonttools --with brotli --with pillow python scripts/og_image.py
Przeglądarka headless nie startuje na tej maszynie, stąd Pillow zamiast zrzutu HTML.
Fonty strony są podzielone na latin i latin-ext (Ł, ą, ż...), więc tekst idzie kawałkami.
"""
import os, sys, tempfile
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = tempfile.mkdtemp()
for name in ('newsreader', 'hanken-grotesk'):
    for sub in ('latin', 'latin-ext'):
        f = TTFont(f'{R}/assets/fonts/{name}-{sub}.woff2'); f.flavor = None
        f.save(f'{S}/{name}-{sub}.ttf')
def inst(name, loc, out):
    for sub in ('latin', 'latin-ext'):
        f = TTFont(f'{S}/{name}-{sub}.ttf')
        instantiateVariableFont(f, loc, inplace=True)
        f.save(f'{S}/{out}-{sub}.ttf')
inst('newsreader', {'wght': 600, 'opsz': 72}, 'ns600')
inst('newsreader', {'wght': 700, 'opsz': 72}, 'ns700')
inst('hanken-grotesk', {'wght': 450}, 'hg450')
def fonts(key, size):
    return (ImageFont.truetype(f'{S}/{key}-latin.ttf', size), ImageFont.truetype(f'{S}/{key}-latin-ext.ttf', size))
def runs(text):
    out = []
    for ch in text:
        ext = 0x100 <= ord(ch) <= 0x2BA
        if out and out[-1][0] == ext: out[-1][1] += ch
        else: out.append([ext, ch])
    return out
def draw_text(d, xy, text, fs, fill):
    x, y = xy
    for ext, s in runs(text):
        f = fs[1] if ext else fs[0]
        d.text((x, y), s, font=f, fill=fill, anchor='ls')
        x += d.textlength(s, font=f)
    return x
W, H = 1200, 630
img = Image.new('RGB', (W, H), '#EAEAE3').convert('RGBA')
# dwa miękkie mycia jak w hero
wash = Image.new('RGBA', (W, H), (0, 0, 0, 0)); wd = ImageDraw.Draw(wash)
wd.ellipse((-500, -500, 760, 340), fill=(146, 186, 155, 70))
wd.ellipse((640, -460, 1700, 300), fill=(146, 186, 155, 52))
img = Image.alpha_composite(img, wash.filter(ImageFilter.GaussianBlur(120)))
band = Image.open(f'{R}/assets/hero-bg.webp').convert('RGBA')
band = band.resize((W, round(band.height * W / band.width)), Image.LANCZOS)
img.alpha_composite(band, (0, H - band.height))
icon = Image.open(f'{R}/icon.png').convert('RGBA').resize((76, 76), Image.LANCZOS)
mask = Image.new('L', (76 * 4, 76 * 4), 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, 76 * 4 - 1, 76 * 4 - 1), 19 * 4, fill=255)
icon.putalpha(Image.composite(icon.getchannel('A'), Image.new('L', (76, 76), 0), mask.resize((76, 76), Image.LANCZOS)))
sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((84, 70, 160, 146), 19, fill=(45, 74, 62, 55))
img = Image.alpha_composite(img, sh.filter(ImageFilter.GaussianBlur(9)))
img.alpha_composite(icon, (84, 66))
d = ImageDraw.Draw(img)
green = '#2D4A3E'
draw_text(d, (178, 120), 'ApkaŁapka', fonts('ns700', 46), green)
draw_text(d, (82, 238), 'Książeczka zdrowia', fonts('ns600', 80), green)
draw_text(d, (82, 318), 'psa i kota', fonts('ns600', 80), green)
draw_text(d, (86, 374), 'Przypomnienia, dziennik opieki i wyniki badań. Android i iOS.', fonts('hg450', 28), '#4D5A50')
img.convert('RGB').save(f'{R}/assets/og-image.jpg', quality=86, optimize=True, progressive=True)
print('zapisano assets/og-image.jpg')
