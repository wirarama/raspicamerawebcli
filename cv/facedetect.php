<!DOCTYPE html>
<html>
<head>
<title>Deteksi Wajah</title>
<script src="jquery.min.js"></script>
</head>
<body>

<h3>Deteksi wajah</h3>
<button class="tombol">Klik sini</button>
<div class="result"></div>
<script>
  $(".tombol").click(function(){
    $.get("http://<?php echo $_SERVER['SERVER_ADDR']; ?>/cgi-bin/violapi.py",{jepret:1}).done(function(data){
      $(".result").html(data);
    });
  });
</script>
</body>
</html>
