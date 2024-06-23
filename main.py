import requests

# User token (Use with caution, preferably use bot tokens)
USER_TOKEN = ''
CHANNEL_ID = '1071317095796715560'

def get_headers():
    return {
        "Authorization": USER_TOKEN,
        "Content-Type": "application/json"
    }

def get_threads(channel_id):
    url = f"https://discord.com/api/v10/channels/{channel_id}/threads/active"
    response = requests.get(url, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get threads: {response.status_code}")
        return None

def get_messages(thread_id):
    url = f"https://discord.com/api/v10/channels/{thread_id}/messages"
    response = requests.get(url, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get messages for thread {thread_id}: {response.status_code}")
        return None

def main():
    threads = get_threads(CHANNEL_ID)
    if threads:
        threads_list = threads['threads']
        all_threads_data = []
        for thread in threads_list:
            thread_info = {
                "id": thread['id'],
                "name": thread['name'],
                "last_message_id": thread.get('last_message_id'),
                "message_count": thread.get('message_count'),
                "total_message_sent": thread.get('total_message_sent'),
                "messages": []
            }
            messages = get_messages(thread['id'])
            if messages:
                thread_info['messages'] = messages
            all_threads_data.append(thread_info)
        
        with open('threads.json', 'w') as f:
            json.dump(all_threads_data, f, indent=4)
        
        print("Threads and messages saved to threads.json")

if __name__ == "__main__":
    main()
