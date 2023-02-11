function submitForm(event) {
  event.preventDefault(); // prevent the form from submitting normally
  const phrase = document.getElementById("input").value;
  const payload = {
    phrase: phrase
  };
  console.log(payload)
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "https://122k881h56.execute-api.us-east-1.amazonaws.com/v1/tts");
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(JSON.stringify(payload));
}