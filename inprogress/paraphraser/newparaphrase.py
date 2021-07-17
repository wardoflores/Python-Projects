import requests

url = "https://text-summarizer1.p.rapidapi.com/summarize"

payload = "{\n  \"text\": \"Amazon Web Services has revealed that adding capacity to an already complex system was the reason its US-EAST-1 region took an unplanned and rather inconvenient break last week. The short version of the story is that the company’s Kinesis service, which is used directly by customers and underpins other parts of AWS’ own operations, added more capacity. Servers in the Kinesis fleet need to communicate with each other, and to do so create new threads for each of the other servers in the front-end fleet. AWS says there are “many thousands of servers” involved and that when new servers are added it can take up to an hour for news of additions to reach the entire fleet. Adding capacity therefore “caused all of the servers in the fleet to exceed the maximum number of threads allowed by an operating system configuration.” AWS figured that out, but also learned that fixing the problem meant rebooting all of Kinesis. But it was only possible to bring “a few hundred” servers back at a time, and as we’ve seen above Kinesis uses “many thousands of servers”. Which explains why recovery from the outage was slow. The whole sad story is explained in much greater detail in this AWS post, which also explains how it plans to avoid such incidents in future.\",\n  \"language\": \"en\",\n  \"output_sentences\": 2\n}".encode('utf-8')
headers = {
    'content-type': "application/json; text/text; charset=utf-8",
    'x-rapidapi-host': "text-summarizer1.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers) 

print(response.text)