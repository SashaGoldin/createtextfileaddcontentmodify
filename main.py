# from pathlib import Path
# file_dir = Path("files")
# for filepath in file_dir.iterdir():
#   with open(filepath, 'r') as file:
#     content = file.read()
#     new_content = content.replace("amount", "units")
    
#   with open(filepath, 'w') as file:
    
#     file.write(new_content)

with open('merged.csv', "r") as file:
  content = file.readlines()
  
content[0] = 'ID,AMOUNT,COST\n'
with open("merged.csv", "w") as file:
  file.writelines(content)

