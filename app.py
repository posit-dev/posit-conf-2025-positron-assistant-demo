import polars as pl
from shiny import App, reactive, render, ui

# Load the species data
species = pl.read_csv("./data/georgia-aquarium-species.csv")

# Get unique values for filter options
unique_conservation = species.select("conservation_status").unique().to_series().to_list()
unique_habitat = species.select("habitat").unique().to_series().to_list()
unique_diet = species.select("diet").unique().to_series().to_list()

# Define the UI
app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.h3("Filters"),
        ui.input_selectize(
            "conservation_filter",
            "Conservation Status",
            choices=["All"] + sorted(unique_conservation),
            selected="All",
            multiple=False
        ),
        ui.input_selectize(
            "habitat_filter", 
            "Habitat",
            choices=["All"] + sorted(unique_habitat),
            selected="All",
            multiple=False
        ),
        ui.input_selectize(
            "diet_filter",
            "Diet",
            choices=["All"] + sorted(unique_diet),
            selected="All",
            multiple=False
        ),
        ui.input_text(
            "name_filter",
            "Search Species Name",
            placeholder="Type to search..."
        ),
        ui.input_action_button(
            "reset_filters",
            "Reset All Filters",
            class_="btn-outline-secondary mt-3"
        )
    ),
    ui.h1("Georgia Aquarium Species"),
    ui.card(
        ui.card_header("All Species in the Georgia Aquarium"),
        ui.output_data_frame("species_table")
    )
)

def server(input, output, session):
    @reactive.calc
    def filtered_species():
        # Start with all species
        filtered_df = species
        
        # Filter by conservation status
        if input.conservation_filter() and "All" not in input.conservation_filter():
            filtered_df = filtered_df.filter(
                pl.col("conservation_status") == input.conservation_filter()
            )
        
        # Filter by habitat
        if input.habitat_filter() and "All" not in input.habitat_filter():
            filtered_df = filtered_df.filter(
                pl.col("habitat") == input.habitat_filter()
            )
        
        # Filter by diet
        if input.diet_filter() and "All" not in input.diet_filter():
            filtered_df = filtered_df.filter(
                pl.col("diet") == input.diet_filter()
            )
        
        # Filter by species name (search both common and scientific names)
        if input.name_filter():
            search_term = input.name_filter().lower()
            filtered_df = filtered_df.filter(
                (pl.col("species_name").str.to_lowercase().str.contains(search_term)) |
                (pl.col("common_name").str.to_lowercase().str.contains(search_term))
            )
		
        print(f"Orginal species df has {species.height} rows")
        print(f"Filtered species df has {filtered_df.height} rows")
        
        return filtered_df
    
    @render.data_frame
    def species_table():
        return render.DataGrid(
            filtered_species().select(pl.col("name"), pl.col("conservation_status")),
            width="100%",
        )
    
    @reactive.effect
    @reactive.event(input.reset_filters)
    def reset_all_filters():
        ui.update_selectize("conservation_filter", selected=["All"])
        ui.update_selectize("habitat_filter", selected=["All"])
        ui.update_selectize("diet_filter", selected=["All"])
        ui.update_text("name_filter", value="")

app = App(app_ui, server)
