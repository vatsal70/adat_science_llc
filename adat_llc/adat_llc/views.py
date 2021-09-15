from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
import pandas as pd



def homepage(request):
    dataframe = pd.read_excel('static/excel_file/data_file.xlsx')
    
    if request.method == 'POST':
        data = request.POST.get('btn')
        dataframe_values = dataframe[dataframe[data]==1]['File Name'].values
        params = {
            'dataframe_values': dataframe_values,
            'data': data,
            'fetching_data': True,
        }
        return render(request, 'adat_llc/index.html', params)
    
    return render(request, 'adat_llc/index.html')