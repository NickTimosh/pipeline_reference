# or incremental load based on the watermark
wm_sql = ''' 
    SELECT COALESCE(MAX(LastUpdated),'1900-01-01')
    FROM orders;
    '''
m_cursor = conn.cursor()
m_cursor.execute(wm_sql)
result = m_cursor.fetchall()

# there's only one row and column returned:
last_updated_warehouse = result[0]

m_query = '''
    SELECT *
    FROM orders
    WHERE LastUpdated > %s
'''

m_cursor = conn.cursor()
m_cursor.execute(m_query, (last_updated_warehouse,))
results = m_cursor.fetchall()