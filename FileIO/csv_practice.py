import csv

# # csv.reader(f):リストで取得する
# with open('example.csv') as f:
#     reader = csv.reader(f)
#     for line in reader:
#         print(line[1])

# # csv.DictReader(f)：ディクショナリーで取得する
# with open('example.csv') as f:
#     reader = csv.DictReader(f)
#     for line in reader:
#         print(line['Country']) # インデックス出なく、columで値をとって来れる


# # csv.writer(f)：リスト形式で書き込み
# with open('sample.csv', mode='w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['value1', 'value2'])
#     writer.writerow(['value3', 'value4'])


# csv.DictWriter(f)：ディクショナリーで書き込み
with open("sample.csv", mode='w') as f:
    writer = csv.DictWriter(f, ['col1', 'col2'])
    writer.writeheader()
    writer.writerow({'col1':'value1', 'col2':'value2'})
    writer.writerow({'col1':'value3', 'col2':'value4'})