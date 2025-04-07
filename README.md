## Description

This Python script goes through a JSON file and replaces all occurrences of the word `"example"` with a new string entered by the user. Then it saves the result to a new JSON file.

## Features

- Loads a JSON file.
- Recursively scans all strings within the JSON structure.
- Replaces all occurrences of `"example"` with the given new text.
- Saves the modified JSON to a new file called `finalTest.json` (or another name if specified).

## Requirements

- Python 3.x

## How to Use

1. Make sure you have a `test.json` file (or another name of your choice) with valid JSON content.
2. Run the script:

    ```bash
    python script.py
    ```

3. When prompted, type the new text to replace `"example"`.
4. The script will generate a new file called `finalTest.json` with the changes.

## Script Structure

- **`changeText(jsonArchive, newText, finalArchive="finalTest.json")`**  
  Main function that opens the JSON file, replaces the text, and writes the result.

- **`change(jsonText)`**  
  Recursive helper function that scans the JSON and replaces `"example"` with the new text.

- **Input**:
  - Original JSON file name (default in script: `"test.json"`).
  - User-provided replacement text.

- **Output**:
  - New JSON file with the modified text (default: `"finalTest.json"`).

## Example

```text
Suppose the `test.json` file contains:

{
    "message": "This is an example",
    "list": ["example", "sample"],
    "nested": {
        "text": "example text"
    }
}

If you type `test` as the new text, the generated `finalTest.json` will be:

{
    "message": "This is an test",
    "list": ["test", "sample"],
    "nested": {
        "text": "test text"
    }
}
