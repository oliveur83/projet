<?php
// On démarre la session AVANT d'écrire du code HTML
session_start();

?>
<!DOCTYPE html>

<html>
<body><FONT size="5">
<?php

    $var_r= rand(1,10); 
    $var_text='rien';
    $var_i=0;
    $bdd= new PDO ('mysql:host=localhost;dbname=stage_s4','root','');
    $bdd->exec("SET NAMES 'utf8'");

    $req=$bdd->query("SELECT* FROM question ");
    ?><FONT size="6"><?php
echo "<b>".$_SESSION['numeroquestion']."/12</b>";
?> </FONT><?php
while ($ligne= $req->fetch()) // afficher la question 
{ 
 if($var_r==$ligne['numq'] AND $_SESSION["clientQCM"][$_SESSION['iQ']]==$ligne['numQCM'] )
     {

  $var_text=$ligne['libelle'];
  $_SESSION['nquestion']=$_SESSION['nquestion']+1;// pour pouvoir change de QCM toutes les deux questions
        $_SESSION['libQ']=$ligne['libelle'];// pour les proposition affiche pour reponse.php
  $_SESSION['idQ']=$ligne['idQ'];       //garder question pour proposition
   $_SESSION['i']=$_SESSION['i']+1;   // nombre de case du tableau  
  $_SESSION["client"][$_SESSION['i']] = $var_r; //tableau contenant tout les  numero de question 
  ?>
  <FONT size="6"><center> <?php
  echo"<b>".$var_text."</b><br>";?> 
  </center></FONT><?php  //affichage
      }
}     echo "<br>";
$req1=$bdd->query("SELECT* FROM proposition ");// affihcer les proposition
while ($ligne= $req1->fetch())
{ 
 if($_SESSION['idQ']==$ligne['idQ']  )
     {
         $var_text=$ligne['libelle'];
     ?>
            <form method="post" action="reponseRAMDOM.php">       
                <input type="checkbox"  name="reponse[]" value= "<?php echo $ligne['numpro'] ?>">
<?php
  echo $var_text."<br>";
      }
}  
echo "<br>";
?>
<input type ="submit" value="Valider " />
</form> 
</body>
</html>