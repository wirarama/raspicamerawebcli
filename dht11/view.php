<?php
$c = new mysqli("localhost","dht11","dht11","dht11");
$r = $c->query("SELECT * FROM dht11 ORDER BY date DESC");
while($d = $r->fetch_assoc()) {
	echo $d['date'].' '.$d['temperature'].' '.$d['humidity'].'<br>';
}
$conn->close();
?>
