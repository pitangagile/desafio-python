import pandas as pd


def json_to_csv(json_path):
    return pd.read_json(json_path)


def merge_csv(csv_a, csv_b, columns):
    return csv_a.merge(csv_b, on=columns)


def generate_file_from_json_and_csv(json_path, csv_path, file_name, columns):
    csv_a = json_to_csv(json_path)
    csv_b = pd.read_csv(csv_path)

    file = merge_csv(csv_a, csv_b, columns)
    file.to_csv(file_name, index=False)


if __name__ == '__main__':
    generate_file_from_json_and_csv('pytan_series.json', 'via_lactea_series.csv', 'database.csv', ['name', 'year'])
