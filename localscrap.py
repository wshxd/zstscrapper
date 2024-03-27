import requests
import imgkit
from bs4 import BeautifulSoup
from datetime import datetime

# URL SCRAPPING (zst)
url = "https://zst.czest.pl/zastepstwa/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Usunięcie przyciskow facebook etc
div_to_remove = soup.find('div', class_='simplesocialbuttons')
if div_to_remove:
    div_to_remove.decompose()

# entry-content
entry_content = soup.find('div', class_='entry-content')


if entry_content:
    text_to_find = '1 TI' # PODMIENIC NA SWOJA KLASE!
    # scarpping time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    time_header = soup.new_tag('h1')
    time_header.string = f"Zescrapowano: {current_time} // wshxd"
    time_header['style'] = 'font-size: 50px;' 
    entry_content.insert(0, time_header)

    # css theme
    css_style = "<style>body { background-color: #141414; color: white; }</style>"
    entry_content.insert(0, BeautifulSoup(css_style, 'html.parser'))

    # usuwanie zbędnych tabelek
    for table in entry_content.find_all('table'):
        found_text = False
        for cell in table.find_all('td'):
            if text_to_find in cell.text.strip():
                found_text = True
            if cell.text.strip() == text_to_find:
                cell['style'] = 'color: #ff0000; font-size: 25px;'  # zamiana twojej klasy okreslonej przez zmienna na czerwony i wiekszy font
        if not found_text:
            table.decompose()

    # Usunięcie przerw między tagami
    html_content = entry_content.prettify()

    # jpg output
    output_image_path = 'zastepstwa.jpg'

    # Ustawienia konwersji
    options = {
        'format': 'jpg',
        'encoding': 'UTF-8',  # Ustawienie kodowania znaków na UTF-8 do polskich znakow
        # Tutaj możesz dodać inne opcje konwersji, jeśli jest to potrzebne
    }

    # Konwersja zawartości HTML na obraz
    imgkit.from_string(html_content, output_image_path, options=options)

    print("strona zostala zescrapowana pomyslnie!")
else:
    print("cos nie dziala, dziwne, mi dziala")
