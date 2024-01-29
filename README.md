Github repo for experiments with Mosaic: https://uwdata.github.io/mosaic/what-is-mosaic/

Mosaic is a framework for linking data visualizations, tables, input widgets, and other data-driven components, while leveraging a database for scalable processing. With Mosaic, you can interactively visualize and explore millions and even billions of data points.

A key idea is that interface components – Mosaic clients – publish their data needs as queries that are managed by a central coordinator. The coordinator may further optimize queries before issuing them to a backing data source such as DuckDB.

This repo uses also Panel: https://panel.holoviz.org/getting_started/installation.html , used to build powerful visualizations with Python. Works with many widgets, including Mosaic.

#INSTALLATION

pip install panel pandas ipywidgets_bokeh mosaic-widget

If there is a problem in Windows saying: 
"UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 687875: character maps to <undefined>", change a line in __init.py__ in:

ESM = (bundled_assets_dir / "index.js").read_text(encoding="utf-8")

If there is an error saying " no module named 'pandas.core.arrays.arrow.dtype' " install pandas with: 

pip uninstall pandas

and run:

pip install pandas==2.0.0

To run a python file containing the visualization write in the terminal: panel serve <name.py>

