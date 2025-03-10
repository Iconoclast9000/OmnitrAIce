# OmnitrAIce Configuration Migration Status

This document outlines the status of the configuration migration from the root `config` directory to the `omnitrace/config` directory.

## Current Status

The configuration files have been copied from the root `config` directory to the `omnitrace/config` directory, but the original files have been kept in place for backward compatibility. This allows for a smooth transition period where both locations are supported.

## Directory Structure

Both locations maintain the same structure:

```
config/
├── config_files/         # Configuration files (YAML/JSON)
├── custom_templates/     # User-created custom templates
└── templates/            # Default agent templates
```

## Configuration Files

The following files have been copied to the new location:

### Templates
- `ceo_template.json`
- `cto_template.json`
- `architect_template.json`
- `developer_template.json`
- `filesystem_template.json`

### Configuration Files
- `default_config.yaml`

## Import Paths

The code has been updated to look for configuration files in the following order:

1. `omnitrace/config/` directory (new location)
2. Root `config/` directory (old location)
3. Default hardcoded templates (fallback)

## Next Steps

Once all code has been updated to use the new configuration location and sufficient testing has been completed, the original configuration files can be removed from the root directory. This migration will be completed in a future update.

## Usage Instructions

### For new code:
Use the configuration files in the `omnitrace/config` directory:

```python
from omnitrace.utils.template_manager import load_template
template = load_template("ceo")  # Will look in omnitrace/config/templates first
```

### For backward compatibility:
The code includes fallbacks to maintain backward compatibility:

```python
try:
    from omnitrace.utils.template_manager import load_template
except ImportError:
    from utils.template_manager import load_template
```

## Completion Timeline

The complete migration of configuration files is scheduled for the next release, after which the duplicate files in the root directory will be removed.
