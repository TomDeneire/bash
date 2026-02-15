import json

EXTENSTIONS = ["b", "i", "l", "m", "d", "x"]
M4PATH = "/home/tdeneire/Dropbox/brocade/support/m4_list.json"
#  M4NVIMPATH = "/home/tdeneire/Dropbox/brocade/support/m4_nvim.txt"
QPATH = "/home/tdeneire/Dropbox/brocade/packages/vscode/"
NVIMPATH = "/home/tdeneire/Dropbox/code/nvim/snippets/"

# vscode snippets structure is not 100% compatible
for ext in EXTENSTIONS:
    with open(f"{QPATH}{ext}file/syntax/{ext}file.json", "r") as reader:
        snippets = json.loads(reader.read())
        new_snippets = {}
        for item, itemv in snippets.items():
            if f"source.{ext}file" in item:
                for sub, subv in itemv.items():
                    new_snippets[sub] = subv
            else:
                new_snippets[item] = itemv
    with open(f"{NVIMPATH}{ext}file.json", "w") as writer:
        writer.write(json.dumps(new_snippets))

# Macros

#  with open(M4PATH, "r") as reader:
#      macros = json.loads(reader.read())
#
#  with open(M4NVIMPATH, "w") as writer:
#      macro_data = []
#      for macro in macros:
#          macro_data.append("m4_" + macro)
#      writer.write("\n".join(macro_data))

# Warning: including macro's in snippets makes Neovim really slow!
#  with open(f"{NVIMPATH}mfile.json", "r") as reader:
#      msnippets = json.loads(reader.read())
#
#  with open(M4PATH, "r") as reader:
#      macros = json.loads(reader.read())
#
#  for macro in macros:
#      macro_name = macro.partition("(")[0]
#      msnippets[macro_name] = {"prefix": "m4_" + macro_name,
#                               "body": ["m4_" + macro]}
#
#  with open(f"{NVIMPATH}mumps.json", "w") as writer:
#      writer.write(json.dumps(msnippets))
#
