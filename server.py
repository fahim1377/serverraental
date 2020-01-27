import psycopg2
Connection = None
Cursor = None

def connect_database():
    try:
        connection = psycopg2.connect(port = '5432',host = "localhost",database = 'serverrental',user = 'postgres',password = '***')
        cursor = connection.cursor()
        global Cursor
        Cursor = cursor
        global Connection
        Connection = connection
        
    except(Exception) as Error:
        print(Error)

def get_all_recources():
    Cursor.execute('SELECT source_id FROM source S WHERE S.ram = 2')
    result = Cursor.fetchone()[0]
    print(result)


def insert_recource(source_id,ram,num_core,source_storage,cpu,net_rate,daily_price):
    query = """insert into source(source_id,ram,num_core,source_storage,cpu,net_rate,daily_price) values ('%s','%s','%s','%s','%s','%s','%s')"""%(source_id,ram,num_core,source_storage,cpu,net_rate,daily_price)
    print(query)
    Cursor.execute(query)
    Connection.commit()




def read(table, **kwargs):
    """ Generates SQL for a SELECT statement matching the kwargs passed. """
    sql = list()
    sql.append("SELECT * FROM %s " % table)
    if kwargs:
        sql.append("WHERE " + " AND ".join("%s = '%s'" % (k, v) for k, v in kwargs.iteritems()))
    sql.append(";")
    return "".join(sql)



def upsert(table, **kwargs):
    """ update/insert rows into objects table (update if the row already exists)
        given the key-value pairs in kwargs """
    keys = ["%s" % k for k in kwargs]
    values = ["'%s'" % v for v in kwargs.values()]
    sql = list()
    sql.append("INSERT INTO %s (" % table)
    sql.append(", ".join(keys))
    sql.append(") VALUES (")
    sql.append(", ".join(values))
    sql.append(") ON DUPLICATE KEY UPDATE ")
    sql.append(", ".join("%s = '%s'" % (k, v) for k, v in kwargs.iteritems()))
    sql.append(";")
    return "".join(sql)


def delete(table, **kwargs):
    """ deletes rows from table where **kwargs match """
    sql = list()
    sql.append("DELETE FROM %s " % table)
    sql.append("WHERE " + " AND ".join("%s = '%s'" % (k, v) for k, v in kwargs.iteritems()))
    sql.append(";")
    return "".join(sql)




if __name__ == "__main__":
    connect_database()
    #get_all_recources()
    # insert_recource('12','2','4','234234','3','4','2435234')
    temp = ['12','2','4','234234','3','4','2435234']
    upsert('source',temp)

