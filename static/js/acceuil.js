$(document).ready(function() {
    $('form').submit(function(e) {
        e.preventDefault();

        
        var email = $('input[name="email"]').val();
        var password = $('input[name="password"]').val();

       
        if (email === "") {
            $('.error-message').text("Entrez votre email").show(); 
        } else {
            $('.error-message').hide(); 
        }
    });
});
