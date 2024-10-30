from csv import writer, reader

def process_data(data):
    try:
        words = [word.lower() for word in data.split(' ') if not (word.startswith('*') or word.startswith('$'))]
        
        if not words:
            return "Invalid data"
        
        if words[0] == 'set':
            return handle_set_command(words)
        elif words[0] == 'get':
            return handle_get_command(words)
        
        else:
            return None

    except Exception as e:
        print("Exception occurred:", e)
        return "Error occurred"


def handle_set_command(words):
    try:
        prepare_data = [words[1]] 
        value = ' '.join(words[2:])
        prepare_data.append(value.strip())
        
        with open('all_mapping.csv', 'a', newline='') as csv_file:
            csv_writer = writer(csv_file)
            csv_writer.writerow(prepare_data)
        
        return None
    
    except Exception as e:
        print("Exception occurred in set:", e)
        return "Error in saving data"


def handle_get_command(words):
    try:
        key = words[1]
        
        with open('all_mapping.csv', 'r') as csv_file:
            csv_reader = reader(csv_file)
            for row in csv_reader:
                if row and row[0] == key:
                    return row[1]
        
        return "Key not found"
    
    except Exception as e:
        print("Exception occurred in get:", e)
        return "Error in fetching data"
