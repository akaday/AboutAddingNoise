# AboutAddingNoise

## How to run

To run the code in a Python environment, follow these steps:

1. Install Python:
   - Download and install Python from the official website: https://www.python.org/downloads/

2. Create a virtual environment:
   - Open a terminal or command prompt.
   - Navigate to the project directory.
   - Run the following command to create a virtual environment:
     ```
     python -m venv env
     ```

3. Activate the virtual environment:
   - On Windows, run:
     ```
     .\env\Scripts\activate
     ```
   - On macOS and Linux, run:
     ```
     source env/bin/activate
     ```

4. Install dependencies:
   - Run the following command to install any required dependencies:
     ```
     pip install -r requirements.txt
     ```

5. Run the `add_noise.py` script:
   - Navigate to the `src` directory:
     ```
     cd src
     ```
   - Run the following command to execute the script and view the output:
     ```
     python add_noise.py
     ```

6. Deactivate the virtual environment (optional):
   - Run the following command to deactivate the virtual environment:
     ```
     deactivate
     ```

## How to run tests

To run the tests using `pytest`, follow these steps:

1. Install `pytest`:
   - Run the following command to install `pytest`:
     ```
     pip install pytest
     ```

2. Run the tests:
   - Navigate to the project directory (if not already there):
     ```
     cd ..
     ```
   - Run the following command to execute the tests:
     ```
     pytest
     ```
