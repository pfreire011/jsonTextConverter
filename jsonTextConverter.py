import json
 
def changeText(jsonArchive, newText, finalArchive="finalTest.json"):
   with open(jsonArchive, "r", encoding="utf-8") as f:
       data = json.load(f)
 
   def change(jsonText):
       if isinstance(jsonText, dict):
           return {key: change(value) for key, value in jsonText.items()}
       elif isinstance(jsonText, list):
           return [change(item) for item in jsonText]
       elif isinstance(jsonText, str):
           return jsonText.replace("example", newText)  
       return jsonText
 
   changedJsonText = change(data)
   with open(finalArchive, "w", encoding="utf-8") as f:
       json.dump(changedJsonText, f, indent=4, ensure_ascii=False)
   print(f"Done, new json created: '{finalArchive}'.")
 
archive = "test.json"  
newValue = input("Type the new text: ")
changeText(archive, newValue)
