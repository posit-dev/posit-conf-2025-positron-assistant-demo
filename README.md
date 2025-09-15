![](images/banner.png)

# Positron Assistant demo

Welcome to the [Positron Assistant](https://positron.posit.co/assistant) demo for [posit::conf](https://posit.co/conference/) 2025 in Atlanta!

With the help of Positron Assistant, this demo will guide you through exploring two datasets:

- the Georgia Aquarium Species dataset using Python

- the Atlanta Falcons football team datasets using R

## Setup

If you're running this demo in a guided workshop, your interpreters and packages should already be set up for you in the demo environment. Please jump ahead to either the [Python demo](#-python-demo) or [R demo](#-r-demo) section and follow the steps!

Otherwise, click to expand the pre-requisites section below and follow the steps to set up your environment.

<details>
<summary>Pre-requisites if you're running this demo on your own machine</summary>

### Pre-requisites

1. Install and open [Positron](https://positron.posit.co/download), ideally version 2025.09.0 or higher

1. Copy this repository's GitHub URL to your clipboard: [`https://github.com/posit-dev/posit-conf-2025-positron-assistant-demo.git`](https://github.com/posit-dev/posit-conf-2025-positron-assistant-demo.git)

1. Clone this repository and open the folder in Positron

    1. Run the [command "Workspaces: New Folder from Git..."](command:positron.workbench.action.newFolderFromGit) in the Command Palette
    
    1. Paste in the repository URL you copied

    1. Select a local directory to clone the repository into

    1. Click <kbd>OK</kbd>

1. Use the [Positron Assistant guide](https://positron.posit.co/assistant.html) to set up Positron Assistant with an Anthropic API key.

#### Python demo pre-requisites

1. Ensure you have a Python interpreter (3.9 through 3.13) installed on your machine

1. Create a virtual environment for this project

    1. Run the [command "Python: Create Environment..."](command:python.createEnvironment) in the Command Palette

    1. Select `Venv` as the environment type
    
    1. Pick a base interpreter (we recommend the latest version of Python)

    1. Select the `requirements.txt` file in the dropdown to install the required packages

    1. Click <kbd>OK</kbd>

    1. Wait for the environment to be created and packages to be installed

1. You're all set! Jump to the [Python demo](#-python-demo) section and follow the steps!

#### R demo pre-requisites

1. Ensure you have R (R 4.2 and higher) installed on your machine.

1. Install the required packages by running the following commands in the R Console:

    ```r
    install.packages("tidyverse")
    ```

1. You're all set! Jump to the [R demo](#-r-demo) section and follow the steps!

</details>

## 🐍 Python demo

### Step 1: Run the script in the Console

1. Open up the Python script [python-demo.py](./python-demo.py) in an editor

1. Run the script by clicking the **Play** button in the Editor Actions bar

   - Once all the code has been run, you should see:

        - code executed in the Console

        - data loaded into the Variables pane

        - a plot rendered in the Plots pane

### Step 2: View the data in the Data Explorer

Follow these steps to view data tables in the Data Explorer:

1. Run the [command "Session: Focus on Variables View"](command:positronVariables.focus), which will open up the Variables View if it is not already open.

1. In the Variables View, double-click on the `species` variable or click the "View Data Table" icon to open the table in the Data Explorer.

1. Play around with the Data Explorer to filter, sort, and visualize the data. For more information, see the [Data Explorer documentation](https://positron.posit.co/data-explorer.html).

    - Open the "Summary Panel", which columns are missing data?

    - Use the "Summary Panel" to see the distribution of `conservation_status`. What is the most common status?

    - Sort the data by `conservation_status` and `scientific_name` by right clicking on the column name and clicking "Sort Ascending" or "Sort Descending".


### Step 3: Explore the data with Positron Assistant

1. Open the Positron Assistant pane by clicking on the Positron Assistant robot icon in the sidebar, or by opening the Command Palette (<kbd>Cmd/Ctrl + Shift + P</kbd>) and running the [command "View: Show Chat"](command:workbench.panel.chat).

1. In the Positron Assistant pane, ensure your chat is in `Ask` mode. You can switch modes by clicking on the mode selector at the bottom of the chat pane. Positron Assistant offers three modes: `Ask` for questions and help (default), `Edit` for collaborative code modifications, and `Agent` for autonomous task execution including file management and code execution.

1. We recommend selecting the **Claude 4 Sonnet** model for this activity. You can change the model by clicking on the model name at the bottom of the chat pane.

1. Use the example messages below to explore the Georgia Aquarium Species dataset.

#### Example prompts

Try out these example prompts in `Ask` mode!

```
Please summarize the `species` data table
```

```
What do you see in the current plot?
```

```
Explain the values of the `conservation_status` column. Is there a hierarchy?
```

```
Based on data tables in my session, please suggest some starter code for interesting analyses or visualizations
```

- Feel free to try out the code snippets Positron Assistant suggests by clicking the Play button on the code blocks.

- If you run into issues, it's a good time to switch over to `Agent` mode (see optional next step) to let Positron Assistant help you debug!

You're done! 🎉

### Step 4: [OPTIONAL] Explore more with `Agent` mode

<details>
<summary>Additional prompts for `Agent` mode</summary>

`Agent` mode allows Positron Assistant to modify and run code in the Console, making it possible to perform more complex tasks.

#### Additional prompts for `Agent` mode

1. Start a new chat by clicking on the "+" icon at the top of the Positron Assistant sidebar chat.

1. Switch to `Agent` mode by clicking on the mode selector at the bottom of the chat pane and selecting `Agent`.

1. Ensure you have [python-demo.py](./python-demo.py) attached to the chat context. If it is not already attached:

    1. Open the file in the editor

    1. Drag the file tab to the sidebar chat; or in the Command Palette (<kbd>Cmd/Ctrl + Shift + P</kbd>), run the [command "Chat: Add File to Chat"](command:workbench.action.chat.attachFile).

1. Then, try these additional prompts:

    ```
    Update the script to change the colour scheme to oceanic colours.
    ```

    - Run the script to see the changes reflected in the plot. If you're satisfied with the changes, you can "Keep" the changes.

    ```
    Create a heatmap of the conservation risk by region.
    ```

    - Positron Assistant may prompt you to "Run Code" to better understand the data and execute code in the Console. Click "Run Code" to execute the code in the Console.

</details>

### Step 5: [OPTIONAL] Explore more with `Edit` mode

<details>
<summary>Additional prompts for `Edit` mode</summary>

`Edit` mode is a good choice when you'd like help making code changes in your files. Assistant will generate new code or edits to existing code based on your prompt.

#### Additional prompts for `Edit` mode

1. Start a new chat by clicking on the "+" icon at the top of the Positron Assistant sidebar chat.

1. Switch to `Edit` mode by clicking on the mode selector at the bottom of the chat pane and selecting `Edit`.

1. Ensure you have [python-demo.py](./python-demo.py) attached to the chat context. If it is not already attached:

    1. Open the file in the editor

    1. Drag the file tab to the sidebar chat; or in the Command Palette (<kbd>Cmd/Ctrl + Shift + P</kbd>), run the [command "Chat: Add File to Chat"](command:workbench.action.chat.attachFile).

1. Then, try these additional prompts:

    ```
    Add another plot to this script that shows the breakdown of different threatened categories
    ```

    ```
    Change the current file’s plotting code from plotnine to seaborn
    ```

    ```
    Port this Python script to R
    ```

    Assistant will take some time to think and generate the suggested code. If you're satisfied with the changes, you can "Keep" the changes. To get a hand with resolving any code errors, switch over to `Agent` mode.

</details>

## 📊 R demo

### Step 1: Run the script in the Console

1. Open up the R script [r-demo.R](./r-demo.R) in an editor

1. Run the script by clicking the **Play** button in the Editor Actions bar

   - Once all the code has been run, you should see:

        - code executed in the Console

        - data loaded into the Environment pane

        - a plot rendered in the Plots pane

### Step 2: View the data in the Data Explorer

Follow these steps to view data tables in the Data Explorer:

1. Run the [command "Session: Focus on Variables View"](command:positronVariables.focus), which will open up the Variables View if it is not already open.

1. In the Variables View, click the "View Data Table" icon or double-click on any of the table variables to open them in the Data Explorer. Start with the `falcons_seasons` dataframe.

1. Play around with the Data Explorer to filter, sort, and visualize the data. For more information, see the [Data Explorer documentation](https://positron.posit.co/data-explorer.html).

    - Open the "Summary Panel", which columns are missing data?

    - Use the "Summary Panel" to see the distribution of `Head Coach`. Which Head Coach has the longest tenure?

    - Sort the data by `W` (wins) and `PF` (points for) by right clicking on the column name and clicking "Sort Ascending" or "Sort Descending".

### Step 3: Explore the data with Positron Assistant

1. Open the Positron Assistant pane by clicking on the Positron Assistant robot icon in the sidebar, or by opening the Command Palette (<kbd>Cmd/Ctrl + Shift + P</kbd>) and running the [command "View: Show Chat"](command:workbench.panel.chat).

1. In the Positron Assistant pane, ensure your chat is in `Ask` mode. You can switch modes by clicking on the mode selector at the bottom of the chat pane. Positron Assistant offers three modes: `Ask` for questions and help (default), `Edit` for collaborative code modifications, and `Agent` for autonomous task execution including file management and code execution.

1. We recommend selecting the **Claude 4 Sonnet** model for this activity. You can change the model by clicking on the model name at the bottom of the chat pane.

1. Use the example messages below to explore the Atlanta Falcons football team datasets.

#### Example prompts

Try out these example prompts in `Ask` mode!

```
Please summarize the `falcons_scores` data table
```

```
What do you see in the current plot?
```

```
Explain what each of the columns means for someone who does not watch football
```

```
Based on the data tables in my session, please suggest some interesting analyses or visualizations
```

- Feel free to try out the code snippets Positron Assistant suggests by clicking the Play button on the code blocks.

- If you run into issues, it's a good time to switch over to `Agent` mode (see optional next step) to let Positron Assistant help you debug!

You're done! 🎉

### Step 4: [OPTIONAL] Explore more with `Agent` mode

<details>
<summary>Additional prompts for `Agent` mode</summary>

`Agent` mode allows Positron Assistant to modify and run code in the Console, making it possible to perform more complex tasks.

#### Additional prompts for `Agent` mode

1. Start a new chat by clicking on the "+" icon at the top of the Positron Assistant sidebar chat.

1. Switch to `Agent` mode by clicking on the mode selector at the bottom of the chat pane and selecting `Agent`.

1. Ensure you have [r-demo.R](./r-demo.R) attached to the chat context. If it is not already attached:

    1. Open the file in the editor

    1. Drag the file tab to the sidebar chat; or in the Command Palette (<kbd>Cmd/Ctrl + Shift + P</kbd>), run the [command "Chat: Add File to Chat"](command:workbench.action.chat.attachFile).

1. Then, try these additional prompts:

    ```
    Change the plot to use a different colour scheme.
    ```

    - Run the script to see the changes reflected in the plot. If you're satisfied with the changes, you can "Keep" the changes.

    ```
    Create a heatmap of the win-loss percentage by season.
    ```

    - Positron Assistant may prompt you to "Run Code" to better understand the data and execute code in the Console. Click "Run Code" to execute the code in the Console.

### Step 5: [OPTIONAL] Explore more with `Edit` mode

<details>
<summary>Additional prompts for `Edit` mode</summary>

`Edit` mode is a good choice when you'd like help making code changes in your files. Assistant will generate new code or edits to existing code based on your prompt.

#### Additional prompts for `Edit` mode

1. Start a new chat by clicking on the "+" icon at the top of the Positron Assistant sidebar chat.

1. Switch to `Edit` mode by clicking on the mode selector at the bottom of the chat pane and selecting `Edit`.

1. Ensure you have [r-demo.R](./r-demo.R) attached to the chat context. If it is not already attached:

    1. Open the file in the editor

    1. Drag the file tab to the sidebar chat; or in the Command Palette (<kbd>Cmd/Ctrl + Shift + P</kbd>), run the [command "Chat: Add File to Chat"](command:workbench.action.chat.attachFile).

1. Then, try these additional prompts:

    ```
    Add another plot to this script that shows the time series of team performance
    ```

    ```
    Port this R script to Python
    ```

    Assistant will take some time to think and generate the suggested code. If you're satisfied with the changes, you can "Keep" the changes. To get a hand with resolving any code errors, switch over to `Agent` mode.

</details>
