# XML_challenge_saude

A python script which validates an FSA029 XML file against the FSA029 XSD schema. 

## Requirements
- Python 3

## Set up instructions
- Get started by first forking and cloning this repositiory.
- Next create your virtual environment using:
```
python -m venv venv
```

- Activate your virtual environment using:
```
source venv/bin/activate
```

- Export PYTHONPATH:
```
export PYTHONPATH=$(pwd)
```

- Install dependincies using:
```
pip install -r requirements.txt
```

## Usage 
Requires two inputs:
1. Path to XML submission file. 
2. Schema folder - the directory containing the FSA029-Schema.xsd.

Example:
```
python validation_script.py Samples/FSA029-Sample-Valid.xml Schemas
```

- `Samples/FSA029-Sample-Valid.xml` -> Path to XML submission file. 
- `Schemas` -> Schema folder containing the XSD file. 

## Expected Outputs
- Valid submission:
```
Submission has been correctly validated against FSA029 schema
```

- Invalid submission:
```
Submission has failed validation against FSA029 schema
Error details: ...
```

## Schema path resolution 
- FSA029 schema references another schema (e.g.CommonTypes schema), using relative paths (e.g. `../../CommonTypes/v14/CommonTypes-Schema.xsd`).
- According to the brief it is forbidden that the location of the files contains `/CommonTypes/v14/`.
- Any needed resources by the FSA029 schema (i.e. CommonTypes schema) must be located in the same folder as FSA029 schema.
- It is required that the schemas are not modified before or after the execution of the script


## Challenge reflections
### 1. Why does FSA029-Sample-Full.xml fail schema validaion?

The "FSA029-Sample-Full.xml" failed validation due to the element "PartnershipsSoleTraders" appearing when it is not expected on line 102. <br />Indicated by this error message:

```
Submission has failed validation against FSA029 schema
Error details: Element '{urn:fsa-gov-uk:MER:FSA029:4}PartnershipsSoleTraders': This element is not expected., line 102
```

This is due to the schema specifying one `choice` for `Capital` (line 132 in the schema), however, the sample has all three options present.

### 2. How would you fix the file to pass the schema validation?
For this specific example, to fix this error you would need to remove two of the options under `choice`, leaving one left. However, more generally you can check data type mismatsches, missing elements, unexpected elements, namespace mismatches, etc.

### 3. Why do you think the regulator has included valida and invalid siles in their examples?
The regulator has included a valid and invalid files in their examples so devlopers can test their validation scripts. Additionally, the invalid file may highlight so common errors made in submissions.