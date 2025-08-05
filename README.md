# POWL Model Collection

A Python-based tool for generating business process models using OpenAI's API and converting them into POWL (Partially Ordered Workflow Language) representations.

## Overview

This project consists of two main components:

1. **Process Description Generator** (`01_generate_tdesc.py`) - Generates complex business process descriptions using OpenAI's GPT models
2. **POWL Model Generator** (`02_get_reference_powl.py`) - Converts textual process descriptions into POWL models and Petri net visualizations

## Features

- **Multi-threaded Generation**: Both scripts support concurrent processing for efficient batch generation
- **Automated Validation**: Ensures generated processes meet specific constraints (activity name length, description complexity, etc.)
- **Visual Output**: Generates SVG visualizations of the resulting Petri nets
- **Retry Logic**: Built-in error handling and retry mechanisms for API failures
- **Flexible Configuration**: Command-line arguments for customizing generation parameters

## Requirements

- Python 3.x
- OpenAI API key (set as environment variable `OPENAI_API_KEY`)
- Required Python packages:
  - `requests`
  - `pm4py`

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install requests pm4py
   ```
3. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

## Usage

### Step 1: Generate Process Descriptions

```bash
python 01_generate_tdesc.py [options]
```

Options:
- `--count`: Number of process descriptions to generate (default: 1000)
- `--max-threads`: Maximum number of concurrent threads (default: 30)
- `--output-dir`: Base output directory (default: models)

This will generate JSON files containing process descriptions in `models/textual_descriptions/`.

### Step 2: Generate POWL Models

```bash
python 02_get_reference_powl.py [options]
```

Options:
- `--model`: OpenAI model to use (default: gpt-4.1-mini)
- `--input-dir`: Directory of input JSON files (default: models/textual_descriptions)
- `--max-threads`: Max concurrent threads (default: 50)
- `--powl-dir`: Directory to save generated POWL Python files
- `--vis-dir`: Directory to save Petri net visualizations
- `--max-global-retries`: Maximum number of global retry attempts (default: 10)
- `--retry-delay`: Delay in seconds between global retries (default: 5)

This will:
- Generate Python files containing POWL model code in `models/{model_name}/powl/`
- Create SVG visualizations of Petri nets in `models/{model_name}/visualization/`

## Output Structure

```
models/
├── textual_descriptions/     # Generated process descriptions (JSON)
├── {model_name}/
│   ├── powl/                # POWL model Python files
│   └── visualization/       # Petri net SVG visualizations
```

## Process Description Format

Generated process descriptions follow this structure:
```json
{
  "title": "Process Title",
  "description": "Detailed process description (≥300 characters)",
  "activities": ["Activity 1", "Activity 2", ...] // At least 15 activities
}
```

## POWL Model Structure

POWL models support:
- **Activities**: Labeled transitions representing process steps
- **Silent Transitions**: Tau transitions for internal flow
- **Operators**:
  - XOR: Exclusive choice between alternatives
  - LOOP: Iterative execution patterns
- **Partial Orders**: Concurrent execution with dependency constraints

## Error Handling

Both scripts include robust error handling:
- API request retries with exponential backoff
- Validation of generated content
- Detailed error logging
- Global retry mechanism for failed files

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Notes

- Activity names are constrained to maximum 2 words and 20 characters
- Each process must contain at least 15 different activities
- Process descriptions must be at least 300 characters long
- The tool validates that generated POWL models contain all specified activities
