import pandas as pd
import openpyxl
import interface
import os

def dbrefresh(orig_curr, transf_curr):
    exch_data = pd.read_excel('exchanges.xlsx')
    old_qnt = exch_data.loc[(exch_data.pairs==f'{orig_curr}-{transf_curr}'), 'quantity']
    exch_data.loc[(exch_data.pairs==f'{interface.get_combo_values()[0]}-{interface.get_combo_values()[1]}'), 'quantity'] = old_qnt + 1
    os.remove('exchanges.xlsx')
    writer = pd.ExcelWriter('exchanges.xlsx')
    exch_data.to_excel(writer, 'exchanges')
    writer.save()

def dbsort ():
    unsorted_data = pd.read_excel('exchanges.xlsx')
    sorted_data = unsorted_data.sort_values(by='quantity', ascending=False)
    return sorted_data

