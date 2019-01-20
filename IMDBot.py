from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard
from ask_sdk_core.skill_builder import SkillBuilder

import pymysql
import top200

sb = SkillBuilder()

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        speech_text = "Welcome to the Alexa Skills Kit, you can say hello!"

        handler_input.response_builder.speak(speech_text).set_card(
          SimpleCard("Hello World", speech_text)).set_should_end_session(
          False)
        return handler_input.response_builder.response

class TopIMDBIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("TopIMDBIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = top200.random_movie()
        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Hello World", speech_text)).set_should_end_session(True)
        return handler_input.response_builder.response

class SearchIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("SearchIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = top200.random_movie()
        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Hello World", speech_text)).set_should_end_session(True)
        return handler_input.response_builder.response

class CancelAndStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.CancelIntent")(handler_input)\
        or is_intent_name("AMAZON.StopIntent")(handler_input)

    def handle(self, handler_input):
        return handler_input.response_builder.response

class SessionEndedRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        return handler_input.response_builder.response

from ask_sdk_core.dispatch_components import AbstractExceptionHandler

class AllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        print(exception)

        speech = "Sorry, I didn't get it. Can you please say it again!!"
        handler_input.response_builder.speak(speech).ask(speech)
        return handler_input.response_builder.response


sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(CancelAndStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(TopIMDBIntentHandler())
sb.add_exception_handler(AllExceptionHandler())
sb.add_exception_handler(SearchIntentHandler())

handler = sb.lambda_handler()
