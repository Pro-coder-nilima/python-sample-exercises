import re
message = "python laboratory"
result = re.search('python',message)
result = re.search('laboratory', string = message)
print(result.group())
print(len(re.findall('p.*',message)))