# Easy-CAD

AI-assisted architectural floor plan generator that creates basic CAD layouts from user requirements and exports them as DXF files.

## Summary

Easy-CAD is a prototype architectural design tool built with Python. Users provide project requirements such as building dimensions, room counts, and layout preferences. The system processes the input, generates a preliminary floor plan structure, and exports the result as a DXF file that can be opened in CAD software.

## Features

- Generate floor plan layouts from user input
- Export drawings in DXF format
- Built with Python and ezdxf
- Simple and extensible architecture
- Foundation for future AI-assisted architectural planning

## Technologies Used

- Python
- ezdxf
- CAD/DXF generation
- Algorithmic layout generation

## Installation

Clone the repository:

```bash
git clone https://github.com/majdalmously/Easy-cad.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
py main.py
```

Follow the prompts to enter project parameters such as building dimensions. The application will generate a DXF file that can be opened in AutoCAD or other CAD software.

## Output

The generated output file:

```text
floor_plan.dxf
```

## Future Improvements

- AI-powered space planning
- Automatic room optimization
- Multi-floor building support
- AutoCAD plugin integration
- Web-based interface
- 3D visualization

## License

This project is provided for educational and demonstration purposes.
