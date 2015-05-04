from unittest import TestCase

from nexmomessage import NexmoMessage


class VerificationTest(TestCase):
    def test_it_should_build_a_verification_request_message(self):
        nexmo_settings = {
            'key': 'key12345',
            'secret': 'secret12'
        }

        brand = 'TESTBRAND'
        msg = {
            'reqtype': 'json',
            'api_key': nexmo_settings['key'],
            'api_secret': nexmo_settings['secret'],
            'from': brand,
            'to': 31612345678,
            'text': 'Message Body',
            'type': 'verification-message'
        }
        sms = NexmoMessage(msg)

        request = sms.build_request()

        expected_request = (
            'https://api.nexmo.com/verify/json'
            '?api_key={api_key}'
            '&api_secret={api_secret}'
            '&number={number}'
            '&brand={brand}'.format(
                api_key=nexmo_settings['key'],
                api_secret=nexmo_settings['secret'],
                number='31612345678',
                brand=brand
            )
        )

        self.assertEqual(expected_request, request)

    def test_it_should_build_a_verification_check_message(self):
        nexmo_settings = {
            'key': 'key12345',
            'secret': 'secret12'
        }

        request_id = '8g88g88eg8g8gg9g90'
        code = 123456

        brand = 'TESTBRAND'
        msg = {
            'reqtype': 'json',
            'api_key': nexmo_settings['key'],
            'api_secret': nexmo_settings['secret'],
            'from': brand,
            'to': 31612345678,
            'text': 'Message Body',
            'type': 'verification-check',
            'request_id': request_id,
            'code': code
        }
        sms = NexmoMessage(msg)

        request = sms.build_request()

        expected_request = (
            'https://api.nexmo.com/verify/json'
            '?api_key={api_key}'
            '&api_secret={api_secret}'
            '&request_id={request_id}'
            '&code={code}'.format(
                api_key=nexmo_settings['key'],
                api_secret=nexmo_settings['secret'],
                request_id=request_id,
                code=code
            )
        )

        self.assertEqual(expected_request, request)