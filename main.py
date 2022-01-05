import pandas as pd
from googlesearch import search


def get_sites_by_kw(kw):
    return search(kw, lang="ru")[:5]


def main():
    df = pd.read_csv("kw.csv")
    df["sites"] = df["kw"].agg(lambda kw: get_sites_by_kw(kw))

    df.to_csv("kw_links.csv")

if __name__ == "__main__":
    main()