<?php
session_start();

?>
   <!-- page de connexion 
   qui permet donc de ce connecter  -->
<!DOCTYPE html>
<FONT size="5">
 <FONT  style="text-align:center">
<html><head>
	<link rel="stylesheet" href="choixQCM.CSS">
</head>
<body>
        <form method="post" action="choixQCM.php">
              <p>Connexion UTILISATEUR: </p> 
             <p>E-mail: <input type="text"   name="i_mail"style="width:200px;height:30px;font-size:20px" > </p> 
            <p>Mot de passe: <input type="password" name="i_mp" style="width:200px;height:30px;font-size:20px"/> </p>

                 <input type ="submit" value="Valider"style=";height:30px;font-size:20px" />
            </form>
            <div class="droite">
                     <form method="post" action="index.php">
                           <input type ="submit"value="Retour"style=";height:30px;font-size:20px"/>
                       </form>   
             </div>  
        <form method="post" action="reini_motdepasse.php">
                     <input type ="submit"value="Réinitialiser votre mot de passe "style=";height:30px;font-size:20px"/>
                     </form>     
</body>
</html>