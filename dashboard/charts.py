import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def create_skill_pie(distribution):

    df = pd.DataFrame({
        "Category": list(distribution.keys()),
        "Count": list(distribution.values())
    })

    fig = px.pie(
        df,
        names="Category",
        values="Count",
        hole=0.5
    )

    fig.update_layout(
        title="Skill Distribution",
        template="plotly_white"
    )

    return fig


def create_skill_bar(distribution):

    df = pd.DataFrame({
        "Category": list(distribution.keys()),
        "Count": list(distribution.values())
    })

    fig = px.bar(
        df,
        x="Category",
        y="Count"
    )

    fig.update_layout(
        title="Skills by Category",
        template="plotly_white"
    )

    return fig


def create_radar_chart(scores):

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=list(scores.values()),
        theta=list(scores.keys()),
        fill='toself'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 20]
            )
        )
    )

    return fig


def create_keyword_chart(keyword_data):

    df = pd.DataFrame(
        keyword_data,
        columns=["Keyword", "Frequency"]
    )

    fig = px.bar(
        df,
        x="Keyword",
        y="Frequency"
    )

    return fig