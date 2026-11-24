# Audio Clip Bench

Listen to a recording, set a time range and export the selected segment as a WAV file.

Download `index.html` and open it in a modern desktop browser. Files are processed locally, with no account or network service.

## Example and supported inputs

For a 10-second recording, set Start to 2 and End to 5. Play the selection and export a 3-second clip. Export uses 16-bit PCM at the browser audio context's sample rate, preserving mono or stereo. Input support depends on the browser's audio decoders. The decoded recording and exported clip must fit in device memory.
