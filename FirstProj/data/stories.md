## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## search restaurants
* search_restaurants
  - action_search_restaurants
  
## covid tracker
* covid_tracker
  - action_covid_tracker

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye
  
## hello world path
* hello_world
  - utter_hello_world

## get custom response
* custom_response
  - action_custom_response

## bot challenge
* bot_challenge
  - utter_iamabot
