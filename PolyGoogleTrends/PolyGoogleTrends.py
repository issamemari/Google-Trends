import pandas as pd
from pytrends.request import TrendReq


def get_most_popular(keyword_list):
    pytrend = TrendReq()
    df = pytrend.get_historical_interest(keyword_list,
                                         year_start=2018,
                                         month_start=1,
                                         day_start=1,
                                         hour_start=0,
                                         year_end=2018,
                                         month_end=2,
                                         day_end=1,
                                         hour_end=0,
                                         cat=0,
                                         geo='',
                                         gprop='',
                                         sleep=0)
    return df, df.max().idxmax()


def get_most_popular_against(keyword_list, most_popular):
    if len(keyword_list) == 0:
        return None

    keyword_list_copy = list(keyword_list)

    result = []

    while len(keyword_list_copy) != 0:
        temp = [keyword_list_copy.pop() for i in range(min(4, len(keyword_list_copy)))]
        temp.append(most_popular)
        df_temp, _ = get_most_popular(temp)
        result.append(df_temp)

    df1 = result[0]
    for df in result[1:]:
        df1 = pd.merge(df1, df, on=list(set(df.columns).intersection(set(df1.columns))))

    return df1


def get_historical_interest(keyword_list):

    cache = []

    keyword_list_copy = list(keyword_list)
    current_most_popular = None

    while len(keyword_list_copy) > 1:
        current_five = [keyword_list_copy.pop() for i in range(min(5, len(keyword_list_copy)))]

        df, new_most_popular = get_most_popular(current_five)

        if new_most_popular != current_most_popular:
            cache = [(df, new_most_popular)]
        else:
            cache.append((df, new_most_popular))

        current_most_popular = new_most_popular

        keyword_list_copy.append(current_most_popular)
        print(f'Current most popular is {current_most_popular} among {current_five}')

    keywords_we_have = set()
    for df, popular in cache:
        for column in df.columns[1:-1]:
            keywords_we_have.add(column)

    keywords_to_get = set(keyword_list_copy) - keywords_we_have

    df1 = None


    thing = get_most_popular_against(keywords_to_get, current_most_popular)
    if thing is not None:
        df1 = thing
    else:
        df1, _ = cache[0]

    for df, _ in cache:
        df1 = pd.merge(df1, df, on=list(set(df.columns).intersection(set(df1.columns))))

    return df1.drop('isPartial', axis=1)


