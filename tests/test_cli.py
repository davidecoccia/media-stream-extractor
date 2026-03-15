import subprocess
from unittest.mock import MagicMock, patch

import pytest


class TestLaunchVlc:
    """Tests for the launch_vlc function."""

    @patch("stream_extractor.cli.subprocess.run")
    def test_launch_vlc_with_headers(self, mock_run):
        """Test VLC is launched with correct arguments."""
        from stream_extractor.cli import launch_vlc

        launch_vlc(
            "https://example.com/stream.m3u8",
            "https://example.com/",
            "Mozilla/5.0"
        )

        mock_run.assert_called_once()
        call_args = mock_run.call_args[0][0]

        assert "vlc" in call_args
        assert "--http-referer" in call_args
        assert "https://example.com/" in call_args
        assert "--http-user-agent" in call_args
        assert "Mozilla/5.0" in call_args
        assert "https://example.com/stream.m3u8" in call_args

    @patch("stream_extractor.cli.subprocess.run")
    def test_launch_vlc_command_list(self, mock_run):
        """Test VLC command is passed as a list."""
        from stream_extractor.cli import launch_vlc

        launch_vlc("https://example.com/stream.m3u8", "", "")

        mock_run.assert_called_once()
        # Verify it's called with a list, not a string
        call_args = mock_run.call_args[0][0]
        assert isinstance(call_args, list)


class TestMain:
    """Tests for the main CLI function."""

    @patch("stream_extractor.cli.extract_stream_info")
    @patch("stream_extractor.cli.launch_vlc")
    def test_main_success(self, mock_launch, mock_extract):
        """Test main function with successful extraction."""
        from stream_extractor.cli import main
        import sys

        mock_extract.return_value = {
            "url": "https://example.com/stream.m3u8",
            "referer": "https://example.com/",
            "user_agent": "Mozilla/5.0"
        }

        with patch.object(sys, "argv", ["stream-extractor", "https://example.com"]):
            main()

        mock_extract.assert_called_once_with("https://example.com")
        mock_launch.assert_called_once()

    @patch("stream_extractor.cli.extract_stream_info")
    def test_main_no_stream_found(self, mock_extract):
        """Test main function when no stream is found."""
        from stream_extractor.cli import main
        import sys

        mock_extract.return_value = {}

        with patch.object(sys, "argv", ["stream-extractor", "https://example.com"]):
            with pytest.raises(SystemExit) as exc_info:
                main()

        assert exc_info.value.code == 1

    @patch("stream_extractor.cli.extract_stream_info")
    @patch("stream_extractor.cli.launch_vlc")
    def test_main_no_play_flag(self, mock_launch, mock_extract):
        """Test main function with --no-play flag."""
        from stream_extractor.cli import main
        import sys

        mock_extract.return_value = {
            "url": "https://example.com/stream.m3u8",
            "referer": "https://example.com/",
            "user_agent": "Mozilla/5.0"
        }

        with patch.object(sys, "argv", ["stream-extractor", "--no-play", "https://example.com"]):
            main()

        mock_extract.assert_called_once()
        mock_launch.assert_not_called()


class TestExtractStreamInfo:
    """Tests for extract_stream_info using a simpler integration-style test."""

    @patch("stream_extractor.cli.sync_playwright")
    def test_extract_stream_info_returns_dict(self, mock_playwright):
        """Test that extract_stream_info returns a dictionary."""
        from stream_extractor.cli import extract_stream_info

        # Setup mock chain
        mock_browser = MagicMock()
        mock_page = MagicMock()
        mock_playwright.return_value.__enter__ = MagicMock(return_value=mock_playwright)
        mock_playwright.return_value.__exit__ = MagicMock(return_value=False)
        mock_playwright.return_value.chromium.launch.return_value = mock_browser
        mock_browser.new_page.return_value = mock_page
        mock_page.goto.return_value = None
        mock_page.wait_for_timeout.return_value = None
        mock_browser.close.return_value = None

        result = extract_stream_info("https://example.com")

        assert isinstance(result, dict)
        # No requests captured, so keys won't be set
        assert "url" not in result
