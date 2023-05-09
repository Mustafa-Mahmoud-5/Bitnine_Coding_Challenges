from psycopg2 import connect

connection = connect(
            host = "localhost",
            database="test",
            user = "postgres",
            password = "159787845pg")

cursor = connection.cursor()

cursor.execute("select * from user_table")

rows = cursor.fetchall()

print(rows)

connection.commit()

cursor.close()

connection.close()




# print(json.dumps(rows, cls = DecimalEncoder))

# import json
# from decimal import Decimal

# # passed in class to convert Decimals into strings
# class DecimalEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Decimal):
#             return str(obj)
#         return super().default(obj)

# for row in rows:
#   print(json.dumps(row, cls = DecimalEncoder))
