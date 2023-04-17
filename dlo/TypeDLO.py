import argparse
import os
import sys
#import pandas

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

print(sys.path, os.getcwd())


from dto.TypeDTO import TypeDTO
from dao.TypeDAO import TypeDAO

class TypeDLO:

    def __init__(self):
        pass

    def selectAllType(self, value=['VW_TYPE_BY_CATEGORY']):
        objDao = TypeDAO()
        lstType = []
        result = []
        try:
            result = objDao.selectAllType(value)
            for i in range(0, len(result)):
                lstType.append(TypeDTO(result[i][0], result[i][1], result[i][2], result[i][3]))
        
        except Exception as exc:
            print(f"Query on Type with error...", exc)
        return lstType

    def selectTypeById(self, value):
        objDao = TypeDAO()
        lstType = []
        result = []
        value = ['VW_TYPE_BY_CATEGORY', 'nu_id_category', value]
        try:
            result = objDao.selectTypeById(value)
            for i in range(0, len(result)):
                lstType.append(TypeDTO(result[i][0], result[i][1], result[i][2], result[i][3]))
        
        except Exception as exc:
            print(f"Query on Type with error...", exc)
        return lstType

if __name__ == '__main__':
    objDlo = TypeDLO()

    qt = objDlo.selectAllType()
    print(type(qt), qt)
