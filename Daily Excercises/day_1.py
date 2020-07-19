#1. Using indexing, retrieve the string ‘willow’ from the list and assign that to the variable plant.

data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []], [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]

plant = data[7][0][0]

#2. nested-2-1: Which of the following is a legal assignment statement, after the following code executes?

d = {'key1': {'a': 5, 'c': 90, 5: 50}, 'key2':{'b': 3, 'c': "yes"}}

#A. d[5] = {1: 2, 3: 4}
#C. d['key1']['d'] = d['key2']


#3. nested-9-2: Say we had a JSON string in the following format. How would you convert it so that it is a python list?

entertainment = """[{"Library Data": {"count": 3500, "rows": 10, "locations": 3}}, {"Movie Theater Data": {"count": 8, "rows": 25, "locations": 2}}]"""

#C. json.loads(entertainment)

#4. requests-6-1: How would you request the URL http://bar.com/goodstuff?greet=hi+there&frosted=no using the requests module?

requests.get("http://bar.com/goodstuff", params = {'greet': 'hi there', 'frosted':'no'})

#5. requests-7-1: Why is it important to use a function like make_cache_key in this caching pattern rather than just uring the full url as the key?

#A. Because when requests.get encodes URL parameters, the keys in the params dictionary might be in any order, which would make it hard to compare one URL to another later on, and you could cache the same request multiple times.