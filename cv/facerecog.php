<!DOCTYPE html>
<html>
<head>
<title>Pengenalan Wajah</title>
<script src="jquery.min.js"></script>
</head>
<body>
<input type="text" class="nama" size="50">
<button type="button" class="simpan">Simpan</button>
<button type="button" class="test">Test</button>
<div class="result"></div>
<script>
  $(".simpan").click(function(){
    $.get("http://<?php echo $_SERVER['SERVER_ADDR']; ?>/cgi-bin/facerecog.py",{jepret:"simpan",nama:$(".nama").val()}).done(function(data){
      $(".result").html(data);
    });
  });
  $(".test").click(function(){
    $.get("http://<?php echo $_SERVER['SERVER_ADDR']; ?>/cgi-bin/facerecog.py",{jepret:"test"}).done(function(data){
      $(".result").html(data);
    });
  });
</script>
</body>
</html>
