# Export Slack Channel Conversations

This repository contains a Python script to export all conversations from a specified Slack channel using Slack's API.

## Prerequisites

Before running the script, ensure you have the following:

1. **Slack API Token**: You will need to generate an API token by creating a Slack app. You must have admin permissions in your Slack workspace to do this.
2. **Python Environment**: Make sure Python is installed on your machine along with necessary libraries.

### Step 1: Create a Slack App and Get an API Token

1. Go to the [Slack API page](https://api.slack.com/apps).
2. Click "Create New App" and follow the instructions.
3. Under "OAuth & Permissions," scroll to the "Scopes" section.
4. Add the following OAuth scopes:
   - `channels:history`
   - `groups:history`
   - `im:history`
   - `mpim:history`
   - `channels:read`
   - `groups:read`
   - `users:read`
5. Install the app in your workspace.
6. Once installed, note the OAuth access token (you will use this in the script).

### Step 2: Install Necessary Python Libraries

Use the following command to install the required libraries:

```bash
pip install requests
```

### Step 3: Run the Script

1. Replace the following placeholders in the script:
   - `YOUR_SLACK_API_TOKEN_HERE`: Replace with the OAuth token obtained from your Slack app.
   - `YOUR_CHANNEL_ID_HERE`: Find the channel ID by going to the Slack channel, clicking on "Details," and copying the channel ID from the URL.
   
2. Save the script.

3. Run the script using the following command:

```bash
python export_slack_messages.py
```

This will export all messages from the specified Slack channel and save them in `slack_conversation_export.json`.

### Step 4: Review the Exported Data

After running the script, you can review the exported messages in the `slack_conversation_export.json` file.
