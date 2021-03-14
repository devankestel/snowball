import os
import datetime

def create_git_log(path, repo_name):
    cwd = os.getcwd()
    os.chdir(path)
    write_git_log = 'git log > {}/{}_git_log.md'.format(cwd, repo_name)
    os.system(write_git_log)
    os.chdir(cwd)
    
def parse_log(filename):
    git_log_raw = open(filename, 'r')
    lines = git_log_raw.readlines()
    shas = []
    dates = []
    for line in lines:
        if line.startswith('commit'):
            _, sha = line.split(' ', 1)
            shas.append(sha.strip())
        if line.startswith('Date'):
            _, date_raw = line.split(' ', 1)
            # eg. 'Wed Jul 13 01:25:57 2005 +0000'
            date = datetime.datetime.strptime(date_raw.strip(), '%a %b %d %H:%M:%S %Y %z')
            dates.append(date)
    shas_and_dates = zip(shas, dates)
    return shas_and_dates

def select_subset_commits(shas_and_dates, interval):
    for sha, date in shas_and_dates:
        print(date.month)



        
        