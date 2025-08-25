import polars as pl
import plotly.express as px

from config import LEGEND_PALETTE

def generate_chart(lf: pl.LazyFrame, short_name_selected : str):
    """Create a professional chart showing NADAC price trends over time"""
    PALLET = LEGEND_PALETTE  # Use the first 10 colors from the palette
    # Create the line chart
    fig = px.line(
        lf.collect(engine='streaming'), 
        x='effective_date', 
        y='unit_price',
        color='product',
        title=f'NADAC Price Trends Over Time: {short_name_selected}',
        labels={
            'effective_date': 'Date',
            'unit_price': 'Unit Price (USD)',
            'product': 'Product'
        },
        line_shape='linear',
        markers=True,
        color_discrete_sequence=PALLET
    )
    
    # Professional styling
    fig.update_layout(
        title={
            'text': f'NADAC Price Trends Over Time: {short_name_selected}',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'family': 'Arial, sans-serif'}
        },
        xaxis={
            'title': {'text': 'Date', 'font': {'size': 14}},
            'showgrid': True,
            'gridwidth': 1,
            'gridcolor': '#E5E5E5'
        },
        yaxis={
            'title': {'text': 'Unit Price (USD)', 'font': {'size': 14}},
            'showgrid': True,
            'gridwidth': 1,
            'gridcolor': '#E5E5E5',
            'tickformat': '$,.2f'  # Format as USD
        },
        showlegend=False,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font={'family': 'Arial, sans-serif', 'size': 12},
        hovermode='x unified',
  
    )
    
    # Update traces for better styling
    fig.update_traces(
        line=dict(width=3),
        marker=dict(size=6),
        hovertemplate='<b>%{fullData.name}</b><br>' +
                     'Date: %{x}<br>' +
                     'Price: $%{y:.2f}<br>' +
                     '<extra></extra>'
    )
    
    
    return fig
