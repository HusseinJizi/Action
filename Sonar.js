// Beispiel 1: Unsafe Function Call (eval)
function executeScript(userInput) {
  eval(userInput);  // 🚨 UNSICHER: eval kann beliebigen Code ausführen!
}

// Beispiel 2: Callback-Funktion ohne Fehlerbehandlung
function fetchData(url, callback) {
  fetch(url)
    .then(response => response.json())
    .then(data => callback(data))
    .catch(error => {
      console.log("Fehler aufgetreten!");
    });
}

// Beispiel 3: Non-Strict Mode (Potential Errors)
function addNumbers(a, b) {
  x = a + b;  // 🚨 Fehler: x ist keine deklarierte Variable (keine Verwendung von 'use strict')
  return x;
}

// Beispiel 4: Redundant Code (doppelte Berechnung)
function isEven(number) {
  if (number % 2 === 0) {
    return true;
  }
  return number % 2 === 0;  // 🚨 Redundante Berechnung
}

// Beispiel 5: Global Variable (Potentielle Kollision)
var globalCounter = 0;

function incrementCounter() {
  globalCounter++;  // 🚨 Globale Variable
  return globalCounter;
}

// Beispiel 6: Unsichere Dateipfade
const fs = require('fs');

function readFile(filePath) {
  fs.readFile("/etc/passwd", "utf8", function(err, data) {  // 🚨 Unsicherer Dateipfad
    if (err) throw err;
    console.log(data);
  });
}

// Beispiel 7: Unangemessene Benennung von Variablen
function calculateSquareArea(side) {
  var x = side * side;  // 🚨 Unklarer Name für eine Variable
  return x;
}

// Beispiel 8: Nicht abgefangene Fehler (Asynchrone Fehlerbehandlung fehlt)
function connectDatabase() {
  db.connect((err) => {  // 🚨 Fehlerbehandlung fehlt
    if (err) {
      console.log('Datenbankverbindung fehlgeschlagen!');
    }
  });
}
