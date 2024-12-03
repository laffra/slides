# Slides with PyScript/LTK

This project is a slide player to show slides from a PDF. 

See a live example of
[Chris Laffra's PyData Global slides](https://laffra.github.io/slides/) for the
[PyScript tutorial on Dec 4, 2024](https://global2024.pydata.org/cfp/talk/XXWRWP/).

## Generating the slides from a PDF

On a command line Python runtime do:

```
pip install -r requirements.txt
python convert_pdf.py
```

This will do the following:
 - Ask for a Google Slides URL.
 - Download the PDF version.
 - Load the PDF and generate 1 PNG per page.
 - Save the PNGs in the `slides` directory.

## Rendering the slides

Open `index.html` in a browser. 
This runs a Python UI, written in PyScript LTK, to show the slides and navigate between them.

## Navigating slides

- Full Screen mode: f
- Prev slide: j, PageUP, Backspace, ArrowUp, ArrowLeft
- Next slide: k, PageDown, Enter, Space, ArrowDown, ArrowRight
- Goto slide: 1, 2, 3, 4, 5, 6, 7, 8, 9
- Goto start: Home
- Goto end: End

## Slide Creation Workflow

![Screenshot 2024-12-02 140713](https://github.com/user-attachments/assets/b4753662-3d1b-4f45-8503-342445fd202b)

