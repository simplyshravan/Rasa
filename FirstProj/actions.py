# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_custom_response"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("debug actions.py")
        dispatcher.utter_message(text="this is custom message")

        return []

class ActionSearchRestaruants(Action):

    def name(self) -> Text:
        return "action_search_restaurants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("searching restaurants")
        entities=tracker.latest_message['entities']
        print(entities)
        for i in entities:
            if i['entity']=='continent':
                cont=i['value']
        if cont=='indian':
            message='Indian indian india'
        elif cont=='italian':
            message='Italy italian'
        elif cont=='chinese':
            message='chinese china'
        dispatcher.utter_message(text=message)

        return []

class ActionCovidTracker(Action):

    def name(self) -> Text:
        return "action_covid_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response=requests.get('https://api.covid19india.org/data.json').json()
        entities = tracker.latest_message['entities']
        print(entities)
        for i in entities:
            if i['entity']=='state':
                statename=i['value']

        message="please enter correct state name"
        #print(response["statewise"])
        print(statename)
        for data in response["statewise"]:
            if data["state"]==statename.title():
                print(data)
                message="Active: "+data['active']+" Confirmed: "+data['confirmed']+ " Death: "+data['deaths']

        print(message)
        dispatcher.utter_message(text=message)

        return []