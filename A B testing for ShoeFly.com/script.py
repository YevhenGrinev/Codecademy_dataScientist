import pandas as pd
import numpy as np

ad_clicks = pd.read_csv('ad_clicks.csv')
# print(ad_clicks.head(10))

most_views_ad_latform = ad_clicks.groupby('utm_source').user_id.count().reset_index()
# print(most_views_ad_platform)

#_doesn't_work_
# ad_clicks['ad_clicks'] = ad_clicks.ad_click_timestamp.apply(lambda row: True if  row != row.isnull() else False)
# print(ad_clicks)

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
# print(ad_clicks)

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(
  columns='is_click',
  index='utm_source',
  values='user_id',
).reset_index()
# print(clicks_pivot)

#_doesn't_work_
# clicks_pivot['percent_clicked'] = clicks_pivot.apply(lambda row: (row.True / (row.True + row.False)), axis = 1)
clicks_pivot['percent_clicked'] = round(clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False]), 2)
# print(clicks_pivot)

show_count_same_users_experimental_group = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
# print(show_count_same_users_experimental_group)
# print(ad_clicks)

who_is_greater = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index().pivot(
  columns='is_click',
  index='experimental_group',
  values='user_id',
).reset_index()
# print(who_is_greater)


a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
print(a_clicks)
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
print(b_clicks)

a_clicks_pivot = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index().pivot(
  columns='is_click',
  index='day',
  values='user_id',
).reset_index()

a_clicks_pivot['percent_of_clicks'] = round(a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False]), 2)

print(a_clicks_pivot)

b_clicks_pivot = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index().pivot(
  columns='is_click',
  index='day',
  values='user_id',
).reset_index()

b_clicks_pivot['percent_of_clicks'] = round(b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False]), 2)

print(b_clicks_pivot)
