import africastalking
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--chemical", required=True,
                help="The chemical whose name just got finished executing")
ap.add_argument("-p", "--phone", required=True,
                help="The phone numbers to be contacted")

args = vars(ap.parse_args())

api_key = "26a2f97b624f315d186d3579901f86f8c8b3868089d41c4c65740bd1285d58a2"
username = "TomiTsuma"
africastalking.initialize(username, api_key)

sms = africastalking.SMS

sms.send(f"Training complete! Chemical: {args['chemical']}", args['phone'])
