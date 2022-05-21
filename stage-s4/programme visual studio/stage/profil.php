<?php
session_start();

?>

<!DOCTYPE html>

<html>
<body>  <FONT size="5">
<?php

$bdd= new PDO ('mysql:host=localhost;dbname=stage_s4','root','');
$req=$bdd->query("SELECT* FROM utilisateur ");
?>    <table border=1>  <?php 
 while ($ligne= $req->fetch())// verification du motdepasse et de email 
     { 
      if($_GET['id']==$ligne['e_mail'])
          {
            ?> <table border=1> 
             <p>Prenom: <?php echo $ligne['nom']."<br>";  ?></p>
             <p>Nom:  <?php echo $ligne['prenom']."<br>";?> </p>
             <p>Formation:<?php echo $ligne['formation']."<br>"; ?> </p> 
            <p>Téléphone de service: <?php echo $ligne['tel_service']."<br>"; ?> </p> <?php
            if($ligne['accord']=='oui')
            {
                ?>  <p>Téléphone portable: <?php echo $ligne['tel_portable']."<br>";?> </p>
                  <p>Courriel: <?php echo $ligne['e_mail']."<br>";?> </p><?php 
            }
           }
     }    
     ?>               
     </table>
 <form method="post" action="accesformateur2.php">
     <input type ="submit" value="Retour " />    
</form> 
</body>
</html>