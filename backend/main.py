import cohere
from cohere.classify import Example

co = cohere.Client("0QhbB7ejcdwWnfaO38OHpWkgi7pdPR5x7AqGpSl9")

prompt = """  
This program generates a startup idea and name given the industry.

Industry: Workplace  
Startup Idea: A platform that generates slide deck contents automatically based on a given outline  
Startup Name: Deckerize  
--  
Industry: Home Decor  
Startup Idea: An app that calculates the best position of your indoor plants for your apartment  
Startup Name: Planteasy
--  
Industry: Healthcare  
Startup Idea: A hearing aid for the elderly that automatically adjusts its levels and with a battery lasting a whole week  
Startup Name: Hearspan

--  
Industry: Education  
Startup Idea: An online school that lets students mix and match their own curriculum based on their interests and goals  
Startup Name: Prime Age

--  
Industry: Productivity  
Startup Idea:"""

response = co.generate(  
    model='xlarge',  
    prompt = prompt,  
    max_tokens=40,  
    temperature=0.6,  
    stop_sequences=["--"])

startup_idea = response.generations[0].text
print(startup_idea)
