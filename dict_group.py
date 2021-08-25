files = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}

def group_by_owners(files):
    ordered_files = {}
    for key, value in files.items():
        if value not in ordered_files.keys():
            ordered_files[value] = [key]
        else: 
            ordered_files[value].append(key)
    return ordered_files


print(group_by_owners(files))




