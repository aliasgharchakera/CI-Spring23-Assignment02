from xml.dom import minidom

# parse an xml file by name
file = minidom.parse('A-n32-k05.xml')

#use getElementsByTagName() to get tag
nodes = file.getElementsByTagName('node')

# one specific item attribute
print('node 2:')
print(nodes[1].attributes['name'].value)

# all item attributes
print('\nAll attributes:')
for elem in nodes:
  print(elem.attributes['name'].value)

# one specific item's data
print('\nmodel #2 data:')
print(nodes[1].firstChild.data)
print(nodes[1].childNodes[0].data)

# all items data
print('\nAll model data:')
for elem in nodes:
  print(elem.firstChild.data)