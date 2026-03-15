# Stream Extractor

CLI tool to extract m3u8 stream URLs from webpages and play them in mpv with the correct headers.

## Prerequisites

- [mpv](https://mpv.io/) installed on your system - [Installation](https://mpv.io/installation/)
- [uv](https://github.com/astral-sh/uv) package manager - [Installation](https://github.com/astral-sh/uv?tab=readme-ov-file#installation)

## Installation

### macOS

```bash
git clone https://github.com/davidecoccia/media-stream-extractor.git
cd media-stream-extractor
uv sync --extra dev
playwright install chromium
```

### Linux

```bash
git clone https://github.com/davidecoccia/media-stream-extractor.git
cd media-stream-extractor
uv sync --extra dev
playwright install chromium
```

### Windows

```powershell
git clone https://github.com/davidecoccia/media-stream-extractor.git
cd media-stream-extractor
uv sync --extra dev
playwright install chromium
```

## Usage

```bash
# Extract stream and play in mpv
uv run stream-extractor <url>

# Extract stream info only (don't launch mpv)
uv run stream-extractor <url> --no-play
```

## Example

```bash
uv run stream-extractor "https://shd247.live/live-go-streaming-29.html"
```

## Development

```bash
# Install dependencies
uv sync --extra dev

# Install Playwright browsers
playwright install chromium

# Run tests
uv run pytest

# Run CLI
uv run stream-extractor <url>
```
