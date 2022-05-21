
<?php
session_start();

?>
<!DOCTYPE html>
<head>

	<link rel="stylesheet" href="choixQCM.CSS">
</head>
<html>
<body><?php
$var_to=0;// variable pour un question pourcent
$var_moi=0;
$var_juste=0;
   $bdd= new PDO ('mysql:host=localhost;dbname=stage_s4','root','');
   $bdd->exec("SET NAMES 'utf8'");//affichage correcte 
   $req1=$bdd->query("SELECT numpro,juste_pasjuste , idQ,libelle FROM proposition ");  
   $req2=$bdd->query("SELECT count(*) AS nb, SUM(juste_pasjuste) AS vrai , idQ FROM proposition GROUP BY idQ");

   while ($ligne= $req2->fetch())
        { 
             if ($_SESSION['idQ']==$ligne['idQ'])
                     { 
                         $var_moi=$ligne['vrai'];//somme des raponse juste 
                        $var_to=$ligne['nb'];// nombre de proposition
                     }    
        } 

if(empty($_POST['reponse']) )// si il a pas cocher 
    {
        echo "vide";
    }  
 else
 {  
$var_to=1/$var_to; //pourcentage dune question 
 $var_moi=$var_to*$var_moi;// pourcentage des question jsute 

   while ($ligne= $req1->fetch()) //test pour savoir si c juste 
    { 

           foreach($_POST['reponse'] as $valeur)//je met dans une variable chaque valeur dun tableau 
        {  
            if($valeur==$ligne['numpro'] and $_SESSION['idQ']==$ligne['idQ'] AND $ligne['juste_pasjuste']==1  )
            {
                    $var_juste=$var_juste+$var_to; // augmentation si la reponse est bonne 
             }
             else if($valeur==$ligne['numpro'] and $_SESSION['idQ']==$ligne['idQ'] AND $ligne['juste_pasjuste']==0 )
             {
                $var_juste=$var_juste-$var_to; 
             }

          
         }
 
    }
 }
if ($var_juste==$var_moi)// si le pourcentage de reponse est egale au poourcentage de reponse juuste alors il a bon 
{ 
     $_SESSION["questionjuste"]=$_SESSION["questionjuste"]+1;
?>
    <FONT size="7"color="#008000"><center>  
<?php
    echo "<b>Bonne réponse </b><br> ";    
 
?>
    </center></FONT> <FONT color="#000000">   
<?php
    $req3=$bdd->query("SELECT numpro,juste_pasjuste , idQ,libelle FROM proposition ");  
    ?> <FONT size="6"color="#000000"><center>  <?php
  echo"<b>".$_SESSION['libQ']."</b><br>";?></center></FONT>  <?php
?>
     <table border=1> 
<?php  
     echo " <td>vos réponses</td> <td>réponses attendues</td><td>  </td>";
    echo "</tr>"; 
    ?></FONT>
     <?php
    while ($ligne= $req3->fetch()) 
    { 
    //les reponses de utilisateur
        if (in_array($ligne['numpro'], $_POST['reponse'] ) AND $_SESSION['idQ']==$ligne['idQ'])
                {
                        echo "<td><img src='dejacoche.png' height='50'></td>";
                }   
        elseif($_SESSION['idQ']==$ligne['idQ'])
        {  
             echo "<td><img src='coche.png' height='50'></td> ";
         }
                 // les reponse de la question qui sont juste     
            if($_SESSION['idQ']==$ligne['idQ'] AND $ligne['juste_pasjuste']==1 )
                      {
                        echo "<td><img src='dejacoche.png' height='50'></td>";
                      }
                      elseif($_SESSION['idQ']==$ligne['idQ'])
                      {
                        echo "<td><img src='coche.png' height='50'></td> ";
                      }
// les libelles de la question   
        if($_SESSION['idQ']==$ligne['idQ']AND $ligne['juste_pasjuste']==1 )
        {  
             echo "<td>"?> 
            <FONT color="#008000"><?php 
            echo "" .$ligne['libelle']. "<br></td>";?> </FONT><?php 
        }
       elseif($_SESSION['idQ']==$ligne['idQ']AND $ligne['juste_pasjuste']==0 )
        { 
            echo "<td>"?> 
            <FONT color="#ff0000"><?php
            echo "" .$ligne['libelle']. "<br></td>";?> </FONT><?php 
        }
        echo "</tr>";
        
    }?>
    </table><?php
}

else 
{    ?><FONT size="7"color="#ff0000"><center>  
<?php
    echo "<b>Mauvaise réponse </b><br> "; 
 ?>
    </center></FONT> <FONT color="#000000">
<?php
    $req3=$bdd->query("SELECT numpro,juste_pasjuste , idQ,libelle FROM proposition ");  
    ?> <FONT size="6"color="#000000"><center>  <?php
    echo"<b>".$_SESSION['libQ']."</b><br>";?></center></FONT>  <?php
  ?>

     <table border=1> 
<?php  
    echo " <td>vos réponses</td> <td>réponses attendues</td><td>  </td>";
    echo "</tr>"; 
    while ($ligne= $req3->fetch())  
    { 
    //les reponses de utilisateur
        if (in_array($ligne['numpro'], $_POST['reponse'] ) AND $_SESSION['idQ']==$ligne['idQ'])
                {
                        echo "<td><img src='dejacoche.png' height='50'></td>";
                }   
        elseif($_SESSION['idQ']==$ligne['idQ'])
        {  
             echo "<td><img src='coche.png' height='50'></td> ";
        }
                // les reponse de la question qui sont juste
                      if($_SESSION['idQ']==$ligne['idQ'] AND $ligne['juste_pasjuste']==1 )
                      {
                        echo "<td><img src='dejacoche.png' height='50'></td>";
                      }
                      elseif($_SESSION['idQ']==$ligne['idQ'])
                      {
                        echo "<td><img src='coche.png' height='50'></td> ";
                      }
// les libelles de la question   
 if($_SESSION['idQ']==$ligne['idQ']AND $ligne['juste_pasjuste']==1 )
        {  echo "<td>"?> 
           <FONT color="#008000"><?php 
            echo "" .$ligne['libelle']. "<br></td>";

        }

       elseif($_SESSION['idQ']==$ligne['idQ']AND $ligne['juste_pasjuste']==0 )
        { echo "<td>"?> 
            <FONT color="#ff0000"><?php
            echo "" .$ligne['libelle']. "<br></td>";

        } 

        echo "</tr>";
    }
?>
    </table>
 <?php
}

 // apres les dix question 
if($_SESSION['i']>8)
{ 
    ?>
    <form method="post" action="Resultat.php">
                    <input type ="submit" value="Résultat " />
            </form>
    <input type="submit" value="Aide" onclick="popup('remarque.php')" /> 
    <script LANGUAGE="JavaScript"> 
        function popup(tmp)
            { 
        window.open(tmp,'popup','width=200,height=100,toolbar=false,scrollbars=false'); 
            } 
        </script>  
 <?php

 }
            
else if  ($_SESSION['i']<9)
{   
    ?> <form method="post" action="question_suivante.php">
    <input type ="submit" value="Question suivante " />
</form>

    <input type="submit" value="Aide" onclick="popup('remarque.php')" /> 
    <script LANGUAGE="JavaScript"> 
        function popup(tmp)
        { 
        window.open(tmp,'popup','width=500,height=300,toolbar=false,scrollbars=false'); 
        }    
        </script>  
     <?php
} 

$_SESSION['numeroquestion']=$_SESSION['numeroquestion']+1;
?>
</body>
</html>