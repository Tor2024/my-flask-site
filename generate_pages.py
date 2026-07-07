# -*- coding: utf-8 -*-
import json
import os

json_raw = r'''
[
    {
        "slug": "wartung", "title": "Wartung",
        "subtitle": "Regelm\u00e4ssige Wartung nach Herstellervorgaben",
        "meta": "Regelm\u00e4ssige Wartung, \u00d6lwechsel, Inspektion und Systemchecks f\u00fcr alle Fahrzeugmarken in Kreuztal.",
        "hero_img": "static/images/wartung1.png",
        "hero_icon": "ri-settings-3-line",
        "intro": "Regelm\u00e4ssige Wartung ist die beste Investition in die Langlebigkeit Ihres Fahrzeugs. Wir f\u00fchren Wartungsarbeiten nach Herstellervorgaben durch \u2013 von \u00d6lwechsel und Filterwechsel bis zur vollst\u00e4ndigen Inspektion mit Systemcheck aller sicherheitsrelevanten Komponenten.",
        "process": [
            ["Annahme & Bedarfsermittlung", "Wir besprechen mit Ihnen den Wartungsbedarf, pr\u00fcfen das Scheckheft, beraten zu f\u00e4lligen Arbeiten und erstellen einen transparenten Kostenvoranschlag.", "ri-service-line"],
            ["Durchf\u00fchrung der Wartung", "Nach Ihrem Okay f\u00fchren wir alle anstehenden Arbeiten durch, verwenden ausschliesslich Marken-\u00d6le und Qualit\u00e4tsteile. Jeder Schritt wird im System dokumentiert.", "ri-tools-fill"],
            ["Qualit\u00e4tskontrolle & Scheckhefteintrag", "Nach der Wartung erfolgt eine Probefahrt und ein finaler Systemcheck. Sie erhalten Ihren Scheckhefteintrag und eine Dokumentation aller durchgef\u00fchrten Arbeiten.", "ri-check-double-line"]
        ],
        "sections": [
            ["\u00d6lwechsel & Filterwechsel", "Der \u00d6lwechsel ist die h\u00e4ufigste Wartungsarbeit und entscheidend f\u00fcr die Motorlebensdauer. Wir verwenden ausschliesslich hochwertige Marken\u00f6le ((5W30, 5W40, 0W20)) passend zur Herstellervorgabe. Motor\u00f6l, Luftfilter, Innenraumfilter, Kraftstofffilter und \u00d6lfilter werden bei jedem Service gepr\u00fcft und bei Bedarf ersetzt."],
            ["Inspektion nach Herstellervorgaben", "Jeder Hersteller definiert feste Inspektionsintervalle und -umf\u00e4nge. Wir f\u00fchren Inspektionen nach den Vorgaben von VW, Mercedes, BMW, Audi, Opel, Ford, Toyota und allen anderen Marken durch. Inklusive Scheckhefteintrag und Plakette."],
            ["Systemcheck & Fahrzeugdiagnose", "Moderne Fahrzeuge verf\u00fcgen \u00fcber vernetzte Steuerger\u00e4te, die permanent Daten erfassen. Bei der Wartung lesen wir alle Systeme aus, pr\u00fcfen Fehlerspeicher und f\u00fchren einen vollst\u00e4ndigen Systemcheck durch \u2013 von der Motorsteuerung bis zu den Assistenzsystemen."],
            ["Rundum-Sorglos-Paket", "Unser Wartungspaket umfasst neben \u00d6lwechsel und Filtern auch die Pr\u00fcfung von Bremsen, Reifen, Beleuchtung, Fahrwerk, Klimaanlage und eine Sichtpr\u00fcfung der Abgasanlage. So verlassen Sie die Werkstatt mit dem guten Gef\u00fchl, rundum versorgt zu sein."]
        ],
        "benefits": [
            "Herstellervorgaben werden exakt eingehalten \u2013 Garantieerhalt",
            "Hochwertige Marken\u00f6le und Originalteile",
            "Vorab Besprechung aller Arbeiten \u2013 kein \u00dcberraschungseffekt",
            "Scheckhefteintrag und vollst\u00e4ndige Dokumentation",
            "Hol- und Bringservice im Stadtgebiet inklusive",
            "Termin innerhalb von 48 Stunden garantiert"
        ],
        "faq": [
            ["Wie oft muss mein Fahrzeug zur Wartung?", "Die Intervalle sind herstellerabh\u00e4ngig. Moderne Fahrzeuge haben oft eine variable Serviceanzeige (LongLife-Service bis 30.000 km oder 2 Jahre). Wir empfehlen: mindestens 1x j\u00e4hrlich oder alle 15.000 km."],
            ["Welche Arbeiten umfasst eine Inspektion?", "Eine kleine Inspektion umfasst \u00d6lwechsel und Filterwechsel. Die grosse Inspektion zus\u00e4tzlich Z\u00fcndkerzen, Luftfilter, Innenraumfilter und Kraftstofffilter. Sie erhalten vorab eine detaillierte Aufstellung aller Arbeiten."],
            ["Kann ich \u00d6l selbst mitbringen?", "Gerne \u2013 wir verwenden dann Ihr mitgebrachtes \u00d6l. Wir empfehlen jedoch unsere Marken\u00f6le, da wir nur gepr\u00fcfte und freigegebene Qualit\u00e4ten verwenden und keine Garantie f\u00fcr Fremd\u00f6le \u00fcbernehmen k\u00f6nnen."],
            ["Was ist der Unterschied zwischen kleiner und grosser Inspektion?", "Die kleine Inspektion umfasst \u00d6lwechsel, Filterwechsel und Sichtpr\u00fcfung. Die grosse Inspektion zus\u00e4tzlich Z\u00fcndkerzen, Luftfilter, Innenraumfilter, Kraftstofffilter und eine erweiterte Systemdiagnose."],
            ["Wird der Service im Scheckheft eingetragen?", "Ja, jede Wartung wird von uns im Scheckheft dokumentiert und mit unserem Werkstattstempel best\u00e4tigt. Auch bei digitalem Serviceheft (z.B. Mercedes, BMW) tragen wir elektronisch ein."]
        ],
        "cta": "F\u00e4llt bald eine Inspektion an oder leuchtet die Serviceanzeige? Vereinbaren Sie jetzt einen Wartungstermin."
    },
    {
        "slug": "unfallreparatur", "title": "Unfallreparatur",
        "subtitle": "Fachgerechte Reparatur aller Unfallsch\u00e4den \u2013 wir stellen die Optik und Sicherheit Ihres Fahrzeugs wieder her.",
        "meta": "Unfallreparatur in Kreuztal: Karosserie, Lackierung, Richtbank, 3D-Vermessung. Unfallinstandsetzung aller Marken. Schnelle und fachgerechte Reparatur.",
        "hero_img": "static/images/Unfallreparatur1.png",
        "hero_icon": "ri-car-washing-line",
        "intro": "Ein Unfall ist immer ein Schock. Wir helfen Ihnen, schnell wieder mobil zu sein. Von der Schadensbegutachtung \u00fcber die Abwicklung mit der Versicherung bis zur fachgerechten Reparatur \u2013 wir begleiten Sie durch den gesamten Prozess. Unfallsch\u00e4den aller Art werden bei uns fachgerecht instandgesetzt.",
        "process": [
            ["Schadensaufnahme & Gutachten", "Wir dokumentieren den Schaden, erstellen das Gutachten oder korrespondieren mit dem Gutachter Ihrer Versicherung. \u00dcbernahme des Gutachtens und der Reparaturplanung.", "ri-file-list-3-line"],
            ["Reparatur & Instandsetzung", "Richtbank, 3D-Vermessung, Karosseriearbeiten, Lackierung \u2013 alles in einer Hand. Wir arbeiten nach Herstellervorgaben und gew\u00e4hrleisten Werksqualit\u00e4t.", "ri-tools-fill"],
            ["Qualit\u00e4tssicherung & \u00dcbergabe", "Nach der Reparatur durchl\u00e4uft Ihr Fahrzeug eine mehrstufige Qualit\u00e4tskontrolle. Sie erhalten ein \u00dcbergabeprotokoll mit allen durchgef\u00fchrten Arbeiten.", "ri-check-double-line"]
        ],
        "sections": [
            ["Karosserieinstandsetzung auf dem Richtbank", "Unsere computergesteuerte Richtbank erm\u00f6glicht millimetergenaue Vermessung und Instandsetzung der Karosserie. Wir richten Ihr Fahrzeug wieder in die urspr\u00fcngliche Form \u2013 nach Herstellervorgaben und mit modernster 3D-Messtechnik."],
            ["Lackierung in Profi-Qualit\u00e4t", "In unserer beheizten Lackierkabine werden Reparaturlackierungen farbtongetreu ausgef\u00fchrt. Der Farbton wird elektronisch ermittelt und exakt angemischt. Ob Einzelteillackierung oder Komplettlackierung \u2013 wir liefern OEM-Qualit\u00e4t."],
            ["Versicherungsabwicklung \u2013 wir k\u00fcmmern uns", "Sie m\u00fcssen sich um nichts k\u00fcmmern. Wir kommunizieren direkt mit Ihrer Versicherung, kl\u00e4ren die Kosten\u00fcbernahme und k\u00fcmmern uns um den Mietwagen. Sie holen Ihr repariertes Fahrzeug einfach wieder ab."],
            ["Ersatzteilbeschaffung & Originalteile", "Wir verwenden ausschliesslich Originalteile oder zertifizierte Qualit\u00e4tsteile. Die Beschaffung erfolgt \u00fcber unsere Partner \u2013 schnell und verl\u00e4sslich. Auch bei seltenen Modellen haben wir Zugriff auf das europ\u00e4ische Teile-Netzwerk."]
        ],
        "benefits": [
            "Alles aus einer Hand \u2013 Karosserie, Lack, Gutachten",
            "Computergesteuerte Richtbank mit 3D-Vermessung",
            "Direkte Versicherungsabwicklung \u2013 Sie haben keine Arbeit",
            "Mietwagen-Organisation inklusive",
            "Herstellergarantie bleibt erhalten",
            "Schnelle Bearbeitung \u2013 in den meisten F\u00e4llen unter 5 Werktagen"
        ],
        "faq": [
            ["Muss ich mein Fahrzeug vor der Reparatur zur Besichtigung vorlegen?", "Ja \u2013 wir m\u00fcssen den Schaden vor Auftragsbeginn sehen. Manchmal sind versteckte Sch\u00e4den vorhanden, die im Gutachten nicht aufgef\u00fchrt sind. Wir informieren Sie umgehend, falls w\u00e4hrend der Reparatur Zusatzsch\u00e4den entdeckt werden."],
            ["Wie lange dauert eine Unfallreparatur?", "Das h\u00e4ngt vom Schadenumfang ab. Ein Kotfl\u00fcgel-Wechsel inkl. Lackierung: 2\u20133 Tage. Eine gr\u00f6ssere Karosseriereparatur: 5\u201310 Werktage. Wir nennen Ihnen vorab eine realistische Zeitschiene."],
            ["Bekomme ich einen Mietwagen?", "Ja \u2013 wir organisieren einen Mietwagen f\u00fcr die Dauer der Reparatur. Die \u00dcbernahme kl\u00e4ren wir direkt mit Ihrer Versicherung. Sie k\u00f6nnen Ihr Fahrzeug bei uns abgeben und den Mietwagen gleich mitnehmen."],
            ["Muss ich in Vorkasse gehen?", "Nein \u2013 bei Unfallreparaturen arbeiten wir direkt mit Ihrer Versicherung zusammen. Sie zahlen nur den vereinbarten Selbstbehalt."],
            ["Bleibt meine Herstellergarantie erhalten?", "Ja \u2013 wir reparieren nach Herstellervorgaben und verwenden Originalteile. Ihre Herstellergarantie bleibt uneingeschr\u00e4nkt erhalten. Wir dokumentieren alle Arbeiten l\u00fcckenlos."]
        ],
        "cta": "Hatten Sie einen Unfall? Keine Panik \u2013 wir k\u00fcmmern uns um alles. Vereinbaren Sie einen Termin zur Schadensaufnahme."
    },
    {
        "slug": "fahrzeugsdiagnose", "title": "Fahrzeugsdiagnose",
        "subtitle": "Computergest\u00fctzte Diagnose aller Fahrzeugsysteme. Schnelle Fehlererkennung und Behebung von St\u00f6rungen.",
        "meta": "Fahrzeugdiagnose in Kreuztal: Fehlerauslese, Steuerger\u00e4te-Diagnose, Systemanalyse f\u00fcr alle Marken. Modernste Diagnosetechnik.",
        "hero_img": "static/images/Fahrzeugsdiagnose1.png",
        "hero_icon": "ri-radar-line",
        "intro": "Wenn die Motorkontrollleuchte leuchtet, das Fahrzeug ruckelt oder ungew\u00f6hnliche Ger\u00e4usche macht, hilft nur eine professionelle Diagnose. Mit modernster Diagnosetechnik lesen wir alle Steuerger\u00e4te aus, analysieren Fehlercodes und finden die Ursache zuverl\u00e4ssig.",
        "process": [
            ["Fehlerauslese & Systemanalyse", "Wir schliessen unsere herstellerspezifische Diagnose an Ihr Fahrzeug an und lesen alle Steuerger\u00e4te aus. Fehlercodes werden dokumentiert und analysiert.", "ri-radar-line"],
            ["Gezielte Fehlersuche", "Ein Fehlercode allein sagt nicht immer, wo der Fehler liegt. Wir f\u00fchren gezielte Tests durch, messen Sensoren und Aktoren und grenzen die Ursache Schritt f\u00fcr Schritt ein.", "ri-search-eye-line"],
            ["Reparatur & Fehlerl\u00f6schung", "Nach der Fehlerbehebung wird der Fehlerspeicher gel\u00f6scht und eine erneute Systempr\u00fcfung durchgef\u00fchrt. Erst wenn keine Fehler mehr auftreten, ist die Diagnose abgeschlossen.", "ri-check-double-line"]
        ],
        "sections": [
            ["Motorsteuerung & Abgasdiagnose", "Von der Lambdasonde \u00fcber den Katalysator bis zum Dieselpartikelfilter \u2013 wir analysieren die gesamte Antriebsstrang-Elektronik. Typische Fehler: Gemischbildung, Z\u00fcndaussetzer, Ladedruckprobleme, AGR-Ventil, Partikelfilter-Regeneration."],
            ["Fahrwerk & Lenkungsdiagnose", "Elektronische Fahrwerke, adaptive D\u00e4mpfer, Lenkwinkelsensor, ESP-Systeme \u2013 moderne Fahrwerke sind vernetzte Systeme. Wir lesen Sensorwerte aus, pr\u00fcfen Stellglieder und kalibrieren Systeme nach Reparaturen."],
            ["Komfort- & Karosserieelektronik", "Standheizung, Sitzheizung, Zentralverriegelung, Fensterheber, Schiebedach \u2013 viele Komfortfunktionen werden \u00fcber Steuerger\u00e4te gesteuert. Wir diagnostizieren und beheben Fehler an der gesamten Karosserieelektronik."],
            ["Diagnose von Assistenzsystemen", "ACC, Spurhalteassistent, Notbremsassistent, Parkpiepser, Kamerasysteme \u2013 Fahrerassistenzsysteme sind komplex und erfordern spezielle Diagnose. Wir pr\u00fcfen Sensoren, Kalibrierung und Systemkommunikation."]
        ],
        "benefits": [
            "Herstellerspezifische Diagnose f\u00fcr alle Marken",
            "Schnelle und pr\u00e4zise Fehlerlokalisierung",
            "Komplette Systemanalyse inkl. Fehlerspeicher",
            "Diagnose aller Steuerger\u00e4te (Motor, Getriebe, Fahrwerk, Komfort)",
            "Sensor- und Aktor-Tests",
            "Ausdruck des Diagnoseergebnisses inklusive"
        ],
        "faq": [
            ["Wann sollte ich eine Fahrzeugdiagnose durchf\u00fchren lassen?", "Sobald die Motorkontrollleuchte aufleuchtet, das Fahrverhalten sich \u00e4ndert (Leistungsverlust, Ruckeln, unruhiger Lauf) oder elektronische Systeme (ABS, ESP, Airbag) Fehler melden. Auch als Vorsorge vor der HU empfehlenswert."],
            ["Kann ich trotz leuchtender Motorkontrollleuchte weiterfahren?", "Kommt auf die Farbe an. Gelb: Sie k\u00f6nnen weiterfahren, sollten aber bald in die Werkstatt. Rot oder Blinken: Sofort anhalten und abschleppen lassen \u2013 es droht ein Motorschaden."],
            ["Lesen Sie auch Fehler bei Elektro- und Hybridfahrzeugen aus?", "Ja \u2013 unsere Diagnoseger\u00e4te sind f\u00fcr alle Antriebsarten ausgelegt, inklusive Hochvoltsystemen."],
            ["Wird der Fehlerspeicher nach der Reparatur gel\u00f6scht?", "Ja \u2013 nach erfolgreicher Reparatur werden alle Fehlercodes gel\u00f6scht und eine erneute Systempr\u00fcfung durchgef\u00fchrt."],
            ["Was passiert, wenn der Fehler nicht gefunden wird?", "Sollte der Fehler trotz Diagnose nicht eindeutig lokalisierbar sein, berechnen wir nur die Zeit f\u00fcr die durchgef\u00fchrten Pr\u00fcfungen \u2013 wir lassen Sie nicht mit einer offenen Rechnung und ungel\u00f6stem Problem gehen."]
        ],
        "cta": "Leuchtet eine Kontrollleuchte oder macht Ihr Fahrzeug Ger\u00e4usche? Vereinbaren Sie eine Diagnose."
    },
    {
        "slug": "motorreparatur", "title": "Motorreparatur",
        "subtitle": "Fachm\u00e4nnische Reparatur und Wartung aller Motortypen \u2013 vom Dichtungswechsel bis zur Komplett\u00fcberholung.",
        "meta": "Motorreparatur in Kreuztal: Zylinderkopf, Steuerkette, Turbolader, \u00d6lverlust, Komplett\u00fcberholung. Reparatur aller Motortypen.",
        "hero_img": "static/images/Motorreparatur1.png",
        "hero_icon": "ri-engine-line",
        "intro": "Der Motor ist das Herz Ihres Fahrzeugs. Ob \u00d6lverlust, Leistungseinbussen, unruhiger Lauf oder ein ernster Motorschaden \u2013 wir diagnostizieren und reparieren Motoren aller Hersteller und Bauarten fachgerecht und nach Herstellervorgaben.",
        "process": [
            ["Motordiagnose & Kompressionstest", "Wir f\u00fchren eine umfassende Motordiagnose durch inklusive Kompressionstest, Dichtheitspr\u00fcfung, Endoskopie und \u00d6ldruckmessung. So finden wir die genaue Ursache.", "ri-stethoscope-line"],
            ["Reparatur & Instandsetzung", "Ob Zylinderkopfdichtung, Steuerkette, Turbolader oder Kolbenringe \u2013 unsere Techniker f\u00fchren die Reparatur fachgerecht durch. Bei Bedarf arbeiten wir mit spezialisierten Motoren-Instandsetzern zusammen.", "ri-tools-fill"],
            ["Funktionspr\u00fcfung & Probefahrt", "Nach der Reparatur: \u00d6ldruckkontrolle, Dichtheitspr\u00fcfung, Probefahrt und erneute Diagnose. Erst wenn alle Werte im Sollbereich liegen, wird das Fahrzeug ausgeliefert.", "ri-check-double-line"]
        ],
        "sections": [
            ["Zylinderkopfreparatur & Dichtungswechsel", "Die Zylinderkopfdichtung ist eine der h\u00e4ufigsten Motorreparaturen. Anzeichen: \u00d6l im K\u00fchlwasser, K\u00fchlwasserverlust, weisser Rauch aus dem Auspuff. Wir tauschen die Dichtung fachgerecht und planen den Zylinderkopf bei Bedarf."],
            ["Steuerkette & Zahnriemen", "Ein Riss der Steuerkette oder des Zahnriemens kann den Motor zerst\u00f6ren. Wir wechseln Steuerketten, Zahnriemen, Spanner und F\u00fchrungsschienen nach Herstellervorgaben. Inklusive Kontrolle der Ventilsteuerzeiten."],
            ["Turbolader-Reparatur & Austausch", "Typische Turboladersch\u00e4den: \u00d6lverlust, pfeifende Ger\u00e4usche, Leistungsverlust. Wir tauschen den Turbolader inklusive \u00d6lversorgung und Reinigung der \u00d6lr\u00fccklaufleitung. Anschliessend erfolgt eine Anpassung der Motorsteuerung."],
            ["Komplett\u00fcberholung & Austauschmotor", "Bei Totalausfall des Motors bieten wir verschiedene Optionen: Instandsetzung des vorhandenen Motors, Austauschmotor mit Garantie oder Gebrauchtmotor von gepr\u00fcften Anbietern. Wir beraten Sie ehrlich, welche L\u00f6sung f\u00fcr Ihr Fahrzeug wirtschaftlich sinnvoll ist."]
        ],
        "benefits": [
            "Fachgerechte Reparatur nach Herstellervorgaben",
            "Modernes Werkzeug und Spezialkenntnisse f\u00fcr alle Marken",
            "Detaillierte Aufstellung aller Arbeiten vor der Reparatur",
            "Gepr\u00fcfte Austauschmotoren mit Garantie",
            "Gerne Reparatur statt Austausch \u2013 wo wirtschaftlich sinnvoll",
            "Gew\u00e4hrleistung auf alle durchgef\u00fchrten Arbeiten"
        ],
        "faq": [
            ["Welche Motorreparaturen f\u00fchren Sie durch?", "Vom Dichtungswechsel \u00fcber Zylinderkopfreparatur bis zur kompletten Motor\u00fcberholung \u2013 wir arbeiten an allen Motortypen. Sie erhalten vorab eine detaillierte Aufstellung aller Arbeiten und eine klare Einsch\u00e4tzung, ob sich die Reparatur lohnt."],
            ["Lohnt sich eine Motorreparatur oder lieber ein Austauschmotor?", "Das h\u00e4ngt vom Fahrzeugwert ab. Bei einem jungen Fahrzeug lohnt sich die Reparatur. Bei \u00e4lteren Fahrzeugen kann ein Austauschmotor wirtschaftlicher sein \u2013 wir beraten Sie ehrlich."],
            ["Wie lange dauert eine Motorreparatur?", "Eine Zylinderkopfdichtung: 2\u20133 Tage. Steuerkette: 1\u20132 Tage. Turbolader: 1\u20132 Tage. Komplett\u00fcberholung: 1\u20132 Wochen. Wir nennen Ihnen vorab die realistische Dauer."],
            ["Erhalte ich Garantie auf die Reparatur?", "Ja \u2013 wir gew\u00e4hren 2 Jahre Garantie auf alle Motorreparaturen (bei fachgerechter Wartung nach Reparatur)."],
            ["Kann ich mein Fahrzeug nach der Reparatur sofort wieder fahren?", "Ja \u2013 nach der Probefahrt und Freigabe k\u00f6nnen Sie sofort losfahren. Wir geben Ihnen Tipps zum Einfahren nach einer Motor\u00fcberholung."]
        ],
        "cta": "Ihr Motor \u00f6lt, klopft oder hat Leistungsverlust? Vereinbaren Sie einen Diagnosetermin \u2013 wir finden die Ursache."
    },
    {
        "slug": "getriebereparatur", "title": "Getriebereparatur",
        "subtitle": "Reparatur und Wartung von Schalt- und Automatikgetrieben. Diagnose und Behebung von Getriebest\u00f6rungen.",
        "meta": "Getriebereparatur in Kreuztal: Schaltgetriebe, Automatikgetriebe, DSG, CVT, Getriebe\u00f6lwechsel. Reparatur aller Getriebetypen.",
        "hero_img": "static/images/Getriebereparatur1.png",
        "hero_icon": "ri-settings-5-line",
        "intro": "Schaltprobleme, Ruckeln beim Gangwechsel, Schleifger\u00e4usche oder ein pl\u00f6tzlicher Gangausfall \u2013 Getriebesch\u00e4den geh\u00f6ren zu den komplexesten Reparaturen am Fahrzeug. Wir diagnostizieren und reparieren Getriebe aller Bauarten fachgerecht und nach Herstellervorgaben.",
        "process": [
            ["Getriebediagnose & Fehleranalyse", "Wir lesen das Getriebesteuerger\u00e4t aus, pr\u00fcfen den \u00d6lzustand und f\u00fchren eine Fahrprobe durch. So ermitteln wir die genaue Ursache \u2013 ob mechanisch, hydraulisch oder elektronisch.", "ri-stethoscope-line"],
            ["Reparatur oder Austausch", "Je nach Schaden entscheiden wir gemeinsam: Instandsetzung des vorhandenen Getriebes oder Einbau eines gepr\u00fcften Austauschgetriebes. Beide Optionen mit Garantie.", "ri-tools-fill"],
            ["Funktionskontrolle & \u00d6lwechsel", "Nach der Reparatur: Getriebe\u00f6lwechsel, Adaption des Steuerger\u00e4ts (bei Automatikgetrieben), ausgiebige Probefahrt und Funktionskontrolle aller G\u00e4nge.", "ri-check-double-line"]
        ],
        "sections": [
            ["Automatikgetriebe & DSG-Reparatur", "Moderne Automatikgetriebe und DSG sind Hightech-Komponenten. H\u00e4ufige Fehler: Ruckeln beim Anfahren, Schaltverz\u00f6gerungen, Notlaufprogramm. Wir tauschen Steuerger\u00e4te, Mechatronik-Einheiten, Kupplungspakete und f\u00fchren Adaptionen durch."],
            ["Schaltgetriebe-Reparatur", "Synchronringe, Lager, Schaltgabeln oder Wellendichtringe \u2013 bei Schaltgetrieben sind h\u00e4ufig mechanische Teile verschlissen. Wir zerlegen und instandsetzen das Getriebe mit Originalteilen."],
            ["Getriebe\u00f6lwechsel \u2013 wichtig f\u00fcr die Lebensdauer", "Viele Hersteller deklarieren Getriebe\u00f6l als \u201elebenslang\u201c, dennoch empfehlen wir einen Wechsel alle 60.000\u201380.000 km. Frisches \u00d6l verhindert Verschleiss und verl\u00e4ngert die Lebensdauer sp\u00fcrbar."],
            ["Austauschgetriebe mit Garantie", "Wenn die Reparatur unwirtschaftlich ist, bieten wir gepr\u00fcfte Austauschgetriebe mit bis zu 3 Jahren Garantie. Einbau inklusive \u00d6lwechsel, Adaption und Probefahrt."]
        ],
        "benefits": [
            "Diagnose und Reparatur aller Getriebetypen",
            "DSG- und Mechatronik-Spezialisten",
            "Getriebe\u00f6lwechsel mit Herstellerfreigabe",
            "Austauschgetriebe mit Garantie",
            "Steuerger\u00e4te-Adaption nach Reparatur",
            "Detaillierte Aufstellung aller Arbeiten vorab"
        ],
        "faq": [
            ["Wann muss ein Getriebe repariert werden?", "Typische Anzeichen: Ruckeln beim Schalten, schleifende Ger\u00e4usche, Gang springt heraus, G\u00e4nge lassen sich schwer einlegen oder das Notlaufprogramm leuchtet auf. Wir f\u00fchren eine Diagnose durch und empfehlen die wirtschaftlichste L\u00f6sung."],
            ["Welche Reparatur ist bei meinem Getriebe n\u00f6tig?", "Das h\u00e4ngt vom Schadensbild ab. Wir empfehlen nach der Diagnose die wirtschaftlichste L\u00f6sung \u2013 ob Getriebe\u00f6lwechsel, Reparatur oder Austauschgetriebe. Sie erhalten vorab eine detaillierte Aufstellung."],
            ["Kann man ein Automatikgetriebe selbst reparieren?", "Nein \u2013 moderne Automatikgetriebe sind hochkomplex und erfordern Spezialwerkzeug, Steuerger\u00e4te-Kenntnisse und Reinraumbedingungen f\u00fcr die Hydraulik."],
            ["Wie lange h\u00e4lt ein Austauschgetriebe?", "Ein gepr\u00fcftes Austauschgetriebe h\u00e4lt bei regelm\u00e4ssigem \u00d6lwechsel genauso lange wie ein Neuteil \u2013 oft 150.000\u2013250.000 km."],
            ["Muss nach dem Getriebeeinbau etwas codiert werden?", "Ja \u2013 bei modernen Fahrzeugen muss das Getriebesteuerger\u00e4t nach dem Einbau angelernt und adaptiert werden. Wir f\u00fchren die Adaption mit unserer Diagnose durch."]
        ],
        "cta": "Schaltet Ihr Getriebe nicht mehr sauber oder h\u00f6ren Sie Ger\u00e4usche? Vereinbaren Sie einen Diagnosetermin."
    },
    {
        "slug": "fahrwerk-aufhaengung", "title": "Fahrwerk & Aufh\u00e4ngung",
        "subtitle": "Reparatur und Austausch von Fahrwerksteilen, Stossd\u00e4mpfern, Lenkung und Stabilisatoren f\u00fcr sicheres Fahrverhalten.",
        "meta": "Fahrwerksreparatur in Kreuztal: Stossd\u00e4mpfer, Federn, Querlenker, Stabilisator, Lenkung, Spur- und Achsvermessung. Fahrwerksinstandsetzung.",
        "hero_img": "static/images/Fahrwerk-Aufhaengung1.png",
        "hero_icon": "ri-steering-2-line",
        "intro": "Ein intaktes Fahrwerk ist die Grundlage f\u00fcr sicheres Fahren, guten Fahrkomfort und eine pr\u00e4zise Strassenlage. Abgefahrene Stossd\u00e4mpfer, ausgeschlagene Gummilager oder eine falsche Spur f\u00fchren nicht nur zu Unbehagen, sondern zu echten Sicherheitsrisiken.",
        "process": [
            ["Fahrwerksdiagnose & Sichtpr\u00fcfung", "Wir pr\u00fcfen Ihr Fahrwerk auf einer Hebeb\u00fchne: Stossd\u00e4mpfer, Federn, Querlenker, Gummilager, Spurstangen, Stabilisatoren. Dazu geh\u00f6rt auch ein Stossd\u00e4mpfer-Test und eine Pr\u00fcfung der Lenkung.", "ri-search-eye-line"],
            ["Reparatur & Austausch", "Verschlissene Teile werden fachgerecht ausgetauscht. Wir verwenden Qualit\u00e4tsteile namhafter Hersteller (Sachs, Bilstein, TRW, Lemf\u00f6rder) und arbeiten nach Herstellervorgaben.", "ri-tools-fill"],
            ["Vermessung & Einstellung", "Nach dem Austausch fahrwerksrelevanter Teile ist eine Achsvermessung Pflicht. Wir vermessen und justieren die Spur, Nachlauf und Sturz \u2013 f\u00fcr perfektes Fahrverhalten und gleichm\u00e4ssigen Reifenverschleiss.", "ri-check-double-line"]
        ],
        "sections": [
            ["Stossd\u00e4mpfer & Federn", "Stossd\u00e4mpfer verschleissen schleichend. Nach 60.000\u201380.000 km ist ein Wechsel ratsam. Anzeichen: Wanken in Kurven, Nachschwingen, verl\u00e4ngerte Bremswege. Wir tauschen D\u00e4mpfer und Federn paarweise aus."],
            ["Querlenker & Gummilager", "Ausgeschlagene Querlenkerlager verursachen Klapperger\u00e4usche und unpr\u00e4zises Lenkverhalten. Wir tauschen komplette Querlenker inklusive Lager oder dr\u00fccken neue Gummilager ein."],
            ["Spur- & Achsvermessung", "Eine falsche Spur f\u00fchrt zu einseitigem Reifenverschleiss und schlechter Strassenlage. Mit unserer 3D-Vermessung (Hella Gutmann) vermessen wir alle Achsen pr\u00e4zise und justieren sie millimetergenau."],
            ["Lenkung & Spurstangen", "Spiel in der Lenkung, ein schwammiges Lenkgef\u00fchl oder Knackger\u00e4usche beim Einlenken deuten auf verschlissene Spurstangen hin. Wir tauschen Spurstangenk\u00f6pfe und stellen die Lenkung ein."]
        ],
        "benefits": [
            "Komplette Fahrwerksdiagnose auf der Hebeb\u00fchne",
            "Qualit\u00e4tsteile von Sachs, Bilstein, TRW, Lemf\u00f6rder",
            "3D-Achsvermessung mit Hella Gutmann-Technik",
            "Paarweiser Austausch f\u00fcr gleichm\u00e4ssiges Fahrverhalten",
            "Verbesserte Strassenlage und Fahrkomfort",
            "Gleichm\u00e4ssiger Reifenverschleiss nach Vermessung"
        ],
        "faq": [
            ["Wann sollten Stossd\u00e4mpfer gewechselt werden?", "Alle 60.000\u201380.000 km oder bei Anzeichen wie Wanken, Nachschwingen, verl\u00e4ngerte Bremswege. Ein Stossd\u00e4mpfer-Test gibt Klarheit."],
            ["Muss eine Achsvermessung extra beauftragt werden?", "Ja \u2013 eine Achsvermessung ist eine separate Dienstleistung und nicht automatisch in jeder Reparatur enthalten. Bei Fahrwerksreparaturen empfehlen wir sie grunds\u00e4tzlich."],
            ["Ist nach einem Querlenkerwechsel eine Spurvermessung n\u00f6tig?", "Ja, zwingend. Nach dem L\u00f6sen der Radaufh\u00e4ngung ver\u00e4ndert sich die Spur. Ohne Vermessung drohen ungleichm\u00e4ssiger Reifenabrieb und unberechenbares Fahrverhalten."],
            ["Erkenne ich einen Fahrwerksschaden selbst?", "H\u00e4ufige Anzeichen: Klappern beim \u00dcberfahren von Bordsteinkanten, Wanken in Kurven, einseitiger Reifenverschleiss, das Fahrzeug zieht nach links oder rechts."],
            ["Was umfasst eine Fahrwerksreparatur typischerweise?", "Stossd\u00e4mpfer werden paarweise getauscht, Querlenker inklusive Lager erneuert, Spurstangen bei Lenkungsspiel ersetzt. Inklusive anschliessender Achsvermessung."]
        ],
        "cta": "Klappert Ihr Fahrwerk, zieht das Fahrzeug zur Seite oder haben Sie das Gef\u00fchl, die Strassenlage ist schwammig? Vereinbaren Sie eine Fahrwerksdiagnose."
    },
    {
        "slug": "bremsenservice", "title": "Bremsenservice",
        "subtitle": "Wartung und Reparatur der Bremsanlage. Austausch von Bel\u00e4gen, Scheiben, Bremsschl\u00e4uchen und Bremsfl\u00fcssigkeit.",
        "meta": "Bremsenservice in Kreuztal: Bremsbel\u00e4ge, Bremsscheiben, Bremsfl\u00fcssigkeit, Handbremse, ABS, Bremsleitungen. Kompletter Bremsenservice.",
        "hero_img": "static/images/Bremsenservice1.png",
        "hero_icon": "ri-brake-line",
        "intro": "Die Bremsanlage ist der wichtigste Sicherheitsfaktor an Ihrem Fahrzeug. Wir bieten den kompletten Bremsenservice \u2013 von der Pr\u00fcfung der Bel\u00e4ge und Scheiben \u00fcber den Austausch bis zur Bremsfl\u00fcssigkeits-Erneuerung. Immer nach Herstellervorgaben und mit Qualit\u00e4tsteilen.",
        "process": [
            ["Bremsenpr\u00fcfung & Verschleisskontrolle", "Wir kontrollieren Belagst\u00e4rke, Scheibenzustand, Bremsfl\u00fcssigkeitszustand und Bremsschl\u00e4uche auf Risse oder Porosit\u00e4t. Mitmessung der Bremskraft auf dem Bremsenpr\u00fcfstand.", "ri-search-eye-line"],
            ["Austausch & Wartung", "Verschlissene Bremsbel\u00e4ge und Bremsscheiben werden fachgerecht getauscht. Wir reinigen die Bremsen, fetten die F\u00fchrungen und erneuern die Bremsfl\u00fcssigkeit.", "ri-tools-fill"],
            ["Funktionskontrolle & Probefahrt", "Nach der Reparatur erfolgen eine Kontrolle der Bremskraft, Dichtheitspr\u00fcfung und eine Probefahrt mit mehreren Vollbremsungen zur Einbremsung.", "ri-check-double-line"]
        ],
        "sections": [
            ["Bremsbel\u00e4ge & Bremsscheiben", "Bremsbel\u00e4ge haben eine Mindestst\u00e4rke von 2 mm, Bremsscheiben eine Mindestdicke. Wir wechseln Bel\u00e4ge und Scheiben paarweise (pro Achse), verwenden Markenqualit\u00e4t (ATE, Textar, Brembo) und achten auf saubere Einbauarbeit."],
            ["Bremsfl\u00fcssigkeitswechsel", "Bremsfl\u00fcssigkeit ist hygroskopisch \u2013 sie zieht Wasser an. Mit der Zeit sinkt der Siedepunkt, was bei starker Bremsung zu Dampfblasen (Bremsversagen) f\u00fchren kann. Wir empfehlen den Wechsel alle 2 Jahre."],
            ["Handbremse & Bremsleitungen", "Eine feste Handbremse oder eine zu hoch eingestellte Handbremse ist ein h\u00e4ufiger Mangel bei der HU. Wir stellen die Handbremse ein, tauschen korrodierte Bremsleitungen und pr\u00fcfen die Bremschl\u00e4uche."],
            ["ABS & Bremsassistent", "Leuchtet die ABS-Leuchte, liegt oft ein defekter Radsensor, ein kaputter Impulsring oder ein Fehler im ABS-Steuerger\u00e4t vor. Wir diagnostizieren und reparieren ABS-Systeme aller Hersteller."]
        ],
        "benefits": [
            "Qualit\u00e4ts-Bremsenteile von ATE, Textar, Brembo",
            "Bremsenpr\u00fcfstand-Messung inklusive",
            "Bremsfl\u00fcssigkeitswechsel mit Siedepunktmessung",
            "Paarweiser Austausch f\u00fcr gleichm\u00e4ssige Bremswirkung",
            "ABS-Diagnose inklusive",
            "Sicherheitscheck vor jeder Bremsenreparatur"
        ],
        "faq": [
            ["Wann m\u00fcssen Bremsbel\u00e4ge gewechselt werden?", "Wenn die Belagst\u00e4rke unter 3 mm sinkt (gesetzlich: 2 mm). Die meisten Fahrzeuge haben eine Verschleisswarnung, die bei ca. 4 mm aufleuchtet."],
            ["Was ist beim Bremsenwechsel zu beachten?", "Wir wechseln Bremsbel\u00e4ge und Bremsscheiben paarweise pro Achse. Nach dem Wechsel ist eine Einbremszeit von etwa 200\u2013300 km einzuplanen \u2013 vermeiden Sie in dieser Zeit unn\u00f6tige Vollbremsungen."],
            ["M\u00fcssen nach dem Bremsenwechsel die Bremsen eingebremst werden?", "Ja \u2013 neue Bel\u00e4ge und Scheiben brauchen etwa 200\u2013300 km Einbremszeit. Vermeiden Sie in dieser Zeit starke Vollbremsungen, wenn nicht n\u00f6tig."],
            ["Woran erkenne ich, dass die Bremsen verschlissen sind?", "Pfeifende oder quietschende Ger\u00e4usche, l\u00e4ngerer Bremsweg, Pulsschlag im Bremspedal, das Fahrzeug zieht beim Bremsen zur Seite oder die Bremswarnleuchte leuchtet."],
            ["Kann man nur die Bel\u00e4ge wechseln oder immer mit Scheiben?", "Wenn die Scheiben noch innerhalb der Mindestdicke und ohne Riefen sind, k\u00f6nnen nur die Bel\u00e4ge gewechselt werden. Wir pr\u00fcfen das f\u00fcr Sie und empfehlen ehrlich."]
        ],
        "cta": "Quietschen die Bremsen oder haben Sie das Gef\u00fchl, der Bremsweg wird l\u00e4nger? Vereinbaren Sie einen Bremsen-Check \u2013 Sicherheit geht vor."
    },
    {
        "slug": "autoelektrik-elektronik", "title": "Autoelektrik & Elektronik",
        "subtitle": "Reparatur und Einstellung von Elektrik: Starter, Generator, Batterien, Beleuchtung, Komfort- und Sicherheitssysteme.",
        "meta": "Autoelektrik in Kreuztal: Batterie, Generator, Starter, Beleuchtung, Steuerger\u00e4te, Codierung, Standheizung. Elektrik-Reparaturen aller Art.",
        "hero_img": "static/images/Autoelektrik-Elektronik1.png",
        "hero_icon": "ri-flashlight-line",
        "intro": "Die Elektrik und Elektronik moderner Fahrzeuge wird immer komplexer. Ob defekter Generator, leere Batterie, ausgefallene Beleuchtung oder Probleme mit Steuerger\u00e4ten \u2013 wir diagnostizieren und reparieren elektrische Systeme aller Fahrzeugmarken professionell und zuverl\u00e4ssig.",
        "process": [
            ["Fehleranalyse & Systemdiagnose", "Mit herstellerspezifischen Diagnoseger\u00e4ten pr\u00fcfen wir die Spannungsversorgung, lesen Fehlerspeicher aus und analysieren die Kommunikation zwischen den Steuerger\u00e4ten.", "ri-flashlight-line"],
            ["Reparatur & Komponententausch", "Defekte Komponenten (Generator, Starter, Batterie, Steuerger\u00e4te) werden instandgesetzt oder ersetzt. Wir pr\u00fcfen die gesamte Lade- und Startanlage nach der Reparatur.", "ri-tools-fill"],
            ["Funktionskontrolle & Systemtest", "Nach der Reparatur erfolgt eine vollst\u00e4ndige Funktionskontrolle aller angrenzenden Systeme, um Folgesch\u00e4den auszuschliessen und die einwandfreie Funktion zu gew\u00e4hrleisten.", "ri-check-double-line"]
        ],
        "sections": [
            ["Batterie, Starter und Generator", "Probleme mit der Starterbatterie, dem Anlasser oder der Lichtmaschine geh\u00f6ren zu den h\u00e4ufigsten Pannenursachen. Wir pr\u00fcfen die gesamte Lade- und Startanlage mit professionellen Pr\u00fcfger\u00e4ten."],
            ["Beleuchtung und Signalanlage", "Eine intakte Beleuchtung ist gesetzlich vorgeschrieben und entscheidend f\u00fcr Ihre Sicherheit. Wir reparieren Scheinwerfer, R\u00fcckleuchten, Nebelscheinwerfer und r\u00fcsten moderne LEDs nach."],
            ["Komfort- und Sicherheitssysteme", "Von der Zentralverriegelung \u00fcber elektrische Fensterheber bis zu Fahrerassistenzsystemen \u2013 wir diagnostizieren und reparieren alle Komfort- und Sicherheitselektroniken."],
            ["Steuerger\u00e4te-Programmierung & Codierung", "Viele Elektronikprobleme lassen sich durch ein Software-Update l\u00f6sen. Wir programmieren und codieren Steuerger\u00e4te aller Hersteller, f\u00fchren Online-Kodierungen durch und passen Fahrzeugkonfigurationen an."]
        ],
        "benefits": [
            "Herstellerspezifische Diagnoseger\u00e4te f\u00fcr alle Marken",
            "Batterietest mit professioneller Kapazit\u00e4tsmessung",
            "Reparatur aller elektrischer Systeme",
            "Software-Updates und Steuerger\u00e4te-Programmierung",
            "LED-Nachr\u00fcstungen und Beleuchtungsoptimierung",
            "Ruhestrommessung bei entladener Batterie"
        ],
        "faq": [
            ["Die Batterie ist st\u00e4ndig leer \u2013 woran liegt das?", "M\u00f6gliche Ursachen: eine defekte Lichtmaschine, hoher Ruhestrom durch ein Steuerger\u00e4t, eine alte oder defekte Batterie oder Kurzstreckenfahrten im Winter."],
            ["Was umfasst eine Elektrik-Diagnose?", "Eine vollst\u00e4ndige Elektrik-Diagnose inklusive Batterietest, Generatormessung, Auslesen aller Steuerger\u00e4te und Pr\u00fcfung der Bordnetzkommunikation. Wir identifizieren die Fehlerquelle gezielt."],
            ["Kann ich selbst eine LED-Nachr\u00fcstung vornehmen?", "Wir raten davon ab \u2013 viele Fahrzeuge verf\u00fcgen \u00fcber CAN-BUS-\u00dcberwachung. Einfache LED-Lampen f\u00fchren zu Fehlermeldungen. Wir codieren das Fahrzeug korrekt um."],
            ["Warum funktioniert meine Standheizung nicht?", "Typische Ursachen: eine schwache Batterie, ein defektes Steuerger\u00e4t, eine verstopfte Brennkammer oder ein abgelaufener Timer."],
            ["R\u00fcsten Sie auch Anh\u00e4ngerkupplungen mit Elektrik nach?", "Ja \u2013 inklusive fahrzeugspezifischem Elektrosatz, Codierung und Funktionstest."]
        ],
        "cta": "Die Batterie ist leer, eine Kontrollleuchte leuchtet oder ein elektrischer Verbraucher funktioniert nicht? Vereinbaren Sie einen Elektrik-Check."
    },
    {
        "slug": "karosserie-lackierung", "title": "Karosserie & Lackierung",
        "subtitle": "Vom kleinen Kratzer bis zur Komplettlackierung \u2013 alles aus einer Hand",
        "meta": "Karosseriearbeiten und Lackierung in Kreuztal: Dellenentfernung, Beulen dr\u00fccken, Richtbank, Unfallinstandsetzung, Lackierung.",
        "hero_img": "static/images/Karosserie-Lackierung1.png",
        "hero_icon": "ri-paint-brush-line",
        "intro": "Ob Parkdelle, Steinschlag oder Unfallschaden \u2013 unsere Karosserie- und Lackierabteilung bringt Ihr Fahrzeug wieder in Bestform. Mit Richtbank, 3D-Vermessung und Lackierkabine liefern wir Ergebnisse, die sich sehen lassen k\u00f6nnen.",
        "process": [
            ["Schadensbegutachtung", "Wir begutachten den Schaden gemeinsam mit Ihnen, zeigen Reparaturm\u00f6glichkeiten und den empfohlenen Ablauf. Oft gibt es mehrere Wege zum Ziel.", "ri-eye-line"],
            ["Reparatur & Vorbereitung", "Karosserie richten, Dellen entfernen, Oberfl\u00e4che vorbereiten. Je nach Schaden: PDR (Ausbeulen ohne Lackieren) oder klassische Spachtelarbeit.", "ri-scissors-2-line"],
            ["Lackierung & Qualit\u00e4tskontrolle", "In unserer beheizten Lackierkabine wird Ihr Fahrzeug farbtongetreu lackiert und nach dem Aush\u00e4rten im Lichtkanal gepr\u00fcft.", "ri-palette-line"]
        ],
        "sections": [
            ["Ausbeulen ohne Lackieren (PDR)", "Kleine Dellen, Hagelsch\u00e4den und Beulen lassen sich oft ohne Lackierarbeit entfernen. PDR ist schnell, schonend zur Werkslackierung und sehr effizient."],
            ["Richt- und Schweissarbeiten", "Mit computergesteuerter 3D-Vermessung wird die Karosserie millimetergenau in die Originalmasse zur\u00fcckgebracht. Schweissarbeiten nach Herstellervorgaben."],
            ["Lackierarbeiten in Profi-Qualit\u00e4t", "Unsere Lackierkabine erf\u00fcllt h\u00f6chste Standards. Wir lackieren mit OEM-qualifizierten Lacksystemen. Der Farbton wird elektronisch ermittelt."],
            ["Korrosionsschutz nach der Reparatur", "Wir versiegeln Hohlr\u00e4ume, bringen Steinschlagschutz auf und konservieren Unterbodenbereiche \u2013 f\u00fcr langfristigen Rostschutz."]
        ],
        "benefits": [
            "Parkdellen-Entfernung ohne Neulackierung (PDR)",
            "Computergesteuerte Richtbank mit 3D-Vermessung",
            "Farbtongenaue Lackierung mit OEM-Lacksystemen",
            "Professionelle Korrosionsschutzbehandlung",
            "Karosseriearbeiten aller Schwierigkeitsgrade",
            "Unverbindliche Begutachtung vor der Reparatur"
        ],
        "faq": [
            ["Kann man jede Delle ohne Neulackierung entfernen?", "Nein \u2013 PDR funktioniert nur, wenn der Lack nicht besch\u00e4digt ist. Bei Steinschl\u00e4gen muss lackiert werden. Wir beraten Sie ehrlich."],
            ["Wie lange dauert eine Parkdellen-Entfernung?", "Eine einzelne Delle ist oft in 1\u20132 Stunden erledigt. Wir sagen Ihnen vorab die Dauer."],
            ["Was umfasst eine Lackierung?", "Wir lackieren einzelne Teile (Stossstangen, Kotfl\u00fcgel, T\u00fcren), Fahrzeugseiten oder komplette Fahrzeuge. Verwendet werden OEM-zertifizierte Lacksysteme mit Farbtongarantie."],
            ["H\u00e4lt die Reparaturlackierung so lange wie die Werkslackierung?", "Moderne Lacksysteme erm\u00f6glichen Ergebnisse nahe der Werksqualit\u00e4t. 5 Jahre Garantie auf Lackierarbeiten."],
            ["Was ist der Lichtkanal?", "Eine speziell beleuchtete Pr\u00fcfstation, die selbst kleinste Unebenheiten im Lack sichtbar macht. Jedes Fahrzeug durchl\u00e4uft diese Kontrolle."]
        ],
        "cta": "Ihr Fahrzeug hat eine Delle oder einen Kratzer? Vereinbaren Sie einen unverbindlichen Begutachtungstermin."
    },
    {
        "slug": "klimaanlagenservice", "title": "Klimaanlagenservice",
        "subtitle": "F\u00fcr frische Luft und angenehme Temperaturen im Fahrzeug",
        "meta": "Klimaanlagenservice in Kreuztal: K\u00e4ltemittel bef\u00fcllen, Desinfektion, Lecksuche, Kompressor-Reparatur. Alle Marken.",
        "hero_img": "static/images/Klimaanlagenservice1.png",
        "hero_icon": "ri-snowflake-line",
        "intro": "Eine funktionierende Klimaanlage sorgt f\u00fcr Komfort an heissen Sommertagen und f\u00fcr Sicherheit durch beschlagfreie Scheiben. Wir warten, reparieren und bef\u00fcllen Klimaanlagen aller Fahrzeugmarken.",
        "process": [
            ["Klima-Check & Leistungspr\u00fcfung", "Wir messen die Ist-Temperatur an den L\u00fcftungsd\u00fcsen, pr\u00fcfen Systemdruck und \u00d6lzustand des Kompressors.", "ri-thermometer-line"],
            ["Wartung & Bef\u00fcllung", "Die Anlage wird entleert, K\u00e4ltemittel recycelt. Nach Dichtheitspr\u00fcfung wird neues K\u00e4ltemittel und Kompressor\u00f6l eingef\u00fcllt. Desinfektion des Verdampfers.", "ri-drinks-line"],
            ["Funktionskontrolle", "Messung der K\u00fchlleistung an den D\u00fcsen. Zieltemperatur: 4\u20138\u00b0C \u2013 das Qualit\u00e4tsmerkmal einer einwandfreien Klimaanlage.", "ri-check-double-line"]
        ],
        "sections": [
            ["Klimaanlagen-Wartung \u2013 alle 2 Jahre", "Durch nat\u00fcrliche Leckage verliert jede Klimaanlage pro Jahr bis zu 10% K\u00e4ltemittel. Wartung alle 2 Jahre empfohlen: absaugen, reinigen, trocknen, neu bef\u00fcllen."],
            ["Lecksuche und Reparatur", "Wenn die Klima nicht mehr k\u00fchlt, liegt meist ein Leck vor. Lecksuche mit UV-Farbstoff oder elektronischem Lecksucher. Reparatur von O-Ringen, Schl\u00e4uchen oder Kondensator."],
            ["Desinfektion und Geruchsbeseitigung", "Muffiger Geruch aus den D\u00fcsen = Bakterien- und Pilzbefall im Verdampfer. Desinfektion mit Spezialger\u00e4t und Ozonbehandlung."],
            ["Kompressor und Expansionsventil", "Der Klimakompressor ist das Herz der Anlage. Defekte erkennen wir an lauten Ger\u00e4uschen oder mangelnder K\u00fchlleistung."]
        ],
        "benefits": [
            "Angenehme Fahrzeugtemperatur an heissen Tagen",
            "Beschlagfreie Scheiben f\u00fcr mehr Sicherheit",
            "Beseitigung unangenehmer Ger\u00fcche und Keime",
            "L\u00e4ngere Lebensdauer der Klimaanlage",
            "Gepr\u00fcfte Dichtheit \u2013 kein K\u00e4ltemittelverlust",
            "Umweltschonende K\u00e4ltemittel-R\u00fcckgewinnung"
        ],
        "faq": [
            ["Wie oft sollte die Klimaanlage gewartet werden?", "Alle 2 Jahre \u2013 K\u00e4ltemittel erneuern, Dichtheitspr\u00fcfung, Innenraumfilter wechseln."],
            ["Warum riecht es muffig?", "Bakterien auf dem Verdampfer. Desinfektion beseitigt den Geruch. Tipp: Klima 5 Minuten vor Fahrtende ausschalten."],
            ["Was wird beim Klimaservice gemacht?", "Ein Klimaservice umfasst K\u00e4ltemittelauff\u00fcllung, Dichtheitspr\u00fcfung, Desinfektion des Verdampfers und Pr\u00fcfung der K\u00fchlleistung. Wir empfehlen den Service alle 2 Jahre."],
            ["Kann ich die Klima im Winter nutzen?", "Ja \u2013 sie trocknet die Luft und verhindert beschlagene Scheiben. Lassen Sie sie ganzj\u00e4hrig laufen."],
            ["Woran erkenne ich, dass die Klima nicht mehr richtig k\u00fchlt?", "Lauwarme Luft an den D\u00fcsen, lange K\u00fchldauer oder laute Ger\u00e4usche aus dem Motorraum."]
        ],
        "cta": "Die Klimaanlage k\u00fchlt nicht mehr richtig oder riecht unangenehm? Vereinbaren Sie einen Klimaservice."
    },
    {
        "slug": "reifenservice-auswuchten", "title": "Reifenservice & Auswuchten",
        "subtitle": "Sicher unterwegs mit optimalen Reifen \u2013 Montage, Einlagerung, Beratung",
        "meta": "Reifenservice in Kreuztal: Montage, Demontage, Auswuchten, saisonaler Wechsel, Einlagerung. Reifen kaufen und beraten lassen.",
        "hero_img": "static/images/Reifenservice-Auswuchten1.png",
        "hero_icon": "ri-steering-2-line",
        "intro": "Die Reifen sind die einzige Verbindung Ihres Fahrzeugs zur Strasse. Wir bieten den kompletten Reifenservice: saisonaler Wechsel, professionelles Auswuchten, fachgerechte Einlagerung und Beratung beim Neukauf.",
        "process": [
            ["Annahme & Reifenpr\u00fcfung", "Wir pr\u00fcfen den Zustand der Reifen (Profil, Alter, Besch\u00e4digungen) und besprechen Ihre W\u00fcnsche.", "ri-search-line"],
            ["Montage & Auswuchten", "Alte Reifen demontieren, neue Reifen aufziehen. Dynamisches Auswuchten jedes Rades f\u00fcr vibrationsfreie Fahrt.", "ri-tools-fill"],
            ["Druckkontrolle & Abfahrt", "Reifendruck pr\u00fcfen und an Beladung anpassen. Radmuttern nach 50 km nachziehen.", "ri-check-double-line"]
        ],
        "sections": [
            ["Montage & Demontage \u2013 felgenschonend", "Reifen aller Gr\u00f6ssen (12\u201324 Zoll) mit modernsten Montiermaschinen. Auch Runflat, Notlaufreifen und RDKS-Sensoren."],
            ["Auswuchten f\u00fcr eine ruhige Fahrt", "Elektronische Auswuchtmaschine f\u00fcr statische und dynamische Unwucht. Auf den Gramm genau."],
            ["Saisonaler Wechsel & Einlagerung", "Kompletter Service: Abholung, Montage, Auswuchten, Einlagern des anderen Satzes in klimatisierter Umgebung."],
            ["Reifenberatung \u2013 neutral und kompetent", "Sommerreifen, Winterreifen, Ganzjahresreifen. Marken: Continental, Michelin, Bridgestone, Goodyear, Pirelli. Beratung ohne Verkaufsdruck."]
        ],
        "benefits": [
            "Felgenschonende Montage mit modernster Technik",
            "Pr\u00e4zises dynamisches Auswuchten",
            "Klimatisierte Einlagerung mit Zustandsprotokoll",
            "Neutrale Reifenberatung \u2013 herstellerunabh\u00e4ngig",
            "Druckkontrolle und Nachzugservice inklusive",
            "Abhol- und Bringservice auf Wunsch"
        ],
        "faq": [
            ["Wann ist Reifenwechselzeit?", "Oktober bis Ostern Winterreifen, Ostern bis Oktober Sommerreifen. Situationsbedingte Winterreifenpflicht."],
            ["Wie erkenne ich, ob Reifen noch gut sind?", "Mindestprofiltiefe 1,6 mm. Empfohlen: Sommerreifen ab 3 mm, Winterreifen ab 4 mm wechseln. Reifen \u00e4lter als 8 Jahre ersetzen."],
            ["Was ist im Komplettservice enthalten?", "Montage, Demontage, Auswuchten und Einlagerung des zweiten Radsatzes in klimatisierter Umgebung \u2013 alles aus einer Hand."],
            ["Sind Ganzjahresreifen eine gute Alternative?", "Bis 15.000 km/Jahr und milde Winter \u2013 ja. Bei Schnee und Bergfahrten empfehlen wir klassische Saisonreifen."],
            ["Was ist RDKS?", "Reifendruckkontrollsystem \u2013 Sensoren in den R\u00e4dern messen den Druck. Beim Reifenwechsel korrekt behandeln und neu anlernen."]
        ],
        "cta": "Bald ist Reifenwechselzeit! Vereinbaren Sie jetzt Ihren Termin \u2013 wir montieren, wuchten und lagern fachgerecht."
    },
    {
        "slug": "tuev-hu-au", "title": "T\u00dcV / HU / AU",
        "subtitle": "Hauptuntersuchung mit Vorbereitung \u2013 stressfrei und aus einer Hand",
        "meta": "T\u00dcV, HU und AU in Kreuztal: Hauptuntersuchung mit Vorbereitung, M\u00e4ngelbeseitigung, Abgasuntersuchung. Alles aus einer Hand.",
        "hero_img": "static/images/TUV1.png",
        "hero_icon": "ri-shield-check-line",
        "intro": "Die Hauptuntersuchung (HU) und Abgasuntersuchung (AU) sind Pflicht f\u00fcr jeden Fahrzeughalter. Wir bereiten Ihr Fahrzeug optimal auf die Pr\u00fcfung vor, begleiten Sie durch den gesamten Prozess und beheben M\u00e4ngel direkt \u2013 oft am selben Tag.",
        "process": [
            ["HU-Vorbereitungs-Check", "Pr\u00fcfung aller relevanten Punkte: Beleuchtung, Bremsen, Reifen, Fahrwerk, Lenkung, Abgasanlage. Kleine M\u00e4ngel beheben wir sofort.", "ri-search-line"],
            ["Pr\u00fcfung bei der Pr\u00fcfstelle", "Wir bringen Ihr Fahrzeug zur amtlichen Pr\u00fcfstelle und begleiten die Pr\u00fcfung.", "ri-shield-check-line"],
            ["M\u00e4ngelbeseitigung & Nachpr\u00fcfung", "Beanstandete Punkte reparieren wir umgehend. Anschliessende Nachpr\u00fcfung \u2013 damit Sie schnell die Plakette erhalten.", "ri-check-double-line"]
        ],
        "sections": [
            ["HU-Vorbereitung \u2013 der Check vor der Pr\u00fcfung", "Kontrolle von Beleuchtung, Bremsen, Reifen, Fahrwerk, Lenkung, Abgasanlage. Wir pr\u00fcfen alles, was bei der HU beanstandet werden k\u00f6nnte."],
            ["Abgasuntersuchung (AU)", "Messung der Emissionswerte: CO, HC, CO2, Lambda bei Benzinern, Tr\u00fcbung bei Dieseln. Bei Grenzwert\u00fcberschreitung: Diagnose und Reparatur."],
            ["M\u00e4ngelbeseitigung \u2013 wir k\u00fcmmern uns", "Nach der HU haben Sie einen Monat Zeit f\u00fcr erhebliche M\u00e4ngel. Wir reparieren und f\u00fchren die Nachpr\u00fcfung durch."],
            ["Tipps f\u00fcr die erfolgreiche HU", "Wischblatt-Zustand? Warndreieck und Verbandskasten vorhanden? Alle Leuchten funktionieren? Reifenprofil ausreichend? Wir pr\u00fcfen alles f\u00fcr Sie."]
        ],
        "benefits": [
            "Komplette HU-Vorbereitung mit Pr\u00fcfcheck",
            "Sofortige M\u00e4ngelbeseitigung in eigener Werkstatt",
            "Nachpr\u00fcfung bei der Pr\u00fcfstelle inklusive",
            "Terminorganisation und Erinnerung",
            "Abgastest (AU) inklusive",
            "Komplette Betreuung von der Vorbereitung bis zur Plakette"
        ],
        "faq": [
            ["Wann muss mein Fahrzeug zur HU?", "Neuwagen: erstmals nach 36 Monaten, dann alle 24 Monate. Auf der Plakette erkennen Sie die F\u00e4lligkeit."],
            ["Was passiert bei \u00dcberziehung?", "Bis 2 Monate: Verwarngeld. 2\u20134 Monate: erh\u00f6htes Verwarngeld. 4\u20138 Monate: Bussgeld und Punkt. Darum rechtzeitig Termin machen."],
            ["Was wird bei der HU/AU gepr\u00fcft?", "HU: Beleuchtung, Bremsen, Fahrwerk, Lenkung, Reifen, Karosserie, Abgasanlage. AU: Messung der Abgaswerte. Wir bereiten alles f\u00fcr Sie vor."],
            ["Welche M\u00e4ngel gibt es?", "Geringe, erhebliche und verkehrsunsichere M\u00e4ngel. Wir helfen bei allen Kategorien."],
            ["Kann ich ohne Termin zur HU?", "Nein \u2013 Pr\u00fcfstellen arbeiten mit Terminvergabe. Wir organisieren alles f\u00fcr Sie."]
        ],
        "cta": "Ihre HU/AU steht an? Wir bereiten vor, organisieren, bringen hin und holen die Plakette."
    }
]
'''
SERVICES_DATA = json.loads(json_raw.replace('None', 'null'))

SERVICE_COLORS = [
    ("#6b7b8d", "#4a5560", "210 15% 45%"),   # 0 Wartung - Slate Blue
    ("#8a7f78", "#5c5550", "25 10% 50%"),    # 1 Unfallreparatur - Warm Stone
    ("#7a8a7a", "#556055", "120 8% 40%"),    # 2 Fahrzeugsdiagnose - Sage
    ("#9a7b6b", "#6b5550", "20 15% 50%"),    # 3 Motorreparatur - Clay
    ("#7a7a8a", "#555560", "240 8% 45%"),    # 4 Getriebereparatur - Pewter
    ("#9a8a7a", "#6b6055", "30 10% 55%"),    # 5 Fahrwerk - Sand
    ("#8a7a8a", "#605560", "300 8% 45%"),    # 6 Bremsenservice - Heather
    ("#6b7a8a", "#4a5565", "210 12% 45%"),   # 7 Autoelektrik - Steel Blue
    ("#8a8278", "#605a50", "30 8% 50%"),     # 8 Karosserie - Fawn
    ("#7a828a", "#555a60", "210 8% 50%"),    # 9 Klimaanlage - Fog
    ("#6b8a7a", "#4a6055", "150 12% 45%"),   # 10 Reifen - Dusty Teal
    ("#8a7a72", "#605550", "15 10% 50%"),    # 11 TÜV - Taupe
]

HERO_VARIANTS = [4]*12
SECTION_ORDERS = [['intro','content','benefits','process','faq','cta']]*12
HEADER = '''    <header class="bg-white/95 backdrop-blur-sm shadow-sm sticky top-0 z-50">
        <div class="container mx-auto px-4 py-3 flex items-center justify-between">
            <div class="flex items-center">
                <a href="/"><img src="static/images/kw.avif" alt="Kreuztaler Werkstatt Logo" class="h-10 mr-2"></a>
                <a href="/" class="text-primary font-['Arimo'] text-xl mr-1 font-bold tracking-tight">Kreuztaler Werkstatt</a>
                <span class="text-gray-400 text-xs hidden sm:inline">GmbH</span>
            </div>
            <nav class="hidden md:flex space-x-6 text-sm">
                <a href="/#home" class="text-gray-600 hover:text-primary transition-colors">Startseite</a>
                <a href="/#about" class="text-gray-600 hover:text-primary transition-colors">&Uuml;ber uns</a>
                <a href="/#services" class="text-primary font-medium">Leistungen</a>
                <a href="/#reviews" class="text-gray-600 hover:text-primary transition-colors">Bewertungen</a>
                <a href="/#faq" class="text-gray-600 hover:text-primary transition-colors">FAQ</a>
                <a href="/#contact" class="text-gray-600 hover:text-primary transition-colors">Kontakt</a>
            </nav>
            <div class="flex items-center space-x-3">
                <a href="tel:+49273227717" class="hidden sm:flex items-center text-primary font-medium text-sm hover:underline"><i class="ri-phone-line mr-1"></i>02732 277 17</a>
                <a href="/#appointment" class="bg-primary text-white text-sm px-4 py-2 !rounded-button whitespace-nowrap hover:bg-primary/90 transition-colors shadow-md hover:shadow-lg">Termin</a>
                <button type="button" id="mobileMenuBtn" class="md:hidden text-gray-600 hover:text-primary p-1"><i class="ri-menu-line ri-lg"></i></button>
            </div>
        </div>
    </header>
'''
FOOTER_COMMON = '''    <footer id="footer" class="relative overflow-hidden text-white">
        <canvas id="footerShader" class="absolute inset-0 w-full h-full"></canvas>
        <div class="absolute inset-0 bg-gray-900/75"></div>
        <div class="relative z-10 pt-12 pb-8">
        <div class="container mx-auto px-4">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-10">
                <div>
                    <div class="flex items-center mb-3">
                        <img src="static/images/kw.avif" alt="Logo" class="h-9 mr-2">
                        <div class="text-white font-['Arimo'] text-lg font-bold">Kreuztaler Werkstatt</div>
                    </div>
                    <p class="text-gray-400 text-sm">Ihr zuverl&auml;ssiger Partner rund ums Auto in Kreuztal und Umgebung.</p>
                </div>
                <div>
                    <h4 class="text-sm font-semibold mb-4 uppercase tracking-wider text-gray-300">Schnellzugriff</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="/#home" class="text-gray-400 hover:text-white transition-colors">Startseite</a></li>
                        <li><a href="/#about" class="text-gray-400 hover:text-white transition-colors">&Uuml;ber uns</a></li>
                        <li><a href="/#services" class="text-gray-400 hover:text-white transition-colors">Leistungen</a></li>
                        <li><a href="/#reviews" class="text-gray-400 hover:text-white transition-colors">Bewertungen</a></li>
                        <li><a href="/#faq" class="text-gray-400 hover:text-white transition-colors">FAQ</a></li>
                        <li><a href="/#contact" class="text-gray-400 hover:text-white transition-colors">Kontakt</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-sm font-semibold mb-4 uppercase tracking-wider text-gray-300">Leistungen</h4>
                    <ul class="space-y-2 text-sm">
''' + "\n".join(f'                        <li><a href="leistung-{s["slug"]}.html" class="text-gray-400 hover:text-white transition-colors">{s["title"]}</a></li>' for s in SERVICES_DATA) + '''
                    </ul>
                </div>
                <div>
                    <h4 class="text-sm font-semibold mb-4 uppercase tracking-wider text-gray-300">Kontakt</h4>
                    <ul class="space-y-2 text-sm text-gray-400">
                        <li class="flex items-start"><i class="ri-map-pin-line mr-2 mt-0.5"></i><span>Hagener Str. 40, 57223 Kreuztal</span></li>
                        <li class="flex items-start"><i class="ri-phone-line mr-2 mt-0.5"></i><a href="tel:+49273227717" class="hover:text-white transition-colors">02732 277 17</a></li>
                        <li class="flex items-start"><i class="ri-mail-line mr-2 mt-0.5"></i><span>info@kreuztaler-werkstatt.de</span></li>
                        <li class="flex items-start"><i class="ri-time-line mr-2 mt-0.5"></i><span>Mo-Fr: 9:00&ndash;17:00 Uhr</span></li>
                        <li class="flex items-start text-gray-500"><i class="ri-time-line mr-2 mt-0.5"></i><span>Mittagspause: 13:00&ndash;14:00 Uhr</span></li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-gray-800 pt-6 flex flex-col md:flex-row justify-between items-center gap-4">
                <p class="text-gray-500 text-xs">&copy; 2025 Kreuztaler Werkstatt GmbH.</p>
                <div class="flex space-x-4 text-xs">
                    <a href="#" onclick="openImpressumModal()" class="text-gray-500 hover:text-white">Impressum</a>
                    <a href="static/Datenschutz.pdf" target="_blank" class="text-gray-500 hover:text-white">Datenschutz</a>
                </div>
            </div>
        </div>
    </div>
    </footer>
<script>
(function(){
    var c = document.getElementById('footerShader');
    if(!c)return;
    var gl = c.getContext('webgl');
    if(!gl)return;
    var vsSrc='attribute vec4 aVertexPosition;void main(){gl_Position=aVertexPosition;}';
    var fsSrc='#version 100\\nprecision highp float;\\nuniform vec2 iResolution;\\nuniform float iTime;\\n'
    +'const float overallSpeed=0.2;\\nconst float gridSmoothWidth=0.015;\\nconst float axisWidth=0.05;\\n'
    +'const float majorLineWidth=0.025;\\nconst float minorLineWidth=0.0125;\\nconst float majorLineFrequency=5.0;\\n'
    +'const float minorLineFrequency=1.0;\\nconst vec4 gridColor=vec4(0.5);\\nconst float scale=5.0;\\n'
+'const vec4 lineColor=vec4(0.0,0.33,0.65,1.0);\\nconst float minLineWidth=0.01;\\nconst float maxLineWidth=0.2;\\n'
+'const float lineSpeed=1.0*overallSpeed;\\nconst float lineAmplitude=1.0;\\nconst float lineFrequency=0.2;\\n'
+'const float warpSpeed=0.2*overallSpeed;\\nconst float warpFrequency=0.5;\\nconst float warpAmplitude=1.0;\\n'
+'const float offsetFrequency=0.5;\\nconst float offsetSpeed=1.33*overallSpeed;\\nconst float minOffsetSpread=0.6;\\n'
+'const float maxOffsetSpread=2.0;\\nconst int linesPerGroup=16;\\n'
+'#define drawCircle(p,r,cd) smoothstep(r+gridSmoothWidth,r,length(cd-(p)))\\n'
+'#define drawSmoothLine(p,hw,t) smoothstep(hw,0.0,abs(p-(t)))\\n'
+'#define drawCrispLine(p,hw,t) smoothstep(hw+gridSmoothWidth,hw,abs(p-(t)))\\n'
+'#define drawPeriodicLine(f,w,t) drawCrispLine(f/2.0,w,abs(mod(t,f)-(f)/2.0))\\n'
+'float drawGridLines(float a){return drawCrispLine(0.0,axisWidth,a)+drawPeriodicLine(majorLineFrequency,majorLineWidth,a)+drawPeriodicLine(minorLineFrequency,minorLineWidth,a);}\\n'
+'float drawGrid(vec2 s){return min(1.0,drawGridLines(s.x)+drawGridLines(s.y));}\\n'
+'float rand(float t){return(cos(t)+cos(t*1.3+1.3)+cos(t*1.4+1.4))/3.0;}\\n'
+'float getPlasmaY(float x,float hf,float o){return rand(x*lineFrequency+iTime*lineSpeed)*hf*lineAmplitude+o;}\\n'
+'void main(){vec2 fc=gl_FragCoord.xy;vec4 fc2;vec2 uv=fc.xy/iResolution.xy;\\n'
+'vec2 sp=(fc-iResolution.xy/2.0)/iResolution.x*2.0*scale;\\n'
+'float hf=1.0-(cos(uv.x*6.28)*0.5+0.5);float vf=1.0-(cos(uv.y*6.28)*0.5+0.5);\\n'
+'sp.y+=rand(sp.x*warpFrequency+iTime*warpSpeed)*warpAmplitude*(0.5+hf);\\n'
+'sp.x+=rand(sp.y*warpFrequency+iTime*warpSpeed+2.0)*warpAmplitude*hf;\\n'
+'vec4 lns=vec4(0.0);vec4 bg1=vec4(0.0,0.07,0.2,1.0);vec4 bg2=vec4(0.0,0.15,0.35,1.0);\\n'
    +'for(int i=0;i<linesPerGroup;i++){float nli=float(i)/float(linesPerGroup);float ot=iTime*offsetSpeed;\\n'
    +'float op=float(i)+sp.x*offsetFrequency;float rd=rand(op+ot)*0.5+0.5;\\n'
    +'float hw=mix(minLineWidth,maxLineWidth,rd*hf)/2.0;\\n'
    +'float os=rand(op+ot*(1.0+nli))*mix(minOffsetSpread,maxOffsetSpread,hf);\\n'
    +'float lp=getPlasmaY(sp.x,hf,os);\\n'
    +'float ln=drawSmoothLine(lp,hw,sp.y)/2.0+drawCrispLine(lp,hw*0.15,sp.y);\\n'
    +'float cx=mod(float(i)+iTime*lineSpeed,25.0)-12.0;\\n'
    +'vec2 cp=vec2(cx,getPlasmaY(cx,hf,os));\\n'
    +'float ci=drawCircle(cp,0.01,sp)*4.0;ln=ln+ci;lns+=ln*lineColor*rd;}\\n'
    +'fc2=mix(bg1,bg2,uv.x);fc2*=vf;fc2.a=1.0;fc2+=lns;gl_FragColor=fc2;}';
    var check=function(s,l){if(!l)console.error('Shader error: '+gl.getShaderInfoLog(s));};
    var vs=gl.createShader(gl.VERTEX_SHADER);gl.shaderSource(vs,vsSrc);gl.compileShader(vs);check(vs,gl.getShaderParameter(vs,gl.COMPILE_STATUS));
    var fs=gl.createShader(gl.FRAGMENT_SHADER);gl.shaderSource(fs,fsSrc);gl.compileShader(fs);check(fs,gl.getShaderParameter(fs,gl.COMPILE_STATUS));
    var prog=gl.createProgram();gl.attachShader(prog,vs);gl.attachShader(prog,fs);gl.linkProgram(prog);
    if(!gl.getProgramParameter(prog,gl.LINK_STATUS)){console.error('Program error: '+gl.getProgramInfoLog(prog));return;}
    var buf=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,buf);
    gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),gl.STATIC_DRAW);
    var aPos=gl.getAttribLocation(prog,'aVertexPosition');
    var uRes=gl.getUniformLocation(prog,'iResolution'),uTime=gl.getUniformLocation(prog,'iTime');
    function resize(){
        c.width=c.offsetWidth;c.height=c.offsetHeight;
        gl.viewport(0,0,c.width,c.height);
    }
    window.addEventListener('resize',resize);resize();
    var t0=Date.now();
    function frame(){
        var t=(Date.now()-t0)/1000;
        gl.clearColor(0,0,0,1);gl.clear(gl.COLOR_BUFFER_BIT);
        gl.useProgram(prog);
        gl.uniform2f(uRes,c.width,c.height);gl.uniform1f(uTime,t);
        gl.bindBuffer(gl.ARRAY_BUFFER,buf);
        gl.vertexAttribPointer(aPos,2,gl.FLOAT,false,0,0);gl.enableVertexAttribArray(aPos);
        gl.drawArrays(gl.TRIANGLE_STRIP,0,4);
        requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
})();
</script>
'''

def esc(t): return t.replace("'", "\\'").replace('"', '\\"')

def page_style(idx, color_hex, color_dark, hsl):
    c = color_hex
    return f'''        <style>
        :root {{ --accent: {c}; --accent-dark: {color_dark}; --accent-hsl: {hsl}; }}
        body {{ font-family: 'Inter', sans-serif; }}
        .reveal {{ opacity: 0; transform: translateY(30px); }}
        .reveal.visible {{ opacity: 1; transform: translateY(0); transition: opacity 0.6s ease-out, transform 0.6s ease-out; }}
        .reveal-l {{ opacity: 0; transform: translateX(-24px); }}
        .reveal-l.visible {{ opacity: 1; transform: translateX(0); transition: opacity 0.6s ease-out, transform 0.6s ease-out; }}
        .reveal-r {{ opacity: 0; transform: translateX(24px); }}
        .reveal-r.visible {{ opacity: 1; transform: translateX(0); transition: opacity 0.6s ease-out, transform 0.6s ease-out; }}
        details[open] summary {{ color: {c}; }}
        details summary::after {{ content: '+'; float: right; font-size: 1.5em; font-weight: 300; transition: transform 0.3s; }}
        details[open] summary::after {{ content: '\\2013'; }}
        .float-up:hover {{ transform: translateY(-3px); box-shadow: 0 12px 32px -8px rgba(0,0,0,0.1); transition: all 0.3s ease; }}
        #mobileMenu {{
            position: fixed;
            top: 0; right: 0; bottom: 0; left: 0;
            background: #fff;
            z-index: 1000;
            padding: 1.5rem;
            transform: translateX(100%);
            transition: transform 0.3s ease;
            overflow-y: auto;
        }}
        #mobileMenu.active {{
            transform: translateX(0);
        }}
        @media (prefers-reduced-motion: reduce) {{
            .reveal, .reveal-l, .reveal-r {{ opacity: 1 !important; transform: none !important; }}
        }}
        </style>'''

def mobile_menu_script():
    return '''
        const mb = document.getElementById('mobileMenuBtn');
        const mm = document.createElement('div');
        mm.id = 'mobileMenu';
        mm.innerHTML = '<div class="flex justify-between items-center mb-6"><img src="static/images/kw.avif" class="h-10"><button id="closeMobileMenu" class="text-gray-500 hover:text-primary text-2xl">&times;</button></div><nav class="flex flex-col space-y-3 text-lg"><a href="/">Startseite</a><a href="/#about">&Uuml;ber uns</a><a href="/#services">Leistungen</a><a href="/#reviews">Bewertungen</a><a href="/#faq">FAQ</a><a href="/#contact">Kontakt</a><a href="/#appointment" class="block bg-primary text-white text-center py-3 rounded-xl font-semibold mt-4">Termin</a></nav>';
        document.body.appendChild(mm);
        if(mb) { mb.addEventListener('click', () => mm.classList.add('active')); }
        const cm = document.getElementById('closeMobileMenu');
        if(cm) cm.addEventListener('click', () => mm.classList.remove('active'));
        mm.querySelectorAll('a').forEach(l => l.addEventListener('click', () => mm.classList.remove('active')));
    '''

def build_head(svc, idx, color_hex):
    return f'''<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{svc['title']} | Kreuztaler Werkstatt GmbH</title>
    <link rel="icon" type="image/avif" href="static/images/kw.avif">
    <meta name="description" content="{svc['meta']}">
    <meta name="keywords" content="Autowerkstatt, Kreuztal, Kfz-Service, {svc['title']}, Kreuztaler Werkstatt, Reparatur">
    <meta property="og:title" content="{svc['title']} | Kreuztaler Werkstatt GmbH">
    <meta property="og:description" content="{svc['meta']}">
    <meta property="og:image" content="static/images/kw.avif">
    <meta property="og:type" content="website">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com/3.4.16"></script>
    <script>tailwind.config={{theme:{{extend:{{colors:{{primary:'{color_hex}',secondary:'#4a4a4a'}},borderRadius:{{'none':'0px','sm':'4px','rounded':'8px','md':'12px','lg':'16px','xl':'20px','2xl':'24px','3xl':'32px','full':'9999px','button':'8px'}}}}}}}}</script>
    <link rel="preconnect" href="https://fonts.googleapis.com/">
    <link rel="preconnect" href="https://fonts.gstatic.com/" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Arimo:wght@400;600;700;800&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/remixicon@4.5.0/fonts/remixicon.css" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.13.0/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.13.0/ScrollTrigger.min.js"></script>
    <script src="https://unpkg.com/lenis@1.1.20/dist/lenis.min.js"></script>
'''

def build_hero_0(svc, c):
    """Diagonal split - image fills left side with diagonal clip"""
    return f'''    <section class="relative min-h-[60vh] flex overflow-hidden bg-gray-900">
        <div class="absolute inset-0 w-1/2 clip-diagonal z-0">
            <img src="{svc['hero_img']}" alt="{svc['title']}" class="w-full h-full object-cover">
        </div>
        <div class="absolute inset-0 z-[1]" style="background: linear-gradient(to right, transparent 50%, {c}33 100%);"></div>
        <div class="container mx-auto px-4 relative z-10 flex items-center min-h-[60vh]">
            <div class="ml-auto max-w-xl py-20 md:py-28 hero-content">
                <span class="inline-block text-white/50 text-xs uppercase tracking-[0.2em] mb-4 font-mono">{svc['title'].upper()}</span>
                <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold text-white mb-5 leading-[1.1]">{svc['title']}</h1>
                <p class="text-base md:text-lg text-white/80 leading-relaxed max-w-lg">{svc['subtitle']}</p>
                <div class="flex gap-3 mt-8">
                    <a href="/#appointment" class="inline-flex items-center bg-white text-[{c}] px-6 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors shadow-lg"><i class="ri-calendar-line mr-2"></i>Termin</a>
                    <a href="#faq-section" class="inline-flex items-center border border-white/20 text-white/80 px-6 py-3 rounded-lg font-medium hover:bg-white/10 transition-colors"><i class="ri-question-line mr-2"></i>FAQ</a>
                </div>
            </div>
        </div>
        <style>.clip-diagonal{{clip-path:polygon(0 0,100% 0,100% 100%,0 100%)}}@media(min-width:768px){{.clip-diagonal{{clip-path:polygon(0 0,70% 0,50% 100%,0 100%)}}}}</style>
    </section>'''

def build_hero_1(svc, c):
    """Full-bleed dark overlay - centered text"""
    return f'''    <section class="relative min-h-[55vh] flex items-center justify-center overflow-hidden bg-gray-900">
        <img src="{svc['hero_img']}" alt="{svc['title']}" class="absolute inset-0 w-full h-full object-cover opacity-35">
        <div class="absolute inset-0" style="background: linear-gradient(180deg, {c}dd 0%, {c}88 60%, transparent 100%);"></div>
        <div class="absolute inset-0 opacity-10" style="background-image: radial-gradient(circle at 25% 25%, white 1px, transparent 1px); background-size: 40px 40px;"></div>
        <div class="container mx-auto px-4 relative z-10 text-center py-24 md:py-32 hero-content">
            <h1 class="text-5xl md:text-7xl font-bold text-white mb-4 leading-[1.05] tracking-tight">{svc['title']}</h1>
            <p class="text-lg md:text-xl text-white/80 max-w-2xl mx-auto leading-relaxed">{svc['subtitle']}</p>
            <div class="flex flex-wrap justify-center gap-3 mt-8">
                <a href="/#appointment" class="inline-flex items-center bg-white text-[{c}] px-7 py-3.5 rounded-lg font-semibold hover:bg-gray-100 transition-colors shadow-lg"><i class="ri-calendar-line mr-2"></i>Termin vereinbaren</a>
                <a href="/tel:+49273227717" class="inline-flex items-center bg-white/10 text-white border border-white/20 px-7 py-3.5 rounded-lg font-medium hover:bg-white/20 transition-colors"><i class="ri-phone-line mr-2"></i>02732 277 17</a>
            </div>
        </div>
    </section>'''

def build_hero_2(svc, c, cd):
    """Technical dark - dot grid + large icon"""
    icon = svc['hero_icon']
    return f'''    <section class="relative min-h-[50vh] flex items-center overflow-hidden" style="background: linear-gradient(160deg, {cd} 0%, #0f0f0f 100%);">
        <div class="absolute inset-0 opacity-[0.04]" style="background-image: radial-gradient(circle at center, {c} 1px, transparent 1px); background-size: 24px 24px;"></div>
        <div class="absolute top-0 right-0 w-96 h-96 opacity-20" style="background: radial-gradient(circle, {c}88 0%, transparent 70%);"></div>
        <div class="container mx-auto px-4 relative z-10 py-20 md:py-28">
            <div class="grid md:grid-cols-2 gap-12 items-center">
                <div class="hero-content">
                    <span class="inline-block text-[{c}] text-xs uppercase tracking-[0.25em] mb-4 font-mono opacity-70">{svc['title'].upper()}</span>
                    <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold text-white mb-4 leading-[1.08]">{svc['title']}</h1>
                    <p class="text-base md:text-lg text-gray-300 leading-relaxed">{svc['subtitle']}</p>
                    <div class="flex gap-3 mt-8">
                        <a href="/#appointment" class="inline-flex items-center px-6 py-3 rounded-lg font-semibold text-white shadow-lg transition-colors" style="background:{c}; hover:opacity-90"><i class="ri-calendar-line mr-2"></i>Termin</a>
                        <a href="#faq-section" class="inline-flex items-center border border-white/10 text-gray-300 px-6 py-3 rounded-lg font-medium hover:bg-white/5 transition-colors"><i class="ri-question-line mr-2"></i>FAQ</a>
                    </div>
                </div>
                <div class="hidden md:flex justify-center hero-icon">
                    <div class="w-32 h-32 rounded-2xl flex items-center justify-center" style="background: linear-gradient(135deg, {c}33, transparent); border:1px solid {c}44;">
                        <i class="{icon} text-6xl" style="color:{c}"></i>
                    </div>
                </div>
            </div>
        </div>
    </section>'''

def build_hero_3(svc, c):
    """Minimal light - large typography, very airy"""
    return f'''    <section class="relative py-28 md:py-36 overflow-hidden bg-white">
        <div class="absolute top-0 right-0 w-[40vw] h-full opacity-[0.03]" style="background: linear-gradient(135deg, transparent 30%, {c} 100%);"></div>
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto text-center hero-content">
                <span class="inline-block text-[{c}] text-xs uppercase tracking-[0.3em] mb-5 font-mono">{svc['title'].upper()}</span>
                <h1 class="text-5xl md:text-7xl lg:text-8xl font-bold text-gray-900 mb-5 leading-[1.02] tracking-tight">{svc['title']}</h1>
                <p class="text-lg md:text-xl text-gray-500 max-w-2xl mx-auto leading-relaxed">{svc['subtitle']}</p>
                <div class="flex flex-wrap justify-center gap-3 mt-10">
                    <a href="/#appointment" class="inline-flex items-center text-white px-7 py-3.5 rounded-lg font-semibold transition-colors shadow-lg" style="background:{c};"><i class="ri-calendar-line mr-2"></i>Termin</a>
                    <a href="#faq-section" class="inline-flex items-center text-gray-600 border border-gray-200 px-7 py-3.5 rounded-lg font-medium hover:border-gray-300 transition-colors"><i class="ri-question-line mr-2"></i>FAQ</a>
                </div>
            </div>
        </div>
    </section>'''

def build_hero_4(svc, c):
    """Split 50/50 - exact split image/tint"""
    return f'''    <section class="min-h-[55vh] flex overflow-hidden">
        <div class="hidden md:block w-1/2 relative">
            <img src="{svc['hero_img']}" alt="{svc['title']}" class="absolute inset-0 w-full h-full object-cover">
            <div class="absolute inset-0" style="background: linear-gradient(to right, transparent 40%, {c}44 100%);"></div>
        </div>
        <div class="w-full md:w-1/2 flex items-center relative" style="background:{c};">
            <div class="px-8 md:px-16 py-20 md:py-28 hero-content">
                <span class="inline-block text-white/40 text-xs uppercase tracking-[0.25em] mb-4 font-mono">{svc['title'].upper()}</span>
                <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold text-white mb-4 leading-[1.08]">{svc['title']}</h1>
                <p class="text-base md:text-lg text-white/80 leading-relaxed">{svc['subtitle']}</p>
                <div class="flex gap-3 mt-8">
                    <a href="/#appointment" class="inline-flex items-center bg-white text-[{c}] px-6 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors"><i class="ri-calendar-line mr-2"></i>Termin</a>
                    <a href="/tel:+49273227717" class="inline-flex items-center border border-white/20 text-white/80 px-6 py-3 rounded-lg font-medium hover:bg-white/10 transition-colors"><i class="ri-phone-line mr-2"></i>02732 277 17</a>
                </div>
            </div>
        </div>
    </section>'''

def build_hero_5(svc, c, cd):
    """Industrial - dark industrial with mini stats"""
    icon = svc['hero_icon']
    subtitle = svc['subtitle']
    title = svc['title']
    img = svc['hero_img']
    bg_style = f"background: linear-gradient(180deg, #0a0a0a 0%, {cd} 100%);" + ("" if img else " opacity:0.7;")
    return f'''    <section class="relative min-h-[55vh] flex items-center overflow-hidden" style="{bg_style}">
        <div class="absolute inset-0 opacity-[0.07]" style="background-image: repeating-linear-gradient(0deg, transparent, transparent 39px, rgba(255,255,255,0.03) 40px), repeating-linear-gradient(90deg, transparent, transparent 39px, rgba(255,255,255,0.03) 40px);"></div>
        <div class="container mx-auto px-4 relative z-10 py-20 md:py-28">
            <div class="flex flex-col md:flex-row items-center gap-12">
                <div class="flex-1 hero-content">
                    <span class="inline-block text-xs uppercase tracking-[0.25em] mb-4 font-mono" style="color:{c}99;">{title.upper()}</span>
                    <h1 class="text-4xl md:text-6xl font-bold text-white mb-4 leading-[1.06]">{title}</h1>
                    <p class="text-base md:text-lg text-gray-400 leading-relaxed max-w-xl">{subtitle}</p>
                    <div class="flex gap-3 mt-8">
                        <a href="/#appointment" class="inline-flex items-center text-white px-6 py-3 rounded-lg font-semibold transition-colors shadow-lg" style="background:{c};"><i class="ri-calendar-line mr-2"></i>Termin</a>
                        <a href="#faq-section" class="inline-flex items-center border border-white/10 text-gray-400 px-6 py-3 rounded-lg font-medium hover:bg-white/5 transition-colors"><i class="ri-question-line mr-2"></i>FAQ</a>
                    </div>
                </div>
                <div class="flex-shrink-0 hero-icon">
                    <div class="w-28 h-28 rounded-full flex items-center justify-center" style="border:2px solid {c}44;">
                        <i class="{icon} text-5xl" style="color:{c}cc;"></i>
                    </div>
                </div>
            </div>
            <div class="grid grid-cols-3 gap-6 max-w-2xl mx-auto mt-16 pt-12 border-t border-white/5 hero-stats">
                <div class="text-center"><div class="text-2xl font-bold text-white" style="color:{c};">15+</div><div class="text-xs text-gray-500 mt-1">Jahre Erfahrung</div></div>
                <div class="text-center"><div class="text-2xl font-bold text-white" style="color:{c};">5000+</div><div class="text-xs text-gray-500 mt-1">Reparaturen</div></div>
                <div class="text-center"><div class="text-2xl font-bold text-white" style="color:{c};">100%</div><div class="text-xs text-gray-500 mt-1">Zufriedenheit</div></div>
            </div>
        </div>
    </section>'''

HERO_BUILDERS = [build_hero_0, build_hero_1, build_hero_2, build_hero_3, build_hero_4, build_hero_5]

def section_intro(svc, c):
    return f'''    <section class="py-20 md:py-24 bg-white">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto reveal">
                <p class="text-lg md:text-xl text-gray-600 leading-relaxed text-center">{svc['intro']}</p>
            </div>
        </div>
    </section>'''

def section_process(svc, c):
    steps = svc["process"]
    n = len(steps)
    return f'''    <section class="py-20 md:py-24 bg-gray-50">
        <div class="container mx-auto px-4">
            <div class="text-center mb-14">
                <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-3">So l&auml;uft es ab</h2>
                <p class="text-gray-500 max-w-xl mx-auto">In {n} Schritten zu Ihrem Serviceerlebnis</p>
            </div>
            <div class="max-w-5xl mx-auto grid grid-cols-1 md:grid-cols-{n} gap-6">
''' + "\n".join(
        f'''                <div class="bg-white rounded-xl p-7 relative overflow-hidden reveal" style="box-shadow:0 1px 3px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.06);">
                    <div class="text-6xl font-black select-none absolute -top-2 -right-1" style="color:{c}08;">{i+1}</div>
                    <div class="w-12 h-12 rounded-lg flex items-center justify-center mb-4" style="background:{c}15;">
                        <i class="{icon} text-xl" style="color:{c};"></i>
                    </div>
                    <h3 class="font-bold text-gray-900 mb-2">{head}</h3>
                    <p class="text-gray-500 text-sm leading-relaxed">{desc}</p>
                </div>'''
        for i, (head, desc, icon) in enumerate(steps)
    ) + '''
            </div>
        </div>
    </section>'''

def section_content(svc, c):
    items = svc["sections"]
    n = len(items)
    return f'''    <section class="py-20 md:py-24 bg-white">
        <div class="container mx-auto px-4">
            <div class="max-w-5xl mx-auto">
                <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-3 text-center">Das Wichtigste im &Uuml;berblick</h2>
                <p class="text-gray-500 text-center mb-12 max-w-xl mx-auto">Details zu den wichtigsten Aspekten dieses Services</p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
''' + "\n".join(
        f'''                    <div class="p-7 rounded-xl reveal" style="background:{c}04; border:1px solid {c}15;">
                        <div class="w-8 h-8 rounded-lg flex items-center justify-center mb-4" style="background:{c}15;">
                            <svg class="w-4 h-4" style="color:{c};" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        </div>
                        <h3 class="font-bold text-gray-900 mb-2">{heading}</h3>
                        <p class="text-gray-500 text-sm leading-relaxed">{body}</p>
                    </div>'''
        for heading, body in items
    ) + '''
                </div>
            </div>
        </div>
    </section>'''

def section_content_3col(svc, c):
    items = svc["sections"]
    return f'''    <section class="py-20 md:py-24 bg-white">
        <div class="container mx-auto px-4">
            <div class="max-w-6xl mx-auto">
                <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-3 text-center">Das Wichtigste</h2>
                <p class="text-gray-500 text-center mb-12 max-w-xl mx-auto">Alle Details auf einen Blick</p>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
''' + "\n".join(
        f'''                    <div class="p-6 rounded-xl reveal" style="background:{c}04; border:1px solid {c}12;">
                        <div class="w-6 h-6 rounded flex items-center justify-center mb-3" style="background:{c}15;">
                            <svg class="w-3 h-3" style="color:{c};" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
                        </div>
                        <h3 class="font-semibold text-gray-900 text-sm mb-2">{heading}</h3>
                        <p class="text-gray-500 text-xs leading-relaxed">{body}</p>
                    </div>'''
        for heading, body in items[:6]
    ) + '''
                </div>
            </div>
        </div>
    </section>'''

def section_benefits(svc, c):
    items = svc["benefits"]
    return f'''    <section class="py-20 md:py-24" style="background:{c}03;">
        <div class="container mx-auto px-4">
            <div class="max-w-4xl mx-auto">
                <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-3 text-center">Ihre Vorteile</h2>
                <p class="text-gray-500 text-center mb-10 max-w-xl mx-auto">Warum Sie uns vertrauen sollten</p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
''' + "\n".join(
        f'''                    <div class="flex items-start gap-3 p-4 rounded-lg reveal-l">
                        <div class="w-7 h-7 rounded-full flex items-center justify-center flex-shrink-0 mt-0.5" style="background:{c};">
                            <svg class="w-3.5 h-3.5 text-white" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
                        </div>
                        <span class="text-gray-700 text-sm">{item}</span>
                    </div>'''
        for item in items
    ) + '''
                </div>
            </div>
        </div>
    </section>'''

def section_faq(svc, c):
    items = svc["faq"]
    return f'''    <section id="faq-section" class="py-20 md:py-24 bg-white">
        <div class="container mx-auto px-4">
            <div class="max-w-3xl mx-auto">
                <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-3 text-center">H&auml;ufige Fragen</h2>
                <p class="text-gray-500 text-center mb-10 max-w-xl mx-auto">Antworten zu "{svc['title']}"</p>
                <div class="space-y-2">
''' + "\n".join(
        f'''                    <details class="rounded-xl overflow-hidden reveal" style="background:{c}04; border:1px solid {c}10;">
                        <summary class="px-6 py-4 font-medium text-gray-800 cursor-pointer list-none flex justify-between items-center text-sm">{q}</summary>
                        <div class="px-6 pb-5 text-gray-500 text-sm leading-relaxed border-t pt-4 mt-0" style="border-color:{c}15;">{a}</div>
                    </details>'''
        for q, a in items
    ) + '''
                </div>
            </div>
        </div>
    </section>'''

def section_cta(svc, c, cd):
    return f'''    <section class="py-24 relative overflow-hidden" style="background: linear-gradient(135deg, {cd} 0%, #0f0f0f 100%);">
        <div class="absolute inset-0 opacity-[0.03]" style="background-image: url('data:image/svg+xml,<svg width=\\"30\\" height=\\"30\\" viewBox=\\"0 0 30 30\\" xmlns=\\"http://www.w3.org/2000/svg\\"><circle cx=\\"15\\" cy=\\"15\\" r=\\"1.5\\" fill=\\"white\\"/></svg>'); background-size: 30px 30px;"></div>
        <div class="container mx-auto px-4 relative z-10 text-center">
            <p class="text-xl md:text-2xl text-white/90 max-w-3xl mx-auto mb-8 leading-relaxed font-medium">{svc['cta']}</p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="/#appointment" class="inline-flex items-center justify-center bg-white text-[{c}] px-8 py-4 rounded-xl font-bold text-lg hover:bg-gray-100 transition-colors shadow-xl"><i class="ri-calendar-line mr-2"></i>Termin online buchen</a>
                <a href="tel:+49273227717" class="inline-flex items-center justify-center bg-white/10 text-white border border-white/20 px-8 py-4 rounded-xl font-semibold text-lg hover:bg-white/20 transition-colors"><i class="ri-phone-line mr-2"></i>02732 277 17</a>
            </div>
        </div>
    </section>'''

def section_cta_short(svc, c, cd):
    return f'''    <section class="py-16 relative" style="background:{cd};">
        <div class="container mx-auto px-4 text-center">
            <p class="text-lg md:text-xl text-white/90 max-w-3xl mx-auto mb-6 leading-relaxed">{svc['cta']}</p>
            <a href="/#appointment" class="inline-flex items-center bg-white text-[{c}] px-6 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors shadow-lg"><i class="ri-calendar-line mr-2"></i>Termin vereinbaren</a>
        </div>
    </section>'''

SECTION_MAP = {
    'intro': section_intro,
    'process': section_process,
    'content': section_content,
    'benefits': section_benefits,
    'faq': section_faq,
    'cta': section_cta,
}

def build_page(svc, idx):
    color_hex, color_dark, hsl = SERVICE_COLORS[idx]
    c = color_hex
    cd = color_dark
    hero_fn = HERO_BUILDERS[HERO_VARIANTS[idx]]
    section_keys = SECTION_ORDERS[idx]
    
    parts = [
        build_head(svc, idx, color_hex),
        page_style(idx, color_hex, color_dark, hsl),
        '</head>\n<body class="bg-gray-50">\n',
        HEADER,
    ]
    
    # Hero
    if hero_fn in (build_hero_2, build_hero_5):
        parts.append(hero_fn(svc, c, cd))
    else:
        parts.append(hero_fn(svc, c))
    
    # Sections
    last_cta = False
    for sk in section_keys:
        if sk == 'cta':
            parts.append(section_cta(svc, c, cd))
            last_cta = True
        elif sk == 'content':
            parts.append(section_content_3col(svc, c))
        else:
            parts.append(SECTION_MAP[sk](svc, c))
    
    if not last_cta:
        parts.append(section_cta(svc, c, cd))
    
    parts.append(FOOTER_COMMON)
    parts.append('''    <div id="impressumModal" class="fixed inset-0 bg-black/60 hidden flex items-center justify-center z-50">
        <div class="bg-white p-8 rounded-2xl max-w-lg w-full mx-4 relative">
            <button onclick="closeImpressumModal()" class="absolute top-4 right-4 text-gray-400 hover:text-gray-600 text-2xl">&times;</button>
            <h2 class="text-2xl font-bold mb-6" style="color:{c};">Impressum</h2>
            <div class="text-gray-600 space-y-2 text-sm">
                <p class="font-bold">Kreuztaler Werkstatt GmbH</p>
                <p>Gesch&auml;ftsf&uuml;hrer: Andre Hovanski</p>
                <p>Hagener Str. 40, 57223 Kreuztal</p>
                <p>Tel: <a href="tel:+49273227717" class="hover:underline" style="color:{c};">02732 277 17</a></p>
                <p>E-Mail: info@kreuztaler-werkstatt.de</p>
                <hr class="my-3">
                <p>Handelsregister: Amtsgericht Siegen, HRB 13036</p>
                <p>USt-IdNr.: DE351358022</p>
            </div>
        </div>
    </div>
''')
    
    parts.append(f'''    <script>
    document.addEventListener('DOMContentLoaded', function() {{
        const lenis = new Lenis({{duration:1.1,easing:t=>Math.min(1,1.001-Math.pow(2,-10*t))}});
        function raf(t){{lenis.raf(t);requestAnimationFrame(raf)}}
        requestAnimationFrame(raf);
        gsap.registerPlugin(ScrollTrigger);
        {mobile_menu_script()}
        const observe = new IntersectionObserver((entries)=>{{entries.forEach(e=>{{if(e.isIntersecting)e.target.classList.add('visible')}})}},{{threshold:0.12}});
        document.querySelectorAll('.reveal,.reveal-l,.reveal-r').forEach(el=>observe.observe(el));
        gsap.fromTo('.hero-content>*',{{opacity:0,y:30}},{{opacity:1,y:0,duration:0.8,stagger:0.1,ease:'power2.out',delay:0.15}});
        gsap.fromTo('.reveal',{{opacity:0,y:40}},{{opacity:1,y:0,duration:0.6,stagger:0.12,ease:'power2.out',scrollTrigger:{{trigger:'.reveal',start:'top 80%',toggleActions:'play none none none'}}}});
    }});
    function openImpressumModal(){{document.getElementById('impressumModal').classList.remove('hidden');document.body.style.overflow='hidden';}}
    function closeImpressumModal(){{document.getElementById('impressumModal').classList.add('hidden');document.body.style.overflow='';}}
    document.getElementById('impressumModal')?.addEventListener('click',function(e){{if(e.target===this)closeImpressumModal();}});
    </script>
</body>
</html>''')
    
    return '\n'.join(parts)

def main():
    out_dir = r'C:\1,5\my-flask-site-main'
    for idx, svc in enumerate(SERVICES_DATA):
        html = build_page(svc, idx)
        filename = f'leistung-{svc["slug"]}.html'
        filepath = os.path.join(out_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Created {filename} ')
    print(f'\nGenerated {len(SERVICES_DATA)} pages')

if __name__ == '__main__':
    main()