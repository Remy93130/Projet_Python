Casse brique créé par Remy Barberet et Léo Chardon
dans le cadre du projet casse brique du DUT informatique 1 de Champs sur Marne.

 _____    _____   _       _____   _____   _____    _   _   _   
|  _  \  | ____| | |     /  _  \ |  _  \ |  _  \  | | | | / /  
| |_| |  | |__   | |     | | | | | |_| | | |_| |  | | | |/ /   
|  _  /  |  __|  | |     | | | | |  _  { |  _  /  | | | |\ \   
| | \ \  | |___  | |___  | |_| | | |_| | | | \ \  | | | | \ \  
|_|  \_\ |_____| |_____| \_____/ |_____/ |_|  \_\ |_| |_|  \_\ 

                    ╔═════════════════════╗                    
╔═══════════════════╣ TABLE DES MATIERES  ╠═══════════════════╗
║                   ╚═════════════════════╝                   ║
║                                                             ║
║ I.    OPTIMISATION DU PROGRAMME                             ║
║ II.   ORGANISATION DU PROGRAMME                             ║
║ III.  CHOIX TECHNIQUES                                      ║
║ IV.   PROBLEMES RENCONTRES                                  ║
║                                                             ║
╚═════════════════════════════════════════════════════════════╝


                 ╔════════════════════════════╗                
╔════════════════╣ OPTIMISATION DU PROGRAMME  ╠═══════════════╗
║                ╚════════════════════════════╝               ║
║                                                             ║
║  Pour optimiser le programme nous avons choisis de faire en ║
║  sorte que le programme supprime et affiche uniquement les  ║
║  objets concernés afin que celui-ci soit plus fluide.       ║
║                                                             ║
║  Au début, nous voulions aussi faire en sorte que les       ║
║  briques est une unique couleur, mais que celles-ci se      ║
║  fissurent si la balle les touchais. Mais l'affichage       ║
║  des images faisait trop ralentir les machines donc nous    ║
║  avons remis les niveaux de couleurs pour les briques.      ║
║                                                             ║
║  Pour augmenter la fluidité possible, nous avons retirés    ║
║  la fonction sleep du module time et fait avec un systeme   ║
║  de module (cf tp snake) afin de mieux pouvoir gerer le     ║
║  rafraichissement du programme                              ║
║                                                             ║
╚═════════════════════════════════════════════════════════════╝


                 ╔════════════════════════════╗                
╔════════════════╣ ORGANISATION DU PROGRAMME  ╠═══════════════╗
║                ╚════════════════════════════╝               ║
║                                                             ║
║  Le programme est organisé en fonction qui sont regrouper   ║
║  par thèmes (collision, animation, etc..) pour le futur, ces║
║  thèmes seront ranger dans des modules.                     ║
║                                                             ║
║  Le corps du programme possède quelque variables            ║
║  initialisées pour le bon fonctionnement des fonctions      ║
║  ainsi que la boucle while qui fait tourner le programme,   ║
║  on sort de cette boucle si l'on gagne ou si l'on n'a plus  ║
║  aucune vie, cela va ramener aux lignes de fin du programme ║
║  qui agit en fonction de la victoire ou de la défaite       ║
║                                                             ║
║                                                             ║
╚═════════════════════════════════════════════════════════════╝


                 ╔════════════════════════════╗                
╔════════════════╣     CHOIX TECHNIQUES       ╠═══════════════╗
║                ╚════════════════════════════╝               ║
║                                                             ║
║  Pour tout ce qui est stockage de variable souvent modifier ║
║  tel que la position de la balle ou de la raquette, nous    ║
║  avons utilise des listes ce qui nous permet de ne pas      ║
║  toujours retourner la valeur modifier                      ║
║                                                             ║
║  Quant aux selection de variable specifique comme le mode   ║
║  auto ou encore augmenter le nombre de vie nous ajouter     ║
║  un parametre pour les activer afin de verifier plus vite   ║
║  la presence ou non de bug dans le programme                ║
║                                                             ║
║  Pour certaine variable, nous avons choisi que celle-ci     ║
║  soient globale car elles sont tres souvent utiliser dans   ║
║  les fonctions que l'ont utilise                            ║
║                                                             ║
╚═════════════════════════════════════════════════════════════╝

                 ╔════════════════════════════╗                
╔════════════════╣   PROBLEMES RENCONTRES     ╠═══════════════╗
║                ╚════════════════════════════╝               ║
║                                                             ║
║  A travers le développement du casse brique, il y a eu une  ║
║ multitude de problèmes comme la collision des briques,      ║
║ leurs affichage ou la fluidité du jeu. La fluidité et       ║
║ l'affichage ont été expliqués dans l'optimisation du        ║
║ programme quant aux collisions des briques, le plus gros    ║
║ problèmes était de régler les coordonnées de collisions     ║
║ pour la gauche et la droite car le haut et le bas des       ║
║ briques étaient prioritaires. Les briques sont donc         ║
║ découpées en quatres parties pour la collision, haut,       ║
║ bas, droite et gauche. Mais le haut et le bas recouvrent    ║
║ toute la partie superieur et inferieur de l'écran ainsi     ║
║ si la balle tapait dans les coins haut et bas il pouvait    ║
║ y avoir des bugs car on inverse son axe des ordonnées,      ║
║ ainsi nous avons donc rajoutés des conditions, si la        ║
║ balle monte et qu'elle touche le haut c'est son axe des     ║
║ abcisses qui doit etre inversé  et c'est pareil pour le     ║
║ bas de la brique. Voilà comment les collisions des          ║
║ briques ont été corrigées.                                  ║
║                                                             ║
╚═════════════════════════════════════════════════════════════╝
