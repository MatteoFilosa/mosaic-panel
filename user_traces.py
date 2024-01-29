import pandas as pd
from mosaic_widget import MosaicWidget

file_prefix = "data/user_traces_falcon/formatted_exploration_falcon_7M_"
file_extension = ".json"
num_files = 50

# Initialize an empty DataFrame to store the combined data
combined_user_trace = pd.DataFrame()

# Loop through the range of file numbers and read each file
for i in range(1, num_files + 1):
    file_path = f"{file_prefix}{i}{file_extension}"
    df = pd.read_json(file_path)

    # Concatenate the current DataFrame with the combined DataFrame
    combined_user_trace = pd.concat([combined_user_trace, df], ignore_index=True)


combined_plot = {
"plot": [
        {
          "mark": "barY",
          "data": { "from": "combined_user_trace" },
          "x": "event",
          "y": { "count": None }
        }
      ],
      "width": 800
}



mosaic = MosaicWidget(combined_plot, data = {"combined_user_trace": combined_user_trace})


# THE PANEL APP

import panel as pn

pn.extension("ipywidgets")

component = pn.panel(mosaic, sizing_mode="stretch_width")

pn.template.FastListTemplate(
    logo="https://panel.holoviz.org/_static/logo_horizontal_dark_theme.png",
    title="Works with MosaicWidget",
    main=[component],
).servable()