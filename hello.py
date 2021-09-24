#!/usr/bin/env python3

import os
import json

print("Content-Type:text/html\r\n\r\n")
print("<title> title </title>")
print(os.environ) # inspec t envrionemtn variables
# serve env back as json
json_env = json.dumps(dict(os.environ), indent=4)
print(json_env)
print("<b>"+"Query string"+"</b> = {" + os.environ.get("QUERY_STRING") + "}"+"<br>")
print("<b>User browser in HTML</b> = {" + os.environ.get("HTTP_USER_AGENT") + "}<br>")