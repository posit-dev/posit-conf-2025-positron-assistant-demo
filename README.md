# Positron Assistant demo

Welcome to the Positron Assistant demo for posit::conf 2025 in Atlanta!

In this demo, with the help of Positron Assistant you will:

1. Explore the Georgia Aquarium Species dataset using Python, or the Atlanta Falcons football team datasets using R

1. Export your chat conversation into a Quarto document

## Setup

If you're running this demo in a guided workshop, your interpreters and packages should already be set up for you in the demo environment. Please jump ahead to either the [Python demo](#python-demo) or [R demo](#r-demo) section and follow the steps!

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

1. Use the [Positron Assistant guide](https://positron.posit.co/assistant.html) to set up Positron Assistant with an Anthropic API key

#### Python demo pre-requisites

1. Ensure you have a Python interpreter (3.9 through 3.13) installed on your machine

1. Create a virtual environment for this project

    1. Run the [command "Python: Create Environment..."](command:python.createEnvironment) in the Command Palette

    1. Select `Venv` or `uv` as the environment type and pick a base interpreter

    1. Select the `requirements.txt` file in the dropdown to install the required packages

    1. Click <kbd>OK</kbd>

    1. Wait for the environment to be created and packages to be installed

1. You're all set! Jump to the [Python demo](#python-demo) section and follow the steps!

#### R demo pre-requisites

1. Ensure you have R (R 4.2 and higher) installed on your machine.

1. Install the required packages by running the following commands in the R Console:

    ```r
    install.packages(c("tidyverse", "patchwork"))
    ```

1. You're all set! Jump to the [R demo](#r-demo) section and follow the steps!

</details>

## 🐍 Python demo

### Step 1: Run the script in the Console

1. Open up [the Python script](./python-demo.py) in an editor

1. Run the script by clicking the **Play** button in the Editor Actions bar

   - Once all the code has been run, you should see:

        - code executed in the Console

        - data loaded into the Variables pane

        - a plot rendered in the Plots pane

### Step 2: Explore the data with Positron Assistant

1. Open the Positron Assistant pane by clicking on the Positron Assistant robot icon in the sidebar, or by opening the Command Palette (<kbd>Cmd/Ctrl + Shift + P</kbd>) and running the [command "View: Show Chat"](command:workbench.panel.chat).

1. In the Positron Assistant pane, ensure your chat is in `Ask` mode. You can switch modes by clicking on the mode selector at the bottom of the chat pane.

1. Use the example messages below to explore the Georgia Aquarium Species dataset.

#### Example prompts

Try out these example prompts in `Ask` mode!

```
What region has the most animals with the highest conservation risk?
```

```
Extract the species size in inches.
```

```
Extract the animal's primary color from their physical characteristics.
```

```
Categorize the different types of habitats and then count the number of species in each habitat type.
```

### Step 3: Export the chat into a Quarto document

1. In the Positron Assistant chat in `Ask` mode, enter `/exportQuarto` and send the message.

1. Positron Assistant will generate a Quarto document based on the chat history, including code chunks and explanations.

1. Save the generated Quarto document as `report.qmd` in your project directory.

You're done! 🎉

### Step 4: [OPTIONAL] Explore more with `Agent` mode

<details>
<summary>Additional prompts for `Agent` mode</summary>

`Agent` mode allows Positron Assistant to modify and run code in the Console, making it possible to perform more complex tasks.

#### Additional prompts for `Agent` mode

1. Start a new chat by clicking on the "+" icon at the top of the Positron Assistant sidebar chat.

1. Switch to `Agent` mode by clicking on the mode selector at the bottom of the chat pane and selecting `Agent`.

1. Ensure you have the [demo script](./python-demo.py) attached to the chat context. If it is not already attached:

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

## 📊 R demo

### Step 1: Run the script in the Console

1. Open up [the R script](./r-demo.R) in an editor

1. Run the script by clicking the **Play** button in the Editor Actions bar

   - Once all the code has been run, you should see:

        - code executed in the Console

        - data loaded into the Environment pane

        - a plot rendered in the Plots pane

### Step 2: Explore the data with Positron Assistant

1. Open the Positron Assistant pane by clicking on the Positron Assistant robot icon in the sidebar, or by opening the Command Palette (<kbd>Cmd/Ctrl + Shift + P</kbd>) and running the [command "View: Show Chat"](command:workbench.panel.chat).

1. In the Positron Assistant pane, ensure your chat is in `Ask` mode. You can switch modes by clicking on the mode selector at the bottom of the chat pane.

1. Use the example messages below to explore the Atlanta Falcons football team datasets.

#### Example prompts

Try out these example prompts in `Ask` mode!

```
Who is the most winning player of all time? Who is the most winning coach?
```

```
Which player has the highest win-loss percentage?
```

```
How has scoring changed over time?
```

```
Are games closer in the modern NFL?
```

```
Does attendance approve on seasons where the Atlanta Falcons do better?
```

```
Which players have the longest careers but have played the fewest games?
```

```
Is it true that the Atlanta Falcons play worse on the road than at home?
```

### Step 3: Export the chat into a Quarto document

1. In the Positron Assistant chat in `Ask` mode, enter `/exportQuarto` and send the message.

1. Positron Assistant will generate a Quarto document based on the chat history, including code chunks and explanations.

1. Save the generated Quarto document as `report.qmd` in your project directory.

You're done! 🎉

### Step 4: [OPTIONAL] Explore more with `Agent` mode

<details>
<summary>Additional prompts for `Agent` mode</summary>

`Agent` mode allows Positron Assistant to modify and run code in the Console, making it possible to perform more complex tasks.

#### Additional prompts for `Agent` mode

1. Start a new chat by clicking on the "+" icon at the top of the Positron Assistant sidebar chat.

1. Switch to `Agent` mode by clicking on the mode selector at the bottom of the chat pane and selecting `Agent`.

1. Ensure you have the [demo script](./r-demo.R) attached to the chat context. If it is not already attached:

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
