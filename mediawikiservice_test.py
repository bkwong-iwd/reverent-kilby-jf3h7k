import unittest
from unittest.mock import patch, MagicMock
from main import MediaWikiService

class TestMediaWikiService(unittest.TestCase):
    
    @patch('main.wptools.page')  # Mock the wptools.page function
    def test_get_infobox_success(self, mock_page):
        # Create a mock page object
        mock_page_instance = MagicMock()
        mock_page_instance.data = {
            'infobox': {
                'release_date': '1897',
                'pages': '418'
            }
        }

        # Set the return value of page().get_parse()
        mock_page.return_value = mock_page_instance
        mock_page_instance.get_parse.return_value = None  # No specific return value for get_parse()

        # Call the method under test
        result = MediaWikiService.get_infobox('Dracula')

        # Assert that the result matches the expected infobox
        self.assertEqual(result, {
            'release_date': '1897',
            'pages': '418'
        })

    @patch('main.wptools.page')
    def test_get_infobox_no_infobox(self, mock_page):
        # Create a mock page object with no infobox data
        mock_page_instance = MagicMock()
        mock_page_instance.data = {'infobox': None}  # No infobox present

        # Set the return value of page().get_parse()
        mock_page.return_value = mock_page_instance
        mock_page_instance.get_parse.return_value = None

        # Call the method under test
        result = MediaWikiService.get_infobox('Unknown Book')

        # Assert that the result is None since no infobox was found
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
