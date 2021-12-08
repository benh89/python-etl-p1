import sql
from pgsql import query
from pgsql import query_create
from pgsql import query_insert
import csv

##

##URL_1='.//datasets//hollywood-theatrical-market-synopsis-1995-to-2021//AnnualTicketSales.csv', newline='',encoding='utf-8-sig'
##URL_2='.//datasets//hollywood-theatrical-market-synopsis-1995-to-2021//HighestGrossers.csv', newline='',encoding='utf-8-sig'
##URL_3='.//datasets//hollywood-theatrical-market-synopsis-1995-to-2021//PopularCreativeTypes.csv', newline='',encoding='utf-8-sig'
##URL_4='.//datasets//hollywood-theatrical-market-synopsis-1995-to-2021//TopDistributors.csv', newline='',encoding='utf-8-sig'
##URL_5='.//datasets//hollywood-theatrical-market-synopsis-1995-to-2021//TopGenres.csv', newline='',encoding='utf-8-sig'
##URL_6='.//datasets//hollywood-theatrical-market-synopsis-1995-to-2021//TopGrossingRatings.csv', newline='',encoding='utf-8-sig'
##URL_7='.//datasets//hollywood-theatrical-market-synopsis-1995-to-2021//TopGrossingSources.csv', newline='',encoding='utf-8-sig'
##URL_8='.//datasets//hollywood-theatrical-market-synopsis-1995-to-2021//TopProductionMethods.csv', newline='',encoding='utf-8-sig'
##URL_9='.//datasets//hollywood-theatrical-market-synopsis-1995-to-2021//WideReleasesCount.csv', newline='',encoding='utf-8-sig'

def csv_parsing():
    with open('.//datasets//hollywood-theatrical-market-synopsis-1995-to-2021//TopProductionMethods.csv', newline='',encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        next(reader)
        for row in reader:
            query_insert(sql.insert_topproductionmethods, row)
            print(row)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create table
    query_create(sql.table_topproductionmethods);
    #query(sql.insert_AnnualTicketSales);

    # parsing data
    csv_parsing()
    #results = query(sql.test_select);
    #print("results: ", results)







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
