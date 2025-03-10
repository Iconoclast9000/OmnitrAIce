# Custom Templates Directory

This directory stores user-created custom templates for the OmnitrAIce agents.

## Template Format

Custom templates should follow the same format as the default templates:

```json
{
  "template": "Template content with {placeholders}",
  "parameters": {
    "param1": "value1",
    "param2": "value2",
    "focus_areas": [
      "Focus area 1",
      "Focus area 2"
    ]
  }
}
```

## Naming Convention

Custom templates should be named descriptively, for example:
- `custom_ceo_template.json`
- `innovative_cto_template.json`
- `my_architect_template.json`
