<!DOCTYPE html>
<html>
<head>
<script src="jquery.min.js"></script>
</head>
<body>

<h3>Mau foto berapa kali?</h3>
<input type="text" class="ketik" value="3" size="4">
<button class="tombol">Klik disini</button>
<div class="result"></div>
<script>
  $(".tombol").click(function(){
    $.get("http://<?php echo $_SERVER['SERVER_ADDR']; ?>/cgi-bin/cameraform.py",{jepret:$(".ketik").val()}).done(function(data){
      $(".result").html(data);
    });
  });
</script>
</body>
</html>
