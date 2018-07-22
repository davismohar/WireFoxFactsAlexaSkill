"""
Simple Python Lambda service for a basic "fact" skill.
Speechlet response code credit to https://github.com/techemstudios/inspiring-women-alexa 
"""

import sys
import re
import logging
import random

logger = logging.getLogger()
logger.setLevel(logging.INFO)




def credits():
    return "<speak> information credit goes to The American Kennel Club</speak>"
def UnhandledIntent():
    return "<speak>I do not understand. Try asking for facts such as height or life expectancy, or ask about famous wire fox terriers. </speak>"
def bestDog():
    return "<speak> The best dog in the world is a Wire Fox Terrier named Maggie! </speak>"
def lifeExpectancy():
    return "<speak> The average life expectancy of a Wire Fox Terrier is twelve to fiveteen years.</speak>"
def personality():
    return "<speak> The Wire Fox Terrier breed standard says they should be on the tip-toe of expectation at the slightest provocation.</speak>"
def smoothFoxFact():
    return "<speak> Although considered one breed for many years, interbreeding of Smooth Fox Terriers and Wire Fox Terriers ceased in the early 1900s. Except for coat, however, the two breeds are essentially identical </speak>"
def goToGroundFact():
    return "<speak> The Wire Fox Terrier was originally bred to go to ground to chase small game from their dens.</speak>"
def huntingFact():
    return "<speak> Fox Terriers as we know them today took shape in the late 1700s, during the heyday of British foxhunts. The terriers job was to bolt the fox from its lair, enabling hounds and horsemen to join the pursuit over open country. Fox Terrier coats are mostly white, with no red allowed, to avoid being mistaken for foxes during a hunt.</speak>"
def showFact():
    return "<speak> The Wire has always been a consistently successful show dog, with, at this writing, a record 13 Westminster Kennel Club Bests in Show. In one of the great bargains in show-dog history, Matford Vic, a Wire bought from a farmer for $10, won Westminster in 1915 and 1916. In England, Wire and Smooth Fox Terriers have been recognized as separate breeds, with different registries and breed standards, since the late 19th century. The AKC did not recognize Wire and Smooth Fox Terriers as distinct breeds until 1985. </speak>"
def ceasarFact():
    return "<speak> Among the many beloved Wires of history was Caesar, the favorite dog of King Edward VII, who enchanted the British Empire. The Wires popularity received a major boost in the 1930s and 40s thanks to Asta, the comical Wire who costarred with William Powell and Myrna Loy in six Thin Man movies. Since Astas time, the Wires striking looks, expressive features, and natural performing skills have made the breed a familiar presence in movies and on TV.</speak>"
def trainingFact():
    return "<speak> Training the Wire Fox Terrier requires consistency, patience, and a great sense of humor. Spunky and happy-go-lucky little dogs, Wires are very smart but are also somewhat independent and get bored easily, so training sessions must be kept fun and interesting. They react well to positive training methods and will shut down if treated harshly. Wires are wonderfully suited for participation in earthdog trials as well as other performance events that require agility, speed, and intelligence.</speak>"
def energyFact():
    return "<speak> Like most terriers, the Wire Fox requires a good bit of exercise. Long walks with his owner, chasing a tennis ball in the backyard, or playtime in a large, securely fenced area are all great ways to exercise your dog and keep him mentally and physically fit. Never allow your Wire Fox Terrier to run off lead, as he is likely to forget all training if he catches sight of a small animal he perceives as prey.</speak>"
def generalFact():
    return "<speak> The Wire Fox Terrier, 15 to 19 pounds of coiled energy is a sturdy, symmetrical, short-backed hunter with fire and intelligence shining in its dark, round eyes. The predominantly white coat is rough and wiry; the V-shaped ears are neatly folded forward, the better to point up the faces distinctive, and completely irresistible, expression </speak>"
def weightFact():
    return "<speak> A healthy weight for a wire fox terrier is 15 to 19 pounds </speak>"
def heightFact():
    return "<speak> Wire fox terriers can grow up to a foot tall</speak>"
def randomFact():
    num = random.randint(1, 11)
    if num == 1:
        return lifeExpectancy()
    if num == 2:
        return personality()
    if num == 3:
        return smoothFoxFact()
    if num == 4:
        return goToGroundFact()
    if num == 5:
        return huntingFact()
    if num == 6:
        return showFact()
    if num == 7:
        return ceasarFact()
    if num == 8:
        return trainingFact()
    if num == 9:
        return energyFact()
    if num == 10:
        return generalFact()
    if num == 11:
        return weightFact()
    if num == 12:
        return heightFact()
# --------------- Functions that implement default intents (only change between the <speak> tags)-------

def launch():
    #Called when the user launches the skill without specifying what they want
    return "<speak>This skill will tell you facts aobut wire fox terriers. You can ask for facts such as height or life expectancy, or ask about famous wire fox terriers</speak>"

def help():
    # Called when the user asks for help
    return "<speak>You can ask for facts such as height or life expectancy, or ask about famous wire fox terriers</speak>"

def end():
    # Called when the user says Stop or Cancel 
    return "<speak> Woof! </speak>"
def fallback():
    return "<speak>I do not understand. Try asking for facts such as height or life expectancy, or ask about famous wire fox terriers. </speak>"




# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):

    card_output = re.sub('<[^>]*>', '', output)
    
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': card_output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    logger.info("on_intent requestId=" + intent_request['requestId'] +
                ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    session_attributes = {} # No session attributes needed for simple fact response
    reprompt_text = None # No reprompt text set
    should_end_session = True # Can end session after fact is returned (no additional dialogue)

    if intent_name == 'launch':
        should_end_session = False # Opening a skill requires the session remain open
    elif intent_name == "AMAZON.HelpIntent":
        should_end_session = False # Asking for help requires the session remain open
        intent_name = 'help'
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        intent_name = 'end'
    elif intent_name == "AMAZON.FallbackIntent":
        intent_name = "fallback"
    else: 
        intent_name = intent_name
   
    speech_output = getattr(sys.modules[__name__],intent_name)()

    return build_response(session_attributes, build_speechlet_response
                          (intent_name,speech_output,reprompt_text,should_end_session))

# --------------- Main handler ------------------

def handler(event, context):
    logger.info("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    TODO: Uncomment the if statement below and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    # Defines an intent_name of "launch" if a LaunchRequest occurs
    if event['request']['type'] == "LaunchRequest":
        event['request']['intent'] = { 'name':'launch' }
    
    return on_intent(event['request'], event['session'])