# 1. Below, we have provided a list of strings called abbrevs. Use map to produce a new list called abbrevs_upper that contains all the same strings in upper case.

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

abbrevs_upper = list(map(lambda x: x.upper(), abbrevs))

# 2. Why is it important to use a function like make_cache_key in this caching pattern rather than just uring the full url as the key?

# A. Because when requests.get encodes URL parameters, the keys in the params dictionary might be in any order, which would make it hard to compare one URL to another later on, and you could cache the same request multiple times.

# 3. Why would you define a function in order to make a request to a REST API for data?

# A. Because that means you have to write less repeated code if you want to make a request to the same API more than once in the same program.
# B. Because writing functions to complete a complex process in your code makes it easier to read and easier to fix later.
# C. Because a lot of things stay the same among different requests to the same API.

# 4. If the results you are getting back from a call to requests.get() are not what you expected, what’s the first thing you should do?

# B. look at the first few characters of the .text attribute of the Response object

# 5. If you wanted to search for photos tagged with either river or mountains, rather than requiring both, what would you change in the code? (Hint: check the documentation)

# C. Set ``params_diction["tag_mode"] = "any"``