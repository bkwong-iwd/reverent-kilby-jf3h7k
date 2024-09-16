import unittest
from unittest.mock import patch
from main import main

class TestMainFunction(unittest.TestCase):
    
    @patch('main.MediaWikiService.get_infobox')
    @patch('main.BooksService.search_books_by_artist')
    def test_main_function(self, mock_search_books, mock_get_infobox):
        # Mock data returned from BooksService.search_books_by_artist
        mock_books = {
            'results': [
                {'title': 'Book 1'},
                {'title': 'Book 2'},
                {'title': 'Book 3 with no wiki infobox'}
            ]
        }
        mock_search_books.return_value = mock_books

        # Mock data returned from MediaWikiService.get_infobox
        mock_get_infobox.side_effect = [
            {'release_date': '1897', 'pages': '418'},  # Info for 'book 1'
            {'release_date': None, 'pages': '337'},     # Info for 'book 2'
            None
        ]

        result = main();

        # Assertions
        self.assertEqual(result, {
            'Book 1': {'pages': '418', 'release_date': '1897'},
            'Book 2': {'pages': '337', 'release_date': None}
        })

if __name__ == '__main__':
    unittest.main()
