import os
import hashlib

def read_file(file_path:str):
    f = open(file_path,mode="r",encoding="utf-8")
    file = f.read()
    f.close()
    return file

def read_folder(folder_path:str):
    folder = []
    
    for  root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                #file_path = folder_path + "/" + file_name
                folder.append(file)
    return folder

def format_data(data:str):
    if len(data) > 0:
        data = data.split("<D>")
        data = "\nTemperature\t>> " + data[0] + "\nHumidity\t>> " + data[1] + "\nDirection\t>>" + data[2]
        return data
    else:
        return "EMPTY NODE"

def display_node(node:str):
    node = node.split("<S>")
    print("Node data\t>> ",format_data(node[1]))
    print("Timestamp\t>> ",node[2])
    print("Previous Hash\t>> ",node[0])

def display_chain(folder_path:str):
    folder = read_folder(folder_path)

    for f in folder:
        if f != "chain_hash.txt":
            print("File\t>> ",f)
            f_path =  folder_path + "/" + f
            current = read_file(f_path)
            display_node(current)

"""def nodes_validate(folder_path:str):
    folder = read_folder(folder_path)

    chain = []
    for f in folder:
        if f != "chain_hash.txt":
            #print("File\t>> ",f)
            f_path =  folder_path + "/" + f
            current = read_file(f_path)
            chain.append(current)
    #print(chain)

    prev_hash= []
    self_hash = []
    for n in chain:
        h = n.split("<S>")[0]
        prev_hash.append(hashlib.sha256(h.encode("utf-8")).hexdigest())
        self_hash.append(hashlib.sha256(n.encode("utf-8")).hexdigest())
    
    del prev_hash[0]
    del self_hash[-1]

    all_correct = True

    for p,s in  zip(prev_hash,self_hash):
        print(p)
        print(s)
        if p != s:
            all_correct == False

    if(all_correct):
        print("Node hashes legit.")
    else:
        print("Node hashes illegit.")"""


def chain_validate(folder_path:str):
    folder = read_folder(folder_path)

    full_chain = ""
    for f in folder:
        if f != "chain_hash.txt":
            #print("File\t>> ",f)
            f_path =  folder_path + "/" + f
            current = read_file(f_path)
            full_chain += current
    
    chain_hash = hashlib.sha256(full_chain.encode("utf-8")).hexdigest()
    if chain_hash == read_file(folder_path + "/" + "chain_hash.txt"):
        print("Chain hash legit.")
    else:
        print("Chain hash illegit.")
        

if __name__ == "__main__":
    folder_path = input("Enter folder path >>")
    display_chain(folder_path)
    chain_validate(folder_path)
