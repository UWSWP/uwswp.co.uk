import csv
import toml

data = {}
# Load the current Hugo config
hugo_config = toml.load("config.toml")


def convert_csv_to_toml():
    """
    Convert the CSV file to TOML and write it to the Hugo config
    """
    with open(".github/populate_website/website.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for line in reader:
            data[line["title"]] = line["value"]

        hugo_config["params"] = data
        f = open("config.toml", "w")
        toml.dump(hugo_config, f)
        f.close()


if __name__ == "__main__":
    convert_csv_to_toml()
