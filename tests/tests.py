from unittest import TestCase
from mock import patch, Mock
from nexmomessage.nexmo import NexmoVerificationRequest, NexmoVerificationCheck

class NexmoMessagesTest(TestCase):
    def setUp(self):
        self.test_key = 'key12345'
        self.test_secret = 'secret12'
        self.msg_config = {
            'api_key': self.test_key,
            'api_secret': self.test_secret,
            'text': 'Message Body',
        }

    def test_it_should_send_a_verification_request_message(self):
        test_brand = 'TESTBRAND'
        test_number = 31612345678
        self.msg_config['from'] = test_brand
        self.msg_config['to'] = test_number
        sms = NexmoVerificationRequest(self.msg_config)
        expected_url = (
            'https://api.nexmo.com/verify/json'
            '?api_key={api_key}'
            '&api_secret={api_secret}'
            '&number={number}'
            '&brand={brand}'.format(
                api_key=self.test_key,
                api_secret=self.test_secret,
                number=test_number,
                brand=test_brand
            ))

        self.message_sent_test(sms, expected_url)

    def test_it_should_send_a_verification_check_message(self):
        request_id = '8g88g88eg8g8gg9g90'
        code = 123456
        self.msg_config['request_id'] = request_id
        self.msg_config['code'] = code
        sms = NexmoVerificationCheck(self.msg_config)

        expected_url = (
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

        self.message_sent_test(sms, expected_url)

    def test_it_should_send_a_verification_status_message(self):
        request_id = '8g88g88eg8g8gg9g90'
        code = 123456
        self.msg_config['request_id'] = request_id
        self.msg_config['code'] = code
        sms = NexmoVerificationCheck(self.msg_config)

        expected_url = (
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

        self.message_sent_test(sms, expected_url)

    def message_sent_test(self, sms, expected_url):
        with patch('nexmomessage.nexmo.urllib2') as urllib2:
            request = Mock()
            response = Mock()
            response.code = 200
            response.read.return_value = '{}'
            urllib2.Request.return_value = request
            urllib2.urlopen.return_value = response

            sms.send_request()
        urllib2.Request.assert_called_with(url=expected_url)
        request.add_header.assert_called_with('Accept', 'application/json')
        urllib2.urlopen.assert_called_with(request)
