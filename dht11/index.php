<!DOCTYPE html>
<html>
<head>
<script src="jquery.min.js"></script>
</head>
<body>

<h3>DHT11</h3>
<div class="result"></div>
<script>
$(function() {
    startRefresh();
});
function startRefresh() {
    setTimeout(startRefresh,1000);
    $.get('view.php', function(data) {
        $('.result').html(data);    
    });
}
</script>
</body>
</html>
