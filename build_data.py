import json
import pandas as pd


def converter(d: dict) -> dict:
    return {
        "dev_id": d["devId"],
        "Короткое название (чичтое)": d["devShortCleanNm"],
        "Короткое название": d["devShortNm"],
        "Полное название": d["devFullCleanNm"],
        "Регион": d.get("regRegionDesc"),
        "Сайт": d["devSite"],
        "ИНН": d["devInn"],
        "ОГРН": d["devOgrn"],
        "КПП": d["devKpp"],
        "Адрес": d["devLegalAddr"],
        "Фактический адрес": d.get("devFactAddr"),
        "Форма организации (полное)": d["orgForm"]["fullForm"],
        "Форма организации": d["orgForm"]["shortForm"],
    }


def main():
    with open('developers.json') as f:
        developers = json.load(f)

    df = pd.DataFrame([converter(developer) for developer in developers])

    print(df.head())


if __name__ == "__main__":
    main()
