import subprocess
import json

result = subprocess.run(['tasklist'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

final_list = {}
if result.returncode == 0:
    lines = result.stdout.splitlines()
    print("start")
    for line in lines[3:]:
        task_list = {}
        task_list["Image Name"] = line.split(maxsplit=5)[0]
        image_name = task_list["Image Name"] = line.split(maxsplit=5)[0]
        task_list["PID"] = line.split(maxsplit=5)[1]
        task_list["Session Name"] = line.split(maxsplit=5)[2]
        task_list["Session#"] = line.split(maxsplit=5)[3]
        task_list["Mem Usage"] = line.split(maxsplit=5)[4]
        final_list[f"Process: {image_name}"] = task_list

    print("done")
    with open("json.json","w") as file:
        file.write(json.dumps(final_list))
        file.close()

else:
    print(f"Error {result.stderr}")

