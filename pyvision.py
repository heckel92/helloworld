########### Python 3.6 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, json

###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.
subscription_key = 'to be defined'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'westeurope.api.cognitive.microsoft.com'

headers = {
    # Request headers.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.parse.urlencode({
    # Request parameters. The smartCropping flag is optional.
    'width': '150',
    'height': '100',
    'smartCropping': 'true',
})

# Replace the three dots below with the URL of the JPEG image for which you want a thumbnail.
body = "{'url':'https://upload.wikimedia.org/wikipedia/commons/9/94/Bloodhound_Puppy.jpg'}"

try:
    # Execute the REST API call and get the response.
    conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/generateThumbnail?%s" % params, body, headers)
    response = conn.getresponse()

    # Check for success.
    if response.status == 200:
        # Success. Use 'response.read()' to return the image data. 
        # Display the response headers.
        print ('Success.')
        print ('Response headers:')
        headers = response.getheaders()
        for field, value in headers:
            print ('  ' + field + ': ' + value)
    else:
        # Error. 'data' contains the JSON error data. Display the error data.
        data = response.read()
        parsed = json.loads(data)
        print ('Error:')
        print (json.dumps(parsed, sort_keys=True, indent=2))

    conn.close()

except Exception as e:
    print('Error:')
    print(e)

####################################
