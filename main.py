import csv
from datetime import datetime


def converter_date(entrada):
    try:
        data_obj = datetime.strptime(entrada, '%B %d, %Y')
        saida = data_obj.strftime('%Y-%m-%d')
        return saida
    except:
        return None


if __name__ == '__main__':
    rows = []
    with open("netflix_titles.csv", 'r', encoding='cp437') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            row[6] = converter_date(row[6])
            rows.append(row)

    with open("netflix_titles_corrigido.csv", 'w', newline="", encoding='cp437') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(header)
        csvwriter.writerows(rows)
