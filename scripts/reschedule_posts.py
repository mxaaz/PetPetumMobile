#!/usr/bin/env python3
"""Przelicza daty postów z kolejki (data z przyszłości) wg rytmu z _config.yml.

Rytm żyje w jednym miejscu: `drip_interval_days` i `drip_time` w `_config.yml`.
Pierwszy post z kolejki dostaje datę: najpóźniejszy już opublikowany post + interwał,
kolejne co interwał. Posty `changelog` i `spolecznosc` mają daty związane z wydaniem
lub z opiekunem pupila, więc ich nie ruszamy.

Domyślnie tylko pokazuje plan. Zmiany wchodzą z `--apply` (git mv + poprawka `date:`).
"""
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "_posts"
FIXED = {"changelog", "spolecznosc"}


def config(key):
    m = re.search(rf"^{key}:\s*\"?([^\"\n#]+?)\"?\s*(#.*)?$", (ROOT / "_config.yml").read_text(), re.M)
    if not m:
        sys.exit(f"Brak `{key}` w _config.yml")
    return m.group(1).strip()


def front(path):
    text = path.read_text()
    date = re.search(r"^date:\s*(\d{4}-\d{2}-\d{2})", text, re.M).group(1)
    cat = re.search(r"^categories:\s*\[(\w+)", text, re.M).group(1)
    return dt.date.fromisoformat(date), cat, text


def main():
    interval = int(config("drip_interval_days"))
    time = config("drip_time")  # np. "09:00:00 +0200"
    today = dt.date.today()

    posts = sorted(POSTS.glob("*.md"))
    published = [front(p)[0] for p in posts if front(p)[0] <= today]
    queue = [p for p in posts if front(p)[0] > today and front(p)[1] not in FIXED]
    anchor = max(d for p in posts if (d := front(p)[0]) <= today and front(p)[1] not in FIXED)

    print(f"Interwał {interval} dni, godzina {time}, ostatni opublikowany {anchor}, w kolejce {len(queue)}")
    for i, p in enumerate(queue, 1):
        new = anchor + dt.timedelta(days=interval * i)
        old, _, text = front(p)
        target = POSTS / f"{new.isoformat()}-{p.name[11:]}"
        print(f"{old} -> {new}  {p.name[11:]}")
        if "--apply" not in sys.argv or target == p:
            continue
        text = re.sub(r"^date:.*$", f"date: {new.isoformat()} {time}", text, count=1, flags=re.M)
        p.write_text(text)
        subprocess.run(["git", "mv", str(p), str(target)], check=True, cwd=ROOT)
    if "--apply" not in sys.argv:
        print("(podgląd; dodaj --apply, żeby zapisać)")


if __name__ == "__main__":
    main()
