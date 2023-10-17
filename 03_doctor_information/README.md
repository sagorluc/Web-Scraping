## Doctor Information Scraper
This Python script scrapes information about doctors from the website doctorbangladesh.com. It uses the requests library to fetch the HTML content and BeautifulSoup for parsing the HTML.

### Dependencies

- requests
- beautifulsoup4

### Usage

1. Ensure you have the required dependencies installed.
2. Run the script.
3. The script will fetch information about doctors, including their photo, name, degree, speciality, designation, workplace, hospital name, address, visiting hours, and appointment details.
4. The information will be saved in text files organized in folders.

### Slug Generator

A slug is generated for each doctor's name to create a unique URL. This is achieved by converting the name to lowercase, replacing spaces with hyphens, and removing special characters.

### Functionality
The script performs the following steps

1. Sends a GET request to doctorbangladesh.com.
2. Parses the HTML content using BeautifulSoup.
3. Retrieves information about each doctor, including:

   - Doctor Photo
   - Doctor Name
   - Doctor Degree
   - Doctor Speciality
   - Doctor Designation
   - Doctor Workplace
   - Hospital Name
   - Address
   - Visiting Hours
   - Appointment Details
4. Creates a folder for each doctor and saves the information in a text file.

### File Structure

- doctor_scraper.py: The Python script for scraping doctor information.
- readme.md: This file, providing information about the script.

### Author
- Md. Sagar Ali


