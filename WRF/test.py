import re
re.purge()
find_parent_id = re.compile('/w')
fulltext = open('tfile', 'r', encoding='utf-8').read()
#fulltext = re.sub(r',', '', fulltext)
parent_id = find_parent_id.search(fulltext)
print(parent_id.group())
