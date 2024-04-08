// Add event listener to detect scroll
window.addEventListener('scroll', function() {
    // Get the scroll position
    var scrollPosition = window.scrollY;

    // Select the animated line element
    var animatedLine = document.querySelector('.animated-line');

    // Add or remove glowing class based on scroll position
    if (scrollPosition > 100) { // Adjust the scroll position threshold as needed
        animatedLine.classList.add('glowing');
    } else {
        animatedLine.classList.remove('glowing');
    }
});

$(document).ready(function() {
    $('#extract_button').click(function(event) {
        event.preventDefault();

        var formData = new FormData();
        formData.append('image', $('#image_input')[0].files[0]);

        $.ajax({
            url: '/upload',
            type: 'POST',
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) {
                // Update the text container with the extracted text
                $('#extracted-text').val(response.extracted_text);

                // Update the image container with the uploaded image
                $('#image-container').html('<img src="data:image/jpeg;base64,' + response.image + '" alt="Uploaded Image">');
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
            }
        });
    });
});


