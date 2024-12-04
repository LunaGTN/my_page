import streamlit as st

def accueil():
    st.title("Bienvenue sur ma page !")
    st.header("Course à pied")
    st.text("Sur mon site, vous pourrez accéder à des idées de recettes aussi saines que délicieuses =) et adapté aux sportifs .")
    st.text("Je vous partage également mon programme d'entraînement")
    st.image("running.png")
    st.header("Fréquence: 3 séances par semaine")
    st.text("Lundi: 15 min d'endurance fondamentale , puis 5 fois 3 min à 6:26 min/km avec 1 min 30 de récupération")
    st.text("Jeudi: Sortie 35 min d'endurance fondamentale")
    st.text("Samedi: Sortie longue entre 40 et 50 min en endurance fondamentale")

def recette():
    st.title("Des recettes saines et délicieuses")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Entrée")
        st.text("Tortillas de pomme de terres avec piquillos")
        st.image("https://cache.marieclaire.fr/data/photo/w1536_ci/51/tortilla-pommes-de-terre-piquillos.webp")
        st.page_link("https://www.marieclaire.fr/cuisine/tortilla-aux-pommes-de-terre-et-piquillos,1211211.asp",label = "Recette")

    with col2:
        st.header("Plat")
        st.text("Saumon aux herbes, citron et câpres")
        st.image("https://cache.marieclaire.fr/data/photo/w1536_ci/5s/saumon-aux-herbes-citron-et-capres.webp")
        st.page_link("https://www.marieclaire.fr/cuisine/saumon-aux-herbes-citron-et-capres,1355721.asp", label = "Recette")

    with col3:
        st.header("Dessert")
        st.text("Gâteau aux pommes")
        st.image("https://assets.afcdn.com/recipe/20180406/78377_w3072h2304c1cx1602cy2527.jpg")
        st.page_link("https://www.marmiton.org/recettes/recette_gateau-aux-pommes-facile_13493.aspx", label = "Recette")