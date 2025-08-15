# Positron Assistant demo

Welcome to the Positron Assistant demo for posit::conf 2025 in Atlanta!

In this demo, you will:

1. Explore the Georgia Aquarium Species dataset with the help of Positron Assistant

1. Export the chat into a Quarto document using Positron Assistant

1. Publish the document to Posit Connect Cloud

## Step 1: Run the script in the Console

1. Open up [the demo script](./python-polars-demo.py) in an editor

1. Run the script cell by cell, or select all the code and run it at once (Cmd/Ctrl + Enter).

   - Once all the code has been run, you should see:

        - code executed in the Console

        - data loaded into the Variables pane

        - a plot rendered in the Plots pane

## Step 2: Explore the data with Positron Assistant

1. Open the Positron Assistant pane by clicking on the Positron Assistant robot icon in the sidebar, or by opening the Command Palette (Cmd/Ctrl + Shift + P) and running the [command "View: Show Chat"](command:workbench.panel.chat).

1. In the Positron Assistant pane, ensure your chat is in `Ask` mode. You can switch modes by clicking on the mode selector at the bottom of the chat pane.

1. Use the example messages below to explore the Georgia Aquarium Species dataset.

### Example prompts

Try out these example prompts in "Ask" mode!

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

## Step 3: Export the chat into a Quarto document

1. In the Positron Assistant chat in "Ask" mode, enter `/exportQuarto` and send the message.

1. Positron Assistant will generate a Quarto document based on the chat history, including code chunks and explanations.

1. Save the generated Quarto document as `report.qmd` in your project directory.

## Step 4: Publish your document

TBD

## Step 5: [OPTIONAL] Explore more with "Agent" mode

<details>
<summary>Additional prompts for "Agent" mode</summary>

### Additional prompts for "Agent" mode

1. Start a new chat by clicking on the "+" icon at the top of the Positron Assistant sidebar chat.

1. Switch to "Agent" mode by clicking on the mode selector at the bottom of the chat pane and selecting "Agent".

1. Ensure you have the demo script attached to the chat context. If it is not already attached:

    1. Open the file in the editor

    1. Drag the file tab to the sidebar chat; or in the Command Palette (Cmd/Ctrl + Shift + P), run the [command "Chat: Add File to Chat"](command:workbench.action.chat.attachFile).

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