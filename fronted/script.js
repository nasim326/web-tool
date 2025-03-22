const apiBaseUrl = "https://web-tool-hxjo.onrender.com"; // Replace with your actual Render URL

document.getElementById('uploadForm').onsubmit = async function (e) {
  e.preventDefault();
  const formData = new FormData(this);

  try {
    const response = await fetch(`${apiBaseUrl}/upload`, {
      method: 'POST',
      body: formData,
    });

    const result = await response.json();
    if (response.ok) {
      document.getElementById('message').innerText = result.message;
      document.getElementById('downloadLink').style.display = 'inline';
      document.getElementById('downloadLink').href = `${apiBaseUrl}/download`;
    } else {
      document.getElementById('message').innerText = `Error: ${result.error}`;
    }
  } catch (error) {
    document.getElementById('message').innerText = `Error: ${error.message}`;
  }
};
