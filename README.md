# Comment builder et lancer l'application avec Docker
1. S'assurer d'avoir docker-compose [d'installer](https://docs.docker.com/compose/install/)
2. Depuis un terminal **(lui de PyCharm fait la job)** aller à la racine du projet → /GLO-2005
3. Builder l'app avec la commande suivante → ``docker-compose build``
4. Lancer le container → ``docker-compose up``

#
Pour relancer les containers de manière a ce que les données MySQL, faire les commande suivant :
```
> docker system prune --volumes
> y
> docker-compose build
> docker-compose up
```