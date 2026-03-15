# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Stream Extractor is a Python CLI tool that extracts m3u8 stream URLs from webpages using Playwright, then launches VLC with the correct authentication headers (referer and user-agent).

## Commands

```bash
# Install dependencies (requires uv)
uv sync --extra dev

# Install Playwright Chromium browser (required before first run)
playwright install chromium

# Run CLI
uv run stream-extractor <url>
uv run stream-extractor <url> --no-play

# Run tests
uv run pytest

# Run a single test
uv run pytest tests/test_cli.py::TestFunctionName
```

## Architecture

- `stream_extractor/cli.py` - Single-module package containing:
  - `extract_stream_info()` - Uses Playwright to intercept .m3u8 requests and capture headers
  - `launch_vlc()` - Spawns VLC subprocess with `--http-referrer` and `--http-user-agent` flags
  - `main()` - CLI entry point using argparse

- `tests/test_cli.py` - Unit tests with pytest-mock for subprocess and Playwright

## Key Details

- Uses `uv` for package management (not pip directly)
- Requires Playwright Chromium browser installed separately
- Stream URLs have time-limited tokens - run immediately after extraction
- VLC is launched with headers as CLI arguments, not playlist options
