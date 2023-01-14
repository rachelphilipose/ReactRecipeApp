import cohere

co = cohere.Client("0QhbB7ejcdwWnfaO38OHpWkgi7pdPR5x7AqGpSl9")

prompt = """  
This program generates a recipe idea based on ingredients from your fridge.

INGREDIENTS: fennel seeds, green olives, ripe olives, garlic, peppercorn, orange rind, orange juice, red chile, extra virgin olive oil
NAME: aww  marinated olives
MINUTES: 15
STEPS: toast the fennel seeds and lightly crush them, place all the ingredients in a bowl , stir well, cover and leave to marinate, keep refrigerated and use within 1 to 2 days
--
INGREDIENTS: pork spareribs, soy sauce, fresh garlic, fresh ginger, chili powder, fresh coarse ground black pepper, salt, fresh cilantro leaves, tomato sauce, brown sugar, yellow onion, white vinegar, honey, a.1. original sauce, liquid smoke, cracked black pepper, cumin, dry mustard, cinnamon sticks, orange, juice of, mirin, water
NAME: backyard style  barbecued ribs
MINUTES: 120
STEPS: in a medium saucepan combine all the ingredients for sauce#1 , bring to a full rolling boil , reduce heat to medium low and simmer for 1 hour , stirring often, rub the ribs with soy sauce , garlic , ginger , chili powder , pepper , salt and chopped cilantro , both sides !, wrap ribs in heavy duty foil, let stand 1 hour, preheat oven to 350 degrees, place ribs in oven for 1 hour , turning once after 30 minutes, 3 times during cooking the ribs open foil wrap and drizzle ribs with sauce#1, place all the ingredients for sauce#2 in a glass or plastic bowl , whisk well and set aside, remove ribs from oven and place on serving platter, offer both sauces at table to drizzle over ribs
--
INGREDIENTS: chocolate sandwich style cookies, chocolate syrup, vanilla ice cream, bananas, strawberry ice cream, whipped cream
NAME: bananas 4 ice cream  pie
MINUTES: 180
STEPS: 1.crumble cookies into a 9-inch pie plate, or cake pan 2.pat down to form an even layer 3.drizzle 1 cup of chocolate topping evenly over the cookies with a small spoon 4.scoop the vanilla ice cream on top of the chocolate and smooth down, cover with half of the sliced bananas, top with strawberry ice cream, cover and freeze until firm, before serving , top with 1 / 4 cup chocolate topping , whipped cream , and sliced bananas
--
INGREDIENTS: aaple, bread, spanich, chicken breast
"""

response = co.generate(  
    model='xlarge',  
    prompt = prompt,  
    max_tokens=40,  
    temperature=0.6,  
    stop_sequences=["--"])

recipe = response.generations[0].text
print(recipe)
