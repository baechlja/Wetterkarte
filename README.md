# Wetterkarte

# Schritt 1: Daten der Wetterstationen holen
  
Zuerst installieren wir mit "pip" Folium Request im terminal, das geht mit Windows so:
```pip install folium requests```
und mit MacOs und Linux so:
```sudo pip3 install folium requests```
# Schritt 2: Importieren

Wir importieren *get*, *json*, *foilum*, *os*, *webbrowser* und *html*.

Mit *JSON*  verarbeiten wir JSON-Daten aus der Datenbank 
*Folium* visualisiert Karten in Python
*os* findet das CWD (current Working Dictionary).
Das sorgt dafür, dass das Programm weiß wo es die gespeicherte Datei laden soll

# Schritt 3: URL verwenden

* wir speichern die url "https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getalllastmeasurement" in einer variabel.

* Wir verwenden die url um die JSON-Daten abzurufen:
```stations_data=get(url).json()```

# Schritt 4: Ein Farbschema für maximale und minimale Temperaturen festlegen

* Wir erstellen zuerst Listen um die Temperaturen(max und min), die Längen- und Breitengrade, sowie die Namen der Wettterstationen darzustellen:

```temps = []```
```tmax = 0.0```
```tmin = 100.0```

```lons = [data['weather_stn_long'] for data in station_data['items']] ```

```lats = [data['weather_stn_lat'] for data in station_data['items']]```

```wsnames = [html.escape(station['weather_stn_name']) for station in station_data['items']] ```

* Dann prüfen wir ob die Temperturen sich alle im normalen Rahmen befinden, also zwischen -30 °C und 50 °C, wenn diese abweichen setzen wir sie auf einen durchschnittlichen     Wert von 20 °C

* Danach schreiben wir direkt unter unsere Imports eine Funktion, die festlegt, dass die Station mit der kältestem Temperatur Blau ist, die mit der wärmsten rot und die         mittleren sollen grün sein.
  Rot, Grün und Blau sind hexadezimal übertragen um es mit dem FoliumMarker anwenden zu können

# Schritt 5:  Die Kate erstellen und Wetterstationen hinzufügen

* Zuerst erstellen wir unsere map:

```map_ws = folium.Map(location = [47,7], zoom_start=6)```

Wir setzen Lörrach (47 N, 7 E) als das Mittelpunkt.

* Dann fügen wir die Wetterstationen hinzu:

```for n in range(len(lons)-1):```
   ```hcol = colourgrad(tmin, tmax, float(temps[n]))```
   ```folium.CircleMarker([lats[n], lons[n]],```
                ```radius = 5,```
                ```popup = wsnames[n]+':'+temps[n],```
                ```fill_color = hcol).add_to(map_ws)```
                
# Schritt 6: Datei speichern und den Webbrowser öffnen

* Wir benuten *os* um das CWD in einer Variablen abzuspeichern.

```CWD = os.getcwd()```

* Dann können wir die neue Karte speichern.

```map_ws.save("wetterkarte.html")```

* Und den Browser öffnen.

```webbrowser.open_new_tab('file://'+CWD+'/'+'wetterkarte.html')```

                
