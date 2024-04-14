# IMDB-Scraper
A Python script that scrapes IMDb's top-rated movies from the official website and saves the data to an Excel file.
![image](https://github.com/vaishnavswe/IMDB-Scraper/assets/145303692/fb3cb880-a525-414b-9531-9741707b45e5)

## Features
- Web scraping: Retrieves data from IMDb's top-rated movies page using BeautifulSoup and requests libraries.
- Data extraction: Extracts movie rank, name, year of release, and IMDb rating from the webpage.
- Excel output: Saves the scraped data to an Excel file for further analysis or presentation.

## Technologies Used
- Python: The primary programming language used for scripting and data manipulation.
- BeautifulSoup: Used for parsing HTML content and extracting relevant data from web pages.
- requests: Used for making HTTP requests to fetch web pages.
- openpyxl: Used for creating and manipulating Excel files.

## Usage
1. Run the script to initiate the scraping process.
2. The script will fetch data from IMDb's top-rated movies page.
3. Extracted movie details (rank, name, year, rating) will be saved to an Excel file named "IMDB Movie Ratings.xlsx" in the script directory.
4. Review the generated Excel file to analyze the top-rated movies data.

## Code Structure
- The script starts by importing necessary libraries: BeautifulSoup, requests, and openpyxl.
- It initializes an Excel workbook and creates a worksheet named "Top Rated Movies".
- The script then sends an HTTP request to IMDb's top-rated movies page and parses the HTML content.
- Using BeautifulSoup, it extracts relevant information such as movie rank, name, year, and rating.
- Extracted data is appended to the Excel worksheet.
- The Excel workbook is saved as "IMDB Movie Ratings.xlsx" in the script directory.

## Error Handling
- The script includes exception handling to deal with potential errors during web scraping or file saving.
- If an error occurs, it prints the error message for debugging purposes.

## Limitations
- Web scraping might be 
