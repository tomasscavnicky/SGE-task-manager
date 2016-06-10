import subprocess, os
from pprint import pprint
from os.path import isfile, join

bashCommand = "qstat -u xscavn00"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]
tasks = output.split('\n')
del tasks[:2]
del tasks[-1]

task_names = []

for task in tasks:
        task_tokens = task.split()
        print task_tokens
        task_names.append(task_tokens[2])

sge_path= "/mnt/matylda5/xscavn00/Speech/SGE/"
for directory in next(os.walk(sge_path))[1]:
        tmp_dir = join(sge_path, directory)
        script_file = [f for f in os.listdir(tmp_dir) if isfile(join(tmp_dir, f))]
        if len(script_file) == 1:
                script_file = script_file[0]
                body = open(join(tmp_dir, script_file)).read()
                body = body.split('\n')
                for line in body:
                        if line.find("#$ -N") != -1:
                                for taskn in task_names:
                                        if line.find(taskn) != -1:
                                                print str(taskn) + " is this file " + str(script_file)
                                                break