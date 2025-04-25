// Hauptskript für die Website-Funktionalität
document.addEventListener('DOMContentLoaded', function() {
    // Initialisierung des mobilen Menüs
    const mobileMenuButton = document.querySelector('button[aria-label="Menu"]');
    const mobileMenu = document.querySelector('nav');
    
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // Initialisierung des Kalenders
    const calendarDays = document.querySelectorAll('.calendar-day');
    if (calendarDays.length > 0) {
        calendarDays.forEach(day => {
            if (!day.classList.contains('text-gray-400')) {
                day.addEventListener('click', function() {
                    calendarDays.forEach(d => d.classList.remove('selected'));
                    this.classList.add('selected');
                });
            }
        });
    }

    // Initialisierung des Chatbots
    const chatToggle = document.getElementById('chat-toggle');
    const chatWindow = document.getElementById('chat-window');
    const chatClose = document.getElementById('chat-close');
    const chatBody = document.getElementById('chat-body');
    const chatOptions = document.querySelectorAll('.chat-option');
    
    if (chatToggle && chatWindow && chatClose && chatBody && chatOptions.length > 0) {
        chatToggle.addEventListener('click', function() {
            chatWindow.classList.add('active');
        });
        
        chatClose.addEventListener('click', function() {
            chatWindow.classList.remove('active');
        });
        
        chatOptions.forEach(option => {
            option.addEventListener('click', function() {
                const optionType = this.getAttribute('data-option');
                const userMessage = document.createElement('div');
                userMessage.className = 'chat-message user-message';
                userMessage.textContent = this.textContent;
                chatBody.appendChild(userMessage);
                chatBody.scrollTop = chatBody.scrollHeight;
                
                setTimeout(() => {
                    const botMessage = document.createElement('div');
                    botMessage.className = 'chat-message bot-message';
                    
                    switch(optionType) {
                        case 'appointment':
                            botMessage.innerHTML = 'Gerne helfe ich Ihnen bei der Terminvereinbarung. Bitte teilen Sie mir folgende Informationen mit:<br><br>1. Welches Fahrzeug haben Sie? (Marke, Modell)<br>2. Welchen Service benötigen Sie?<br>3. Wann würden Sie gerne einen Termin haben?';
                            break;
                        case 'availability':
                            botMessage.innerHTML = 'Aktuell haben wir in dieser Woche noch freie Termine am Mittwoch und Freitag. Nächste Woche sind noch viele Termine verfügbar. Für welchen Tag möchten Sie die Verfügbarkeit prüfen?';
                            break;
                        case 'services':
                            botMessage.innerHTML = 'Wir bieten folgende Leistungen an:<br><br>• Wartung & Inspektion<br>• Unfallinstandsetzung<br>• 3D Achsvermessung<br>• Diagnose<br>• Service für alle Marken<br><br>Zu welchem Service möchten Sie mehr Informationen?';
                            break;
                        case 'faq':
                            botMessage.innerHTML = 'Hier sind einige häufig gestellte Fragen:<br><br>• Wie lange dauert eine Inspektion?<br>• Bieten Sie einen Hol- und Bringservice an?<br>• Kann ich während der Reparatur ein Ersatzfahrzeug bekommen?<br>• Wie funktioniert die Abwicklung mit der Versicherung?<br><br>Welche Frage haben Sie?';
                            break;
                        case 'contact':
                            botMessage.innerHTML = 'Sie können uns telefonisch unter +49 2732 27717 erreichen oder eine E-Mail an info@kreuztaler-werkstatt.de senden. Möchten Sie, dass ein Mitarbeiter Sie zurückruft?';
                            break;
                        default:
                            botMessage.innerHTML = 'Entschuldigung, ich konnte Ihre Anfrage nicht verstehen. Bitte wählen Sie eine der verfügbaren Optionen.';
                    }
                    
                    chatBody.appendChild(botMessage);
                    chatBody.scrollTop = chatBody.scrollHeight;
                }, 500);
            });
        });
    }
}); 