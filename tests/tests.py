from unittest import TestCase
from nexmomessage.nexmo import NexmoVerificationRequest, NexmoVerificationCheck


class VerificationMessageTest(TestCase):
    def setUp(self):
        self.test_key = 'key12345'
        self.test_secret = 'secret12'
        self.msg = {
            'api_key': self.test_key,
            'api_secret': self.test_secret,
            'text': 'Message Body',
        }

    def test_it_should_build_a_verification_request_message(self):
        test_brand = 'TESTBRAND'
        self.msg['from'] = test_brand
        test_number = 31612345678
        self.msg['to'] = test_number
        sms = NexmoVerificationRequest(self.msg)

        request = sms.build_request()

        expected_request = (
            'https://api.nexmo.com/verify/json'
            '?api_key={api_key}'
            '&api_secret={api_secret}'
            '&number={number}'
            '&brand={brand}'.format(
                api_key=self.test_key,
                api_secret=self.test_secret,
                number=test_number,
                brand=test_brand
            )
        )

        self.assertEqual(expected_request, request)

    def test_it_should_build_a_verification_check_message(self):

        request_id = '8g88g88eg8g8gg9g90'
        code = 123456
        self.msg['request_id'] = request_id
        self.msg['code'] = code

        sms = NexmoVerificationCheck(self.msg)

        request = sms.build_request()

        expected_request = (
            'https://api.nexmo.com/verify/json'
            '?api_key={api_key}'
            '&api_secret={api_secret}'
            '&request_id={request_id}'
            '&code={code}'.format(
                api_key=self.test_key,
                api_secret=self.test_secret,
                request_id=request_id,
                code=code
            )
        )

        self.assertEqual(expected_request, request)

    # def test_it_should_send_a_verification_message(self):
    #     sms = NexmoVerification(self.msg)

