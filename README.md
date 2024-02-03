# pdfgrep.py

A robust Python version of pdfgrep.

[pdfgrep](https://pdfgrep.org/) is a beautiful utility, which already available on a large of Linux distributions.

However I needed to include the feature into a Python script serving greater purposes: [pdfgrep_date_in_mails](https://github.com/synopsis8/pdfgrep_date_in_mails)

While calling the pdfgrep binary from inside Python is a working option, I wanted
to reduce dependencies on 3rd party software, especially 

The other current Python available versions of pdfgrep didn't give me satisfaction, so I
decided to cook my own.

Usage: python script.py <pattern> <pdf_file>
