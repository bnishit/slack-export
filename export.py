import requests
import json
import time

# Set up your credentials and Slack API token
SLACK_API_TOKEN = 'YOUR_SLACK_API_TOKEN_HERE'  # Replace with your Slack API token
CHANNEL_ID = 'YOUR_CHANNEL_ID_HERE'  # Replace with the ID of the Slack channel you want to export
EXPORT_FILE = 'slack_conversation_export.json'

def get_channel_messages(channel_id, token):
    url = 'https://slack.com/api/conversations.history'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    params = {
        'channel': channel_id,
        'limit': 200  # Slack returns a max of 200 messages at once
    }
    
    all_messages = []
    has_more = True
    next_cursor = None
    
    while has_more:
        if next_cursor:
            params['cursor'] = next_cursor
        
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        if not data.get('ok'):
            print(f"Error fetching messages: {data['error']}")
            break
        
        messages = data['messages']
        all_messages.extend(messages)
        
        has_more = data['has_more']
        next_cursor = data.get('response_metadata', {}).get('next_cursor', None)

        # Slack rate limits API calls, so be sure to pause if fetching a lot of data
        time.sleep(1)

    return all_messages

def save_messages_to_file(messages, filename):
    with open(filename, 'w') as f:
        json.dump(messages, f, indent=4)

def main():
    messages = get_channel_messages(CHANNEL_ID, SLACK_API_TOKEN)
    save_messages_to_file(messages, EXPORT_FILE)
    print(f"Exported {len(messages)} messages to {EXPORT_FILE}")

if __name__ == '__main__':
    main()
