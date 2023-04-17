import argparse
import os
import sys
#import pandas

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

print(sys.path, os.getcwd())


#from app.DTO.CiclistaDTO import CiclistaDTO
from dao.HlDAO import HlDAO

class HlDLO:

    def __init__(self):
        pass

    # def selectById(self, table, column, value):
    #     objDao = HlDAO()
    #     lstCiclista = []

    #     try:
    #         result = objDao.select(table, column, value)
    #         for i in range(0, len(result)):
    #             lstCiclista.append(CiclistaDTO(result[i][0], result[i][1], result[i][2], result[i][3], result[i][4]))

    #     except Exception as exc:
    #         print(f"Erro ao buscar {table} pelo id!", exc)
    #     return lstCiclista

    def selectWorkerByService(self, service, value):
        objDao = HlDAO()
        #lstCiclista = []
        result = []
        try:
            result = objDao.selectWorkerByService(service, "ini_zipcode", "end_zipcode", value)
            # print("=======", result[0][0])
            # for i in range(0, len(result)):
            #     lstCiclista.append(CiclistaDTO(result[i][0], result[i][1], result[i][2], result[i][3], result[i][4]))

        except Exception as exc:
            print(f"Erro ao na consulta!", exc)
        return str(result[0][0]) #lstCiclista

if __name__ == '__main__':
    objDlo = HlDLO()
    lst = []

    qt = objDlo.selectWorkerByService("Plumbing", "90007")
    print(type(qt), qt)


