from lxml import etree

# Parsing schema 
schema_doc = etree.parse("Schemas/FSA029-Schema.xsd")
xmlschema = etree.XMLSchema(schema_doc)

# Parsing sample
sample =  etree.parse("Samples/FSA029-Sample-Valid.xml")

# Validating  
print(xmlschema.validate(sample))
