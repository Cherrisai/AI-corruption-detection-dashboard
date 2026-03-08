import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import IsolationForest, RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
import time

st.set_page_config(layout="wide")

# ------------------------------
# DARK UI
# ------------------------------

st.markdown("""
<style>

body{
background:#0e1117;
color:white;
}

.kpi{
background:#141a22;
padding:20px;
border-radius:14px;
border:1px solid #2d3748;
text-align:center;
box-shadow:0px 3px 10px rgba(0,0,0,0.5);
}

.kpi-title{
font-size:14px;
color:#9ca3af;
}

.kpi-value{
font-size:28px;
color:#00eaff;
font-weight:bold;
}

.kpi-pred{
color:#fbbf24;
font-size:13px;
}

.summary{
background:#141a22;
padding:12px;
border-radius:10px;
border:1px solid #2d3748;
margin-top:10px;
}

</style>
""",unsafe_allow_html=True)

# ------------------------------
# LOAD DATA
# ------------------------------

df=pd.read_csv("corrupt_data.csv")
df.fillna(0,inplace=True)

# convert column names to readable
df.columns=[c.replace("_"," ") for c in df.columns]

def crore(x):
    return x/10000000

df["corruption cr"]=df["corruption amount rs"]/10000000

# ------------------------------
# FILTERS
# ------------------------------

st.sidebar.title("Search Filters")

state=st.sidebar.selectbox("State",["All"]+list(df["state"].unique()))
city=st.sidebar.selectbox("City",["All"]+list(df["city"].unique()))
category=st.sidebar.selectbox("Project Category",["All"]+list(df["project category"].unique()))
year=st.sidebar.selectbox("Year",["All"]+list(df["year"].unique()))

data=df.copy()

if state!="All":
    data=data[data["state"]==state]

if city!="All":
    data=data[data["city"]==city]

if category!="All":
    data=data[data["project category"]==category]

if year!="All":
    data=data[data["year"]==year]

# ------------------------------
# KPI PREDICTION
# ------------------------------

year_data=df.groupby("year")["corruption amount rs"].sum().reset_index()

next_pred=0

if len(year_data)>1:

    model=LinearRegression()
    model.fit(year_data[["year"]],year_data["corruption amount rs"])

    next_year=year_data.year.max()+1
    next_pred=model.predict([[next_year]])[0]

# ------------------------------
# KPI CARDS
# ------------------------------

total_corruption=data["corruption amount rs"].sum()
allocated=data["allocated budget rs"].sum()
actual=data["actual cost rs"].sum()

c1,c2,c3,c4=st.columns(4)

c1.markdown(f"""
<div class="kpi">
<div class="kpi-title">Total Corruption</div>
<div class="kpi-value">₹{crore(total_corruption):.2f} Cr</div>
<div class="kpi-pred">Next Year Prediction ₹{crore(next_pred):.2f} Cr</div>
</div>
""",unsafe_allow_html=True)

c2.markdown(f"""
<div class="kpi">
<div class="kpi-title">Allocated Budget</div>
<div class="kpi-value">₹{crore(allocated):.2f} Cr</div>
</div>
""",unsafe_allow_html=True)

c3.markdown(f"""
<div class="kpi">
<div class="kpi-title">Actual Cost</div>
<div class="kpi-value">₹{crore(actual):.2f} Cr</div>
</div>
""",unsafe_allow_html=True)

c4.markdown(f"""
<div class="kpi">
<div class="kpi-title">Projects</div>
<div class="kpi-value">{len(data)}</div>
</div>
""",unsafe_allow_html=True)

st.divider()

# ====================================
# STATE CORRUPTION
# ====================================

st.header("State Wise Corruption")

state_grp=data.groupby("state")["corruption cr"].sum().sort_values(ascending=False)

fig=px.bar(state_grp,color=state_grp.index,template="plotly_dark",
labels={"value":"Corruption (₹ Crore)","state":"State"})

st.plotly_chart(fig,use_container_width=True)

highest=state_grp.idxmax()
lowest=state_grp.idxmin()

st.markdown(f"""
<div class="summary">

This chart compares corruption across states.

Highest corruption state: <b>{highest}</b>  
Lowest corruption state: <b>{lowest}</b>

States with larger corruption bars indicate higher financial leakage risks in public projects.

</div>
""",unsafe_allow_html=True)

# ====================================
# CITY CORRUPTION
# ====================================

st.header("City Wise Corruption")

city_grp=data.groupby("city")["corruption cr"].sum().sort_values(ascending=False)

fig=px.bar(city_grp,color=city_grp.index,template="plotly_dark")

st.plotly_chart(fig,use_container_width=True)

st.markdown(f"""
<div class="summary">

This chart displays corruption levels across cities.

Highest corruption city: <b>{city_grp.idxmax()}</b>  
Lowest corruption city: <b>{city_grp.idxmin()}</b>

Major urban infrastructure spending often results in higher corruption exposure.

</div>
""",unsafe_allow_html=True)

# ====================================
# STATE FORECAST
# ====================================

st.header("State Corruption Forecast (Past)")

select_state=st.selectbox("Select State",df["state"].unique())

state_data=df[df["state"]==select_state]

year_grp=state_data.groupby("year")["corruption amount rs"].sum().reset_index()

fig=px.line(year_grp,x="year",y="corruption amount rs",template="plotly_dark")

st.plotly_chart(fig,use_container_width=True)

st.subheader("State Corruption Future Prediction")

if len(year_grp)>1:

    model=LinearRegression()
    model.fit(year_grp[["year"]],year_grp["corruption amount rs"])

    future_years=np.arange(year_grp.year.max()+1,year_grp.year.max()+6)

    preds=model.predict(future_years.reshape(-1,1))

    pred_df=pd.DataFrame({"year":future_years,"prediction":preds/10000000})

    fig2=px.line(pred_df,x="year",y="prediction",template="plotly_dark",
    labels={"prediction":"Predicted Corruption (₹ Crore)"})

    st.plotly_chart(fig2,use_container_width=True)

# ====================================
# CITY FORECAST
# ====================================

st.header("City Corruption Forecast (Past)")

select_city=st.selectbox("Select City",df["city"].unique())

city_data=df[df["city"]==select_city]

year_grp=city_data.groupby("year")["corruption amount rs"].sum().reset_index()

fig=px.line(year_grp,x="year",y="corruption amount rs",template="plotly_dark")

st.plotly_chart(fig,use_container_width=True)

st.subheader("City Corruption Future Prediction")

if len(year_grp)>1:

    model=LinearRegression()
    model.fit(year_grp[["year"]],year_grp["corruption amount rs"])

    future=np.arange(year_grp.year.max()+1,year_grp.year.max()+6)

    preds=model.predict(future.reshape(-1,1))

    pred_df=pd.DataFrame({"year":future,"prediction":preds/10000000})

    fig=px.line(pred_df,x="year",y="prediction",template="plotly_dark")

    st.plotly_chart(fig,use_container_width=True)

# =====================================
# ANN POPULATION CORRUPTION BENEFIT
# =====================================

st.header("Public Benefit if Corruption Did Not Happen (ANN Prediction)")

import numpy as np

features=[
    "allocated budget rs",
    "actual cost rs",
    "population",
    "traffic density",
    "year"
]

features=[f for f in features if f in df.columns]

target="corruption amount rs"

if len(features)>=3:

    X=df[features]
    y=df[target]

    scaler=StandardScaler()
    X_scaled=scaler.fit_transform(X)

    ann_model=MLPRegressor(
        hidden_layer_sizes=(128,64,32),
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    ann_model.fit(X_scaled,y)

    df["ann corruption prediction"]=ann_model.predict(X_scaled)

    # Year filter
    year_select=st.selectbox(
        "Select Year",
        sorted(df["year"].unique())
    )

    year_df=df[df["year"]==year_select]

    # State corruption total
    state_year=year_df.groupby("state").agg({
        "ann corruption prediction":"sum",
        "population":"first"
    }).reset_index()

    # Convert corruption to crore
    state_year["corruption crore"]=state_year["ann corruption prediction"]/10000000

    # Per person benefit
    state_year["per person benefit rs"]=(
        state_year["ann corruption prediction"]/
        state_year["population"]
    )

    # Chart corruption by state
    fig=px.bar(
        state_year,
        x="state",
        y="corruption crore",
        template="plotly_dark",
        labels={
            "corruption crore":"Predicted Corruption ₹ Crore",
            "state":"State"
        }
    )

    st.plotly_chart(fig,use_container_width=True)

    # Per person benefit chart
    fig2=px.bar(
        state_year,
        x="state",
        y="per person benefit rs",
        template="plotly_dark",
        labels={
            "per person benefit rs":"₹ Per Person Benefit",
            "state":"State"
        }
    )

    st.plotly_chart(fig2,use_container_width=True)

    # Highest and lowest
    max_state=state_year.loc[
        state_year["per person benefit rs"].idxmax(),"state"
    ]

    max_value=state_year["per person benefit rs"].max()

    min_state=state_year.loc[
        state_year["per person benefit rs"].idxmin(),"state"
    ]

    min_value=state_year["per person benefit rs"].min()

st.markdown(f"""
### AI Insight Summary

If corruption did not occur in **{year_select}**:

• People in **{max_state}** could receive around **₹{max_value:,.0f} per person**.

• People in **{min_state}** would receive around **₹{min_value:,.0f} per person**.

This analysis divides total corruption loss by the population of each state,
estimating how much financial benefit citizens could receive if corruption were eliminated.

The ANN model predicts corruption trends based on infrastructure spending,
population size, and traffic density factors.
""")

# =====================================
# CITIZEN WEALTH LOSS COUNTER (STRONG)
# =====================================

import time
import numpy as np

st.header("Citizen Wealth Loss Counter")

year_selected = st.selectbox(
    "Select Year for Corruption Impact",
    sorted(df["year"].unique())
)

year_data = df[df["year"] == year_selected]

# -------------------------------------
# TOTAL CORRUPTION (SUM ALL PROJECTS)
# -------------------------------------

total_corruption = year_data["corruption amount rs"].sum()

# -------------------------------------
# UNIQUE POPULATION BY STATE
# -------------------------------------

state_population = (
    year_data
    .groupby("state")["population"]
    .first()   # ensures unique population per state
)

total_population = state_population.sum()

# -------------------------------------
# PER PERSON LOSS
# -------------------------------------

if total_population > 0:
    per_person_loss = total_corruption / total_population
else:
    per_person_loss = 0

# Convert corruption to crore
total_corruption_crore = total_corruption / 10000000

# -------------------------------------
# DISPLAY COUNTERS
# -------------------------------------

col1, col2 = st.columns(2)

counter1 = col1.empty()
counter2 = col2.empty()

# Smooth animation
steps = 80

for value in np.linspace(0, total_corruption_crore, steps):

    corruption_progress = value
    person_progress = per_person_loss * (value / total_corruption_crore) if total_corruption_crore > 0 else 0

    counter1.metric(
        "Total Corruption Loss (₹ Crore)",
        f"₹ {corruption_progress:,.0f} Cr"
    )

    counter2.metric(
        "Per Citizen Wealth Loss",
        f"₹ {person_progress:,.0f}"
    )

    time.sleep(0.02)

# -------------------------------------
# FINAL VALUES
# -------------------------------------

counter1.metric(
    "Total Corruption Loss (₹ Crore)",
    f"₹ {total_corruption_crore:,.0f} Cr"
)

counter2.metric(
    "Per Citizen Wealth Loss",
    f"₹ {per_person_loss:,.0f}"
)

# -------------------------------------
# INSIGHT SUMMARY
# -------------------------------------

highest_state = (
    year_data
    .groupby("state")["corruption amount rs"]
    .sum()
    .idxmax()
)

st.markdown(f"""
### Corruption Impact Insight

In **{year_selected}**, total corruption loss reached **₹{total_corruption_crore:,.0f} Crore**.

If corruption did not occur, every citizen could receive approximately **₹{per_person_loss:,.0f}**.

The state contributing the highest corruption loss is **{highest_state}**.

This counter shows how corruption directly reduces the financial wealth available to citizens.
""")






# ====================================
# ANN MODEL : PROJECT CONSTRUCTION ANALYSIS
# ====================================

st.header("AI Corruption detect(ANN Model)")

project_types=["road type","bridge type","park type","government building type"]

existing_types=[p for p in project_types if p in df.columns]

features=["allocated budget rs","actual cost rs","population","traffic density","year"]
features=[f for f in features if f in df.columns]

target="corruption amount rs"

if len(features)>=2:

    X=df[features]
    y=df[target]

    scaler=StandardScaler()
    X_scaled=scaler.fit_transform(X)

    ann=MLPRegressor(
        hidden_layer_sizes=(128,64,32),
        activation="relu",
        solver="adam",
        max_iter=500,
        random_state=42
    )

    ann.fit(X_scaled,y)

    df["ann corruption prediction"]=ann.predict(X_scaled)

    # --------------------------------
    # STATE LEVEL ANALYSIS
    # --------------------------------

    st.subheader("State Wise Construction vs Corruption")

    state_construct=df.groupby("state")[["actual cost rs","corruption amount rs"]].sum()/10000000

    fig=px.bar(
        state_construct,
        barmode="group",
        template="plotly_dark",
        labels={"value":"₹ Crore","state":"State"}
    )

    st.plotly_chart(fig,use_container_width=True)

    highest_state=state_construct["corruption amount rs"].idxmax()

    st.markdown(f"""
    <div class="summary">

    This AI analysis compares **construction spending vs corruption losses** across states.

    State with highest corruption leakage: <b>{highest_state}</b>

    Large infrastructure projects like roads, bridges and buildings increase financial risk.

    </div>
    """,unsafe_allow_html=True)

    # --------------------------------
    # CITY LEVEL ANALYSIS
    # --------------------------------

    st.subheader("City Wise Construction vs Corruption")

    city_construct=df.groupby("city")[["actual cost rs","corruption amount rs"]].sum()/10000000

    fig=px.bar(
        city_construct,
        barmode="group",
        template="plotly_dark"
    )

    st.plotly_chart(fig,use_container_width=True)

    top_city=city_construct["corruption amount rs"].idxmax()

    st.markdown(f"""
    <div class="summary">

    This chart compares infrastructure construction spending and corruption leakage across cities.

    City with highest corruption risk: <b>{top_city}</b>

    Urban infrastructure investments often involve higher budgets,
    which increases corruption exposure if monitoring systems are weak.

    </div>
    """,unsafe_allow_html=True)

    # --------------------------------
    # PROJECT TYPE ANALYSIS
    # --------------------------------

    if existing_types:

        st.subheader("Project Type Analysis")

        project_select=st.selectbox("Select Infrastructure Type",existing_types)

        project_data=df.groupby(project_select)[["actual cost rs","corruption amount rs"]].sum()/10000000

        fig=px.bar(
            project_data,
            barmode="group",
            template="plotly_dark",
            labels={"value":"₹ Crore"}
        )

        st.plotly_chart(fig,use_container_width=True)

        worst_project=project_data["corruption amount rs"].idxmax()

        st.markdown(f"""
        <div class="summary">

        This AI section analyzes corruption risk by **infrastructure project type**.

        Highest corruption detected in project type: <b>{worst_project}</b>

        Infrastructure sectors like roads and bridges usually involve large budgets,
        which increases corruption risk.

        </div>
        """,unsafe_allow_html=True)


# =====================================
# STRONG ANN CORRUPTION INTELLIGENCE MODEL
# =====================================

st.header("Advanced AI Corruption Prediction (ANN)")

features=[
    "allocated budget rs",
    "actual cost rs",
    "population",
    "traffic density",
    "year"
]

features=[f for f in features if f in df.columns]

target="corruption amount rs"

if len(features)>=3:

    X=df[features]
    y=df[target]

    # Scaling
    scaler=StandardScaler()
    X_scaled=scaler.fit_transform(X)

    # Train test split
    X_train,X_test,y_train,y_test=train_test_split(
        X_scaled,
        y,
        test_size=0.2,
        random_state=42
    )

    # Deep ANN model
    ann_model=MLPRegressor(
        hidden_layer_sizes=(128,64,32),
        activation="relu",
        solver="adam",
        learning_rate="adaptive",
        max_iter=1000,
        random_state=42
    )

    ann_model.fit(X_train,y_train)

    predictions=ann_model.predict(X_scaled)

    df["ann corruption prediction"]=predictions

    # Convert to crore
    df["ann corruption prediction crore"]=df["ann corruption prediction"]/10000000

    st.success("ANN model trained successfully")


# =====================================
# CORRUPTION LEAKAGE %
# =====================================

st.subheader("Project Corruption Leakage %")

df["corruption percent"]=(df["corruption amount rs"]/df["allocated budget rs"])*100

leakage=df.groupby("project category")["corruption percent"].mean().sort_values(ascending=False)

fig=px.bar(
    leakage,
    template="plotly_dark",
    labels={"value":"Corruption %","project category":"Project"}
)

st.plotly_chart(fig,use_container_width=True)

highest=leakage.idxmax()

st.markdown(f"""
Highest corruption leakage detected in **{highest}** projects.

This means a larger percentage of public funds is lost due to corruption in this infrastructure category.
""")


# =====================================
# AI CORRUPTION RISK SCORE
# =====================================

st.subheader("AI Corruption Risk Score")

df["risk score"]=(
    df["ann corruption prediction"]/df["allocated budget rs"]
)*100

def risk_level(x):
    if x<5:
        return "Low Risk"
    elif x<15:
        return "Medium Risk"
    else:
        return "High Risk"

df["risk level"]=df["risk score"].apply(risk_level)

risk=df.groupby("state")["risk score"].mean()

fig=px.bar(
    risk.sort_values(ascending=False),
    template="plotly_dark",
    labels={"value":"Risk Score %","state":"State"}
)

st.plotly_chart(fig,use_container_width=True)

highest_risk=risk.idxmax()

st.markdown(f"""
AI model indicates **{highest_risk}** has the highest corruption risk based on ANN predictions.

Risk score measures how much corruption may occur relative to project budgets.
""")

# =====================================
# FUTURE CORRUPTION FORECAST
# =====================================

st.subheader("Future Corruption Forecast (ANN)")

future_years=np.arange(df["year"].max()+1,df["year"].max()+6)

avg_features=df[features].mean()

future_data=[]

for year in future_years:
    
    row=avg_features.copy()
    row["year"]=year
    
    future_data.append(row)

future_df=pd.DataFrame(future_data)

future_scaled=scaler.transform(future_df)

future_df["predicted corruption"]=ann_model.predict(future_scaled)/10000000

fig=px.line(
    future_df,
    x="year",
    y="predicted corruption",
    template="plotly_dark",
    markers=True,
    labels={"predicted corruption":"₹ Crore"}
)

st.plotly_chart(fig,use_container_width=True)

st.markdown("""
This ANN forecast estimates corruption trends for the next 5 years
based on historical infrastructure spending patterns.
""")

