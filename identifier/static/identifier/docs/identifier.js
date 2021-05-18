// https://medium.com/@bryanjenningz/how-to-record-and-play-audio-in-javascript-faa1b2b3e49b

function recordAudio() {
  navigator.mediaDevices.getUserMedia({ audio: {channelCount: 1, sampleRate: 44100} }).then((stream) => {
    const mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start();

    const audioChunks = [];
    mediaRecorder.addEventListener("dataavailable", (event) => {
      audioChunks.push(event.data);
    });

    mediaRecorder.addEventListener("stop", () => {
      const audioBlob = new Blob(audioChunks);
      console.log(audioBlob.arrayBuffer())
      return audioBlob;
    });

    setTimeout(() => {
      mediaRecorder.stop();
    }, 4000);
  });
}


//const arrayBuffer = await recordAudio();
//console.log(arrayBuffer)
