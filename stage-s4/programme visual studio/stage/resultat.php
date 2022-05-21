<?php
session_start();
 date_default_timezone_set('UTC');
?>
<!DOCTYPE html>
<FONT size="8">
 <FONT  style="text-align:center">
<html>
<body>      
 <?php
$var_id=0;
$bdd= new PDO ('mysql:host=localhost;dbname=stage_s4','root','');
 
             if( $_SESSION['numQCM']<7)// les 6 premier QCM
              {      
                        if($_SESSION["questionjuste"]>7)// superieu a 80
                           {                
                              ?><center> <?php
                              $_SESSION["questionjuste"]=$_SESSION["questionjuste"]*10;
                              ?> 
                           <FONT color="#008000"><?php echo "Score obtenu:"; 
                          echo  $_SESSION['questionjuste'] . "%<br/>";?>   <FONT color="#000000"><?php
                          echo "Bravo! Résultat trés satisfaisant!"; 
                          echo "<br><td><img src='smile.jpg' height='100'></td>";
                           ?> 
                              </center><?php
                           }   
                       elseif($_SESSION["questionjuste"]>4) //superieur a 50 
                           {                
                            ?><center> <?php
                            $_SESSION["questionjuste"]=$_SESSION["questionjuste"]*10;
                          ?> 
                         <FONT color="#FFA500"><?php   echo "Score obtenu:"; 
                        echo  $_SESSION['questionjuste'] . "%<br/>"; ?>   <FONT color="#000000"><?php
                        echo "Résultat montrant une maitrise moyenne des connaissances "; 
                        echo "<br><td><img src='smilemoyen.jpg' height='100'></td>";
                        ?> 
                            </center><?php
                           }   
                     elseif($_SESSION["questionjuste"]<5) // moin de 50
                          {                
                            ?><center> <?php
                            $_SESSION["questionjuste"]=$_SESSION["questionjuste"]*10;
                            ?> 
                         <FONT color="#ff0000"><?php echo "Score obtenu:";
                        echo  $_SESSION['questionjuste'] . "%<br/>";?>   <FONT color="#000000"><?php
                        echo "Résultat montrant une connaissance insuffisante nous vous invitons<br/>à nous contacter pour un entretien<br/>explicative"; 
                        echo "<br><td><img src='pascontent.jpg' height='100'></td>";
                       ?> 
                            </center><?php
                         }  
                         
              }

    if($_SESSION['numQCM']==8)// QCM 20 question
   {      
                if($_SESSION["questionjuste"]>15) //superieur a 80
                {                
                  ?><center> <?php
                  $_SESSION["questionjuste"]=$_SESSION["questionjuste"]*10; 
                  $_SESSION["questionjuste"]= $_SESSION["questionjuste"]/2;
                ?> 
               <FONT color="#008000"><?php   echo "Score obtenu:";
              echo  $_SESSION['questionjuste'] . "%<br/>";?>   <FONT color="#000000"><?php
              echo " Bravo! Résultat trés satisfaisant!"; 
               ?> 
                  </center><?php
              }   
          elseif($_SESSION["questionjuste"]>9)// superieur a 50
              {                
                ?><center> <?php
                $_SESSION["questionjuste"]=$_SESSION["questionjuste"]*10;
                $_SESSION["questionjuste"]= $_SESSION["questionjuste"]/2;
              ?> 
             <FONT color="#FFA500"><?php   echo "Score obtenu:";
            echo  $_SESSION['questionjuste'] . "%<br/>";?>   <FONT color="#000000"><?php
            echo "Résultat montrant une maitrise moyenne des connaissances "; 
            echo "<br><td><img src='smilemoyen.jpg' height='50'></td>";
            ?> 
                </center><?php
            }   
   elseif($_SESSION["questionjuste"]<10) // moin de 50
            {                
              ?><center> <?php
              $_SESSION["questionjuste"]=$_SESSION["questionjuste"]*10;
              $_SESSION["questionjuste"]= $_SESSION["questionjuste"]/2;
             ?> 
           <FONT color="#ff0000"><?php  echo "Score obtenu:";
          echo  $_SESSION['questionjuste'] . "%<br/>";?>   <FONT color="#000000"><?php
          echo "Résultat montrant une connaissance insuffisante nous allons <br/>vous contacter pour un entretien <br/>explicative"; 
          echo "<br><td><img src='pascontent.jpg' height='100'></td>";
            ?> 
              </center><?php
          }  
 }
if($_SESSION['numQCM']==9) //QCM ramdom
            {      
           if($_SESSION["questionjuste"]>9) // plus de 80 pourcent
                         {                
                           ?><center> <?php
                           $_SESSION["questionjuste"]=$_SESSION["questionjuste"]*10; 
                           $_SESSION["questionjuste"]= $_SESSION["questionjuste"]/1.2;
                          ?> 
                        <FONT color="#ff0000"><?php echo "Score obtenu:"; 
                       echo  $_SESSION['questionjuste'] . "%<br/>";?>   <FONT color="#000000"><?php
                       echo "Bravo! Résultat trés satisfaisant!"; 
                       echo "<td><img src='smile.jpg' height='50'></td>";
                        ?> 
                           </center><?php
                       }   
               elseif($_SESSION["questionjuste"]>5)// plus de 50 
                       {                
                         ?><center> <?php
                         $_SESSION["questionjuste"]=$_SESSION["questionjuste"]*10;
                         $_SESSION["questionjuste"]= $_SESSION["questionjuste"]/1.2;
                         ?> 
                      <FONT color="#ff0000"><?php Echo "Score obtenu:"; 
                     echo  $_SESSION['questionjuste'] . "%<br/>";?>   <FONT color="#000000"><?php
                     echo "Résultat montrant une maitrise moyenne des connaissances  "; 
                     echo "<td><img src='smilemoyen.jpg' height='100'></td>";
                      ?> 
                         </center><?php
                     }   
            elseif($_SESSION["questionjuste"]<6)// moin de 50
                     {                
                       ?><center> <?php
                       $_SESSION["questionjuste"]=$_SESSION["questionjuste"]*10;
                       $_SESSION["questionjuste"]= $_SESSION["questionjuste"]/1.2;
                      ?> 
                    <FONT color="#ff0000"><?php  echo "Score obtenu:";
                   echo  $_SESSION['questionjuste'] . "%<br/>";?>   <FONT color="#000000"><?php
                   echo "Montrant une connaisance insuffisante nous allons vous contactez"; 
                   echo "<td><img src='pascontent.jpg' height='50'></td>";
                    ?> 
                       </center><?php
                   }  
            }
                   
///............insertion du scor dans la base de donnée..............
               $bdd= new PDO ('mysql:host=localhost;dbname=stage_s4','root','');
               $req=$bdd->query("SELECT max(idhis)aS idrecent FROM historique");
               while ($ligne= $req->fetch()) // afficher la question 
               { 
                  $var_id=$ligne['idrecent']+1;
               } 
            $req=$bdd->exec("INSERT INTO historique(score,datee,e_mail,idhis,idQCM) 
            VALUES ('".$_SESSION['questionjuste']."', NOW() ,'".$_SESSION['e_mail']."','".$var_id."','".$_SESSION['numQCM']."');");

    ?>
            <form method="post" action="choixQCM2.php">
                    <input type ="submit" value="Retour au choix des QCM "style="height:30px;font-size:20px" />
            </form>
</body>
</html>