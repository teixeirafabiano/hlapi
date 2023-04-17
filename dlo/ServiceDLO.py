import argparse
import os
import sys
#import pandas

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

print(sys.path, os.getcwd())


from dto.ServiceDTO import ServiceDTO
from dao.ServiceDAO import ServiceDAO

class ServiceDLO:

    def __init__(self):
        pass

    def selectService(self, value):
        objDao = ServiceDAO()
        lstService = []
        result = []
        try:
            result = objDao.selectService(value)
            print("=======", result[0][0])
            for i in range(0, len(result)):
                print(result[i][0], result[i][1], result[i][2], result[i][4], result[i][3])
                lstService.append(ServiceDTO(result[i][0], result[i][1], result[i][2], result[i][4], result[i][3]))
        
        except Exception as exc:
            print(f"Query on Service with error...", exc)
        return lstService

    def insertService(self, nm_service, jn_service):
        objDao = ServiceDAO()
        nu_id = 0
        try:
            nu_id = int(objDao.insert(nm_service, jn_service))
            # print("=======", result[0][0])
            # for i in range(0, len(result)):
            #     print(result[i][0], result[i][1], result[i][2], result[i][4], result[i][3])
            #     lstService.append(ServiceDTO(result[i][0], result[i][1], result[i][2], result[i][4], result[i][3]))
        
        except Exception as exc:
            print(f"Query on Service with error...", exc)
        return nu_id


if __name__ == '__main__':
    objDlo = ServiceDLO()
    lst = []

    lst.append('tbl_service')
    lst.append('nu_id')
    lst.append('1')

    qt = objDlo.selectService(lst)
    print(type(qt), qt)


