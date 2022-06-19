import bibtexparser
import subprocess
import sys
import os
import re
import argparse
from argparse import RawTextHelpFormatter
from pathlib import Path
import calendar
import logging
from datetime import datetime
from academic import __version__ as version
from academic.import_assets import import_assets

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.customization import convert_to_unicode



def import_bibtex(bibtex):
    """Import publications from BibTeX file"""

    # Check BibTeX file exists.
    if not Path(bibtex).is_file():
        err = "Please check the path to your BibTeX file and re-run"
        print(err)


    # Load BibTeX file for parsing.
    with open(bibtex, "r", encoding="utf-8") as bibtex_file:
        parser = BibTexParser(common_strings=True)
        parser.customization = convert_to_unicode
        parser.ignore_nonstandard_types = False
        bib_database = bibtexparser.load(bibtex_file, parser=parser)
        for entry in bib_database.entries:
            parse_bibtex_entry(entry) 


def parse_bibtex_entry(entry):
    """Parse a bibtex entry and look for doi"""

    if "doi" in entry:
        #GOOGLE SEARCH
        print(f'doi: "{entry["doi"]}"')


import_bibtex(r"c:\LocalRepos\scholar.py\testWeibullWind.bib")