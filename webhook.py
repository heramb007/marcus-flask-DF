from flask import Flask, request

# initialize the flask app
app = Flask(__name__)

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():

   req = request.get_json(silent=True, force=True)
   fulfillmentText = ''
   name = ''
   query_result = req.get('queryResult')
   if query_result.get('action') == 'welcome':
       slotvalue = query_result.get('parameters')
       print("value",slotvalue.get('custid'))

       fulfillmentText = "Thank You "+name+". How can i assist you today? "
       return {
           "fulfillmentText": fulfillmentText,
           "source": "webhookdata"
                    }
   elif query_result.get('action') == 'pastOrder':

       fulfillmentText = name+""" Based on your previous order , you have purchased 3 items.\n
                             1.Sun - Dermalogica Solar Defense Booster SPF 50-1.7 oz.\n
                             2.Face - Neutrogena Wave Deep Clean Foaming Pad Refills, 30 Count\n
                             3.Face - The Body Shop Nutriganics Smoothing Day Cream, 1.69 Fluid Ounce \n\nWe have exciting offers for you, do you want to explore?"""
           return {
           "fulfillmentText": fulfillmentText,
           "source": "webhookdata"
           }        


   elif query_result.get('action') == 'Past_Order.Past_Order-yes':


       fulfillmentText = """We have found products across categories that you might be interested in .\n
                             1.Hands &Nails - Mavala Stop - Helps Cure Nail Biting and Thumb Sucking, 0.3-Fluid Ounce \n
                             2.Eyes - Neutrogena Visibly Firm Eye Cream, Active Copper, 0.5 Ounce   \n
                             3.Eyes - Estee Lauder Stress Relief Eye Mask 10 pads \n\nPlease specify the category you're interested in. Such as skincare, sun protection, body care, eyes etc., to assist you"""
           return {
           "fulfillmentText": fulfillmentText,
           "source": "webhookdata"
           }  
# run the app
if __name__ == '__main__':
   app.run()
