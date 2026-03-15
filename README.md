# Stream Extractor

CLI tool to extract m3u8 stream URLs from webpages and play them in VLC with the correct headers.

## Installation

```bash
uv sync --extra dev
playwright install chromium
```

## Usage

```bash
# Extract stream and play in VLC
uv run stream-extractor <url>

# Extract stream info only (don't launch VLC)
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
