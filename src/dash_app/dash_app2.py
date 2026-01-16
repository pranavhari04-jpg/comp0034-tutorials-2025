from io import StringIO
from dash import Dash, html, dcc  # Ensure dcc is imported
import dash_ag_grid as dag
import pandas as pd
from src.data.mock_api import get_event_data
from src.utils.line_chart import line_chart

# 1. Load and process data
para_data = get_event_data()
df = pd.read_json(StringIO(para_data))
df['start'] = pd.to_datetime(df['start'], dayfirst=True)
df['end'] = pd.to_datetime(df['end'], dayfirst=True)

# 2. Initialize the app
app = Dash(__name__)

# 3. Define the layout
app.layout = html.Div([
    
    html.H1(children='Title of Dash App'),

    # The Table
    dag.AgGrid(
        rowData=df.to_dict("records"),
        columnDefs=[{"field": col} for col in df.columns]
    ),

    # --- THE FIX IS HERE ---
    # You must put the chart INSIDE a dcc.Graph component within the layout
    dcc.Graph(
        figure=line_chart("participants", df)
    )
])

if __name__ == '__main__':
    app.run(debug=True)
