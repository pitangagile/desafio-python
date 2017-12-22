import pandas as pd


def generate_file_from_json_and_csv(json_path, csv_path, file_name, columns):
    csv_a = pd.read_json(json_path)
    csv_b = pd.read_csv(csv_path)

    file = csv_a.merge(csv_b, on=columns)
    file.to_csv(file_name, index=False)


if __name__ == '__main__':
    generate_file_from_json_and_csv('pytan_series.json', 'via_lactea_series.csv', 'database.csv', ['name', 'year'])
