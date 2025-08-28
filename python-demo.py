# %% Load libraries and data
import math

import plotnine as p9
import polars as pl

species = pl.read_csv("./data/georgia-aquarium-species.csv")
species

# %% Create an order for the categorical data
conservation_status_enum = pl.Enum(
    [
        # Conservation categories from most to least threatened
        # Threatened...
        "Critically Endangered",
        "Endangered",
        "Vulnerable",
        # Least concern...
        "Near Threatened",
        "Least Concern",
        # Data...
        "Data Deficient",
        "Not Evaluated",
    ]
)

species = (
    species
    .with_columns(
        pl.col("conservation_status").cast(conservation_status_enum)
    )
)

species

# %% Summarize the number of species by conservation status
conservation_status_summary = (
    species
    .group_by("conservation_status")
    .len()
    .sort("conservation_status", descending=True)
)

conservation_status_summary
# %% Plot the summary using Plotnine
threatened_index = 3.5 # Everything from 3.5 to 0 is considered threatened

p = (
    p9.ggplot(conservation_status_summary, p9.aes(x="conservation_status", y="len"))
    + p9.geom_col()
    + p9.geom_text(
        p9.aes(label="len"), 
        ha="left", 
        nudge_y=1
    )
    + p9.geom_vline(
        p9.aes(xintercept=threatened_index), 
        linetype="dashed", 
        color="red"
    )
    + p9.annotate(
        'rect', 
        xmin=0.5, 
        xmax=3.5, 
        ymin=0, 
        ymax=math.inf, 
        fill="red", 
        alpha=0.1
    )
    + p9.annotate(
        "text",
        label="Species is Threatened",
        x=threatened_index - 1.5,
        y=60,
        color="red",
    )
    + p9.scale_y_continuous(expand=(0, 0, 0, 10))
    + p9.labs(
        x="Conservation Status",
        y="Number of Species",
        title="Species Conservation Status Summary",
    )
    + p9.coord_flip()
)

p.show()
