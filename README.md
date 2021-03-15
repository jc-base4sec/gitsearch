```
                  _..__
                .' I   '.
                |.-"""-.|
               _;.-"""-.;_
           _.-' _..-.-.._ '-._
          ';--.-(_o_I_o_)-.--;'
           `. | |  | |  | | .`
             `-\|  | |  |/-'
                |  | |  |
                |  \_/  |
             _.'; ._._. ;'._
        _.-'`; | \  -  / | ;'-.
      .' :  /  |  |   |  |  \  '.
     /   : /__ \  \___/  / __\ : `.
    /    |   /  '._/_\_.'  \   :   `\
   /     .  `---;"""""'-----`  .     \
  /      |      |()    ()      |      \
 /      /|      |              |\      \
/      / |      |()    ()      | \      \
|         |
\     \   |][     |   |    ][ |   /     /
 \     \ ;=""====='"""'====""==; /     /
  |/`\  \/      |()    ()      \/  /`\|
   |_/.-';      |              |`-.\_|
     /   |      ;              :   \

GitSearch by Juan Cruz Tommasi - Base4 Security - www.base4sec.com
```

# **Github CLI Searcher**
#### Program to search for repositores from CLI using official github api.

#### First install required dependency:
> pip3 install pygithub

As the search is done through the github api, multiple api tokens must be registered to have a good flow of requests / searches. Keys are registered from the following address and many keys can be registered in a single user. https://github.com/settings/tokens/new
When creating the key just add all the permissions of "repo> public_repo", these are the permissions that this script needs to work.
In case you cannot find how to register the new tokens, here is a guide: https://docs.github.com/es/github/authenticating-to-github/creating-a-personal-access-token  

Once multiple keys have been registered, paste them in the ACCESS_TOKENS array found on line 23 of gitsint.py


### **ARGS**
```
-s --search / Simple Search
-t --time / Sleep time between api calls
-f --file / Read string to search from file (one by line)
--status / Show how many requests the key in use has available.
```

## **EXAMPLES**:

> Search in github taking each line of the t.txt as search pattern with a time of 5 seconds between api calls:  
> `python3 gitsearch.py --file t.txt --time 5`  

> Simple search with 1s waiting time between requests to perform the searches:  
> `python3 gitsearch.py -s 'CVE-2019–0708' -t 1`  

> If --status is added, it will first show how many requests the key in use has available:  
> `python3 gitsearch.py -s 'CVE-2019–0708' -t 10 --status`
