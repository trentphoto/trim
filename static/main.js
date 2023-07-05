document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('file-input').addEventListener('change', function(event) {

        // define file reader and file
        var file = event.target.files[0];
        var formData = new FormData();
        formData.append('file', file);
    
        // send file to server endpoint
        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(data => console.log(data))
        .catch(error => console.error(error));
    });
    
    document.getElementById('trim-button').addEventListener('click', function() {

        // get start and end times from user input
        var startTime = document.getElementById('start-time').value;
        var endTime = document.getElementById('end-time').value;
        var filename = document.getElementById('file-input').files[0].name;
        
        // send start and end times to server endpoint
        fetch('/trim', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: `start_time=${startTime}&end_time=${endTime}&filename=${filename}`
        })
        .then(response => response.text())
        .then(data => {
            // Assuming that the trimmed file is named 'trimmed_filename.mp3'
            var trimmedFilename = 'trimmed_' + filename;

            // update download button
            document.getElementById('download-button').href = '/download/' + trimmedFilename;
            document.getElementById('download-button').classList.remove('disabled');

            // update audio player
            document.getElementById('audio-preview').src = '/download/' + trimmedFilename;
        })
        .catch(error => console.error(error));
    });
});
