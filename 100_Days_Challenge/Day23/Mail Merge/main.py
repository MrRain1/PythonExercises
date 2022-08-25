name_list = []

with open("./names.txt") as names:
    name_list = names.readlines()
        
for index in range(len(name_list)):
    name_list[index] = name_list[index].replace("\n", "")

# open the blue print file
    
with open("./invite blueprint.docx") as invite_blueprint:
    blueprint_content = invite_blueprint.read()
    
    # iter on every element of the name list and replace the placeholder text 
    
    for name in name_list:
        named_invite = blueprint_content.replace("[]", name)
        
        # write a new file
        with open(f"./Output Files/letter_for_{name}.docx", "w") as letter:
            letter.write(named_invite)