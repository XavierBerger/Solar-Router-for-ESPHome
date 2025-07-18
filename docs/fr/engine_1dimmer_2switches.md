# Engine 1 x dimmer + 2 x switches

Ce package implémente le moteur du routeur solaire qui détermine quand et quelle quantité d'énergie doit être déviée vers trois charges utilisant trois canaux, ou une seule charge avec trois canaux comme un chauffe-eau avec trois résistances de chauffage.

Le moteur utilise 2 relais pour contrôler les différentes charges et d'un régulateur supplémentaire pour un contrôle fin de la puissance. Les charges sont activées de manière séquentielle au fur et à mesure que la puissance devient disponible :
1. 1er canal : Relay 1 (On/Off)
2. 2ème canal: Relay 2 (On/Off)
3. 3ème canal: Un gradateur TRIAC ou SSR (Contrôl variable)

Lorsque les besoins en énergie augmentent :

- Tout d'abord, le régulateur du canal 3 augmente progressivement la puissance.
- Lorsque le régulateur atteint 33,33 %, le relais 1 s'active
- Lorsque le régulateur atteint 66,66 %, le relais 2 s'active

**Le moteur 1 x variateur + 2 x interrupteurs** appelle toutes les secondes le compteur électrique pour obtenir l'énergie réelle échangée avec le réseau. Si l'énergie produite est supérieure à l'énergie consommée et dépasse l'objectif d'échange défini, le moteur déterminera la combinaison appropriée de relais et d'ouverture du régulateur pour atteindre l'objectif.

La régulation automatique du moteur peut être activée ou désactivée à l'aide de du switch d'activation.

## Comment câbler les relais (canaux 1 et 2)

- Ligne sur le relais Commun (COM)
- Normalement ouvert (NO) du relais de la charge d'entrée directement à la charge

## Comment câbler le gradateur (Canal 3)

Comme n'importe quel autre gradateur, l'entrée de la charge est directement reliée à la charge, sans connexion à d'autres relais ou canaux 1 et 2.

## Schema d'exemple de cablage

![Wiring schema example for water heater](images/3ResistorsWaterHeaterExample.svg)

## Configuration

Pour utiliser ce package, ajoutez les lignes suivantes à votre fichier de configuration :

```yaml linenums="1"
packages:
  engine:
    url: https://github.com/XavierBerger/Solar-Router-for-ESPHome/
    files:
      - path: solar_router/engine_1dimmer_2switches.yaml
        vars:
          green_led_pin: GPIO1
          green_led_inverted: 'False'
          yellow_led_pin: GPIO2
          yellow_led_inverted: 'False'
          hide_regulators: 'True'
          hide_leds: 'True'
```
Il est necessaire de définir `green_led_pin` et `yellow_led_pin` dans la section `vars` comme montré dans l'exemple ci-dessus.
 
 * Le paramètre `xxx_led_inverted` permet de définir si la LED est active sur niveau haut ou bas. Ce paramètre est optionnel.
 * Le paramètre `hide_regulators` permet de définir si le capteur de régulateur est affiché dans HA. Ce paramètre est optionnel.
 * Le paramètre `hide_leds` permet de définir si les valeurs des leds sont affichées dans HA. Ce paramètre est optionnel.

!!! note "Distribution de la puissance"
    Le moteur divise la puissance totale disponible en trois parties égales (33,33 % chacune). Cela permet des transitions en douceur entre les différents niveaux de puissance et une distribution efficace de l'énergie solaire excédentaire sur plusieurs charges.

!!! tip "Ajustement du Bypass tempo"
    Le `Bypass tempo` détermine combien de régulations consécutives à 33.33% ou 66.66% sont nécessaires avant d'activer le relais de bypass. Une valeur plus basse rendra le bypass plus réactif mais pourrait causer des commutations plus fréquentes (scintillement). Comme il y a environ 1 régulation par seconde, `Bypass tempo` peut être approximé comme le temps en secondes avec le régulateur à 33.33% ou 66.66% avant que le relais de bypass ne soit activé.


![HA](images/countdown_engine_1dimmer_2switch.png){ align=left }
!!! note ""
    **Capteurs**
    
    * ***Compte à rebours du relai n° X***  
      Pour chaque relai on affiche le compte à rebours en cours.
      Au départ le compte à rebours est égale à la valeur du bypass tempo, puis à chaque régulation d'énergie où le régulateur est à 100% on diminue le compte à rebours, enfin lorsque le compte à rebours est égale à zéro on active le relai.
    * ***Ouverture du régulateur***  
      Caché par défaut (voir `hide_regulators`), permet d'affiché le niveau du régulateur (TRIAC ou SSR).

Ce paquet nécessite l'utilisation du package Relais régulateur ET d'un package régulateur (TRIAC ou SSR). N'oubliez pas de les inclure également.

Vous trouverez ci-dessous l'exemple de configuration pour les relais :

```yaml linenums="1"
packages:
  relay1_regulator:
    url: https://github.com/XavierBerger/Solar-Router-for-ESPHome/
    files:
      - path: solar_router/regulator_mecanical_relay.yaml
        vars:
          relay_regulator_gate_pin: GPIO17
          relay_unique_id: "1"
  relay2_regulator:
    url: https://github.com/XavierBerger/Solar-Router-for-ESPHome/
    files:
      - path: solar_router/regulator_mecanical_relay.yaml
        vars:
          relay_regulator_gate_pin: GPIO18
          relay_unique_id: "2"
```

!!! note "Relay Ids"
    Les identifiants uniques des relais ne peuvent pas être modifiés pour utiliser ce moteur.