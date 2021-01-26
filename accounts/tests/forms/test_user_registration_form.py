import logging

from django.test import TestCase
from typing      import Optional

from accounts.exception                    import AccountsException
from accounts.forms.user_registration_form import UserRegistrationForm

logger = logging.getLogger('accounts.tests')


class TestUserRegistrationForm(TestCase):
    _test_user_registration_form: Optional[UserRegistrationForm] = None
    _test_name                  : Optional[str]                  = None

    def test_password_one_and_password_two_do_not_match(self) -> None:
        self._test_name = 'Test Password One and Password Two Do Not Match'
        try:
            self._test_user_registration_form = UserRegistrationForm(
                data={
                    'username'              : 'test_user',
                    'first_name'            : 'Raymond',
                    'last_name'             : 'Sutton',
                    'email'                 : 'test@test.com',
                    'password'              : 'abc12321cba',
                    'password_confirmation' : 'acb123cba'
                }
            )

            self.assertFalse(self._test_user_registration_form.is_valid())

            self.assertEqual(
                self._test_user_registration_form.errors['password_confirmation'],
                ['Your password inputs do not match. Please re-enter your password information.']
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #1 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #1 - {self._test_name}')

    def test_username_is_required(self) -> None:
        self._test_name = 'Test Username Is Required'
        try:
            self._test_user_registration_form = UserRegistrationForm(
                data={
                    'username'             : '',
                    'first_name'           : 'Raymond',
                    'last_name'            : 'Sutton',
                    'email'                : 'test@test.com',
                    'password'             : 'abc12321cba',
                    'password_confirmation': 'abc12321cba'
                }
            )

            self.assertFalse(self._test_user_registration_form.is_valid())

            self.assertEqual(
                self._test_user_registration_form.errors['username'],
                ['This field is required.']
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #2 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #2 - {self._test_name}')

    def test_invalid_email_address_pattern(self) -> None:
        self._test_name = 'Test Invalid Email Address Pattern'
        try:
            self._test_user_registration_form = UserRegistrationForm(
                data={
                    'username'              : 'test_user',
                    'first_name'            : 'Raymond',
                    'last_name'             : 'Sutton',
                    'email'                 : 'aaa',
                    'password'              : 'acb12321cba',
                    'password_confirmation' : 'acb12321cba'
                }
            )

            self.assertFalse(self._test_user_registration_form.is_valid())

            self.assertEqual(
                self._test_user_registration_form.errors['email'],
                ['Enter a valid email address.']
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #3 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #3 - {self._test_name}')

    def test_email_is_required(self) -> None:
        self._test_name = 'Test Email Is Required'
        try:
            self._test_user_registration_form = UserRegistrationForm(
                data={
                    'username'             : 'test_user',
                    'first_name'           : 'Raymond',
                    'last_name'            : 'Sutton',
                    'email'                : '',
                    'password'             : 'abc12321cba',
                    'password_confirmation': 'abc12321cba'
                }
            )

            self.assertFalse(self._test_user_registration_form.is_valid())

            self.assertEqual(
                self._test_user_registration_form.errors['email'],
                ['This field is required.']
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #4 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #4 - {self._test_name}')

    def test_email_with_capitalization_is_cleaned_properly(self) -> None:
        self._test_name = 'Test Email With Capitalization Is Cleaned Properly'
        try:
            self._test_user_registration_form = UserRegistrationForm(
                data={
                    'username'             : 'test_user',
                    'first_name'           : 'Raymond',
                    'last_name'            : 'Sutton',
                    'email'                : 'tEsT@tEst.CoM',
                    'password'             : 'abc12321cba',
                    'password_confirmation': 'abc12321cba'
                }
            )

            self.assertTrue(self._test_user_registration_form.is_valid())

            self.assertEqual(
                self._test_user_registration_form.cleaned_data['email'],
                'test@test.com'
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #5 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #5 - {self._test_name}')

    def test_first_name_with_incorrect_capitalization(self) -> None:
        self._test_name = 'Test First Name With Incorrect Capitalization'
        try:
            self._test_user_registration_form = UserRegistrationForm(
                data={
                    'username'              : 'test_user',
                    'first_name'            : 'rAymond',
                    'last_name'             : 'Sutton',
                    'email'                 : 'test@test.com',
                    'password'              : 'abc12321cba',
                    'password_confirmation' : 'abc12321cba'
                }
            )

            self.assertTrue(self._test_user_registration_form.is_valid())

            self.assertEqual(
                self._test_user_registration_form.cleaned_data['first_name'],
                'Raymond'
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #6 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #6 - {self._test_name}')

    def test_first_name_is_required(self) -> None:
        self._test_name = 'Test First Name Is Required'
        try:
            self._test_user_registration_form = UserRegistrationForm(
                data={
                    'username'             : 'test_user',
                    'first_name'           : '',
                    'last_name'            : 'Sutton',
                    'email'                : 'test@test.com',
                    'password'             : 'abc12321cba',
                    'password_confirmation': 'abc12321cba'
                }
            )

            self.assertFalse(self._test_user_registration_form.is_valid())

            self.assertEqual(
                self._test_user_registration_form.errors['first_name'],
                ['Your first name must be at least one character in length.']
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #7 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #7 - {self._test_name}')

    def test_last_name_with_incorrect_capitalization(self) -> None:
        self._test_name = 'Test Last Name With Incorrect Capitalization'
        try:
            self._test_user_registration_form = UserRegistrationForm(
                data={
                    'username'             : 'test_user',
                    'first_name'           : 'Raymond',
                    'last_name'            : 'sUTTon',
                    'email'                : 'test@test.com',
                    'password'             : 'abc12321cba',
                    'password_confirmation': 'abc12321cba'
                }
            )

            self.assertTrue(self._test_user_registration_form.is_valid())

            self.assertEqual(
                self._test_user_registration_form.cleaned_data['last_name'],
                'Sutton'
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #8 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #8 - {self._test_name}')

    def test_last_name_is_required(self) -> None:
        self._test_name = 'Test Last Name Is Required'
        try:
            self._test_user_registration_form = UserRegistrationForm(
                data={
                    'username'             : 'test_user',
                    'first_name'           : 'Raymond',
                    'last_name'            : '',
                    'email'                : 'test@test.com',
                    'password'             : 'abc12321cba',
                    'password_confirmation': 'abc12321cba'
                }
            )

            self.assertFalse(self._test_user_registration_form.is_valid())

            self.assertEqual(
                self._test_user_registration_form.errors['last_name'],
                ['Your last name must be at least one character in length.']
            )
        except AssertionError as error:
            logger.exception(f'Failed Test #9 - {self._test_name}')
            self.fail()
        else:
            logger.info(f'Completed Test #9 - {self._test_name}')
            


