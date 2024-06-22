## Media to G-code Converter

This Python application converts various forms of media, such as text and SVG files, into G-code. It provides functionality to visualize and control stepper and servo motors using Turtle graphics.

### Features

- **Text to G-code Conversion**: Enter text to generate corresponding G-code for motor control.
- **SVG to G-code Conversion**: Upload SVG files to convert complex designs into G-code.
- **Visualization**: Display SVG images and their G-code output directly within the application.
- **Statistical Insights**: Calculate and display metrics such as G-code length and estimated writing time.

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shahalt1/media-to-gcode-converter.git
   cd media-to-gcode-converter
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

### Usage

1. **Text Input:**
   - Enter text in the provided input box.
   - Click on **Plot!** to convert the text into G-code.
   - View the G-code output and related statistics.

2. **SVG File Upload:**
   - Click on **Upload File** to select an SVG file.
   - See the SVG image displayed alongside its G-code output.
   - Adjust the SVG image display size by modifying `basewidth` in the `show_svg` function.


### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This concise README provides an overview of the application's capabilities, setup instructions, usage guidelines, and an example snippet for reference. Adjust and expand upon it based on your project's specific requirements and additional features.
