from lxml import etree
from io import BytesIO
import os 

def FSA029_validation(sample_path, schema_folder):
    base_path = os.path.abspath(schema_folder)

    # Editing schema in memory 
    with open(f"{schema_folder}/FSA029-Schema.xsd", "rb") as file:
        schema_doc = file.read()
        altered_schema = schema_doc.replace(b"../../CommonTypes/v14/CommonTypes-Schema.xsd", b"CommonTypes-Schema.xsd")

    altered_schema_doc = BytesIO(altered_schema)

    # Parsing schema 
    schema_doc = etree.parse(altered_schema_doc, base_url=f"file://{base_path}/")
    xmlschema = etree.XMLSchema(schema_doc)

    # Parsing sample
    try:
        sample =  etree.parse(sample_path)
    except:
        raise Exception("XML file is not well-formed")

    # Validating   
    if xmlschema.validate(sample):
        print("Submission has been correctly validated against FSA029 schema")
    else:
        print("Submission has failed validation against FSA029 schema") 

if __name__ == "__main__":
    FSA029_validation("Samples/FSA029-Sample-Valid.xml", "Schemas")
