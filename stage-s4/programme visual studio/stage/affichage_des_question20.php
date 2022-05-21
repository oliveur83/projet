
<?php
// On démarre la session AVANT d'écrire du code HTML
session_start();
$_SESSION['numeroquestion']=1;// variable coresspondant a exemple 1/20
$_SESSION['i']=0;// nombre de question pour le tableau
$_SESSION['idQ'] ='rien';// pour les proposition 
$_SESSION["client"][0] = 0;// ppou avoir toute les question 
$_SESSION["questionjuste"]= 0;// variable booleen 
$_SESSION['libQ'] ='rien';// pour les question affiche
$var_t= 0;


$_SESSION['Cmp'] =$_POST['i_cmp'] ;
?>

<!DOCTYPE html>
<html>

<body> 
<FONT size="5">
<?php


$bdd= new PDO ('mysql:host=localhost;dbname=stage_s4','root','');
$req=$bdd->query("SELECT * FROM qcm;");
           
 while ($ligne= $req->fetch())//verification du mot de passe
     { 
      if($_SESSION['Cmp']==$ligne['code'])
          {
            $var_t= 1;
           }

     }   
    
 if($var_t==1)//si c bon on affihce les qeustion et proposition
 {

    $var_r= rand(1,20); //question aleatoi
    $var_text='rien';


    $_SESSION["num"] = $var_r; // Créera $prenoms[0]


    $bdd= new PDO ('mysql:host=localhost;dbname=stage_s4','root','');
    $bdd->exec("SET NAMES 'utf8';");//afficher correctement 
       //requete pour affiche les question 
    $req=$bdd->query("SELECT * FROM question;");
        // affiche sur 10 pour savoir ou on en ai dans le QCM
    ?><FONT size="6"><?php



    echo "<b>".$_SESSION['numeroquestion']."/20</b>";
    ?> </FONT><?php
    // afficher la question 
    while ($ligne= $req->fetch()) 
      { //li dans la table pour trouver le numQCM et la question tiré aleatoirement
        //echo "je suis là"; 

        if($var_r==$ligne['numq'] AND $_SESSION['numQCM']==$ligne['numQCM'] )
           {
              $var_text=$ligne['libelle'];
?> 
              <FONT size="6"><center> 
<?php
             
              echo "<b>".$var_text."</b><br>"; //affiche la question 
?> 
              </center></FONT><?php 
                $_SESSION['libQ']=$ligne['libelle'];//garde la question pour reponse.php
               $_SESSION['idQ']=$ligne['idQ'];//garder question pour proposition 
             $_SESSION["client"][$_SESSION['i']] = $var_r;// mettre valeur pour savoir laquel ni est pas 
            }
      }      
        echo "<br>";
  //----------------------------------------------------------------------------- 
        $req1=$bdd->query("SELECT* FROM proposition ");
  // affihcer les proposition
      while ($ligne= $req1->fetch())
      { //verification de la question 
        if($_SESSION['idQ']==$ligne['idQ']  )
              {
                 $var_text=$ligne['libelle'];
?>   <!-- chekbox-->
                 <form method="post" action="reponse20.php">       
                   <input type="checkbox"  name="reponse[]" value= "<?php echo $ligne['numpro'] ?>">
<?php
                 echo $var_text."<br>";//affiche  la proposition 
              }

        }         
          echo "<br>";
?>

                    <input type ="submit" value="Valider " />
                  </form> 
 <?php 
  }
 else 
     {
              echo "il y a une erreur dans ton mot de passe ou ton e-mail.";
             ?> 
           <form method="post" action="codesQCM.php">
                     <input type ="submit" value="retour " />
          </form> 
            <?php
         } ?> 
</body>
</html>