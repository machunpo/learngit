import time
from id_validator import validator

#生成出生当年所有日期
def dateRange(year):
    fmt = '%Y-%m-%d'
    bgn = int(time.mktime(time.strptime(year+'-01-01',fmt)))
    end = int(time.mktime(time.strptime(year+'-12-31',fmt)))
    list_date = [time.strftime(fmt,time.localtime(i)) for i in range(bgn,end+1,3600*24)]
    return [i.replace('-','') for i in list_date]

def vali_dator(id1,id2,id3):#区域码（6位），出生日期（8位），顺序码（2位）+性别码（1位）+校验码（1位）
    count=0
    for i in dateRange(id2):
        theid = id1 + i + id3
        if validator.is_valid(theid):
            count=count+1
            print(theid,count)

    print(count)



if __name__ == '__main__':

    data_time = dateRange('1993')

    print(len(data_time))

    vali_dator('330221','1993','4914')