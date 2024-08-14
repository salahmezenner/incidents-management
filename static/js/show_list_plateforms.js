document.addEventListener("DOMContentLoaded", function() {
    var sidebar = document.getElementById('sidebar');
    sidebar.addEventListener('mouseenter', expandSidebar);
    sidebar.addEventListener('mouseleave', collapseSidebar);

    var profileText = document.getElementById('profilename');
    profileText.addEventListener('mouseenter', function() {
        profileText.style.fontWeight = 'bold';
        profileText.style.fontSize = '12px';
    });
    profileText.addEventListener('mouseleave', function() {
        profileText.style.fontWeight = 'bold';
        profileText.style.fontSize = '14px';
    });

    var links = document.querySelectorAll('.sidebar-link');
    links.forEach(function(link) {
        link.addEventListener('mouseenter', function() {
            link.style.fontSize = '15px';  
            link.style.fontWeight = 'bold'; 
        });
        link.addEventListener('mouseleave', function() {
            link.style.fontWeight = 'normal';
            link.style.fontSize = '15px'; 
        });
    });
});

function expandSidebar() {
    var sidebar = document.getElementById('sidebar');
    sidebar.style.width = '220px';
    document.querySelector('.sidebar-expanded').style.display = 'block';
}

function collapseSidebar() {
    var sidebar = document.getElementById('sidebar');
    sidebar.style.width = '100px';
    document.querySelector('.sidebar-expanded').style.display = 'none';
}

