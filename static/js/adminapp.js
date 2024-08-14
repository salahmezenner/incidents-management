document.addEventListener("DOMContentLoaded", function() {
    var sidebar = document.getElementById('sidebar');
    sidebar.addEventListener('mouseenter', expandSidebar);
    sidebar.addEventListener('mouseleave', collapseSidebar);
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

  var profileText = document.getElementById('profilename');
  var links = document.querySelectorAll('.sidebar-link');

  profileText.addEventListener('mouseenter', function() {
    profileText.style.fontWeight = 'bold';
    profileText.style.fontSize = '14px'; 
  });

  profileText.addEventListener('mouseleave', function() {
    profileText.style.fontWeight = 'bold';
    profileText.style.fontSize = '11px'; 
  });

  links.forEach(function(link) {
    link.addEventListener('mouseenter', function() {
 
      link.style.fontSize = '16px';  
      link.style.fontWeight = 'bold';
      
    });

    link.addEventListener('mouseleave', function() {
      link.style.fontWeight = 'normal';
      link.style.fontSize = '15px'; 
    });
  });
