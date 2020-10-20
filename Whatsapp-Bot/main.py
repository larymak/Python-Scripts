from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse 
 
account_sid = 'YOUR_ACCOUNT_SID' 
auth_token = 'YOUR_AUTH_TOKEN' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:TWILIO_NUMBER_HERE',  
                              body='YOUR_MESSAGE_HERE',      
                              to='whatsapp:YOUR_NUMBER_HERE' 
                          ) 
 
