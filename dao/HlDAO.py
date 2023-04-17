import argparse
import os
import sys
import pandas

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

print(sys.path, os.getcwd())

from dao.DAO import DAO

class HlDAO(DAO):

    def __init__(self):
        super().__init__()

    def select(self, value):
        result = []
        try:
            self._connect()
            result = self.executeComplex(value)
        except Exception as exc:
            print("Erro ao executar query!", exc)
        return result


    def selectWorkerByService(self, service, column_ini, column_fim, value):
        result = []
        query = f"SELECT COUNT(*) as qtd FROM tbl_worker WHERE nm_service = '{service}' AND '{value}' BETWEEN {column_ini} AND {column_fim}" 
        try:
            self._connect()
            result = self.execute(query)
        except Exception as exc:
            print("Erro ao executar query!", exc)
        return result


    def update(self, table, value):
        query = "update ? set name = ?, email = ?, bike = ?, kind = ? where id = ?"
        try:
            self._connect()
            result = self.execute(query, table, value)
        except Exception as exc:
            print(f"Erro ao atualizar {table}!", exc)
        return result

    def delete(self, table, value):
        query = "delete from ? where nu_id = ?"
        try:
            self._connect()
            result = self.execute(query, table, value)
        except Exception as exc:
            print("Erro ao deletar ciclista!", exc)
        return result

    def insert(self, column, value):
        query = "insert into cyclist values ( ?, ?, ?, ?, ? )"
        try:
            self._connect()
            result = self.execute(query, value)
        except Exception as exc:
            print("Erro ao inserir ciclista!", exc)
        return result

if __name__ == '__main__':
    objDao = HlDAO()
    lst = []

    # primeira execução execute
    #lst.append('tbl_service')
    #lst.append('nu_id')
    #lst.append(1)

    # segunda execução executev
    #lst.append('VW_LABOR')
    #lst.append('nu_id_service = 1 AND nu_id_worker = 1')

    ##lst.append({'nu_id_service': 1, 'nu_id_worker': 1})

    # terceira execução executev
    lst.append('VW_LABOR')
    lst.append('nu_id_service')
    lst.append('1')
    lst.append('nu_id_worker')
    lst.append('1')
    c = objDao.select(lst) #select(['VW_LABOR', 'nu_id_service', 1])
    print(c)

