"""
Tests for the ytmp4-kp package
"""

import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Add the parent directory to the path so we can import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ytmp4_kp.main import download_video
from ytmp4_kp.utils import check_yt_dlp_installed

class TestYtmp4Kp(unittest.TestCase):
    """Test cases for the ytmp4-kp package"""
    
    @patch('ytmp4_kp.utils.subprocess.run')
    def test_check_yt_dlp_installed_success(self, mock_run):
        """Test check_yt_dlp_installed when yt-dlp is already installed"""
        # Configure the mock to return a successful result
        mock_run.return_value = MagicMock(returncode=0)
        
        # Call the function
        result = check_yt_dlp_installed()
        
        # Assert that it returned True
        self.assertTrue(result)
        
        # Assert that subprocess.run was called with the correct arguments
        mock_run.assert_called_once()
        args, kwargs = mock_run.call_args
        self.assertEqual(args[0][0], "yt-dlp")
    
    @patch('ytmp4_kp.utils.subprocess.run')
    def test_check_yt_dlp_installed_not_found(self, mock_run):
        """Test check_yt_dlp_installed when yt-dlp is not installed"""
        # First call raises FileNotFoundError, second call (pip install) succeeds
        mock_run.side_effect = [
            FileNotFoundError("yt-dlp not found"),
            MagicMock(returncode=0)
        ]
        
        # Call the function
        result = check_yt_dlp_installed()
        
        # Assert that it returned True (because installation succeeded)
        self.assertTrue(result)
        
        # Assert that subprocess.run was called twice
        self.assertEqual(mock_run.call_count, 2)
    
    @patch('ytmp4_kp.main.check_yt_dlp_installed')
    @patch('ytmp4_kp.main.subprocess.run')
    def test_download_video_success(self, mock_run, mock_check):
        """Test download_video with a successful download"""
        # Configure the mocks
        mock_check.return_value = True
        mock_run.return_value = MagicMock(returncode=0)
        
        # Call the function
        result = download_video("https://www.youtube.com/watch?v=example")
        
        # Assert that it returned True
        self.assertTrue(result)
        
        # Assert that subprocess.run was called twice
        self.assertEqual(mock_run.call_count, 2)
    
    @patch('ytmp4_kp.main.check_yt_dlp_installed')
    def test_download_video_no_yt_dlp(self, mock_check):
        """Test download_video when yt-dlp is not installed"""
        # Configure the mock
        mock_check.return_value = False
        
        # Call the function
        result = download_video("https://www.youtube.com/watch?v=example")
        
        # Assert that it returned False
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
