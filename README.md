Projekt stworzony w ramach kursu Metody Wytwarzania Oprogramowania prowadzonego na Politechnice Wrocławskiej w semestrze zimowym 2025/2026.  
Autorzy projektu:  
-  Piotr Kozarzewski  
-  Dawid Nowak  
  
Celem projektu jest zaznajomienie się ze współczesnymi praktykami tworzenia oprogramowania oraz wdrożenie ich.  
Tematem projektu jest stworzenie strony internetowej pozwalającej na komunikację z chatbotem doradzającym użytkownikowi w zakresie inwestowania.  
  
W celu stworzenia środowiska dla backendu wykonać w folderze backend:  
1.  python -m venv venv  
2.  source venv/bin/activate  # lub venv\Scripts\activate (Windows)  
3.  uvicorn app.main:app --reload --host 127.0.0.1 --port 8081  
    -  w przypadku problemów z portem należy go skorygować zarówno w komendzie uruchamiającej jak i kodzie frontendu - plik _frontend/src/config.js_  
4.  utworzyć plik .env w folderze backend oraz wpisać w nim odpowiednie klucze AI ze strukturą (dane przykładowe):  
    -  OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx 
    -  OPENAI_MODEL=gpt-4o-mini  
  
W celu uruchomienia backendu wykonać w folderze backend:  
1.  python app\main.py  
  
W celu stworzenia środowiska dla frontendu wykonać w folderze frontend:  
1.  npm install  
  
W celu uruchomienia frontendu wykonać w folderze backend:  
1.  npm run dev  
  
Projekt powinien być dostępny w przeglądarce pod adresem: http://localhost:5173  
  
