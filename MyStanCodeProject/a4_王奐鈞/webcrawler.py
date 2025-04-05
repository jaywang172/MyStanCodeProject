"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #

        # Initial the variable
        male_total = 0
        female_total = 0

        table = soup.find('table', {'class': 't-stripe'})

        rows = table.find_all('tr')

        for row in rows:
            columns = row.find_all('td')

            # Ensure that column is stored with the data
            if len(columns) >= 5:
                # Use the comma to spilt the data and join it together
                male_count = int(''.join(columns[2].text.split(',')))
                female_count = int(''.join(columns[4].text.split(',')))
                male_total += male_count
                female_total += female_count

        print(f"Male Number: {male_total}")
        print(f"Female Number: {female_total}")


if __name__ == '__main__':
    main()
