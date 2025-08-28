# Load libraries and data

library(tidyverse)
library(patchwork)

falcons_roster <- read_csv("data/falcons-roster.csv")
falcons_scores <- read_csv("data/falcons-scores.csv")
falcons_seasons <- read_csv("data/falcons-seasons.csv")

# Create visualization

falcons_seasons |>
  filter(season_type == "regular", !is.na(PF), !is.na(PA)) |>
  ggplot(aes(x = PF, y = PA)) +
  geom_point(aes(color = PCT, size = W), alpha = 0.7) +
  geom_abline(slope = 1, intercept = 0, linetype = "dashed", alpha = 0.5) +
  scale_color_gradient2(
    low = "#8B0000", mid = "#FFB347", high = "#228B22",
    midpoint = 0.5, name = "Win %"
  ) +
  scale_size_continuous(name = "Wins", range = c(2, 8)) +
  labs(
    title = "Offensive vs Defensive Performance",
    subtitle = "Points scored vs points allowed (diagonal = break-even)",
    x = "Points For (PF)",
    y = "Points Against (PA)"
  ) +
  theme_minimal() +
  theme(plot.title = element_text(color = "#A71930", face = "bold"))
