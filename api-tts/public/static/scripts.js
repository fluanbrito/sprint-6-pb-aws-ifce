const form = document.querySelector("form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const phrase = formData.get("phrase");
  
  try {
    const response = await axios.post("https://1cqp5koc14.execute-api.us-east-1.amazonaws.com/v1/tts", {
      phrase
    });
    const { received_phrase, url_to_audio, created_audio } = response.data;
    console.log(`Received Phrase: ${received_phrase}`);
    console.log(`URL to Audio: ${url_to_audio}`);
    console.log(`Created Audio: ${created_audio}`);
  } catch (error) {
    console.error(error);
  }
});