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
    ui.layout_column_wrap(
		ui.card(
			ui.card_header("All Species in the Georgia Aquarium"),
			ui.output_data_frame("species_table")
		),
		ui.card(
			ui.card_header("Selected Species Details"),
			ui.output_ui("species_details"),
		),
		# 2 columns when width is greater than 750px
		width="500px",
        heights_equal='row',
	),
	fillable=True,
    title="🐟 posit::conf(2025) Georgia Aquarium Species App",
    window_title="🐟 posit::conf(2025) Georgia Aquarium Species App",
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
            selection_mode="row"
		)
    
    
    @render.ui
    def species_details():
        selected_rows = input.species_table_selected_rows()

        if not selected_rows:
            selected_index = 0
        else:
            selected_index = selected_rows[0]  # Get first selected row

        # Get the selected species data
        filtered_df = filtered_species()
        
        # Get the species data for the selected row
        selected_species = filtered_df.slice(selected_index, 1)
        selected_species_object = selected_species.row(0, named=True)
        print(f"{selected_species_object=}")
        
        # Create conservation status badge with appropriate color
        status_color = {
            "Critically Endangered": "danger",
            "Endangered": "warning", 
            "Vulnerable": "warning",
            "Near Threatened": "secondary",
            "Least Concern": "success",
            "Data Deficient": "info",
            "Not Evaluated": "light"
        }.get(selected_species_object["conservation_status"], "secondary")
        
        return ui.div(
            ui.h4(f"{selected_species_object['name']}", class_="mb-2"),
            ui.h6(f"Scientific name: {selected_species_object['scientific_name']}", class_="text-muted mb-3"),
            ui.div(
                ui.div(
					ui.img(src=selected_species_object["image_url"]),
                    class_="mb-2"
				),
                ui.div(
                    ui.strong("Conservation Status: "),
                    ui.span(selected_species_object["conservation_status"], class_=f"badge bg-{status_color} ms-2"),
                    class_="mb-2"
                ),
                ui.div(
                    ui.strong("Range: "), 
                    ui.span(selected_species_object["range"]),
                    class_="mb-2"
                ),
                ui.div(
                    ui.strong("Habitat: "), 
                    ui.span(selected_species_object["habitat"]),
                    class_="mb-2"
                ),
                ui.div(
                    ui.strong("Diet: "), 
                    ui.span(selected_species_object["diet"]),
                    class_="mb-2"
                ),
                ui.div(
                    ui.strong("Size: "), 
                    ui.span(selected_species_object["size"]),
                    class_="mb-2"
                ),
                ui.div(
                    ui.strong("Physical Characteristics: "), 
                    ui.span(selected_species_object["physical_characteristics"]),
                    class_="mb-2"
                ),
                ui.div(
                    ui.strong("Fun Fact: "), 
                    ui.span(selected_species_object["fun_fact"]),
                    class_="mb-2"
                ),
                ui.div(
					ui.a("Aquarium Page ↗", href=selected_species_object["url"], target="_blank"),
                    class_="mb-2"
				),
                
            )
        )
    
    @reactive.effect
    @reactive.event(input.reset_filters)
    def reset_all_filters():
        ui.update_selectize("conservation_filter", selected=["All"])
        ui.update_selectize("habitat_filter", selected=["All"])
        ui.update_selectize("diet_filter", selected=["All"])
        ui.update_text("name_filter", value="")

app = App(app_ui, server)
