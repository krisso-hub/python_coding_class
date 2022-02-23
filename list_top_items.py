'''A program that sort list of shop items and print out
    three(3) top most in the list
    Author: Ndubuisi,  Date: 02/20/22
'''
sample = {'Apple': 0.50, 'Banana': 0.20, 'Mango': 0.99, 'Coconut': 2.99, 'Pineapple': 3.99}

# sorting the sample by values
def by_value(item):
    return item[1]

# setting a counter to break out when after three(3) counts
counter = 0
for k, v in sorted(sample.items(), key=by_value, reverse=True):
    counter+=1
    if counter == 4:
        break
    print(k, v)
    

