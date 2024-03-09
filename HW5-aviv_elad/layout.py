from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify
from additional import *

All = html.Div([
    dbc.Row(dbc.Col(html.H1("Zoltar!", className="bg-opacity-50 p-2 m-1 bg-primary text-light fw-bold rounded"),
                    width={'size': 12, 'offset': 1})),

    dbc.Row(dbc.Col(html.H4(
        "Please input a potential marketing call and when done press the Predict! button to see it's predicted score of success"),
                    width={'size': 12, 'offset': 1})),

    dbc.Row(
        [
            dbc.Col(
                html.Div([
                    html.Hr(),
                    html.Div([
                        dbc.Label('Age', html_for='age'),
                        dcc.Slider(min_age, max_age, 1, id='age', value=median_age,
                                   marks={i: '{}'.format(i) for i in range(min_age, max_age) if i % 10 == 0},
                                   tooltip={"placement": "bottom", "always_visible": True}, included=False)],
                        className=DESIGN_CLASS, id='slider_age'),

                    html.Div([
                        dbc.Label('Number of contacts performed during this campaign and for this client:',
                                  html_for='campaign'),
                        dcc.Slider(min_campaign, max_campaign, 1, id='campaign', value=median_campaign,
                                   marks={i: '{}'.format(i) for i in range(int(min_campaign), int(max_campaign)) if i % 10 == 0},
                                   tooltip={"placement": "bottom", "always_visible": True}, included=False)],
                        className=DESIGN_CLASS, id='slider_campaign'),

                    html.Div([
                        dbc.Label('Number of contacts performed before this campaign and for this client:',
                                  html_for='previous'),
                        dcc.Slider(min_previous, max_previous, 1, id='previous', value=median_previous,
                                   marks={i: '{}'.format(i) for i in range(int(min_previous), int(max_previous)+1)},
                                   tooltip={"placement": "bottom", "always_visible": True}, included=False)],
                        className=DESIGN_CLASS, id='slider_previous'),

                    html.Div([
                        dbc.Label('Consumer price index:', html_for='cons_price_idx'),
                        dcc.Slider(min_cons_price_idx, max_cons_price_idx, 0.1, id='cons_price_idx',
                                   value=median_cons_price_idx,
                                   marks={i: '{}'.format(i) for i in range(int(min_cons_price_idx), int(max_cons_price_idx)+1)},
                                   tooltip={"placement": "bottom", "always_visible": True}, included=False)],
                        className=DESIGN_CLASS, id='slider_cons_price_idx'),

                    html.Div([
                        dbc.Label('Consumer confidence index:', html_for='cons_conf_idx'),
                        dcc.Slider(min_cons_conf_idx, max_cons_conf_idx, 0.1, id='cons_conf_idx',
                                   value=median_cons_conf_idx,
                                   marks={i: '{}'.format(i) for i in range(int(min_cons_conf_idx), int(max_cons_conf_idx)) if i % 5 == 0},
                                   tooltip={"placement": "bottom", "always_visible": True}, included=False)],
                        className=DESIGN_CLASS, id='slider_cons_conf_idx'),

                    html.Div([
                        dbc.Label('Euribor 3 month rate:', html_for='euribor3m'),
                        dcc.Slider(min_euribor3m, max_euribor3m, 0.1, id='euribor3m', value=median_euribor3m,
                                   marks={i: '{}'.format(i) for i in range(int(min_euribor3m), int(max_euribor3m)+1)},
                                   tooltip={"placement": "bottom", "always_visible": True}, included=False)],
                        className=DESIGN_CLASS, id='slider_euribor3m'),

                    html.Div([
                        dbc.Label('Last contact month of year:', html_for='month'),
                        dbc.Select(options=options_month, id='month', value=mode_month)],
                        className=DESIGN_CLASS, style={"width": "50%"}),

                    html.Div([
                        dbc.Label('Last contact day of the week:', html_for='day_of_week'),
                        dbc.Select(options=options_day_of_week, id='day_of_week', value=mode_day_of_week)],
                        className=DESIGN_CLASS, style={"width": "50%"})
                ]),
                width={'size': 4, 'order': 1, 'offset': 1}
            ),
            dbc.Col(
                html.Div([
                    html.Br(),
                    html.Div([
                        dbc.Label('Job:', html_for='job'),
                        dbc.Select(options=options_job, id='job', value=mode_job)],
                        className=DESIGN_CLASS, style={"width": "50%"}),

                    html.Div([
                        dbc.Label('Marital Status:', html_for='marital'),
                        dbc.Select(options=options_marital, id='marital', value=mode_marital)],
                        className=DESIGN_CLASS, style={"width": "50%"}),

                    html.Div([
                        dbc.Label('Education:', html_for='education'),
                        dbc.Select(options=options_education, id='education', value=mode_education)],
                        className=DESIGN_CLASS, style={"width": "50%"}),

                    html.Div([
                        dbc.Label('Has credit in default?', html_for='default'),
                        dbc.Select(options=options_default, id='default', value=mode_default)],
                        className=DESIGN_CLASS, style={"width": "50%"}),

                    html.Div([
                        dbc.Label('Has housing loan?', html_for='housing'),
                        dbc.Select(options=options_housing, id='housing', value=mode_housing)],
                        className=DESIGN_CLASS, style={"width": "50%"}),

                    html.Div([
                        dbc.Label('Has hersonal loan:', html_for='loan'),
                        dbc.Select(options=options_loan, id='loan', value=mode_loan)],
                        className=DESIGN_CLASS, style={"width": "50%"}),

                    html.Div([
                        dbc.Label('Contact communication type:', html_for='contact'),
                        dbc.Select(options=options_contact, id='contact', value=mode_contact)],
                        className=DESIGN_CLASS, style={"width": "50%"}),

                    html.Div([
                        dbc.Label('Outcome of the previous marketing campaign:', html_for='poutcome'),
                        dbc.Select(options=options_poutcome, id='poutcome', value=mode_poutcome)],
                        className=DESIGN_CLASS, style={"width": "50%"})
                ]),
                width={'size': 4, 'order': 2}
            ),

            dbc.Col(
                html.Div([
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    dbc.Button([DashIconify(icon='nimbus:discount-circle'), ' Predict!'], outline=True, color="primary",
                               id='button', n_clicks=0, size='lg', className="me-1",),
                    html.Br(),
                    html.Br(),
                    html.H5('Zoltar Says...', className="text-primary", style={"font-size": "250%"}),
                    html.Br(),
                    html.Div(id="example-output", className="text-danger", style={"font-size": "250%", "verticalAlign": "middle"}, children=[])],
                    id="page-content"),
                width={'size': 2, 'order': 3})
        ]
    )
]
)

def make_layout():
    return html.Div([All])
