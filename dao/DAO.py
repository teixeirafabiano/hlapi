import os
import psycopg2
from psycopg2 import sql
import psycopg2.extras
from psycopg2 import OperationalError, errorcodes, errors

class DAO():

    key = "postgres://pmhwcoymaetmge:e415725e6bfb2721c15b78998eab8bd40ce6f5060d02bfa1359c67a3e561c912@ec2-52-1-26-88.compute-1.amazonaws.com:5432/d4slgof1eec3kv" # os.environ['DATABASE_URL']

    def __init__(self, database=key):
        #print("Database", database) 
        self.database = database
        self.conn = None

    def __enter__(self):
        return self._connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self._connect().rollback()
        else:
            self._connect().commit()
        try:
            self.conn.close()
        except AttributeError:
            pass
        finally:
            self.conn = None

    def _connect(self):
        try:
            if self.conn is None:
                self.conn = psycopg2.connect(self.database, sslmode='require')
                self.conn.autocommit = True
                #print(self.conn)
        except psycopg2.DatabaseError as sqlerror:
            print("Erro ao conectar ao banco!", sqlerror)
        return self.conn

    def executeComplex(self, parameters=()):
        result = []
        column = []
        params = []
        filtro = ""
        try:
            if len(parameters[1:]) > 0:
                for i, val in enumerate(parameters[1:]):
                    if i%2==0:
                        column.append(val)
                    else:
                        params.append(val)

                for j, col in enumerate(column):
                    if j == 0:
                        filtro = filtro + col + " = " + params[j]
                    else:
                        filtro = filtro + " AND " + col + " = " + params[j]

                cmd = f'SELECT * FROM {parameters[0]} WHERE %s' % (filtro)
                print("CMD:", cmd)
            else:
                cmd = f'SELECT * FROM {parameters[0]}'
                print("CMD:", cmd)

            cur = self.conn.cursor()
            
            print(cur.mogrify(cmd))
            cur.execute(cmd)

            result = cur.fetchall()

            for row in result:
                print("Id = ", row[0], )

        except psycopg2.DatabaseError as sqlerror:
            print("Erro ao executar query!", sqlerror)

        return result

    def executeSimple(self, parameters=()):
        params = []
        sql = ""
        try:
            for i, val in enumerate(parameters):
                params.append(str(val))

            table = params[0]
            column = params[1]
            value = params[2]
            
            cur = self.conn.cursor()
            sql = 'SELECT * FROM ' + table + ' WHERE ' + column + ' = %s'
            cur.execute(sql, (value,))
            result = cur.fetchall()
            for row in result:
                print("Id = ", row[0], )

        except psycopg2.DatabaseError as sqlerror:
            print("Erro ao executar query!", sqlerror)

        return result

    def insertId(self, query):
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            result = cur.fetchone()
            #for row in result:
            #    print("Id = ", row[0], )

        except psycopg2.DatabaseError as sqlerror:
            print("Erro ao executar insert!", sqlerror)

        return result[0]

    def execute(self, query):
        params = []
        sql = ""
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            result = cur.fetchall()
            for row in result:
                print("Id = ", row[0], )

        except psycopg2.DatabaseError as sqlerror:
            print("Erro ao executar query!", sqlerror)

        return result


    def disconnect(self):
        self.conn.close()

if __name__ == '__main__':
    objDao = DAO()
    c = objDao._connect()
    print(c)


