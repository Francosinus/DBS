<!doctype html>

<?php
	// including FusionCharts PHP wrapper
	include("fusioncharts.php");
	// Datenban Connection herstellen
	$host= "host=localhost";
	$port= "port=5432";
	$dbname="dbname=Election";
	$dbuser="user=postgres";
	$dbpwd="password=postgres";
  $dbconn=pg_connect("$host $port $dbname $dbuser $dbpwd");
  if(!$dbconn) {
		exit("Verbindung konnte nicht hergestellt werden");
	}
?>

<html>
   <head>
      <title>Barchart</title>

      <!-- Stil und Schriftart einfügen -->
      <link href='https://fonts.googleapis.com/css?family=Merriweather:300' rel='stylesheet' type='text/css'>
      <style>
      	* {
      		margin: 0;
      		padding: 0;
      		background-color: #FAF6F3;
      	}
      </style>

      <!-- FusionCharts Pakete -->
      <script src="https://static.fusioncharts.com/code/latest/fusioncharts.js"></script>
      <script src="https://static.fusioncharts.com/code/latest/fusioncharts.charts.js"></script>
      <script src="https://static.fusioncharts.com/code/latest/themes/fusioncharts.theme.fint.js"></script>
   </head>
   <body>

<?php
  $result = pg_query($dbconn, "select count(anzahl), date(time) from hashtags, tweets,contains where t_id=id1 and h_id=id2 group by date(time) order by date(time) asc;") or exit("Error with quering database");
  
  if ($result) {
  // Array erstellen um Attribute zu speichern
	$arrData = array(
	
        "chart" => array(
          	// Titel 
            "caption"=> "Hashtags im Laufe der Zeit",
          	"captionFontSize"=> "24",
            "captionFontColor"=> "#4D394B",
            // Schriftgröße, Farbe
            "baseFontColor"=> "#ABA39D",
            "outCnvBaseColor"=> "#ABA39D",
            "baseFontSize"=> "15",
            "outCnvBaseFontSize"=> "15",
            // Linien
            "divLineColor"=> "#ABA39D",
            // Y-Achse
            "yAxisMinValue"=> "0",
            "yAxisMaxValue"=> "100",

            "theme"=> "fint",
            "paletteColors"=> "#7B5A85",
            "showBorder"=> "0",
      			"bgColor"=> "#FAF6F3",
            "canvasBgColor"=> "#FAF6F3",
            "bgAlpha"=> "100",
            "showValues"=> "0",
            "formatNumberScale"=> "0",
            "plotSpacePercent"=> "33",
          )
    );
    
    $arrData["data"] = array();
	// Daten in $arrData Array packen
	while($row = pg_fetch_array($result)) {
		array_push($arrData["data"], array(
			"label" => $row["date"],
			"value" => $row["count"]
			)
		);
	}
  $jsonEncodedData = json_encode($arrData);
	// FusionCharts erstellen
	$postgresChart = new FusionCharts"HashtagsChart" , '100%', '450', "postgres-chart", "json", $jsonEncodedData);

  $postgresChart->render();
	// Datenbank Verbindung schließen
  pg_close($dbconn);
  }
?>
 	<!-- chart container erstellen -->
 	<center><div id="postgres-chart">Es folgt ein Barchart der die Anzahl von Hashtags im Laufe der Zeit anzeigt</div></center>
   </body>
</html>

