# Comment builder et lancer l'application avec Docker

1. S'assurer d'avoir Python 3.7 d'instaler
2. Depuis un terminal **(lui de PyCharm fait la job)** Aller à la racine de l'application → /GLO-2005/app
3. Builder l'app avec la commande suivante → ``docker build --tag <nomQuelconque> .``
4. Lancer le container → ``docker run --name <autreNom> -p 5000:5000 <nomQuelconque>``

Voir [ici](https://www.wintellect.com/containerize-python-app-5-minutes/) pour plus d'information.

#UPDATE
######Cette methode ↓ sera utiliser par les correcteurs. Ne pas utiliser la première ↑. Je la laisse à titre indicatif
1. S'assurer d'avoir docker-compose [d'installer](https://docs.docker.com/compose/install/)
2. Depuis un terminal **(lui de PyCharm fait la job)** aller à la racine du projet → /GLO-2005
3. Builder l'app avec la commande suivante → ``docker-compose build``
4. Lancer le container → ``docker-compose up``