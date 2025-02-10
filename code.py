print("one")
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

print("two")
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())

print("three")
agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")

print("four")
