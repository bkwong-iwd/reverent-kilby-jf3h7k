import unittest
from unittest.mock import patch
from main import BooksService

class TestBooksService(unittest.TestCase):
    @patch('main.requests.get')  # Mock the requests.get method
    def test_search_books_by_artist_success(self, mock_get):
        # Define the mock response object
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'results': [
                {'title': 'Dracula', 'author': 'Bram Stoker'},
                {'title': 'The Jewel of Seven Stars', 'author': 'Bram Stoker'}
            ]
        }

        # Set the return value of the mocked requests.get
        mock_get.return_value = mock_response

        # Call the method under test
        result = BooksService.search_books_by_artist('Bram Stoker')

        # Assert that the result matches the expected output
        self.assertEqual(result['results'], [
            {'title': 'Dracula', 'author': 'Bram Stoker'},
            {'title': 'The Jewel of Seven Stars', 'author': 'Bram Stoker'}
        ])

    @patch('main.requests.get')  # Mock the requests.get method
    def test_search_books_by_artist_failure(self, mock_get):
        # Mock an error response with a non-200 status code
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Call the method under test
        result = BooksService.search_books_by_artist('Bram Stoker')

        # Assert that the result is None due to the error
        self.assertIsNone(result)

    @patch('main.requests.get')  # Mock the requests.get method
    def test_search_books_by_artist_empty_response(self, mock_get):
        # Mock a response with a 200 status code but no results
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'results': []}
        mock_get.return_value = mock_response

        # Call the method under test
        result = BooksService.search_books_by_artist('Unknown Author')

        # Assert that the result is an empty list
        self.assertEqual(result['results'], [])

if __name__ == '__main__':
    unittest.main()
