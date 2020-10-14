'''
    chatbot_test.py
    
    This file tests all methods in chatbot.py.
'''

import unittest
from chatbot import KEY_IS_BOT, KEY_BOT_COMMAND, KEY_MESSAGE
import chatbot

KEY_INPUT = "input"
KEY_EXPECTED = "expected"
KEY_LENGTH = "length"
KEY_FIRST_WORD = "first_word"
KEY_SECOND_WORD = "second_word"

class ChatbotTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "!!help",
                KEY_EXPECTED: {
                    KEY_IS_BOT: True,
                    KEY_BOT_COMMAND: "!!help",
                    KEY_MESSAGE: "help",
                }
            },
            {
                KEY_INPUT: "!about me",
                KEY_EXPECTED: {
                    KEY_IS_BOT: False,
                    KEY_BOT_COMMAND: "about",
                    KEY_MESSAGE: "me",
                }
            },
            # TODO HW13 - add another
        ]
        
        self.failure_test_params = [
            # TODO HW13
        ]


    def test_parse_message_success(self):
        for test in self.success_test_params:
            response = chatbot.parse_message(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            
            self.assertEqual(response[KEY_IS_BOT], expected[KEY_IS_BOT])
            self.assertEqual(response[KEY_BOT_COMMAND], expected[KEY_BOT_COMMAND])
            self.assertEqual(response[KEY_MESSAGE], expected[KEY_MESSAGE])
            # Alternatively (and preferably), you can do self.assertDictEqual(response, expected)
            
    def test_parse_message_failure(self):
        for test in self.failure_test_params:
            response = chatbot.parse_message(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            
            # TODO add assertNotEqual cases here instead
            self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()