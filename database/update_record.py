import sqlite3

con = sqlite3.connect('sample.db')
cursor = con.cursor()

target_name = input("whose 'age' do you want to update?:")
new_age = input("Tell me new age:")
# print(target_name, new_age)

# update_query = f"UPDATE User SET age = {new_age} WHERE name = '{target_name}'"
# cursor.executescript(update_query)
"""
SQL injectionの脆弱性あり！
実行した際に、例えば[31; DROP User;]などの文字列を入力されてしまった場合、
DROP User;も実行されてしまい、tableをデリートできてしまう。
"""
# じゃあどうするのか↓
update_query = 'UPDATE User SET age = ? WHERE name = ?'
cursor.execute(update_query, (new_age, target_name))
con.commit()