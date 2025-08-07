library(tidyverse)

# 👀 CSV file path -- update this path as needed!
csv_file_path <- 'data/data.csv'

# Load CSV file into a data frame
data <- read_csv(csv_file_path)

#########################################################################
# TBD adapt the plotting depending on the data; placeholder code for now
#########################################################################

# Reshape the data from wide to long format using unpivot

data_long <- data |>
  mutate(row = row_number()) |> # Add row indices
  pivot_longer(cols = -row, names_to = "column", values_to = "value")

# Create heatmap
ggplot(data_long, aes(x = column, y = factor(row), fill = value)) +
  geom_tile() +
  scale_fill_gradient(low = "blue", high = "red") +
  labs(title = "Data Heatmap", x = "Columns", y = "Rows") +
  theme_minimal()
