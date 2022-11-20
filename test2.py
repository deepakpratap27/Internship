import json
import test


class Username:
    def write_json(user_object):
        new_data = json.dumps(user_object.__dict__)
        with open(filename,'r+') as file:
            file_data = json.load(file)
            file_data['user_info'].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent = 4)


