
import http_plus_purplelemons_dev as http_plus
from http_plus_purplelemons_dev import Request, Response
from openai import OpenAI
import numpy as np

server = http_plus.Server()
client = OpenAI()

@server.get("/")
def _(req:Request, res:Response):
    return res.set_body("Hello, world!")

server.listen(8000)
