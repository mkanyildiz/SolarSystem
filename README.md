A07 - VISIT OUR SOLAR SYSTEM ...

Wir wollen nun unser Wissen aus Medientechnik und SEW nützen um eine etwas kreativere Applikation zu erstellen.

Eine wichtige Library zur Erstellung von Games mit 3D-Grafik ist Pygame. Die 3D-Unterstützung wird mittels PyOpenGL erreicht.

Die Kombination ermöglicht eine einfache und schnelle Entwicklung.

Während pygame sich um Fensteraufbau, Kollisionen und Events kümmert, sind grafische Objekte mittel OpenGL möglich.


Die Aufgabenstellung:

Erstellen Sie eine einfache Animation unseres Sonnensystems.


In einem Team (2) sind folgende Anforderungen zu erfüllen.
-Ein zentraler Stern
-Zumindest 2 Planeten, die sich um die eigene Achse und in elliptischen Bahnen um den Zentralstern drehen
-Ein Planet hat zumindest einen Mond, der sich zusätzlich um seinen Planeten bewegt
-Kreativität ist gefragt: Weitere Planeten, Asteroiden, Galaxien,...
-Zumindest ein Planet wird mit einer Textur belegt (Erde, Mars,... sind im Netz verfügbar)

Events:
-Mittels Maus kann die Kameraposition angepasst werden: Zumindest eine Überkopf-Sicht und parallel der Planentenbahnen
-Da es sich um eine Animation handelt, kann diese auch gestoppt werden. Mittels Tasten kann die Geschwindigkeit gedrosselt und beschleunigt werden.
-Mittels Mausklick kann eine Punktlichtquelle und die Textierung ein- und ausgeschaltet werden.
-Schatten: Auch Monde und Planeten werfen Schatten.

Hinweise:
-Ein Objekt kann einfach mittels glutSolidSphere() erstellt werden.
-Die Planten werden mittels Modelkommandos bewegt: glRotate(), glTranslate()
-Die Kameraposition wird mittels gluLookAt() gesetzt
-Bedenken Sie bei der Perspektive, dass entfernte Objekte kleiner - nahe entsprechende größer darzustellen sind.
-Wichtig ist dabei auch eine möglichst glaubhafte Darstellung. gluPerspective(), glFrustum()
-Für das Einbetten einer Textur wird die Library Pillow benötigt! Die Community unterstützt Sie bei der Verwendung.

Tutorials:
Pygame: https://www.youtube.com/watch?v=K5F-aGDIYaM
Viel Erfolg!

Team: 
- Dorfinger
- Maran


a) Gruppenbildung (Dorfinger & Maran)

b) Anforderungenanalyse (Text -> funktionale Anforderungen, -> nicht funktionale Andorferungen
 b.1) tabellarische Auflistung
 b.2) Rücksprache mit Auftraggeber (=Wimberger & Brein)

c) Designüberlegung (UML, Sequenzdiagramm)
 c.1) Prototyp
 c.2) SW-Design
 c.3) GUI-Design (Prototypen auf Papier)
 c.4) Rücksprache mit Auftraggeber
 c.5) UAT-Überlegung (User Acceptance Test)
 
d) Implementierung + Tests (Code Reviews)

e) Abgabemoludaritäten klären und Abgabe

Momentaner Abgabetermin: 30.03.2015 22:00 Uhr
