import urllib2, json

# Replace this with your own
API_KEY = '6404f06f50bd47669bb1b33af77b1688'

# def sample_function(name):
#     print 'I am a sample function'
#     print 'My name is %s' % name
#     return

########## YOUR CODE GOES HERE ##########

def get_bills(state, subject):
    
    response = urllib2.urlopen('http://openstates.org/api/v1/bills/?state=%s&type=bill&subject=%s&apikey=%s' % (state, subject, API_KEY))
    json_object = json.load(response)

    for result in json_object:
        print result['title']
    
    # '''
    # This function should accomplish the following tasks:
    #   - Open a connection to the /bills/ endpoing of Sunlight Foundation's OpenStates API:
    #     http://sunlightlabs.github.io/openstates-api/bills.html#methods/bill-search
    #   - Retrieve an API response with bills from the current legislative session in Missouri
    #   - print the titles of bills that contain "Transportation" in the "subjects" list
    # '''
    return

########## RUN FUNCTIONS HERE ##########

# Uncomment this to run your function with the appropriate arguments, as specified above
get_bills('mo', 'Transportation')

