
<?php
// On démarre la session AVANT d'écrire du code HTML
session_start();
$_SESSION['numeroquestion']=1;// variable coresspondant a exemple 1/12
$_SESSION['i']=0; // incrementer le tableau 
$_SESSION['nquestion']=0;// reference au nombre de questin jusqua 2 
$_SESSION['numQCM'] =$_POST['toto'] ;//num de QCM
$_SESSION['idQ'] ='rien';// savoir question pour porposition
$_SESSION["client"][0] = 0;//tableau pour les question  
$_SESSION['iQ']=0;// variable qui prend le numerodu QCM
$_SESSION["clientQCM"][$_SESSION['iQ']] = $_POST['toto'];// tableau pour les QCM
$_SESSION["questionjuste"]= 0;// savoir si la question est juste
?>
<!DOCTYPE html>

<html>
<FONT size="5">
<body>
<?php

    $var_r= rand(1,10); //choix de qestion aléatoire 
    $var_text='rien';
    

    $_SESSION["num"] = $var_r; // Créera $prenoms[0]
 

    $bdd= new PDO ('mysql:host=localhost;dbname=stage_s4','root','');
    $bdd->exec("SET NAMES 'utf8'");//afficher correctement 
      //requete pour affiche les question 
        $req=$bdd->query("SELECT* FROM question ");
         // affiche sur 10 pour savoir ou on en ai dans le QCM
        ?><FONT size="6"><?php
        echo "<b>".$_SESSION['numeroquestion']."/12</b>";
        ?> </FONT><?php
        
// afficher la question 
while ($ligne= $req->fetch()) 
{ 
 if($var_r==$ligne['numq'] AND $_SESSION['numQCM']==$ligne['numQCM'] )
     {  
          $_SESSION['libQ']=$ligne['libelle'];//garde pour affiche reponse.php
        $_SESSION['nquestion']=$_SESSION['nquestion']+1;//apres 2 change QCM
         $_SESSION['idQ']=$ligne['idQ'];//garder question pour proposition 
        $_SESSION["client"][$_SESSION['i']] = $var_r;// mettre valeur pour savoir laquel ni est pas 
        $var_text=$ligne['libelle'];

?>
         <FONT size="6"><center> 
<?php
   echo"<b>".$var_text."</b><br>"; //affiche la question 
   ?> 
             </center></FONT><?php 
     }
}    
     echo "<br>";
     
// affihcer les proposition
$req1=$bdd->query("SELECT* FROM proposition ");
while ($ligne= $req1->fetch())
{ 
 if($_SESSION['idQ']==$ligne['idQ']  )//verification de la question 
     {
         $var_text=$ligne['libelle'];
 ?>
            <form method="post" action="reponseRAMDOM.php">       
                <input type="checkbox"  name="reponse[]" value= "<?php echo $ligne['numpro'] ?>">
<?php
             echo $var_text."<br>";//affichage 
      }

}  
     echo "<br>";
 ?>

                <input type ="submit" value="Valider " />
            </form> 
</body>
</html>