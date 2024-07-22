import pandas as pd
import altair as alt

df = pd.read_csv('./results/number_of_hallucination.csv')

# Create a bar chart
chart = alt.Chart(df).mark_bar(size=60).encode(
    x=alt.X('Model:N', axis=alt.Axis(title='Model')),
    y=alt.Y('Number of Hallucinations:Q', axis=alt.Axis(title='Number of Hallucinations')),
    tooltip=['Model', 'Number of Hallucinations']
).properties(
    title='Number of Hallucinations by Model',
    width=400
).interactive()

# Save the chart
chart.save('hallucinations_by_model_bar_chart.html')