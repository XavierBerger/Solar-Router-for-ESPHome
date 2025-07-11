# Firmware

Le firmware a été divisé en plusieurs *packages* qui peuvent être assemblés selon les besoins de l'utilisateur.

![combinaison des *packages*](images/packages.drawio.png)

Les *packages* sont :

* **Power meter** : conçus pour mesurer l'énergie échangée avec le réseau.
* **Engine** : conçu pour déterminer quelle quantité d'énergie et quand le surplus d'énergie doit être détourné vers la charge.
* **Regulator** : conçu pour canaliser le surplus d'énergie vers une charge désignée.
* **Energy counter** : conçu pour rapporter la quantité d'énergie détournée vers la charge.
* **Temperature limiter** : conçu pour arrêter le système lorsqu'une limite de température est atteinte.
* **Scheduler** : conçu pour planifier des automatisations.

## Packages

Les *packages* peuvent être combinés pour créer une variété de routeurs solaires comme dans les exemples suivants.

### Configuration autonome

Dans cette configuration autonome, un seul ESP32 effectue le travail et exécute les 3 *packages*.

![connexion matérielle](images/standalone.drawio.png){width=374}

### Configuration avec proxy de compteur d'énergie

Dans cette configuration avec proxy, deux ESP effectuent le travail. Le premier (qui pourrait être situé dans le panneau électrique) recueille les informations du compteur d'énergie. Le second (qui pourrait être situé près du chauffe-eau) obtient les informations du compteur d'énergie du premier ESP via le réseau et effectue la régulation.

![connexion matérielle](images/with_proxy.drawio.png){width=535}

!!! Note
    Un proxy de compteur d'énergie ne nécessite pas beaucoup de puissance CPU et pourrait donc être exécuté sur un ESP8285 ou ESP8266.

### Configuration avec plusieurs routeurs solaires

Dans cette configuration à plusieurs routeurs solaires, deux routeurs solaires sont installés. Le premier lit la puissance échangée avec le réseau et détourne le surplus vers un chauffe-eau. Le second lit les informations d'échange de puissance du premier en utilisant un proxy de compteur d'énergie. Sur la base des informations collectées, il détournera le surplus d'énergie vers un système antigel.

![connexion matérielle](images/multiple_routers.drawio.png){width=756}

!!! Note
    La `réactivité` et l'`échange cible avec le réseau` devront être ajustés soigneusement sur les deux routeurs solaires pour éviter les conflits de régulation.
