import json
import os 

def load_json(path):
    try:
        if os.path.exists(path):
            with open(path,'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e: 
        print(f"Error with loading json file: {e}")
        return{}
    
def save_json(path,data):
    try:
        if os.path.exists(path):
            with open(path,'r', encoding='utf-8') as f:
                return json.dump(path, f ,ensure_ascii=False, indent = 2)
    except Exception as e: 
        print(f"Error with saving json file: {e}")
        return{}

def exit_json(path, data):
    print("Exiting program... Goodbye!")
    exit()


            