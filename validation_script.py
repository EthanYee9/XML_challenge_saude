from lxml import etree
from io import BytesIO

# Editing schema in memory 
with open("Schemas/FSA029-Schema.xsd", "rb") as file:
    schema_doc = file.read()
    altered_schema = schema_doc.replace(b"../../CommonTypes/v14/CommonTypes-Schema.xsd", b"/home/ethan-yee/projects/XML_challange_saude/Schemas/CommonTypes-Schema.xsd")

altered_schema_doc = BytesIO(altered_schema)

# Parsing schema 
schema_doc = etree.parse(altered_schema_doc)
xmlschema = etree.XMLSchema(schema_doc)

# Parsing sample
sample =  etree.parse("Samples/FSA029-Sample-Valid.xml")

# Validating  
print(xmlschema.validate(sample))