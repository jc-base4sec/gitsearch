from github import Github
from argparse import ArgumentParser
import sys
import time

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    if v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean Value Expected')

parser = ArgumentParser(description='GitSearch by Juan Cruz Tommasi - Base4 Security - www.base4sec.com')
parser.add_argument('-s', '--search', type=str, metavar='', help='Busqueda simple')
parser.add_argument('-t', '--time', type=str, metavar='', required=True,help='Tiempo de espera entre busquedas (REQUERIDO)')
parser.add_argument('-f', '--file', type=str, metavar='', help='Buscar desde un archivo linea por linea')
parser.add_argument('--status', type=str2bool, nargs='?', const=True, default=False, help='Muestra las querys disponibles de las llaves guardadas en la constante ACCESS_TOKENS')
args = parser.parse_args()

ACCESS_TOKENS = ['ACA_ACCESS_TOKEN1',' ACA_ACCESS_TOKEN2','ACA_ACCESS_TOKEN3','ACA_ACCESS_TOKEN4','ACA_ACCESS_TOKEN5']

RED   = "\u001b[31m"
BLUE  = "\u001b[34m"
CYAN  = "\u001b[36m"
YELLOW = "\u001b[33m"
GREEN = "\u001b[32m"
MAGENTA = "\u001b[35m"
RESET = "\u001b[0m"

sleep_time = int(args.time)

def search_github(keywords):
    query = '+'+keywords + '+in:readme+in:description'
    result = g.search_repositories(query, 'stars', 'desc')
    if result.totalCount == 0:
        sys.stdout.write(RED)
        print(f'Found {result.totalCount} repo(s) for query: %s' % keywords)
        sys.stdout.write(RESET)
    else:
        sys.stdout.write(GREEN)
        print(f'Found {result.totalCount} repo(s) for query: %s' % keywords)
        for repo in result:
            sys.stdout.write(GREEN)
            print(f'\t[{repo.stargazers_count} stars] {repo.clone_url}')
            sys.stdout.write(RESET)

def printRemainingApiCalls(g, apikey):
    rate_limit = g.get_rate_limit()
    rate = rate_limit.search
    if rate.remaining == 0:
        sys.stdout.write(YELLOW)
        print(f'[!] You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}')
        print('\tAPI KEY : %s' % apikey)
        sys.stdout.write(RESET)
    else:
        sys.stdout.write(GREEN)
        print(f'[*] You have {rate.remaining}/{rate.limit} API calls remaining')
        print('\tAPI KEY : %s' % apikey)
        sys.stdout.write(RESET)

def checkAndReturnAvKey(keys):
    for apikey in keys:
        g = Github(apikey)
        rate_limit = g.get_rate_limit()
        rate = rate_limit.search
        if args.status:
            printRemainingApiCalls(g, apikey)
        if rate.remaining > 0:
            return apikey

if args.file:
    f = open(args.file, 'r')
    f = f.read()
    flines = f.splitlines()
    for query in flines:
        time.sleep(sleep_time)
        key = checkAndReturnAvKey(ACCESS_TOKENS)
        g = Github(key)
        search_github(query)
else:
    g = Github(checkAndReturnAvKey(ACCESS_TOKENS))
    search_github(args.search)
    time.sleep(sleep_time)
