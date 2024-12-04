import streamlit as st
import streamlit_authenticator 
from my_page.acc import accueil, recette
from streamlit_option_menu import option_menu

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(credentials = lesDonneesDesComptes, # Les données des comptes
    cookie_name = 'cookie session', # Le nom du cookie, un str quelconque
    key = 'secret_key', # La clé du cookie, un str quelconque# Le nombre de jours avant que le cookie expire 
)

authentication_status = authenticator.login("Connexion", "sidebar")
if st.session_state['authentication_status'] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state['authentication_status'] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
#authenticator.login()
if st.session_state['authentication_status'] is True:
    with st.sidebar:
            selection = option_menu(
                        menu_title=None,
                        options = ["🔥Accueil", "🍽️ Recettes"]
                    )
    if selection == "🔥Accueil":
        accueil()
    elif selection == "🍽️ Recettes":
        recette()

    authenticator.logout("Déconnexion", "sidebar")