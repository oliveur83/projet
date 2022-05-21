   <!-- 1er page de création dun compte
   la ou on met tout les information neccesaire pour pouvoir 
   crée son compte  -->
<!DOCTYPE html>
   <!-- fichier CSS  -->
<head>
	<link rel="stylesheet" href="choixQCM.CSS">
</head>
<body>
<p> Information:</p>    
<form method="post" action="creation_du_compte_2.php"> <!-- debut de la form -->

    <table border=0>  <!--creation du tableau  -->
                 <!-- i_nom est la reference pour la page creation_du_compte_2-->
         <?php echo "<td>"?> <p>Nom de naissance <?php echo "</td>"?> 
         <?php echo "<td>"?>   <input type="text" name="i_nom" />  (*)<?php echo "<td></tr>"?> </p>
       <!-- i_nomj est la reference pour la page creation_du_compte_2-->
     <?php echo "<td>"?>  <p>Nom d'usage<?php echo "</td>"?>
     <?php echo "<td>"?>  <input type="text" name="i_nomj" /><?php echo "<td></tr>"?> </p>
    <!-- i_prenom est la reference pour la page creation_du_compte_2-->
     <?php echo "<td>"?> <p>Prénom <?php echo "</td>"?> 
     <?php echo "<td>"?>  <input type="text" name="i_prenom" />  (*)<?php echo "</td></tr>"?> </p>
    <!-- i_telp est la reference pour la page creation_du_compte_2-->
     <?php echo "<td>"?> <p>Tel Portable <?php echo "</td>"?> 
     <?php echo "<td>"?>  <input type="text" name="i_telp" /> (*)<?php echo "</td></tr>"?></p>
    <!-- i_mail est la reference pour la page creation_du_compte_2-->
     <?php echo "<td>"?> <p>E-mail<?php echo "</td>"?> 
     <?php echo "<td>"?>  <input type="text" name="i_mail" />  (*)<?php echo "<td></tr>"?> </p>
    <!-- i_tels est la reference pour la page creation_du_compte_2-->
     <?php echo "<td>"?> <p>Tel service<?php echo "</td>"?> 
     <?php echo "<td>"?>  <input type="text" name="i_tels" />  (*)<?php echo "</td></tr>"?> </p> 
    <!-- formation  est la reference pour la page creation_du_compte_2-->
     <?php echo "<td>"?>  <p>Formation<?php echo "</td>"?></p> 
     <?php echo "<td>"?> <select name= " formation">
		          	<option value='interne'>Interne</option>
		          	<option value='medecin'>Médecin</option>
               <option value='infirmiere'>Inférmièr(e)</option>
	  	      </select> <?php echo "</td></tr>"?> 
    <!-- i_mp est la reference pour la page creation_du_compte_2-->
      <?php echo "<td>"?>   <p>Mot de passe<?php echo "</td>"?> 
      <?php echo "<td>"?>  <input type="text" name="i_mp" /> (*)<?php echo "</td></tr>"?> </p>

    </table>      <!-- fin du tableau -->

    <p>j'autorise l'utilisation de mon courriel et de mon téléphone pour
     communiquer avec l'équipe de formation 
      <!-- accord est la referenc pour la page creation_du_comptre_2-->    
      	<select name= "accord">
		        <option value='oui'>OUI</option>
		      	<option value='non'>NON</option>
	  	</select> </p>
    (*)=Obligatoire
           <?php echo "<br>";?>   
           
                      <div class="droite2">
                       <input type ="submit" value="Valider" />
                      </div> 

</form> <!-- fin de la form -->
              <div class="droite">
                     <form method="post" action="index.php">

                           <input type ="submit"value="Retour"/>
                       </form>   
             </div> 
</body>
</html>