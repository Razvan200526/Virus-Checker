import hashlib
import os 

def load_hashes(filename = 'signature.txt'):
    with open(filename , 'r') as f:
        hashes = [line.strip() for line in f.readlines()]
    return hashes

def calculate_file_hash(file_path,hash_algo='sha256'):
    hash_func = hashlib.new(hash_algo)
    with open(file_path,'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def check_viruses(directory,known_hashes):
    for root,dirs,files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root,file)
            file_hash = calculate_file_hash(file_path)
            
            if file_hash in known_hashes:
                print(f"Virus detected : {file_path} with hash {file_hash}")
                

if __name__ == '__main__':
    hashes = load_hashes('signatures.txt')
    
    directory_to_scan = 'path/to/any/one/of/your/dirs'
    
    check_viruses(directory_to_scan,hashes)