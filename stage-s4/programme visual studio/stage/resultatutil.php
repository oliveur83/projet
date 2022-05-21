<!-- page activé grace au bouton voir plus de la pga accesformateur-->
<?php
session_start();

?>

<!DOCTYPE html>
<head>

	<link rel="stylesheet" href="choixQCM.CSS">
</head>
<html>
    <body>  
    <?php
    $var_x=1;
        $bdd= new PDO ('mysql:host=localhost;dbname=stage_s4','root','');
        $bdd->exec("SET NAMES 'utf8'");
        //differente requete SQL
        $req=$bdd->query("SELECT * FROM QCM ");
        $req1=$bdd->query("SELECT max(datee) aS daterecent, score,idQCM,e_mail FROM historique GROUP BY idQCM,e_mail ");
           
        // affichage des 9 QCM 
    
// boucle lisant le tableau historique 
       while ($ligne= $req1->fetch())
                { //affichage su score du QCM en focntion de utilisateur
                      if ($ligne['score']==TRUE  AND $_POST['toto']==$ligne['e_mail'])
                          {               
   ?> 
                             <div class="droite"><?php    
                             //methode pour bien disposé les score en face des bon QCM
                                while ($var_x<$ligne['idQCM'] )
                                {
                                    echo "<br><br>";$var_x=$var_x+1;
                                }      
                                $var_to=$ligne['daterecent'];
                                echo "date:".$var_to."<br>";
                               echo "score" .$ligne['score'];
?> 
                                </div>
 <?php                          $var_x=1;
                                }
   }     
                   
           while ($ligne= $req->fetch())
             { 
                echo "".$ligne['libelleqcm']."<br><br>";
             }   

                ?> 
 <form method="post" action="accesformateur2.php">
     <input type ="submit" value="Retour " />    
</form> 
</body>
</html>