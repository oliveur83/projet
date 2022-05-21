<?php
// On démarre la session AVANT d'écrire du code HTML
session_start();

?>
<!DOCTYPE html>

<html>
<body>
<?php

    $var_r= rand(1,20); //question aleatoire
    $var_text='rien';//libelle
    $bdd= new PDO ('mysql:host=localhost;dbname=stage_s4','root','');
    $bdd->exec("SET NAMES 'utf8'");
    $req=$bdd->query("SELECT* FROM question ");

if (in_array( $var_r, $_SESSION["client"]))//cherche valeur existe 
{
    while (in_array( $var_r, $_SESSION["client"])==TRUE )
    {
        $var_r= rand(1,20); 
    }
}
        // affiche sur 10 pour savoir ou on en ai dans le QCM
        ?><FONT size="6"><?php
        echo "<b>".$_SESSION['numeroquestion']."/20</b>";
        ?> </FONT><?php
while ($ligne= $req->fetch()) // afficher la question 
{ 
 if($var_r==$ligne['numq'] AND $_SESSION['numQCM']==$ligne['numQCM'] )
     {
  $var_text=$ligne['libelle'];
  ?> <FONT size="6"><center> <?php
  echo"<b>".$var_text."</b><br>";?> 
  </center></FONT><?php 
  $_SESSION['idQ']=$ligne['idQ'];       
   $_SESSION['i']=$_SESSION['i']+1;   
  $_SESSION["client"][$_SESSION['i']] = $var_r; 
  $_SESSION['libQ']=$var_text;
  
      }
}     echo "<br>";
$req1=$bdd->query("SELECT* FROM proposition ");// affihcer les proposition
while ($ligne= $req1->fetch())
{ 
 if($_SESSION['idQ']==$ligne['idQ']  )
     {
         $var_text=$ligne['libelle'];
     ?>
            <form method="post" action="reponse20.php">       
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