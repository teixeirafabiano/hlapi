import argparse
import os
import sys
import pandas

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

print(sys.path, os.getcwd())

from dao.DAO import DAO

class ServiceDAO(DAO):

    def __init__(self):
        super().__init__()

    def selectService(self, value):
        result = []
        try:
            self._connect()
            result = self.executeComplex(value)
        except Exception as exc:
            print("Erro ao executar query!", exc)
        return result


    def selectServiceById(self, service, column_ini, column_fim, value):
        result = []
        query = f"SELECT * FROM tbl_service WHERE nu_id = {nu_id}" 
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

    def insert(self, nm_service, tx_service_json):
        query = f"insert into tbl_service (nm_service, jn_service) values ( '{nm_service}', '{tx_service_json}' ) RETURNING nu_id;"
        try:
            self._connect()
            result = self.insertId(query)
        except Exception as exc:
            print("Insert error on service...", exc)
        return result

if __name__ == '__main__':
    objDao = ServiceDAO()
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
    lst.append('tbl_service')
    lst.append('nu_id')
    lst.append('1')

    c = objDao.selectService(lst) #select(['VW_LABOR', 'nu_id_service', 1])

    nm_service = "Plumbing"
    tx_json = '{"zipcode": "37915", "service": "plumbing", "project": "Faucet, Fixtures and/or Pipes", "describe": "Repair a plumbing item/find a leak", "emergency": "yes", "repair": ["Item not working properly", "Leaking pipe"], "replace": ["Shower", "Bathtub"], "location": "Home/Residence", "status": "Planning & Budgeting", "completed": "More than 2 weeks", "street": "Iroquois St 215 #2", "city": "Knoxville, TN", "f_name": "Jorge","l_name": "Oliveira", "phone": "+1(110)201-0300", "email": "joransioli@gmail.com"}'
    c = objDao.insert(nm_service, tx_json)

    print(c)

