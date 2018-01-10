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
║  rafraichissement du programme.                             ║
║                                                             ║
║  Lors du Premier rendus, notre casse brique ne possedait pas║
║  de vecteur vitesse, la balle ne faisait que s'incrementer  ║
║  de 1 par rafraichissement, désormais il y a la possibilité ║
║  de modifier ce vecteur vitesse, ainsi la balle peut        ║
║  s'incrementer de 1 comme de 3 sans pour autant avoir des   ║
║  problèmes avec la collision. Cette optimisation permet aux ║
║  machines lentes de pouvoir jouer sans problèmes.           ║
║                                                             ║
╚═════════════════════════════════════════════════════════════╝


                 ╔════════════════════════════╗                
╔════════════════╣ ORGANISATION DU PROGRAMME  ╠═══════════════╗
║                ╚════════════════════════════╝               ║
║                                                             ║
║  Le programme est organisé en fonctions qui sont regrouper  ║
║  par thèmes (collision, animation, etc..) pour le futur, ces║
║  thèmes seront ranger dans des modules.                     ║
║                                                             ║
║  Le corps du programme possède quelque variables            ║
║  initialisées pour le bon fonctionnement des fonctions      ║
║  ainsi que la boucle while qui fait tourner le programme,   ║
║  on sort de cette boucle si l'on gagne ou si l'on n'a plus  ║
║  aucune vie, cela va ramener aux lignes de fin du programme ║
║  qui agit en fonction de la victoire ou de la défaite.      ║
║                                                             ║
║  Lorsque le joueur perd ou gagne, il a la possibilité de    ║
║  directement relancer une partie dans une nouvelle fenêtre  ║
║  en appuyant sur R, d'où l'interêt de couper le code en     ║
║  différents fichiers qui peuvent s'appeler les uns et       ║
║  les autres.                                                ║
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
║  Désormais, seul le main.py possède un corps, tout nos      ║
║  autres fichier possède des fonctions qui contribue aux jeu ║
║  même les variables sont maintenant dans des fonctions      ║
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
║ découpées en quatre parties pour la collision, haut,        ║
║ bas, droite et gauche. Mais le haut et le bas recouvrent    ║
║ toute la partie superieur et inferieur de l'écran ainsi     ║
║ si la balle tapait dans les coins haut et bas il pouvait    ║
║ y avoir des bugs car on inverse son axe des ordonnées,      ║
║ ainsi nous avons donc rajoutés des conditions, si la        ║
║ balle monte et qu'elle touche le haut c'est son axe des     ║
║ abscisses qui doit etre inversé  et c'est pareil pour le    ║
║ bas de la brique. Voilà comment les collisions des          ║
║ briques ont été corrigées.                                  ║
║                                                             ║
║ Après avoir insérer un vecteur vitesse, il y a eu d'autres  ║
║ problèmes avec la collision, notamment lorsque la balle     ║
║ possedait un vecteur vitesse trop important, mais nous avons║
║ su corriger ce problème en utilisant plus de précisions     ║
║ sur les coordonnées de la balle et des briques dans notre   ║
║ programme.                                                  ║
║                                                             ║
║ La gestion du menu pause était aussi assez compliquée.      ║
║ En effet, il fallait utiliser les fonctions événements de   ║
║ la bibliothèque upemtk en même temps que les déplacements   ║
║ de la raquette car un seul événement peut donner plusieurs  ║
║ possibilité ( position de la souris, clic ou touche)        ║
║ c'est pour cette raison que la fonction pause a uniquement  ║
║ la possibilité d'être appelée dans la fonction qui          ║
║ contrôle la raquette.                                       ║
║                                                             ║
╚═════════════════════════════════════════════════════════════╝