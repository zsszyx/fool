from data.update import update_manager
from basic_funcs.sql_utils import load, delete

# um=update_manager()
# um.update_all()

df = load('hs300')
print(df.tail(60))
# delete('hs300')