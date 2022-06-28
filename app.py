# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 08:29:56 2022

@author: jjubin
"""

#limpiar explorador de variables
from IPython import get_ipython
get_ipython().magic('reset -sf')

#librerias básicas
import pandas as pd
import plotly.express as px
from dash import dcc
import dash
from dash import html
from dash.dependencies import Input, Output
from flask import Flask, render_template, request
from dash import Dash
import dash_html_components as dash_html


col_discr_map = {"Indice Obsoleto": "limegreen",
                "Tolerancias dimensionales AFG": "yellow",
                "Faltas de Material": "Red",
                "Marcas o golpes en las superficies": "cyan",
                "Otros": "Indigo",
                "Tolerancias dimensionales Subcontratas": "darkgrey",  
                "Delgadas": "darkcyan",
                "Obsolete index": "White",
                "Grietas / Pliegues / Fisuras": "Silver",
                "Pilladas (Forja/Calibrador)": "Gray",
                "Cascarilla / Cráteres": "Black",
                "Tolerancias geométricas AFG": "Maroon",
                "Falta trazabilidad": "DarkSalmon",
                "Defectos de punzonado": "Olive",
                "Desplazamientos": "Lime",
                "Oxido": "Green",
                "Rebabas": "Teal",
                "Gruesas": "Blue",
                "Torceduras": "Navy",
                "Marcas de macho": "Fuchsia",
                "Defectos superficiales (trazabilidad)": "Purple",
                "Incrustaciones": "darkslategrey",
                "Amolado": "lightslategray",
                "Limpieza de las piezas": "navajowhite",
                "Tolerancias superficiales AFG": "slateblue"}


a = pd.read_excel('C:/Users/alasalde/Downloads/File/prueba1datos.xlsx').reset_index()  
c = pd.read_excel('C:/Users/alasalde/Downloads/File/prueba1data3.xlsx').reset_index()




# app = Flask(__name__)

# dashApp = dash.Dash(server=app, routes_pathname_prefix="/")

# dashApp.layout = html.Div([
    

app = Dash(__name__, server=Flask(__name__))
app.layout = dash_html.Div([
            
        
        
        html.Div([
            dcc.Graph(id='grafic1')
        ]),
        
        html.Div([
            dcc.RangeSlider(a["index"].min(),
                            a["index"].max(),
                            2,
                            value=[a["index"].min(),a["index"].max()],
                            id='ArtVentas1'
                )
        ],style={"width": "75%", 
                 "margin-left":"5%"}),
                 
          
    
    
    ])

   

@app.callback(
    Output('grafic1','figure'),
    [Input('ArtVentas1','value')]
)



def update_graph(elegido1):

    dll=a["ArticuloVentas"][(a['index']>=elegido1[0])&(a['index']<elegido1[1])]
    print(dll)   
    dff = pd.merge(left=dll,right=c,how='left', left_on='ArticuloVentas', right_on='ArticuloVentas')

    scatterplot = px.bar(
        data_frame=dff,
        x="ArticuloVentas",
        y="Coste",
        color='Defecto',
        height=550,
        title="Chatarra por Referencia",
        color_discrete_map=col_discr_map
    )
    
    scatterplot.update_layout(xaxis={'categoryorder':'total descending'})
    return (scatterplot)






if __name__ == '__main__':
   app.run()














