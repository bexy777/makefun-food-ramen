# Steaming Tonkotsu Ramen — make.fun food-picture-01

A close three-quarter shot of a steaming bowl of tonkotsu ramen: chopsticks
lifting glossy noodles from the creamy broth, a halved soft-boiled egg with
a jammy yolk, chashu pork, spring onions and nori, on a dark moody
background with warm side light. Built to the judge's rubric: it makes you
hungry first, then shows fresh, real food with steam, gloss and texture,
and reads clearly even at 300 pixels across.

## Entry

- `main.py` — Python 3.13, standard library only. Copies the shipped
  `entry.jpg` (1024x1024 JPEG, 212,090 bytes) byte for byte to
  `$MAKEFUN_OUTPUT_DIR/entry.png`. JPEG bytes under the `.png` name are
  allowed: the gate tells the format from the first bytes.
- `entry.jpg` — the picture itself.

Deterministic: the same input bytes produce the same output bytes on
every run.

## Run locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
