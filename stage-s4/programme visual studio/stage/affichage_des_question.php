
<?php
// On démarre la session AVANT d'écrire du code HTML
session_start();
$_SESSION['numeroquestion']=1;// variable coresspondant a exemple 1/10
$_SESSION['i']=0;// nombre de case du tableau 
$_SESSION['numQCM'] =$_POST['toto'] ;// numero du QCM 
$_SESSION['idQ'] ='rien';// pour les proposition affiche
$_SESSION['libQ'] ='rien';// pour les question affiche
$_SESSION["client"][0] = 0;//tableau contenant tout les  numero de question 
$_SESSION["questionjuste"]=0;// variable quon mutiplira par 10 a la fin pour avoir les score
?>
<!DOCTYPE html>

<html><FONT size="5">
<body>
<?php
    $var_r= rand(1,10); //choix de qestion aléatoire 
    $var_text='rien';// pour les libelle 
    $_SESSION["num"] = $var_r; // Créera $prenoms[0]
    $bdd= new PDO ('mysql:host=localhost;dbname=stage_s4','root','');
    //afficher correctement 
    $bdd->exec("SET NAMES 'utf8'");
    //requete pour affiche les question 
    $req=$bdd->query("SELECT* FROM question ");
    // affiche sur 10 pour savoir ou on en ai dans le QCM
    ?><FONT size="6"><?php
    echo "<b>".$_SESSION['numeroquestion']."/10</b>";
    ?> </FONT><?php
    // afficher la question
while ($ligne= $req->fetch())  
{ //li dans la table pour trouver le numQCM et la question tiré aleatoirement 
    if($var_r==$ligne['numq'] AND $_SESSION['numQCM']==$ligne['numQCM'] )
        {
             $var_text=$ligne['libelle'];
            $_SESSION['libQ']=$ligne['libelle'];//garde la question pour reponse.php
            $_SESSION['idQ']=$ligne['idQ'];//garder question pour proposition 
            $_SESSION["client"][$_SESSION['i']] = $var_r;// mettre valeur pour savoir laquel ni est pas 
 ?>
             <FONT size="6"><center> 
<?php
             echo"<b>".$var_text."</b><br>"; //affiche la question 
?> 
             </center></FONT><?php 
          }
}
         echo "<br>";


         //requete SQL pour affihcer les proposition
        $req1=$bdd->query("SELECT* FROM proposition ");

while ($ligne= $req1->fetch())
{ //verification de la question 
 if($_SESSION['idQ']==$ligne['idQ']  )
     {
         $var_text=$ligne['libelle'];//  propositon  dans variable
 ?>        <!-- chekbox-->
            <form method="post" action="reponse.php">       
                <input type="checkbox"  name="reponse[]" value= "<?php echo $ligne['numpro'] ?>">
<?php
             echo $var_text."<br>";//affichage 
      }
    
}  
        echo "<br>";
 ?>
            <input type ="submit" value="Valider " style=";height:30px;font-size:20px"/>
        </form> 
</body>
</html>