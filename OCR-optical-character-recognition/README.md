# Optical Character Recognition 

Here some Python scripts for OCR technology, using Pytesseract library. All the infos and techniques of this folders are taken from ithaka/tdm-notebooks.git repository by Nathan Kelber, in particular from this three explanations:

https://github.com/ithaka/tdm-notebooks/blob/c663639521ab105faf2d5f2c7678a13f7eca855b/ocr-basics.ipynb
https://github.com/ithaka/tdm-notebooks/blob/c663639521ab105faf2d5f2c7678a13f7eca855b/ocr-workflow-1.ipynb
https://github.com/ithaka/tdm-notebooks/blob/c663639521ab105faf2d5f2c7678a13f7eca855b/ocr-workflow-2.ipynb

convert_pdf_to_jpg script could be useful keeping in mind this tip: "Tesseract prefers image files (...). Technically, it's possible to feed Tesseract a PDF, but breaking up a PDF into images breaks down the OCR process from one massive task into a bunch of smaller tasks that are better for your computer -- if something happens, and the process is interrupted, you'll be able to pick up from where you left off if you are working from images. If you are processing an entire PDF and your computer freezes, you'll need to start over from the beginning..."
