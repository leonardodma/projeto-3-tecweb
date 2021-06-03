function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// https://stackoverflow.com/questions/60431835/how-to-convert-a-blob-url-to-a-audio-file-and-save-it-to-the-server
const sendAudioFile = (file) => {
  const csrftoken = getCookie("csrftoken");
  console.log(csrftoken);

  const formData = new FormData();
  formData.append("audio-file", file);
  return fetch("/api/mp3/", {
    method: "POST",
    headers: { "X-CSRFToken": csrftoken },
    body: formData,
  }).then((response) => response.json());
};

// https://medium.com/@bryanjenningz/how-to-record-and-play-audio-in-javascript-faa1b2b3e49b
function recordAudio() {
  navigator.mediaDevices
    .getUserMedia({ audio: { channelCount: 1, sampleRate: 44100 } })
    .then((stream) => {
      const mediaRecorder = new MediaRecorder(stream);
      mediaRecorder.start();

      const audioChunks = [];
      mediaRecorder.addEventListener("dataavailable", (event) => {
        audioChunks.push(event.data);
        console.log(event.data);
      });

      mediaRecorder.addEventListener("stop", () => {
        const audioBlob = new Blob(audioChunks, { type: "audio/mpeg-3" });
        console.log(audioBlob);
        sendAudioFile(audioBlob).then((ID) => {
          console.log(ID);
          if (ID === "") {
            window.location.href = "/error/";
          } else {
            window.location.href = `/music/${ID}`;
          }
        });
      });

      setTimeout(() => {
        mediaRecorder.stop();
      }, 5000);
    });
}

document.querySelector("#record").classList.add("notRec");

document.querySelector("#record").addEventListener("click", (e) => {
  if (e.currentTarget.classList.contains("notRec")) {
    e.currentTarget.classList.add("Rec");
  } else {
    e.currentTarget.classList.add("notRec");
  }
});

function hideLyrics() {
  var x = document.getElementById("lyrics");
  var h1 = document.getElementById("h1-lyrics");

  if (x.classList.contains('lyrics-hided')){
    h1.innerText = "Hide Lyrics";
    x.classList.remove("lyrics-hided");
    x.classList.add("lyrics");
  }
  else{
    h1.innerText = "Show Lyrics";
    x.classList.remove("lyrics");
    x.classList.add("lyrics-hided");
  }
}
