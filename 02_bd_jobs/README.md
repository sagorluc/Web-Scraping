## Job Scraper from bdjobs.com

This Python script scrapes job listings from bdjobs.com. It utilizes the requests library to fetch the HTML content of the job search page and BeautifulSoup for parsing the HTML.

### Dependencies
- requests
- beautifulsoup4

### Usage

1. Make sure you have the required dependencies installed in your environment.
2. Run the script.
3. The script will fetch the job listings, extract relevant information (job title, company name, education requirements, location, experience, and application deadline), and display the results.

### Functionality
The script does the following:

1. Sends a GET request to bdjobs.com to retrieve job listings.
2. Parses the HTML content using BeautifulSoup.
3. Extracts information for each job listing, including:

   - Job Name
   - Company Name
   - Education Requirements
   - Location
   - Experience
   - Application Deadline
4. Prints the extracted information for each job listing.

### Notes
- if education requirements are specified, it extracts them. Otherwise, it defaults to "Not Specified".
- The script also contains commented-out code for saving the job details to text files.

### File Structure
- main.py: The Python script for scraping job listings.
- readme.md: This file, providing information about the script.

### Author
- Md. Sagar Ali

