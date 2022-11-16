import pandas as pd

def csv_return_list_total(csvPath):
    mainTableList = pd.read_csv(csvPath)
    mainTableListTotal = mainTableList.shape[0]
    return mainTableListTotal

def csv_return_cell_data(csvPath,columnTitle,rowNumber):
    mainTableList = pd.read_csv(csvPath)
    mainCellData = mainTableList[columnTitle][rowNumber]
    return mainCellData