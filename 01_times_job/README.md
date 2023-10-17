## Job Search Filter
This Python script scrapes job listings from TimesJobs and filters them based on a specified unfamiliar skill. It uses the requests library to fetch the HTML content, and BeautifulSoup for parsing the HTML.

### Dependencies
- requests
- beautifulsoup4

### Usage
1. Run the script.
2. Enter the unfamiliar skill you want to filter jobs by.
3. The script will scrape job listings related to Python from TimesJobs and filter out those that require the specified unfamiliar skill.
4. Filtered jobs will be saved in text files in the posts_job directory, organized by page number.

### Functionality
The script performs the following steps:

1. Accepts user input for an unfamiliar skill.
2. Sends a GET request to TimesJobs Python job listings.
3. Parses the HTML content using BeautifulSoup.
4. Retrieves information for each job listing, including:
   - Company Name
   - Required Skills
   - Job Published Date
   - More Info Link
5. Filters out jobs that require the specified unfamiliar skill.
6. Saves the filtered jobs in text files.

### File Structure

- main3.py: The Python script for filtering job listings.
- readme.md: This file, providing information about the script.

### Author
- Md. Sagar Ali

