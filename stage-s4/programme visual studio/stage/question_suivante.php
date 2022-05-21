   <!--  cette sert pour les question suivante jusqua 10 ou 20 ou 12-->
<?php
// On démarre la session AVANT d'écrire du code HTML
session_start();

?>
<!DOCTYPE html>

<html><FONT size="5">
<body>
<?php

    $var_r= rand(1,10); //question aleatoire 
    $var_text='rien';// libelle
    $bdd= new PDO ('mysql:host=localhost;dbname=stage_s4','root','');
    $bdd->exec("SET NAMES 'utf8'");


if (in_array( $var_r, $_SESSION["client"]))// test pour savoir si il y a question 
{
    while (in_array( $var_r, $_SESSION["client"])==TRUE )
    {
        $var_r= rand(1,10); 
    }
}
?><FONT size="6"><?php
echo "<b>".$_SESSION['numeroquestion']."/10</b>";
?> </FONT><?php
$req=$bdd->query("SELECT* FROM question ");
while ($ligne= $req->fetch()) 
{ 
 if($var_r==$ligne['numq'] AND $_SESSION['numQCM']==$ligne['numQCM'] )
     {
  $var_text=$ligne['libelle'];
  ?>
   <FONT size="6"><center> <?php
  echo"<b>".$var_text."</b><br>";// afficher la question 
  ?> 
  </center></FONT>
  <?php 
  $_SESSION['libQ']=$ligne['libelle'];// pour les proposition affiche pour reponse.php
  $_SESSION['idQ']=$ligne['idQ'];  //garder question pour proposition      
   $_SESSION['i']=$_SESSION['i']+1;  // nombre de case du tableau  
  $_SESSION["client"][$_SESSION['i']] = $var_r; //tableau contenant tout les  numero de question 

      }
}     echo "<br>";
$req1=$bdd->query("SELECT* FROM proposition ");// affihcer les proposition
while ($ligne= $req1->fetch())
{ //verification de la question 
 if($_SESSION['idQ']==$ligne['idQ']  )
     {
         $var_text=$ligne['libelle'];//  propositon  dans variable
     ?>
            <form method="post" action="reponse.php">       
                <input type="checkbox"  name="reponse[]" value= " <?php echo $ligne['numpro']?>">
<?php
  echo $var_text."<br>";//affichage 
      }
}    echo "<br>";
?>
<input type ="submit" value="Valider " />
</form> 
</body>
</html>