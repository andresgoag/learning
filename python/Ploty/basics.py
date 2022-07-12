import os
import plotly.io as pio
import plotly.graph_objects as go



if not os.path.exists("images"):
    os.mkdir("images")


tiempo = [1,2,3,4,5,6,7,8,9,10]
temperatura = [5,3,1,4,2,6,6,6,5,4]
humedad = [60,60,60,50,40,50,30,10,40,20]



layout = dict(

    showlegend = True,
    plot_bgcolor = "#fff",

    margin = dict(
        autoexpand = True,
        b=0,
        l=0,
        r=0,
        t=0,
        pad=0
    ),

    # Crear ejes
    # NOTA: estos se pueden adicionar despues con la funcion fig.update_layout()

    # crear el eje x
    xaxis = dict(
        # calendar='gregorian', # activarlo si es un eje de calendario
        domain=[0.05, 1], #Sets the domain of this axis (in plot fraction).
        showgrid=True, 
        gridwidth=1, 
        gridcolor='#000',
        zeroline=True, 
        zerolinewidth=1, 
        zerolinecolor='#000',
         tickfont = dict(color = "#000", family="sans-serif", size=20),
    ),

    # crear el eje y
    yaxis = dict(
        title='yaxis 1',
        showgrid=True, 
        gridwidth=1, 
        gridcolor='#000',
        zeroline=True, 
        zerolinewidth=1, 
        zerolinecolor='#000',
        linewidth=2,
        linecolor="#000",
        titlefont = dict(color = "#000", family="sans-serif", size=20),
        tickfont = dict(color = "#000", family="sans-serif", size=20),
    ),

    yaxis2 = dict(
        showgrid=False,
        title="yaxis2 title",
        titlefont = dict(color = "#b0a", family="sans-serif", size=20),
        tickfont = dict(color = "#b0a", family="sans-serif", size=20),
        anchor = "free",
        overlaying = "y",
        side = "left",
        # position = 0,
        linewidth=2,
        linecolor="#000",
    )
)



# Crear figura
fig = go.Figure(layout=layout)


# Añadir linea
fig.add_trace(
    go.Scatter(
        name="yaxis1",
        x=tiempo, 
        y=temperatura, 
        xaxis="x", # Sets a reference between this trace's x and a 2D cartesian x axis. If "x" (default), refers to layout.xaxis, "x2" refers to layout.xaxis2.
        yaxis="y", # Sets a reference between this trace's y and a 2D cartesian y axis. If "y" (default), refers to layout.yaxis, "y2" refers to layout.yaxis2.
        line = dict(
            color = "#0af",
            width = 2,
            shape = "spline",
        ),
    )
)

fig.add_trace(
    go.Scatter(
        name="yaxis2",
        x=tiempo, 
        y=humedad,
        line = dict(
            color = "#b0a",
            width = 2,
            shape = "spline",
        ),
        xaxis="x",
        yaxis="y2",
    )
)





# Mostrar la grafica en un browser
fig.show()




# Exportar imagenes de la grafica
# pio.write_image(fig, file, format=None, scale=None, width=None, height=None, validate=True, engine='auto')

# Raster
pio.write_image(fig, 'images/fig1.png', format="png", scale=2, width=1920, height=500)

# vector format svg, pdf
fig.write_image("images/fig1.svg")

fig.write_image("images/fig1.pdf", format="pdf", scale=2, width=1920, height=500)







'''

layout
======

https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html



Scatter traces docs:
https://plotly.com/python/reference/scatter/


Parameter of scatter

line: Dict
============


color
Type: color
Sets the line color.

width
Type: number greater than or equal to 0
Default: 2
Sets the line width (in px).

shape
Type: enumerated , one of ( "linear" | "spline" | "hv" | "vh" | "hvh" | "vhv" )
Default: "linear"
Determines the line shape. With "spline" the lines are drawn using spline interpolation. The other available values correspond to step-wise line shapes.

smoothing
Type: number between or equal to 0 and 1.3
Default: 1
Has an effect only if `shape` is set to "spline" Sets the amount of smoothing. "0" corresponds to no smoothing (equivalent to a "linear" shape).

dash
Type: string
Default: "solid"
Sets the dash style of lines. Set to a dash type string ("solid", "dot", "dash", "longdash", "dashdot", or "longdashdot") or a dash length list in px (eg "5px,10px,2px,2px").

'''

