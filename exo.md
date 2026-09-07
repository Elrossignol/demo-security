1. Créer une api avec fastapi
2. Ajouter 2 endpoints (register et login)
    - register (POST) (username, password, email, role)
        enregistrer l'utilisateur en DB (le mot de passe sera hashé)
    - login (POST) (username, password)
        si les données sont valides renvoyer un token (JWT)
        sinon renvoyer un code 401 (unauthorized)