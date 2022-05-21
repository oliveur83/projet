 <!-- 2er page partie formateur 
 sur cette page nous pouvons voir historique -->
<?php
session_start();
?>

<!DOCTYPE html><FONT size="5">
<head>

	<link rel="stylesheet" href="choixQCM.CSS"> 
</head>
<html>
<body>
<?php
$var_t= 0; // verifie dans la base si oui ou non les identifant et mp sont juste 
$bdd= new PDO ('mysql:host=localhost;dbname=stage_s4','root','');
   // differente requete pour les different cas 
       $req=$bdd->query("SELECT * FROM historique GROUP BY idhis DESC ");
       $req1=$bdd->query("SELECT * FROM historique GROUP BY idhis ASC ");
       $req2=$bdd->query("SELECT * FROM historique  GROUP BY score DESC ");
       $req3=$bdd->query("SELECT * FROM historique GROUP BY score ASC ");
       $req4=$bdd->query("SELECT * FROM utilisateur GROUP BY prenom ASC ");
       $req5=$bdd->query("SELECT * FROM historique");
      
 ?>        
   <!-- different bouton pour organisé la visualisation de historique -->
 <!--  toto tant la reference des bouton -->
 <table border=1>  <?php 
          echo "<td>UTILISATEUR</td><td> DATE </td> <td>SCORE </td> <td>n°QCM</td> <td></td></tr>";
                   echo "<td>"   ?> <form method="post" action="accesformateur2.php">
                   <input type ="submit" name="toto"value="Liste des utilisateurs" /><?php 
                   echo "</td><td> "?> 
                   <input type ="submit" name="toto"value="Plus recente" />
                   <input type ="submit" name="toto"value="Plus ancienne" />  <?php 
                   echo "</td> <td>"?> 
                   <input type ="submit" name="toto"value="Plus haut" />
                   <input type ="submit" name="toto"value="Plus bas" /> </form> <?php 
                   "</td> <td></td> <td></td></tr>";?> 

    <!--  div droite pour mettre bouton de decoonexion et intervalle des dates -->
    <div class="droite">
              <form method="post" action="index.php">
                   <input type ="submit" value="Déconnexion" style=";height:30px;font-size:20px" />
            </form>   
            <form method="post" action="accesformateur2.php">
         choisir un intervalle<?php  echo "<br>"; ?> 
               <input type="date" name="debut" />  <?php  echo "<br>"; ?> 
             à 
 <?php   echo "<br>";?> 
               <input type="date" name="fin" />
               <?php   echo "<br>";?> 
               <input type ="submit"name="toto" value="Valider" style=";height:30px;font-size:20px"/>
               <?php echo "<br>"; ?> 
               nb: AAAA-MM-JJ </form> 
               trie par QCM:
               <form method="post" action="accesformateur2.php">
                                 <select name="totor">
                                       <option value='0'>tout</option>
                                       <option value='1'>1</option>
                                     <option value='2'>2</option>
                                      <option value='3'>3</option>
                                         <option value='4'>4</option>
                                         <option value='5'>5</option>
                                       <option value='6'>6</option>
                                     <option value='7'>7</option>
                                      <option value='8'>8</option>

                                 </select>
                                 <?php   echo "<br>";?> 
               <input type ="submit"name="toto" value="Valider" style=";height:30px;font-size:20px"/>
                </form>  
      </div> 
<?php
//------------------------------------------------------------------------------
   if(isset($_POST['totor']))// pour le trie du QCM ligne 57
   {   
   echo "</tr>";
      while ($ligne= $req5->fetch())//recherche dans historique 
      { 
         if ($_POST['totor']==0)// si il égale a 0 c'est tout les QCM
         { echo "</tr>";
                                 // affiche email en lien la date le score et le QCM
                                 echo'<td><a href="profil.php?id='.$ligne['e_mail']. '">'.$ligne['e_mail']. '</a></td>'   ;
                                 echo "<td>".$ligne['datee']."</td> <td>".$ligne['score']."</td> <td>".$ligne['idQCM']."</td>";
                                    echo" <td>"; ?> 
                                   <!-- bouton voir plus pour voir les dernier resultat -->
                                  <form method="post" action="resultatutil.php">
                                     <input type ="submit" value="Voir plus  " />    
                                    <input type="text" name="toto" value="<?php echo $ligne['e_mail'] ?>" style="display:none" />
                               </form>  
              <?php
                               echo "</td>";
                               echo "</tr>";
         }
         elseif($_POST['totor']==$ligne['idQCM'])
              {         echo "</tr>";       
                     // affiche email en lien la date le score et le QCM
                  echo'<td><a href="profil.php?id='.$ligne['e_mail']. '">'.$ligne['e_mail']. '</a></td>'   ;
                   echo "<td>".$ligne['datee']."</td> <td>".$ligne['score']."</td> <td>".$ligne['idQCM']."</td>";
                      echo" <td>"; ?> 
                     <!-- bouton voir plus pour voir les dernier resultat -->
                    <form method="post" action="resultatutil.php">
                       <input type ="submit" value="Voir plus  " />    
                      <input type="text" name="toto" value="<?php echo $ligne['e_mail'] ?>" style="display:none" />
                 </form>  
<?php
                 echo "</td>";
                 echo "</tr>";
            }
   }
   }
   //---------------------------------------------------------------------------------------------
    if(isset($_POST['toto']))//  si pour les lignes 29 a 38
    {
       if($_POST['toto']=='Plus recente')// clique sur le bouton date la plus recente 
          {
            echo "</tr>";
                 while ($ligne=$req->fetch())
                 {  // affiche email en lien la date le score et le QCM
                      echo'<td><a href="profil.php?id='.$ligne['e_mail']. '">'.$ligne['e_mail']. '</a></td>'   ;
                     echo "<td>".$ligne['datee']."</td> <td>".$ligne['score']."</td> <td>".$ligne['idQCM']."</td>";
                     
                    echo" <td>"; ?> 
                     <!-- bouton voir plus pour voir les dernier resultat -->
                    <form method="post" action="resultatutil.php">
                       <input type ="submit" value="Voir plus  " />    
                       <input type="text" name="toto" value="<?php echo $ligne['e_mail'] ?>" style="display:none" />
                  </form>  <?php
                      echo "</td>";
                     echo "</tr>";
                 } 
 ?>
                 </table>
 <?php
          }  
           elseif($_POST['toto']=='Plus ancienne')// clique sur le bouton date la plus ancienne 
               {
                  echo "</tr>";
                 while ($ligne=$req1->fetch())//recherche dans historique 
                 { 
                     // affiche email en lien la date le score et le QCM
                      echo'<td><a href="profil.php?id='.$ligne['e_mail']. '">'.$ligne['e_mail']. '</a></td>'   ;
                     echo "<td>".$ligne['datee']."</td> <td>".$ligne['score']."</td> <td>".$ligne['idQCM']."</td>";
                      echo" <td>"; ?> 
                     <!-- bouton voir plus pour voir les dernier resultat -->
                    <form method="post" action="resultatutil.php">
                       <input type ="submit" value="Voir plus  " />    
                       <input type="text" name="toto" value="<?php echo $ligne['e_mail'] ?>" style="display:none" />
                   </form>  
 <?php
                  echo "</td>";
                     echo "</tr>";
                 } 
?>
                 </table>
 <?php
              }  
              elseif($_POST['toto']=='Plus haut')// clique sur le bouton score le plus haut 
              {
               echo "</tr>";
       while ($ligne= $req2->fetch())//recherche dans historique 
                     {  
                         // affiche email en lien la date le score et le QCM
                          echo'<td><a href="profil.php?id='.$ligne['e_mail']. '">'.$ligne['e_mail']. '</a></td>'   ;
                         echo "<td>".$ligne['datee']."</td> <td>".$ligne['score']."</td> <td>".$ligne['idQCM']."</td>";
                         echo" <td>"; 
?> <!-- bouton voir plus pour voir les dernier resultat -->
                         <form method="post" action="resultatutil.php">
                              <input type ="submit" value="Voir plus  " />   
                               <input type="text" name="toto" value="<?php echo $ligne['e_mail'] ?>" style="display:none" /> 
                         </form>  <?php
                           echo "</td>";
                         echo "</tr>";
                        } 

             }  
             elseif($_POST['toto']=='Plus bas')// clique sur le bouton score le plus bas 
             {
               echo "</tr>";
                     while ($ligne= $req3->fetch())//recherche dans historique 
                     {   // affiche email en lien la date le score et le QCM
                       echo'<td><a href="profil.php?id='.$ligne['e_mail']. '">'.$ligne['e_mail']. '</a></td>'   ;
                        echo "<td>".$ligne['datee']."</td> <td>".$ligne['score']."</td> <td>".$ligne['idQCM']."</td>";
                         echo" <td>"; ?> 
                  <!-- bouton voir plus pour voir les dernier resultat -->
                          <form method="post" action="resultatutil.php">
                            <input type ="submit" value="Voir plus  " />    
                            <input type="text" name="toto" value="<?php echo $ligne['e_mail'] ?>" style="display:none" />
                        </form>  <?php
                     echo "</td>";
                      echo "</tr>";
                      }   
  ?>
              </table>
                     <?php }
    // clique sur le bouton liste des utilisateurs                 
         elseif($_POST['toto']=='Liste des utilisateurs')
             {    echo "</tr>";

                     while ($ligne= $req4->fetch())//recherche dans historique 
                     {   // affiche email en lien la date le score et le QCM
                       echo'<td><a href="profil.php?id='.$ligne['e_mail']. '">'.$ligne['e_mail']. '</a></td><td> </td><td> </td><td> </td><td> </td>'   ;
                      
                      echo "</tr>";
                      }   
  ?>
              </table><?php  
            }  
            elseif($_POST['toto']=='Valider')
            {
               if(isset($_POST['debut']))//  si debut des bouton nexiste pas 
               {    
                  $req5=$bdd->query("SELECT * FROM historique ");

                                while ($ligne= $req5->fetch())// lire la base de donnée
                                {   echo "</tr>";
                                   if ($ligne['datee']>$_POST['debut'] AND $ligne['datee']<$_POST['fin'])
                                  {        // affiche les ifnormation qui sont compris dans lintervalle choisi par le formateur             
                                       echo'<td><a href="profil.php?id='.$ligne['e_mail']. '">'.$ligne['e_mail']. '</a></td>'   ;
                                      echo "<td>".$ligne['datee']."</td> <td>".$ligne['score']."</td> <td>".$ligne['idQCM']."</td>";
                                        echo" <td>"; ?> 
                                                <!-- bouton voir plus pour voir les dernier resultat -->
                                   <form method="post" action="resultatutil.php">
                                           <input type ="submit" value="Voir plus  " />    
                                           <input type="text" name="toto" value="<?php echo $ligne['e_mail'] ?>" style="display:none" />
                                    </form> 
                <?php
                                      echo "</td>";
                                       echo "</tr>";
                                    }
                                 }
               
               echo "<p>Date de début : " . $_POST['debut'] . "</p>";// afficher la date de debut 
               echo "<p>Date de fin : " . $_POST['fin'] . "</p>"; //afficher la date de fin 
               }
            }
                

                 
?>
                 </table>
 <?php
              }  
else
   {

     while ($ligne= $req->fetch())//recherche dans l'historique 
     {    echo "</tr>"; // affiche email en lien la date le score et le QCM
        echo'<td><a href="profil.php?id='.$ligne['e_mail']. '">'.$ligne['e_mail']. '</a></td>'   ;
         echo "<td>dddd".$ligne['datee']."</td> <td>".$ligne['score']."</td> <td>".$ligne['idQCM']."</td>";
       echo" <td>"; ?> 
         <!-- bouton voir plus pour voir les dernier resultat -->
        <form method="post" action="resultatutil.php">
           <input type ="submit" value="Voir plus  " />    
           <input type="text" name="toto" value="<?php echo $ligne['e_mail'] ?>" style="display:none" />
      </form>  
<?php
      echo "</td>";
         echo "</tr>";
     } 
?>
     </table>
<?php
    }
   
     ?>
</body>
</html>