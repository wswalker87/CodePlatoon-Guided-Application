# Exercise 1: Manipulate Text
# Write a script to identify longest sentence by word count.

'''
Nestled in the heart of the Pacific Northwest, Washington State is a mesmerizing blend of natural wonders and urban sophistication. Its geography is a tapestry of contrasts, stretching from the rugged Pacific coastlines to the dense, verdant rainforests of the Olympic Peninsula, culminating in the majestic Cascade Mountains. Among these peaks, Mt. Rainier stands as a sentinel, an active volcano and the pinnacle of the state’s natural beauty. This diverse terrain provides a playground for adventurers and nature lovers alike, offering an array of activities from serene hiking trails and challenging ski slopes to tranquil kayaking routes. Beyond its scenic landscapes, Washington's ecological diversity is a testament to its environmental richness, hosting an array of wildlife that includes the majestic orcas navigating the Puget Sound and elusive elk roaming the shadowy rainforests. This harmonious blend of natural beauty and wildlife creates a unique backdrop for the state, inviting both residents and visitors to immerse themselves in its outdoor wonders. Washington State, through its stunning geography and vibrant ecosystems, stands as a beacon of the Pacific Northwest's splendor, embodying the essence of adventure and the tranquility of nature in one cohesive landscape.
'''
paragraph = "Nestled in the heart of the Pacific Northwest, Washington State is a mesmerizing blend of natural wonders and urban sophistication. Its geography is a tapestry of contrasts, stretching from the rugged Pacific coastlines to the dense, verdant rainforests of the Olympic Peninsula, culminating in the majestic Cascade Mountains. Among these peaks, Mt. Rainier stands as a sentinel, an active volcano and the pinnacle of the state’s natural beauty. This diverse terrain provides a playground for adventurers and nature lovers alike, offering an array of activities from serene hiking trails and challenging ski slopes to tranquil kayaking routes. Beyond its scenic landscapes, Washington's ecological diversity is a testament to its environmental richness, hosting an array of wildlife that includes the majestic orcas navigating the Puget Sound and elusive elk roaming the shadowy rainforests. This harmonious blend of natural beauty and wildlife creates a unique backdrop for the state, inviting both residents and visitors to immerse themselves in its outdoor wonders. Washington State, through its stunning geography and vibrant ecosystems, stands as a beacon of the Pacific Northwest's splendor, embodying the essence of adventure and the tranquility of nature in one cohesive landscape."

lc_paragraph = paragraph.lower()
lc_paragraph = lc_paragraph.replace("mt. rainier", "mount rainier")

sent_list = lc_paragraph.split('.') # .split() automatically splits into a list.

for sent in sent_list:
    pass
   #print(sent.strip())



word_list = []

for sent in sent_list:
    word_list.append(sent.split())
   #print(word_list)

max_words = 0
max_list = []

for word in word_list:
    if len(word) > max_words:
        max_words = len(word)
        max_list = word
    else:
        continue
#print(max_words, max_list)

    formatted_sent = " ".join(max_list) + "."
    formatted_sent = formatted_sent.capitalize()

print(formatted_sent)