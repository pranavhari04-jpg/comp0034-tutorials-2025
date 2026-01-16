import streamlit as st
from io import StringIO
import pandas as pd
from src.data.mock_api import get_event_data
from src.utils.line_chart import line_chart
import plotly.express as px

# --- 1. Load the Actual Paralympics Data ---
@st.cache_data
def load_data():
    """ Read the JSON structured data into a pandas DataFrame """
    para_data = get_event_data()
    df = pd.read_json(StringIO(para_data))
    df['start'] = pd.to_datetime(df['start'], dayfirst=True)
    df['end'] = pd.to_datetime(df['end'], dayfirst=True)
    return df

st.title('Paralympics data')

# Call the function to get the real data
df_paralympics = load_data()

# Display the real data table
st.dataframe(df_paralympics)

# --- 2. Create the Chart using the REAL Data ---
# Use df_paralympics here, NOT the dummy df you created later
chart = line_chart("participants", df_paralympics)
st.plotly_chart(chart)


# --- 3. (Optional) Your Practice Code Below ---
# If you still want to keep the "Roadmap/Stars" example, use a different variable name
# like 'df_dummy' so it doesn't overwrite your real data.

from numpy.random import default_rng as rng

df_dummy = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": [
            "https://roadmap.streamlit.app",
            "https://extras.streamlit.app",
            "https://issues.streamlit.app",
        ],
        "stars": rng(0).integers(0, 1000, size=3),
        "views_history": rng(0).integers(0, 5000, size=(3, 30)).tolist(),
    }
)

st.write("---")
st.subheader("Streamlit Column Config Example")
st.dataframe(
    df_dummy,
    column_config={
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)
