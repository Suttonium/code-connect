import logging

from django.http.response import HttpResponse
from django.test          import TestCase
from http                 import HTTPStatus
from typing               import Optional

logger = logging.getLogger('accounts.tests')


class TestUserRegistrationView(TestCase):

    _test_response : Optional[HttpResponse] = None
    _test_name     : Optional[str]          = None
    
    def test_get(self) -> None:
        self._test_name = 'Test Get Method For UserRegistrationView'
        try:
            self._test_response = self.client.get('/accounts/registration/')

            self.assertEqual(
                self._test_response.status_code,
                HTTPStatus.OK
            )

            self.assertTemplateUsed(
                self._test_response,
                'accounts/user_registration_template.html'
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #1 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #1 - {self._test_name}')

    def test_post(self) -> None:
        self._test_name = 'Test Post Method For UserRegistrationView'
        try:
            self._test_response = self.client.post(
                '/accounts/registration/',
                data={
                    'username'              : 'test_user',
                    'first_name'            : 'Raymond',
                    'last_name'             : 'Sutton',
                    'email'                 : 'test_email',
                    'password'              : 'abc12321cba',
                    'password_confirmation' : 'abc12321cba'
                }
            )

            self.assertEqual(
                self._test_response.status_code,
                HTTPStatus.OK
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #2 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #2 - {self._test_name}')

