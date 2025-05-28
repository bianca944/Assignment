Am făcut un proiect simplu cu Arduino UNO care citește temperatura cu un senzor TMP36. Valorile apar în Serial Monitor și se actualizează la fiecare secundă. Am adăugat și o condiție: dacă temperatura trece de 30°C, se activează un buzzer.

Am simulat totul în Tinkercad, pentru că nu am avut placa fizică. Am conectat TMP36 la pinul A0 și buzzerul la pinul digital 8. În cod, temperatura se calculează din voltajul citit de la senzor, iar dacă e prea mare, buzzerul pornește. Am exportat și log-ul din Serial Monitor într-un fișier text.

Este un proiect basic, dar arată cum poate fi folosit un senzor pentru monitorizare + reacție automată.
