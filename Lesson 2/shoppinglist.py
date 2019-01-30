shopping_list = ["borscht","lettuce","asiago cheese","cantaloupes","cabbage","fish sauce","pumpkins","barley sugar","Havarti cheese","beer","cayenne pepper","cream of tartar","poppy seeds","habanero chilies","graham crackers","raisins","pico de gallo","bacon","tomato juice","zinfandel wine","andouille sausage","cod","sazon","rhubarb","Romano cheese","yogurt","parsley","mussels","chicken liver","pickles","pineapples","arugula","green onions","pears","prunes","granola","lemons","tortillas","crabs","baking powder","sweet peppers","ale","geese","curry powder","brown rice","chicken","passion fruit","capers","gouda","orange peels","succotash","custard","molasses","bok choy","red cabbage","almonds","oranges","angelica","onion powder","oatmeal","caviar","tomato paste","squid","peanut butter","bananas","prosciutto","potato chips","vegemite","plums","brussels sprouts","provolone","pink beans","aioli","wine","artificial sweetener","octopus","gelatin","ricotta cheese","margarine","milk","apple butter","breadfruit","soy sauce","tofu","tarragon","amaretto","turnips","nectarines","mustard","limes","water","applesauce","chocolate","bourbon","grits","soybeans","cremini mushrooms","ketchup","salsa","Mandarin oranges"]

shopping_list.sort()

shopping_list.remove('Havarti cheese')
shopping_list.append('havarti cheese')

shopping_list.remove('Mandarin oranges')
shopping_list.append('mandarin oranges')

shopping_list.remove('Romano cheese')
shopping_list.append('romano cheese')
print('<ul>')

for ingredient in shopping_list:
	
	print('<li>' + ingredient + '</li>')
print('</ul>')
	