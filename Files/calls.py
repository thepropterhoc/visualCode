import requests

payload = dict(
        name="CHATEAU DE SAINT COSME",
        year="2009",
        grapes="Grenache / Syrah",
        country="France",
        region="Southern Rhone",
        description="The aromas of fruit and spice...",
        picture="saint_cosme.jpg")
r = requests.delete("http://ec2-54-187-104-253.us-west-2.compute.amazonaws.com:3000/wines/534f617aff0677de0d89ec16")
print r