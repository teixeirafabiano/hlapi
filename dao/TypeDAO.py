import argparse
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

print(sys.path, os.getcwd())

from dao.DAO import DAO

class TypeDAO(DAO):

    def __init__(self):
        super().__init__()

    def selectAllType(self, value):
        result = []
        try:
            self._connect()
            result = self.executeComplex(value)
        except Exception as exc:
            print("Erro ao executar query!", exc)
        return result


    def selectTypeById(self, value):
        result = []
        #query = f"SELECT * FROM tbl_service WHERE nu_id = {nu_id}" 
        try:
            self._connect()
            result = self.executeComplex(value)
        except Exception as exc:
            print("Erro ao executar query!", exc)
        return result

if __name__ == '__main__':
    objDao = TypeDAO()
    lst = []

    # terceira execução executev
    lst.append('vw_type_by_category')
    c = objDao.selectAllType(lst) #select(['VW_LABOR', 'nu_id_service', 1])
    print(c)

    lst.append('nu_id_type')
    lst.append('7')
    c = objDao.selectTypeById(lst)

    print(c)

