# Audio Clip Bench

Listen to a recording, set a time range and export the selected segment as a WAV file.

Download `index.html` and open it in a modern desktop browser. Files are processed locally, with no account or network service.

## Example and supported inputs

For a 10-second recording, set Start to 2 and End to 5. Play the selection and export a 3-second clip. Export uses 16-bit PCM at the browser audio context's sample rate, preserving mono or stereo. Input support depends on the browser's audio decoders. The decoded recording and exported clip must fit in device memory.

## Limitations

Work stays in the browser tab. Save the result before closing or refreshing the page.

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup and test commands, and the [changelog](CHANGELOG.md) for project history.

## License

[MIT License](LICENSE). Copyright (c) 2026 audio-clip-bench contributors.
