# pip install panel pandas ipywidgets_bokeh mosaic-widget
import pandas as pd
from mosaic_widget import MosaicWidget

weather = pd.read_csv(
    "https://uwdata.github.io/mosaic-datasets/data/seattle-weather.csv",
    parse_dates=["date"],
)

specification = {
    "meta": {
        "title": "Seattle Weather",
        "description": "An interactive view of Seattle’s weather, including maximum temperature, amount of precipitation, and type of weather. By dragging on the scatter plot, you can see the proportion of days in that range that have sun, fog, drizzle, rain, or snow.\n",
        "credit": "Based on a [Vega-Lite/Altair example](https://vega.github.io/vega-lite/examples/interactive_seattle_weather.html) by Jake Vanderplas.",
    },
    "params": {
        "click": {"select": "single"},
        "domain": ["sun", "fog", "drizzle", "rain", "snow"],
        "colors": ["#e7ba52", "#a7a7a7", "#aec7e8", "#1f77b4", "#9467bd"],
    },
    "vconcat": [
        {
            "hconcat": [
                {
                    "plot": [
                        {
                            "mark": "dot",
                            "data": {"from": "weather", "filterBy": "$click"},
                            "x": {"dateMonthDay": "date"},
                            "y": "temp_max",
                            "fill": "weather",
                            "r": "precipitation",
                            "fillOpacity": 0.7,
                        },
                        {
                            "select": "intervalX",
                            "as": "$range",
                            "brush": {"fill": "none", "stroke": "#888"},
                        },
                        {
                            "select": "highlight",
                            "by": "$range",
                            "fill": "#ccc",
                            "fillOpacity": 0.2,
                        },
                        {"legend": "color", "as": "$click", "columns": 1},
                    ],
                    "xyDomain": "Fixed",
                    "xTickFormat": "%b",
                    "colorDomain": "$domain",
                    "colorRange": "$colors",
                    "rDomain": "Fixed",
                    "rRange": [2, 10],
                    "width": 680,
                    "height": 300,
                }
            ]
        },
        {
            "plot": [
                {
                    "mark": "barX",
                    "data": {"from": "weather"},
                    "x": {"count": None},
                    "y": "weather",
                    "fill": "#ccc",
                    "fillOpacity": 0.2,
                },
                {
                    "mark": "barX",
                    "data": {"from": "weather", "filterBy": "$range"},
                    "x": {"count": None},
                    "y": "weather",
                    "fill": "weather",
                    "order": "weather",
                },
                {"select": "toggleY", "as": "$click"},
                {"select": "highlight", "by": "$click"},
            ],
            "xDomain": "Fixed",
            "yDomain": "$domain",
            "yLabel": None,
            "colorDomain": "$domain",
            "colorRange": "$colors",
            "width": 680,
        },
    ],
}
mosaic = MosaicWidget(specification, data={"weather": weather})

# THE PANEL APP

import panel as pn

pn.extension("ipywidgets")

component = pn.panel(mosaic, sizing_mode="stretch_width")

pn.template.FastListTemplate(
    logo="https://panel.holoviz.org/_static/logo_horizontal_dark_theme.png",
    title="Works with MosaicWidget",
    main=[component],
).servable()