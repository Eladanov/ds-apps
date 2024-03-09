from dash import Output, Input, State
from additional import p
from additional import gb

def make_callbacks(app):
    @app.callback(
        Output(component_id='example-output', component_property='children'),
        [Input('button', 'n_clicks'),
         State('age', 'value'),
         State('job', 'value'),
         State('marital', 'value'),
         State('education', 'value'),
         State('default', 'value'),
         State('housing', 'value'),
         State('loan', 'value'),
         State('contact', 'value'),
         State('month', 'value'),
         State('day_of_week', 'value'),
         State('campaign', 'value'),
         State('previous', 'value'),
         State('poutcome', 'value'),
         State('cons_price_idx', 'value'),
         State('cons_conf_idx', 'value'),
         State('euribor3m', 'value')])
    def update_predict_value(button, age, job, marital, education, default, housing, loan, contact, month, day_of_week,
                             campaign, previous, poutcome, cons_price_idx, cons_conf_idx, euribor3m):
        p0 = p.copy()
        if button == 0:
            return None
        else:
            p0['age'] = age
            p0['campaign'] = campaign
            p0['previous'] = previous
            p0['cons_price_idx'] = cons_price_idx
            p0['cons_conf_idx'] = cons_conf_idx
            p0['euribor3m'] = euribor3m
            p0[f"job_{job}"] = 1
            p0[f"marital_{marital}"] = 1
            p0[f"education_{education}"] = 1
            p0[f"default_{default}"] = 1
            p0[f"housing_{housing}"] = 1
            p0[f"loan_{loan}"] = 1
            p0[f"contact_{contact}"] = 1
            p0[f"month_{month}"] = 1
            p0[f"day_of_week_{day_of_week}"] = 1
            p0[f"poutcome_{poutcome}"] = 1
            try:
                score = round(gb.predict_proba(p0)[0][1] * 100, 1)
                return f"{score}%"
            except:
                return "OOPS, error has occurred - Please check you chose values for all input features"
