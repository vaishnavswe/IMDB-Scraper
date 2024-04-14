from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Top Rated Movies'
sheet.append(['Movie Rank', 'Movie Name', 'Year of Release', 'IMDB Rating'])

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

try:
    source = requests.get('https://www.imdb.com/chart/top/', headers=headers)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    
    movies = soup.find_all('li', class_="ipc-metadata-list-summary-item")
    
    for movie in movies:
        rank_and_title = movie.find('h3', class_="ipc-title__text").get_text(strip=True).split('.')
        rank = rank_and_title[0]
        title = rank_and_title[1].strip()
        year = movie.find('span', class_="cli-title-metadata-item").get_text(strip=True)
        rating = movie.find('span', class_="ipc-rating-star").get_text(strip=True).split('(')[0]

        sheet.append([rank, title, year, rating])

except Exception as e:
    print(e)

excel.save('IMDB Movie Ratings.xlsx')
