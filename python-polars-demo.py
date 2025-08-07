import polars as pl
from plotnine import ggplot, aes, geom_tile, labs, theme_minimal, scale_fill_gradient

# 👀 CSV file path -- update this path as needed!
csv_file_path = 'data/data.csv'

# Load CSV file into a Polars DataFrame
data = pl.read_csv(csv_file_path)

###########################################################################
# TBD the plotting code probably needs to be adjusted depending on the data
############################################################################

# Reshape the data from wide to long format using unpivot
data_long = (
    data.with_row_index("row")  # Add row indices
    .unpivot(index="row", variable_name="column", value_name="value")
)

# Create heatmap
(ggplot(data_long, aes(x='column', y='row', fill='value')) +
        geom_tile() +
        scale_fill_gradient(low='blue', high='red') +
        labs(title='Data Heatmap', x='Columns', y='Rows') +
        theme_minimal())
