# Restful Booker API – Testare Automată (Python)

## Prezentare proiect
Acest proiect conține **teste automate de tip API** pentru aplicația **Restful Booker** (public demo API).  
Testele sunt implementate în **Python**, folosind **Pytest** și **Requests**, și acoperă **scenarii pozitive, negative și edge cases**.

Scopul proiectului este de a demonstra:
- abilități de **API Automation Testing**
- structură clară și ușor de întreținut
- gestionarea autentificării prin token
- testare negativă și identificare de defecte reale
- bune practici QA

---

## Tehnologii utilizate
- Python 3
- Pytest
- Requests
- REST API
- Postman
- JSON

---

## API testat
- **Base URL:** `https://restful-booker.herokuapp.com`

---

## Structura proiectului
```
Proiect-Restful-Booker-API-Tests/
│
├── api/
│   ├── create_token.py
│   └── restful_booker_requests.py
│
├── tests/
│   ├── test_restful_booking.py
│   └── negative_test_restful_booking.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

---

## Autentificare
Autentificarea se face prin endpoint-ul:
```
POST /auth
```

Token-ul este:
- generat o singură dată pe sesiune folosind un **fixture Pytest**
- transmis în request-uri prin header:
```
Cookie: token=<auth_token>
```

---

## Acoperire teste

### Teste pozitive
- Obținere listă booking IDs
- Creare booking
- Obținere booking după ID
- Update booking (PUT)
- Partial update booking (PATCH)
- Ștergere booking (DELETE)

### Teste negative
- Get booking cu ID inexistent → `404`
- Create booking cu body gol → **BUG (500 în loc de 400)**
- Create booking fără câmpuri obligatorii → **BUG (500 în loc de 400)**
- Update booking fără autentificare → `403`
- Delete booking fără autentificare → `403`
- Delete booking inexistent → `404 / 405`

---

## Defecte identificate (Known Issues)

| Scenariu | Răspuns actual | Răspuns așteptat |
|--------|---------------|-----------------|
| Creare booking cu body gol | 500 Internal Server Error | 400 Bad Request |
| Lipsă câmpuri obligatorii | 500 Internal Server Error | 400 Bad Request |

---

## ▶Rulare teste

### Instalare dependențe
```bash
pip install -r requirements.txt
```

### Rulare toate testele
```bash
pytest -v
```

---

## Colecție Postman
Fișier inclus:
```
Restful_Booker.postman_collection.json
```
---

## Autor
**QA Tester**
