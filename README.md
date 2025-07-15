# Excel Compare App

This project is a Python application designed to compare two Excel files based on various criteria. Users can upload Excel files and select comparison options to identify differences and generate a new Excel file with the results.

## Features

- Compare two Excel files based on:
  - Item Number
  - Part Number
  - Item Name
  - Item Price
- Handle duplicate items by merging quantities.
- Generate a new Excel file with comparison results.
- Maintain the original files for reference.

## Installation

To get started with the Excel Compare App, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/excel-compare-app.git
   cd excel-compare-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. Use the GUI to:
   - Upload the two Excel files you want to compare.
   - Select the criteria for comparison.
   - View the results and save the new Excel file with the comparison data.

## Dependencies

The project requires the following Python packages:
- pandas
- openpyxl
- [GUI library of your choice, e.g., Tkinter or PyQt]

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.