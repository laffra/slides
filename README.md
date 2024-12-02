# Slides with PyScript/LTK

This project is a slide player to show slides from a PDF.

## Generating the slides from a PDF

On a command line Python runtime do:

```
pip install -r requirements.txt
python convert_pdf.py
```

This loads `slides.pdf` from the local file system and generates 1 PNG per page.

## Rendering the slides

Open `index.html` in a browser. A live preview can be seen on [GitHub Pages](https://laffra.github.io/slides/).
This runs a Python UI, written in PyScript LTK, to show the slides and navigate between them.

## Navigating slides

- Full Screen mode: f
- Prev slide: j, PageUP, Backspace, ArrowUp, ArrowLeft
- Next slide: k, PageDown, Enter, Space, ArrowDown, ArrowRight
- Goto slide: 1, 2, 3, 4, 5, 6, 7, 8, 9
- Goto start: Home
- Goto end: End
