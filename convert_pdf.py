"""
LTK player written in Python for (Google Slides) PDF
"""

import pymupdf

print("Loading PDF...")
doc = pymupdf.open('slides.pdf')
for n in range(doc.page_count):
    print(f"Processing page {n + 1}")
    page = doc.load_page(n)
    pixmap = page.get_pixmap(dpi=300)
    img = pixmap.tobytes()
    with open(f"slides/page-{n+1}.png", "wb") as f:
        f.write(img)
    print(f"Saving page Output_{n + 1}.png => {len(img)} bytes")
