import re

txt = "The rain in Spain"
print(re.search("^The.+Spain$", txt))
print(re.findall("S.{3}n",txt))
print(txt[4:9])
