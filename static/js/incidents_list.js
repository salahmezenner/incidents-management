document.addEventListener('DOMContentLoaded', function() {
    var searchInput = document.getElementById('rechinput');
    var startDateInput = document.getElementById('startDate');
    var endDateInput = document.getElementById('endDate');
    var userFilter = document.getElementById('userFilter');
    var platformFilter = document.getElementById('platformFilter');

    // Add event listeners for input events on filter elements
    [searchInput, startDateInput, endDateInput, userFilter, platformFilter].forEach(function(element) {
        element.addEventListener('input', filterIncidents);
    });

    function filterIncidents() {
        var searchValue = searchInput.value.toLowerCase().trim();
        var startDateString = startDateInput.value;
        var endDateString = endDateInput.value;
        var userValue = userFilter.value.toLowerCase().trim();
        var platformValue = "platforme: "+ platformFilter.value.toLowerCase().trim();

    
        var startDateValue = new Date(startDateString);
        var endDateValue = new Date(endDateString);
    
        var cards = document.querySelectorAll('.card');
    
        cards.forEach(function(card) {
            var intitule = card.querySelector('h4').textContent.toLowerCase();
            var user = card.querySelector('.user-info h5').textContent.toLowerCase();
            var platform = card.querySelector('.tag').textContent.toLowerCase();
            var dateString = card.querySelector('.user small').textContent;
            var date = parseDateString(dateString)
            var date1 = new Date(date)
    
            var showCard = true;
    
            if (searchValue && !intitule.includes(searchValue)) {
                showCard = false;
            }
    
            if (!isNaN(startDateValue) && !isNaN(endDateValue)) {
                if (date < startDateValue || date > endDateValue) {
                    showCard = false;
                }
            }
    
            if (userValue && user !== userValue) {
                showCard = false;
            }
    
            if (platformValue && platform !== platformValue) {
                showCard = false;
            }
    
            if (showCard) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }    

    function parseDateString(dateString) {
        // Split the date string into components
        var parts = dateString.split(/[\s,]+/);
        
        // Get the month, day, year, and time from the parts
        var month = parts[0];
        var day = parseInt(parts[1], 10);
        var year = parseInt(parts[2], 10);
        var time = parts[3];
    

        // Convert 12-hour time to 24-hour time
        var hour = parseInt(time);
        if (time.toLowerCase().indexOf('p') !== -1 && hour !== 12) {
            hour += 12;
        }

    
        // Convert month name to month number
        var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        var monthNumber = months.indexOf(month.substring(0, 3)); // Ensure the month name matches the format in the array
    
    
        // Create a new Date object
        var date = new Date(year, monthNumber, day, hour);
    
        return date;
    }
    
    
});

$(document).ready(function(){

    $('.input-daterange').datepicker({
        format: 'dd-mm-yyyy',
        autoclose: true,
        calendarWeeks : true,
        clearBtn: true,
        disableTouchKeyboard: true
    });
    
    });