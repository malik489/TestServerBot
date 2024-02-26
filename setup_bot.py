import json

def get_values_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    bot_token = data.get('bot_token')
    give_bot_token = data.get('give_bot_token')
    sudo = data.get('sudo')

    return bot_token, give_bot_token, sudo

def append_values_to_json(file_path, bot_token, give_bot_token, sudo):
    with open(file_path, 'r+', encoding='utf-8') as file:
        data = json.load(file)

        data['bot_token'] = bot_token
        data['give_bot_token'] = give_bot_token
        data['sudo'] = sudo

        file.seek(0)
        json.dump(data, file, indent=4, ensure_ascii=False)
        file.truncate()

# Example usage:
json_file_path = 'config.json'
bot_token = input('Add bot token: ')
give_bot_token = input('Add bot token of Give: ')
sudo = int(input('Add Sudo id: '))

# Get values from JSON
file_bot_token, file_give_bot_token, file_sudo = get_values_from_json(json_file_path)

# Update values
if bot_token:
    file_bot_token = bot_token
if give_bot_token:
    file_give_bot_token = give_bot_token
if sudo:
    file_sudo = sudo

append_values_to_json(json_file_path, file_bot_token, file_give_bot_token, file_sudo)
print("Ok")