# Hospital Management System

## Description

The Hospital Management System is a simple Python project designed for practice. It allows users to manage patient data, including patient ID, name, disease, bill amount, and room number. The data is stored and updated using JSON files. The system offers the following functionalities:

1. **Add Patient**: Add new patient data to the system.
2. **Show Patient Info**: Display patient details by providing the patient ID.
3. **Billing**: View and update the bill details of a patient.
4. **Exit**: Exit the application.

This project serves as an example of basic data management and file I/O operations in Python.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/honeylalmj/hospital_management_system.git
   ```

2. **For Windows Users (Using `hosp.exe`):**

   - Simply double-click `hosp.exe` to run the application on Windows.
   
   **Note:** Make sure that you have the `hosp.exe` file in the project directory.

3. **For All Users (Using Python Script):**

   - If you prefer to run the application using the Python script, open a terminal in the project directory and execute:

     ```bash
     python hosp.py
     ```
### Running in a Virtual Environment

You can run this project within a virtual environment to manage its dependencies and isolate it from your system's global Python environment. Here are the steps to set up and run the project in a virtual environment:

1. Create a virtual environment (replace `venv` with your preferred environment name):

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   - On Windows:

    ``` bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```
## Usage

1. Launch the application by running `hosp.exe` (for Windows users) or `hosp.py` (for all users).
2. Use the following commands within the application:

   - `ADD`: Add a new patient's data to the system.
   - `Show`: Display patient details by entering the patient's ID.
   - `Bill`: View and update the bill amount for a patient.
   - `q`: Exit the application.

Follow the on-screen prompts to interact with the system.

## Features

- Add new patients to the system with their information.
- Retrieve patient details by providing their unique ID.
- Easily update the bill amount for each patient.
- Data is stored in a JSON file for persistence between sessions.

## Contributing

Contributions to this project are welcome! If you'd like to contribute, please follow these steps:

1. Fork the project on GitHub.
2. Create a new branch with a descriptive name: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to your branch: `git push origin feature/your-feature`.
5. Open a pull request on the GitHub repository.

Please ensure your code adheres to the project's coding standards and includes relevant tests if applicable.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it in accordance with the terms of the license.
