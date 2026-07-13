// Formular- und Website-Funktionalität
document.addEventListener('DOMContentLoaded', function() {
    let currentDate = new Date();
    let currentMonth = currentDate.getMonth();
    let currentYear = currentDate.getFullYear();
    let selectedDate = null;
    let selectedTime = null;

    // Kalender-Elemente initialisieren
    const monthYearDisplay = document.querySelector('[data-calendar-month]');
    const calendarDays = document.querySelectorAll('.calendar-day');
    const timeSlotsContainer = document.querySelector('.time-slots-container');
    const selectedDateInput = document.getElementById('selected-date');
    const selectedTimeInput = document.getElementById('selected-time');

    // ─── Toast-Benachrichtigungssystem ───────────────────────────
    const TOAST_ICONS = {
        error:   'error',
        warning: 'warning',
        info:    'info',
        success: 'check_circle'
    };

    function showToast(type, title, message, duration) {
        duration = duration || 5000;
        const container = document.getElementById('toast-container');
        if (!container) return;

        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        toast.setAttribute('role', type === 'error' ? 'alert' : 'status');

        toast.innerHTML = `
            <div class="toast-icon">
                <span class="material-symbols-outlined" style="font-variation-settings:'FILL' 1;">${TOAST_ICONS[type] || 'info'}</span>
            </div>
            <div class="toast-body">
                <div class="toast-title">${title}</div>
                ${message ? `<div class="toast-msg">${message}</div>` : ''}
            </div>
            <button type="button" class="toast-close" aria-label="Schließen">
                <span class="material-symbols-outlined" style="font-size:1.125rem;">close</span>
            </button>
            <div class="toast-bar" style="animation-duration:${duration}ms;"></div>
        `;

        container.appendChild(toast);
        requestAnimationFrame(() => toast.classList.add('show'));

        const remove = () => {
            toast.classList.remove('show');
            toast.classList.add('hide');
            setTimeout(() => toast.remove(), 400);
        };

        toast.querySelector('.toast-close').addEventListener('click', remove);
        const timer = setTimeout(remove, duration);
        toast.addEventListener('mouseenter', () => {
            clearTimeout(timer);
            const bar = toast.querySelector('.toast-bar');
            if (bar) bar.style.animationPlayState = 'paused';
        });
        toast.addEventListener('mouseleave', () => {
            const bar = toast.querySelector('.toast-bar');
            if (bar) bar.style.animationPlayState = 'running';
            setTimeout(remove, 1500);
        });
    }

    // ─── Individuelle Validierungsnachrichten ────────────────────
    const FIELD_MESSAGES = {
        name:    { title: 'Name fehlt', msg: 'Bitte geben Sie Ihren Namen ein, damit wir den Termin zuordnen können.' },
        email:   { title: 'E-Mail fehlt', msg: 'Wir benötigen Ihre E-Mail-Adresse, um die Terminbestätigung zu senden.' },
        phone:   { title: 'Telefon fehlt', msg: 'Eine Telefonnummer hilft uns, Sie bei Rückfragen schnell zu erreichen.' },
        service: { title: 'Leistung wählen', msg: 'Bitte wählen Sie die gewünschte Serviceleistung aus dem Dropdown.' },
        privacy: { title: 'Einwilligung nötig', msg: 'Bitte stimmen Sie der Datenschutzerklärung zu, damit wir Ihre Anfrage bearbeiten dürfen.' },
        date:    { title: 'Datum fehlt', msg: 'Bitte wählen Sie zuerst einen Wunschtag im Kalender aus.' },
        time:    { title: 'Uhrzeit fehlt', msg: 'Bitte wählen Sie eine verfügbare Uhrzeit aus den Zeitfenstern.' },
        emailInvalid: { title: 'E-Mail ungültig', msg: 'Die eingegebene E-Mail-Adresse scheint nicht korrekt zu sein. Bitte überprüfen Sie die Schreibweise.' }
    };

    // Monats- und Jahresanzeige aktualisieren
    function updateMonthYearDisplay() {
        const monthNames = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni',
                          'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'];
        if (monthYearDisplay) monthYearDisplay.textContent = `${monthNames[currentMonth]} ${currentYear}`;
    }

    // Kalender aktualisieren
    async function updateCalendar() {
        const firstDay = new Date(currentYear, currentMonth, 1);
        const lastDay = new Date(currentYear, currentMonth + 1, 0);
        const daysInMonth = lastDay.getDate();
        const startingDay = firstDay.getDay() || 7;

        updateMonthYearDisplay();

        calendarDays.forEach(day => {
            day.textContent = '';
            day.className = 'calendar-day';
        });

        let dayCounter = 1;
        for (let i = 0; i < 42; i++) {
            if (i >= startingDay - 1 && dayCounter <= daysInMonth) {
                const date = new Date(currentYear, currentMonth, dayCounter);
                const dateString = formatDateForAPI(date);
                const dayElement = calendarDays[i];
                dayElement.textContent = dayCounter;

                if (isPastDate(date) && !isToday(date)) {
                    dayElement.classList.add('text-outline', 'opacity-40');
                } else if (isWeekend(date) || isGermanHoliday(date)) {
                    dayElement.classList.add('booked');
                } else {
                    getBlockedSlots(dateString).then(blockedSlots => {
                        const totalSlots = getAvailableTimeSlots(date).length;
                        if (blockedSlots.length >= totalSlots) {
                            dayElement.classList.add('booked');
                        } else if (blockedSlots.length > 0) {
                            dayElement.classList.add('partially');
                        } else {
                            dayElement.classList.add('available');
                        }
                    });
                }

                dayCounter++;
            }
        }
    }

    function isWeekend(date) {
        const day = date.getDay();
        return day === 0 || day === 6;
    }

    function isPastDate(date) {
        const today = new Date();
        today.setHours(0, 0, 0, 0);
        return date < today;
    }

    function isPastTime(time, date) {
        const now = new Date();
        const [hours, minutes] = time.split(':').map(Number);
        const slotTime = new Date(date);
        slotTime.setHours(hours, minutes, 0, 0);
        return slotTime < now;
    }

    function getAvailableTimeSlots(date) {
        const slots = [];
        const startMorning = 9;
        const endMorning = 13;
        const startAfternoon = 14;
        const endAfternoon = 17;

        for (let hour = startMorning; hour < endMorning; hour++) {
            const time = `${hour.toString().padStart(2, '0')}:00`;
            slots.push({ time, available: !isPastTime(time, date) });
            const time30 = `${hour.toString().padStart(2, '0')}:30`;
            slots.push({ time: time30, available: !isPastTime(time30, date) });
        }

        for (let hour = startAfternoon; hour < endAfternoon; hour++) {
            const time = `${hour.toString().padStart(2, '0')}:00`;
            slots.push({ time, available: !isPastTime(time, date) });
            const time30 = `${hour.toString().padStart(2, '0')}:30`;
            slots.push({ time: time30, available: !isPastTime(time30, date) });
        }

        return slots;
    }

    async function getBlockedSlots(date) {
        try {
            const response = await fetch('/api/appointments');
            if (!response.ok) throw new Error('API-Fehler');
            const data = await response.json();
            return data.blocked_slots[date] || [];
        } catch (error) {
            return [];
        }
    }

    // Zeitfenster aktualisieren
    async function updateTimeSlots(dateString) {
        const slots = getAvailableTimeSlots(new Date(dateString));
        timeSlotsContainer.innerHTML = '';

        const blockedSlots = await getBlockedSlots(dateString);

        slots.forEach(slot => {
            const button = document.createElement('button');
            button.type = 'button';

            const isBlocked = blockedSlots.includes(slot.time);
            const isAvailable = slot.available && !isBlocked;

            button.className = isBlocked
                ? 'flex items-center justify-center gap-1 disabled'
                : isAvailable
                    ? 'flex items-center justify-center gap-1'
                    : 'flex items-center justify-center gap-1 disabled';

            button.textContent = slot.time;
            button.disabled = !isAvailable;

            if (isAvailable) {
                button.onclick = async function(e) {
                    e.preventDefault();
                    timeSlotsContainer.querySelectorAll('button').forEach(btn => {
                        btn.classList.remove('bg-primary-container', 'text-on-primary-container', 'border-primary-container');
                    });
                    this.classList.add('bg-primary-container', 'text-on-primary-container', 'border-primary-container');
                    selectedTimeInput.value = this.textContent.trim();
                    updateSelectedDateTimeDisplay();
                };
            } else {
                const icon = document.createElement('span');
                icon.className = 'material-symbols-outlined';
                icon.style.cssText = 'font-size:0.875rem;';
                icon.textContent = isBlocked ? 'lock' : 'schedule';
                button.appendChild(icon);
            }

            timeSlotsContainer.appendChild(button);
        });
    }

    // Ausgewählte Datum/Uhrzeit anzeigen
    function updateSelectedDateTimeDisplay() {
        const dateVal = selectedDateInput.value;
        const time = selectedTimeInput.value;
        if (!dateVal || !time) return;

        const date = new Date(dateVal + 'T00:00:00');
        const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        const formattedDate = date.toLocaleDateString('de-DE', options);

        let displayContainer = document.getElementById('selected-date-time-display');
        const appointmentForm = document.getElementById('appointment-form');
        if (!displayContainer && appointmentForm) {
            displayContainer = document.createElement('div');
            displayContainer.id = 'selected-date-time-display';
            displayContainer.className = 'p-3 bg-primary-container/5 border border-primary-container/20 rounded-md flex items-center gap-2 text-sm';
            appointmentForm.insertBefore(displayContainer, appointmentForm.firstChild);
        }
        if (displayContainer) {
            displayContainer.innerHTML = `<span class="material-symbols-outlined text-primary-container" style="font-size:1.125rem;">event_available</span><span class="text-on-surface"><strong>${formattedDate}</strong> &middot; ${time} Uhr</span>`;
        }
    }

    function isToday(date) {
        const today = new Date();
        return date.getDate() === today.getDate() &&
               date.getMonth() === today.getMonth() &&
               date.getFullYear() === today.getFullYear();
    }

    // Deutsche Feiertage
    function isGermanHoliday(date) {
        const year = date.getFullYear();
        const month = date.getMonth() + 1;
        const day = date.getDate();

        const fixedHolidays = [
            { month: 1, day: 1 }, { month: 4, day: 25 }, { month: 5, day: 1 },
            { month: 10, day: 3 }, { month: 12, day: 25 }, { month: 12, day: 26 }
        ];
        for (const h of fixedHolidays) {
            if (month === h.month && day === h.day) return true;
        }

        const easter = calculateEaster(year);
        const offsets = [-2, 1, 39, 50];
        for (const off of offsets) {
            const hd = new Date(easter);
            hd.setDate(easter.getDate() + off);
            if (month === hd.getMonth() + 1 && day === hd.getDate()) return true;
        }
        return false;
    }

    function calculateEaster(year) {
        const a = year % 19, b = Math.floor(year / 100), c = year % 100;
        const d = Math.floor(b / 4), e = b % 4, f = Math.floor((b + 8) / 25);
        const g = Math.floor((b - f + 1) / 3), h = (19 * a + b - d - g + 15) % 30;
        const i = Math.floor(c / 4), k = c % 4;
        const l = (32 + 2 * e + 2 * i - h - k) % 7;
        const m = Math.floor((a + 11 * h + 22 * l) / 451);
        const month = Math.floor((h + l - 7 * m + 114) / 31);
        const day = ((h + l - 7 * m + 114) % 31) + 1;
        return new Date(year, month - 1, day);
    }

    // Navigations-Buttons
    const prevButton = document.getElementById('cal-prev');
    const nextButton = document.getElementById('cal-next');

    if (prevButton) {
        prevButton.addEventListener('click', function(e) {
            e.preventDefault();
            currentMonth--;
            if (currentMonth < 0) { currentMonth = 11; currentYear--; }
            updateCalendar();
        });
    }
    if (nextButton) {
        nextButton.addEventListener('click', function(e) {
            e.preventDefault();
            currentMonth++;
            if (currentMonth > 11) { currentMonth = 0; currentYear++; }
            updateCalendar();
        });
    }

    // Datumauswahl
    calendarDays.forEach(day => {
        day.addEventListener('click', function() {
            if (this.classList.contains('opacity-40') || this.classList.contains('booked')) return;
            if (!this.textContent.trim()) return;

            calendarDays.forEach(d => d.classList.remove('selected'));
            this.classList.add('selected');

            const selectedDay = parseInt(this.textContent);
            const selDate = new Date(currentYear, currentMonth, selectedDay);
            const formattedDate = formatDateForAPI(selDate);
            selectedDateInput.value = formattedDate;

            updateTimeSlots(formattedDate);
        });
    });

    updateCalendar();
    updateSelectedDateTimeDisplay();

    // ─── Formular absenden mit individueller Validierung ─────────
    const appointmentForm = document.getElementById('appointment-form');
    if (appointmentForm) {
        appointmentForm.addEventListener('submit', async function(e) {
            e.preventDefault();

            const name = document.getElementById('name');
            const email = document.getElementById('email');
            const phone = document.getElementById('phone');
            const service = document.getElementById('service');
            const privacy = document.getElementById('privacy-consent');

            // Pflichtfelder einzeln prüfen — erste Lücke gewinnt
            const checks = [
                { el: name,    key: 'name' },
                { el: email,   key: 'email', validate: v => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) },
                { el: phone,   key: 'phone' },
                { el: service, key: 'service' }
            ];

            // Visuelles Reset
            [name, email, phone, service].forEach(el => {
                if (el) el.classList.remove('border-error', 'ring-1', 'ring-error');
            });

            let firstError = null;
            for (const c of checks) {
                if (!c.el || !c.el.value.trim()) {
                    firstError = FIELD_MESSAGES[c.key];
                    c.el && c.el.classList.add('border-error');
                    break;
                }
                if (c.validate && !c.validate(c.el.value.trim())) {
                    firstError = FIELD_MESSAGES.emailInvalid;
                    c.el.classList.add('border-error');
                    break;
                }
            }

            if (!firstError && privacy && !privacy.checked) {
                firstError = FIELD_MESSAGES.privacy;
            }
            if (!firstError && !selectedDateInput.value) {
                firstError = FIELD_MESSAGES.date;
            }
            if (!firstError && !selectedTimeInput.value) {
                firstError = FIELD_MESSAGES.time;
            }

            if (firstError) {
                showToast('warning', firstError.title, firstError.msg);
                return;
            }

            const formData = {
                date: selectedDateInput.value,
                time: selectedTimeInput.value,
                client: { name: name.value, email: email.value, phone: phone.value },
                service: service.value,
                message: document.getElementById('message').value
            };

            // Submit-Button sperren + Ladeanzeige
            const submitBtn = appointmentForm.querySelector('button[type="submit"]');
            const btnLabel = submitBtn ? submitBtn.innerHTML : '';
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<span class="material-symbols-outlined animate-spin">progress_activity</span><span>Wird gesendet…</span>';
            }

            try {
                const response = await fetch('/api/appointments', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
                    body: JSON.stringify(formData)
                });

                if (!response.ok) {
                    const errorData = await response.json().catch(() => ({}));
                    throw new Error(errorData.error || 'Server antwortet nicht');
                }

                await response.json();

                const serviceText = service.options[service.selectedIndex].text;
                const waText = encodeURIComponent(`Guten Tag, ich habe soeben einen Termin auf Ihrer Website angefragt.\n\n*Name:* ${formData.client.name}\n*Telefon:* ${formData.client.phone}\n*Leistung:* ${serviceText}\n*Datum:* ${formData.date}\n*Uhrzeit:* ${formData.time}\n*Nachricht:* ${formData.message || '-'}\n\nBitte bestätigen Sie meine Anfrage.`);
                const waUrl = `https://wa.me/491797399039?text=${waText}`;

                // Erfolgsmeldung im Luminous-Precision-Stil
                const successMessage = document.createElement('div');
                successMessage.className = 'glass-panel rounded-xl p-8 text-center relative overflow-hidden';
                successMessage.innerHTML = `
                    <div class="absolute inset-0 bg-primary-container/5 pointer-events-none"></div>
                    <div class="relative">
                        <div class="w-16 h-16 mx-auto mb-5 rounded-full bg-primary-container/10 flex items-center justify-center">
                            <span class="material-symbols-outlined text-primary-container" style="font-size:2rem; font-variation-settings:'FILL' 1;">check_circle</span>
                        </div>
                        <h3 class="font-headline text-2xl text-on-surface mb-2">Terminanfrage übermittelt</h3>
                        <p class="text-on-surface-variant mb-6 max-w-sm mx-auto leading-relaxed">
                            Vielen Dank, <strong class="text-on-surface">${formData.client.name}</strong>!
                            Ihre Anfrage für <strong class="text-primary">${serviceText}</strong> am
                            <strong class="text-on-surface">${formData.date}</strong> um
                            <strong class="text-on-surface">${formData.time} Uhr</strong> ist eingegangen.
                            Wir melden uns zur Bestätigung.
                        </p>
                        <div class="bg-surface-container-lowest border border-outline-variant/40 rounded-lg p-4 max-w-sm mx-auto">
                            <p class="font-mono text-xs text-on-surface-variant uppercase tracking-wider mb-3">Schnellere Bestätigung</p>
                            <a href="${waUrl}" target="_blank" rel="noopener"
                               class="flex items-center justify-center gap-2 w-full bg-primary-container text-on-primary-container py-3 px-4 rounded-md font-medium transition-all hover:shadow-[inset_0_0_12px_rgba(13,105,171,0.6)] active:scale-95">
                                <span class="material-symbols-outlined">forum</span>
                                <span>Details per WhatsApp senden</span>
                            </a>
                        </div>
                        <button type="button" id="new-appointment-btn"
                                class="mt-4 font-mono text-xs text-on-surface-variant hover:text-primary transition-colors uppercase tracking-wider">
                            Neue Anfrage stellen
                        </button>
                    </div>
                `;

                appointmentForm.style.display = 'none';
                appointmentForm.parentNode.insertBefore(successMessage, appointmentForm);

                document.getElementById('new-appointment-btn').addEventListener('click', function() {
                    successMessage.remove();
                    appointmentForm.style.display = '';
                    appointmentForm.reset();
                    selectedDateInput.value = '';
                    selectedTimeInput.value = '';
                    const disp = document.getElementById('selected-date-time-display');
                    if (disp) disp.remove();
                    calendarDays.forEach(d => d.classList.remove('selected'));
                    timeSlotsContainer.innerHTML = '';
                    updateCalendar();
                });

                showToast('success', 'Anfrage gesendet', 'Wir melden uns innerhalb der Geschäftszeiten zur Bestätigung.', 6000);
            } catch (error) {
                showToast('error', 'Senden fehlgeschlagen',
                    'Ihre Anfrage konnte nicht übermittelt werden. Bitte versuchen Sie es erneut oder rufen Sie uns an: 02732 277 17.', 8000);
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = btnLabel;
                }
            }
        });
    }

    function formatDateForAPI(date) {
        const y = date.getFullYear();
        const m = String(date.getMonth() + 1).padStart(2, '0');
        const d = String(date.getDate()).padStart(2, '0');
        return `${y}-${m}-${d}`;
    }
});
