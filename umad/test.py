import subprocess
import json

result = subprocess.run(['tasklist'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

if result.returncode == 0:
    lines = result.stdout.splitlines()
    task_list = {}
    final_list = []
    x = 1
    for line in lines[3:]:
        task_list["Image Name"] = line.split(maxsplit=5)[0]
        task_list["PID"] = line.split(maxsplit=5)[1]
        task_list["Session Name"] = line.split(maxsplit=5)[2]
        task_list["Session#"] = line.split(maxsplit=5)[3]
        task_list["Mem Usage"] = line.split(maxsplit=5)[4]
        final_list.update()
        final_list[f"{str(x)}"] = task_list
        x=x+1

    print(final_list)
    
    with open("json.json","w") as file:
        file.write(json.dumps(final_list))
        file.close()
    
else:
    print(f"Error {result.stderr}")

