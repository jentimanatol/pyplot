import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

data_file = 'marine-heat-waves_fig-3.csv'
df = pd.read_csv(data_file, skiprows=6, header=0)
df.columns = df.columns.str.strip().str.replace(' ', '_')
df_long = pd.melt(df, id_vars=['Year'], var_name='Region_Intensity', value_name='Percent_Area')
df_long[['Region', 'Intensity']] = df_long['Region_Intensity'].str.split('_', n=1, expand=True)
df_long.drop(columns=['Region_Intensity'], inplace=True)

regions = df_long['Region'].unique()

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='region-dropdown',
        options=[{'label': region, 'value': region} for region in regions],
        value=regions[0]
    ),
    dcc.Graph(id='region-plot')
])

@app.callback(
    Output('region-plot', 'figure'),
    [Input('region-dropdown', 'value')]
)
def update_plot(selected_region):
    filtered_df = df_long[df_long['Region'] == selected_region]
    fig = go.Figure()

    for intensity in filtered_df['Intensity'].unique():
        intensity_data = filtered_df[filtered_df['Intensity'] == intensity]
        fig.add_trace(go.Scatter(x=intensity_data['Year'], y=intensity_data['Percent_Area'], mode='lines', name=intensity))

    fig.update_layout(title=f'{selected_region} - Percent Area Affected Over Time',
                      xaxis_title='Year',
                      yaxis_title='Percent Area Affected (%)')

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
