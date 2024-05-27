# API REST BOTIGA ONLINE
# Crear un projecte de Django REST FRAMEWORK de nom Api_Store

A través d’aquesta API REST s’hauran de realitzar les accions més importants pròpies d’una botiga online com són: gestionar productes, el seu stock, el carretó de la compra, les comandes i els pagaments.

Dissenyar un model relacional de les taules de les BBDD tenint en compte que com a mínim tindrem les següents taules:
- **client**
- **producte**
- **carreto**
- **comanda**
- **pagament**

On la taula client tindrà els següents camps:
- id (pk)
- nom
- cognoms
- email
- password

**IMPORTANT:** Totes les taules hauran de tenir els camps de control `created_at` i `update_at` i s’hauran de fer servir correctament.

## Desenvolupar l’API REST a través de Django

Aquest projecte haurà de tenir 4 aplicacions:

### CATÀLEG (2,5 punts)

**Gestió del catàleg de productes (mínim 10 registres) (branca catalog).**

#### Accions:
- Afegir nous productes (commit amb missatge).
- Actualitzar productes (commit amb missatge).
- Actualitzar stock productes (commit amb missatge).
- Eliminar productes a través d’un borrat lògic (commit amb missatge).
- Veure tots els productes (commit amb missatge).
- Veure informació detallada d’un producte (commit amb missatge).

#### Condicions:
La taula producte ha de tenir, mínim, 6 camps sense comptar la id i els camps de control.

#### Funcionament:
S’ha de fer un CRUD de productes tenint en compte les accions indicades en l’enunciat.
El borrat lògic significa que els productes no s’eliminen físicament sinó que es “marquen” com a borrats.

#### Dades de retorn:
Cada acció ha de retornar un JSON on com a mínim hi hagi:
- Un estat per indicar si ha anat bé.
- Un missatge informant si l’acció s’ha realitzat correctament o indicant l’error que s’ha produït.

### CARRETÓ (3 punts)

**Gestió del carretó de productes que volem comprar (mínim, un carretó amb 4 productes) (branca cart).**

#### Accions:
- Crear un nou carretó (commit amb missatge).
- Afegir productes al carretó (commit amb missatge).
- Eliminar productes del carretó a través d’un borrat físic (commit amb missatge).
- Eliminar tot el carretó a través d’un borrat físic (commit amb missatge).
- Modificar quantitat d’un producte (commit amb missatge).
- Consultar el llistat de productes del carretó (commit amb missatge).
- Comprar (commit amb missatge).

#### Funcionament:
- Quan es crea un carretó s’haurà de relacionar amb el client.
- No es pot crear un carretó si ja existeix un carretó obert per aquest client.
- Mentres el carretó estigui en estat obert o no finalitzat es poden fer les accions pròpies del carretó.

Un cop es realitza la compra:
- El carretó passarà en un estat finalitzat i ja no es podrà modificar.
- Es crearà un nou registre a la taula de comanda amb la informació necessària del carretó.
- La comanda estarà en un estat obert.

#### Funcionalitats extres (0,5 punts):
Si un producte no té stock, ha d’informar que aquest producte no es pot afegir al carretó.

#### Dades de retorn:
Cada acció ha de retornar un JSON on com a mínim hi hagi:
- Un estat per indicar si l’acció ha anat bé.
- Un missatge informant si l’acció s’ha realitzat correctament o indicant l’error que s’ha produït.
- Informació del carretó.
- Llista de productes on hi hagi: nom producte, unitats i preu per cada producte.
- Preu total del carretó.

### COMANDES (2 punts)

**Gestió de comandes (repartir 10 registres entre cada estat) (branca orders).**

#### Accions:
- Mostrar historial de comandes (commit amb missatge).
- Mostrar historial de comandes per un client en concret (commit amb missatge).
- Mostrar historial de comandes que no estan finalitzades (commit amb missatge).

#### Dades de retorn:
Cada acció ha de retornar un JSON on com a mínim hi hagi:
- Un estat per indicar si l’acció ha anat bé.
- Un missatge informant si l’acció s’ha realitzat correctament o indicant l’error que s’ha produït.
- Informació de la comanda: Ha d’aparèixer la id de la comanda, el total de productes i el preu total de la compra.

### PAGAMENT (2,5 punts)

**Gestió pagaments (simulat) (branca payments).**

#### Accions:
- Pagar una comanda (commit amb missatge).
- Consultar estat comanda (commit amb missatge).

#### Funcionament:
Per poder fer el pagament serà necessari informar:
- Número de tarjeta.
- Data caducitat.
- CVC.

El pagament només es podrà realitzar per aquelles comandes que estiguin obertes.
S’haurà de controlar primerament si la comanda que es vol pagar està oberta.
Un cop realitzada la compra la comanda s’actualitzarà a finalitzada o tancada.

#### Funcionalitats extres (0,5 punts):
Comprobar a través de les regular expressions que el format del número de tarjeta informada és correcte.

#### Dades de retorn:
Cada acció ha de retornar un JSON on com a mínim hi hagi:
- Un estat per indicar si l’acció ha anat bé.
- Un missatge informant si l’acció s’ha realitzat correctament o indicant l’error que s’ha produït.

### A tenir en compte:
- Cal utilitzar `@api_view`, `Response`, queries database, forms per fer POSTS.
- **NO** es demana frontend. Només crear una API amb DRF (Django Rest Framework).
