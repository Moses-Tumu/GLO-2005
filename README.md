# Comment builder et lancer l'application avec Docker
1. S'assurer d'avoir docker-compose [d'installer](https://docs.docker.com/compose/install/)
2. Depuis un terminal **(lui de PyCharm fait la job)** aller à la racine du projet → /GLO-2005
3. Builder l'app avec la commande suivante → ``docker-compose build``
4. Lancer le container → ``docker-compose up``

#
Pour relancer les containers de manière a ce que les scripts MySQL se relance, faire les commande suivant :
```
> docker system prune --volumes
> y
> docker-compose build
> docker-compose up
```

#
###### En date du 17-04-19 14:00, tout fonctionnait sur [Docker Desktop for Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows), Windows 10 Professionnel version 1809

## Arborescence du projet
* GLO-2005
    * /app
        * app.py
        * Dockerfile
    * /bd_init
    * /doc
        * Rapport-Équipe21.pdf
    * docker-compose.yml
    * README.md
    * .gitignore
    
Lien [GitHub ici](https://github.com/Moses-Tumu/GLO-2005) 

######si le lien ne marche pas
https://github.com/Moses-Tumu/GLO-2005