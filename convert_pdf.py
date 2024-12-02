"""
LTK player written in Python for (Google Slides) PDF
"""

import os
import re
import shutil
import urllib.request

import pymupdf

PDF_FILENAME = "slides.pdf"


def load_pdf(filename):
    """ Load a PDF from a URL """
    url = input("Enter your Google Slides URL: ")
    url = re.sub("/edit.*", "/export/pdf", url)
    print("Loading ", url)
    with open(filename, "bw") as fp:
        data = urllib.request.urlopen(url).read()
        fp.write(data)
        print(f"Saved {len(data):,} bytes into {filename}")


def generate_slides(filename):
    """ Load the contents of a PDF and generate slides. """
    doc = pymupdf.open(filename)
    total_size = 0
    for n in range(doc.page_count):
        page = doc.load_page(n)
        pixmap = page.get_pixmap(dpi=300)
        img = pixmap.tobytes()
        with open(f"slides/page-{n+1}.png", "wb") as f:
            f.write(img)
        print(f"Saving page Output_{n + 1}.png => {len(img):,} bytes")
        total_size += len(img)
    return total_size


def clear():
    """ Remove the old slides """
    shutil.rmtree('slides')
    os.mkdir('slides')



clear()
load_pdf(PDF_FILENAME)
print(f"Total size is {generate_slides(PDF_FILENAME):,} bytes")
os.remove(PDF_FILENAME)
