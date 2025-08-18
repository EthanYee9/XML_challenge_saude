from lxml import etree
from io import BytesIO
import os 

def FSA029_validation(sample_path, schema_folder):
    base_path = os.path.abspath(schema_folder)

    # Editing schema in memory 
    with open(f"{schema_folder}/FSA029-Schema.xsd", "rb") as file:
        schema_doc = etree.parse(file)
    
    for include_elem in schema_doc.findall(".//{http://www.w3.org/2001/XMLSchema}include"):
        if include_elem.get("schemaLocation") == "../../CommonTypes/v14/CommonTypes-Schema.xsd":
            include_elem.set("schemaLocation", "CommonTypes-Schema.xsd")

    # Create altered schema object
    altered_schema = etree.tostring(schema_doc, pretty_print=True, xml_declaration=True, encoding="UTF-8")
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
    try:
        xmlschema.assert_(sample)
        print("Submission has been correctly validated against FSA029 schema")
    except Exception as e:
        print("Submission has failed validation against FSA029 schema") 
        print(f"Error details: {e}")

if __name__ == "__main__":
    FSA029_validation("Samples/FSA029-Sample-Full.xml", "Schemas")
