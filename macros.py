from anet.core import base

import os
from pathlib import Path
import re

WORKDIR = "/home/tdeneire/Dropbox/brocade/source/data/"
MACRODIR = "/home/tdeneire/Dropbox/brocade/support/macros"

REPO = Path(WORKDIR)

base.mkdir(MACRODIR, pathmode="tempdir")
base.rmpath(MACRODIR, keep=True)

MACRO_PATTERN = re.compile(r"macro.*?'''.*?'''.*?»", re.DOTALL)
MACRO_NAME_PATTERN = re.compile(r"macro.*:")

macros = []

for file in REPO.rglob("**/*.d"):
    with open(file, "r") as reader:
        file_contents = reader.read()
        macros.extend(re.findall(MACRO_PATTERN, file_contents))

for macro in macros:
    matches = re.findall(MACRO_NAME_PATTERN, macro)
    macro_name = (
        matches[0].partition(":")[0].partition("(")[0].replace("macro ", "m4_")
    )
    path = os.path.join(MACRODIR, macro_name + ".d")
    #  print(macro_name, "\n---------------", macro)
    with open(path, "w") as writer:
        writer.write(macro)
