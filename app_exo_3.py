import streamlit as st
import pandas as pd

from streamlit_option_menu import option_menu

from streamlit_authenticator import Authenticate


url ="https://raw.githubusercontent.com/unbiglow/my_csv/refs/heads/main/users.csv"

df = pd.read_csv(url)

#st.write(df)

df = pd.read_csv(url)
df["password"] = df["password"].astype(str)
df["failed_login_attempts"] = df["failed_login_attempts"].astype(str)
dict_info_users = {}

for iterrow in df.iterrows():
    name = iterrow[1]["name"]
    dict_info_users[name] = {
        "name": iterrow[1]["name"],
        "password": iterrow[1]["password"],
        "email": iterrow[1]["email"],
        "failed_login_attempts": iterrow[1]["failed_login_attempts"],
        "logged_in": False,
        "role": iterrow[1]["role"]
    }


users_info = {
    "usernames": dict_info_users
}


authenticator = Authenticate(

    users_info,  

    "cookie name",    

    "cookie key",         

    30,

)

authenticator.login()


def accueil():

    with st.sidebar:

        authenticator.logout("Déconnexion")
        st.write(f"Bonjour, {st.session_state['username']}")
        selection = option_menu(

            menu_title=None,

            options = ["Accueil", "Photos de bébé phoque"]

        )
    
    if selection == "Accueil":

        st.title("Bienvenue sur la page d'accueil !")

        st.image("https://i.ytimg.com/vi/0iXiEkJVReU/hq720.jpg?sqp=-oaymwE7CK4FEIIDSFryq4qpAy0IARUAAAAAGAElAADIQj0AgKJD8AEB-AH-CYAC0AWKAgwIABABGHIgQigwMA8=&rs=AOn4CLBSwOYqFsxe5zlnpgavYJTPjR4GrQ")

    elif selection == "Photos de bébé phoque":

        st.title("Bienvenue sur mon album photo")



        st.write("Il y a un..ou plus plusieurs imposter... trouver le !")
        col1, col2, col3 = st.columns(3)

        with col1:

            st.image("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxISEhUTEhIVFRUVFRUVFRUWFQ8PFRUQFRUWFhUVFRUYHSggGBolGxUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDQ0NFQ8PFSsZFRkrKzcrKy0rKystKysrLS03LSstKysrNysrKy0rKys3LTctKystNystNysrNy03Kys3N//AABEIALcBEwMBIgACEQEDEQH/xAAcAAACAwEBAQEAAAAAAAAAAAACAwABBAUGBwj/xAA6EAACAgECAwUGBAUCBwAAAAAAAQIRAwQhEjFBBQZRYXETIoGRofAyQrHBB1Ji0eGy8RQVFnKCkqL/xAAYAQADAQEAAAAAAAAAAAAAAAAAAQIDBP/EABoRAQEBAQEBAQAAAAAAAAAAAAABEQIhMRL/2gAMAwEAAhEDEQA/APo0JpDPaGWPIbFGCh5G+gj2eQ0RDUhhj/4eb6jsOjfVjuMuOURjx4EupoRmUxkZC0YdZTkLsriJ0YZYFlsWLTOTGRQmI5DlJHEuKBbDiOAxFcQLYmcytIeTIAmBYUWiP0eDci4sW2glENGHIbEzqwoscow5ksBMuytLFtlWA5F2PRhvGX7YQi0y+ek2NXEBQHGMNYkMhLYeVlxjQAKRBnEQA8qp0G5mVsB5aOVo3LKF7WznPOLepFp46lhRlRz8epXU0YtSmLRjcpjIyFQCchUzeIJMVFhRTJ0xOQcSoxCaACgXLICwYK2MHYxqKhAcoGkSRJFPFZqUQZhgIWIF4h9kYsDK8ZUZNGvgF5MZNhgjMZzEOIUZC0zgWwFItj0sXYPEVYMkGg2LCszRkOiy5SOxsaxMA29jbmpqIJsRGYTkWkRAdyAHismoSKjkvlFv4HpsHY8H0Oli0EFyijKcK14xaTI+UGFh7LyPpR7b2CCWFD/EGvG/8jm+Zny9kTjvFs93KBiz6dE3mDXndFqX+GWzNgWq7PvdGNZHF0zLqKjfjHIy4Z2bIsiKFCJVDGiowGQKNOHCHhw9R5chWgUSyNguRQXYMynkKeRCAWy+IpzQDkIH2E1Zn4hkJgYckDNJUbmrM+WBNglIsvjAmqIpEKNBkyIqQ9ILCxyBkSBUJqgxqM0ZDsbNeamihiDWEuMh0DaJJ9myjUQZEY1Q5FqISQAKQVFkEaqFziNKYqGLJjOXrdKmd2UDLmxGdhvNwTg6ZvxSsvWaazHilwumZXnFa7CQ2GIRglZuwjkA1shM5B5JGeyqBTmZ55iZpGPLImg15wXnMzZVk6bStQMWWzCMUhabYpD8cjBjmaYSGTZFlyFY5DEMM+eJnRtyrYwSI6VDkySATDaFAqgkiRiHwlxIR0GLcSIuE0QZoxmaBpgzblNOIDZC0mEKJYjWVZTkDYAdkspIIAgucbGFMVgZMuE5et0p25ozZomdinN7MT62dQzYcaTNDJBeaZkk2OzM8l3k7+aXRz9lJuU/zRglLhT5cTbVeg5NDuZpNGZZ1dN+noYey+8mHV4+PFK+jW6afVNeP9zk6nS5JZ4ZE/djNPm0uDgaapf1Vs/BB+Rr0s5g8Zn47KcybDa1IpT+/wBzznb3as8bjGHJ3KcmnUYRVvddXyXqdfs9vJGMqa4ldOr+I7wNb45DTjyGKWCS36FY8hGYbrRyDoZLMOJ2XjnuIOk2YM3M0QkIzsnqnAYmN4hEGGmRKo+DLTF8RakXKk5MCaBiwmXCHjkPxSMjdDcEjblFbkyClIhaT+IpzM0s5WOTZRa0pjELgHxAYywUyxBZCEAy5iJo1NCpxIsNlitwnIVKW5aZmbldv6z2OHJk/kg2vN9EfmztzUueabbt8TtvnJ3vJ+be5+ke8mg9vp8uK69pCUU/BtbP50fANd3P1yyuEsEm23764XF+fHdfM14wqb3B7Sni1UYJ+7kTUl0bSbXxtfU+yYYutz513U7kZceaGTK17u/DFt1LzkuZ9Nx4aVMOqIBKgJvYZJATgZmz5OH8yTf7/dHH7d72w0cf5pte7HlXq+iOhrcnCnS6HxvvJnlPPkeS7TapK/w7Jc+VmnMJ67Q/xT1KmuLHCUb5JSi6vo23+h9F7P7Rx6nFDPifuy5rk4yXOMl0Z+eIZFsfUP4V6qV5ca3hKMZvwWVbP5qvkHfMwSvp2m5BcNMXph9nNVwyMhOZhisjM+lxcQkBFlkGYmXZSLouJHFkUheSVCVlNJUnzkHgkZuOw8UtzblFdBSII4yGiS1kb6UOhm8DX7BNbomHSKLtIosKhnHwmBl0du7oZHBXUR4bFhoFRCDTWUyFNiCrI2VxFWAc/UfiDXIrWvcrHK0Y36onUTRzp6NSe51ljTFZ9hyhjyRiuiXohGQvXZ444Oc+S+L38jBPXqvDa667+I8ApK2MjTESzKr+6Jjyxtbrfz+IYGiemjNU/vyPN9t91MWVNSjs+UklxRfin+x6PdPma8W6rx6hLgfGtX/DTUcTeKWOa6W3BtdLXKz6L3M7srRYWnLiyTSc30TV7R8tzuSw8DuthkcqDrsSGYQ7Bgg4owtXEbETkOmZ5GXSoZBhJgRDiiYZqBciNmTVZdti0pmz2ykzHjkaIsqFT4SG4p0Y3OhWPUNP1N+Kix1XlIJhC1ZDbUY9IiwFINMZrIURsQXZdgJl2AERg2U5gAtAstzEzzEhn1gGCXxA1c9hWPI0rclFLm9l9Xt9DO/VOg5bbxf0f6M5Gr1NP3bfK1yat+f36mqU2064mvFueNfDdfseH7x9qrGmk5N2q3lFRnGV+/kT3tNbeRXM0M/fnttPFUHUou3B2mppXFSr1TPCY+8+Vq1u2uae3yFa7WylPflKPCrlxy51xSfV/s0cBtwU0ntxNrrz5/W38jaTCeqwd6sqdtt7fJ9GdDSd45Z5wpr3Msb2Wy8n02Z4DVZJ8EYwbufXwj19Dv4NNHT4IQ343K58NuSg0tm+km1ddBB9ueaMls75efQLT5Kdf5+iPB93+0uJNSUbXvZGuOMkoq4UvzbVsj2fZ2s4lG63Vxe6XDe1umoumtmZ3k3dUOJGOeLc34Jbbr4rdASiY9HCYKkEgpIEhQJsSx0kKkjOqi0w0wC0wkFFOZyNfm3SOjlkcTUSuZWFp+KRogzPCI1MrALJIyTl7w1yEZsduy+U12cOpVIhx/akNdTj3aYcZCyJmiT0yMBEsAtFtg2UxBcpC5SLbFZGADOZnnIHJkM88xl1VRNRkaTfy8/L4sywy005Ljm+S6R9PBefN+eyK1eoS3ZzsWt3uPOTq/D7ROm7WSDnbnJVHd81CCq911/XraTp/P8Avx2dO7jF8H4lHwv8MpUtpttbdEj3OLOmkq92O9P80792/wDy6+KL1WK40/e5yl5yfN/RqvQuXCfBM2gnJpKPX8q3+vklsvA06rDjcYxUeGdb0uaa5S89/p8D67m7s48nL3d96VWrm6tNPw69DzPa38Ps0m/Z6hpfli+LGl/67fE0nUJ87jopJt1bW21e7vdsXjwu74Xbu3zk4cqaf6nrNP3W7QxZFGeOOVX+JTgp0vBp/PiTvxNOo7Lipxhmw5I21T9nN72ufCnF7Po2VocPsNS4knKezT24vdSf47fRdT6j2JCTjcnU+cmncVKNRbS5qPjXjfLc4/ZHYOONNpyuKdNSit4riTT6e69j12lxuO0VTglKPVvH4eq3/TqzPro5G/Dts9peXKXn4Mb6/wCBKikl/K+X9L8n0X3sNTu0+a+0/o/kzGmXNFQQyiUThlTRnkashmyImw5QWXxAtGbVZaTYTkWq1eel4nHhl4pWZcmrcpNJ8v0HYCyb1MZF2JjuNjIWGtoKKAlIQsm9FQq1rEiCvaIhSXtLLRVFHQk2LLsVxF2IDJYNkAI2JyvYY2Z8zEGDPOjFkdk1Url5CMuWkY9fVwjVRsyZFwpUuja9eSX34mmc96X9xT50Rp4Tp9dwNJvlu/F9F/8AUjs4NYpbf0P4ySXL4WfPe0NY3qJxXRcKr+ZVL52kjd2fr8iab2XCkv6a2fzSXzK5pV9I07XTxf62vp+o44HZ3aSdLwrb5HZhnTGRk8afQyzxRvlX+63+hp4gMi+/2DaGXEqcW1+TH9ZPi+jY+O1f08vRq3/pfzKkl9K+G1f6fqHxb/Bfv/cRixpe9Hpdr/tf+U/kVDZ+ia9eVAx2+SXwVkbAGplSkLsqUxBchUpAZNQkcrtDtFRTf0Hg1q1OrS6/7+B5Xtjtp01Dm/ozHrNfOcnT2L02kvdlSE53ZUskcjct1Ln5M9LBmd6LbZDdPdU+a5isONmOQ32ny+RliNUicM+UvvmIfMNSAkPAPj9PkQUpEF6T39l3YIPI67GUoi4sKO5TgJS7JYFMpsQXNmfMxzYqaAOF2pxLaK3f09Tl5ptKmn68z0Oq0rkYs/ZDfJ15czO8qlcPTarik11XPxp8rN+PHdmf/pqUJTlGTucuJ73vSW3yRrjpprr5Gd5PXm9b2ZwTlP8Amk35lww38fu0d3Jo3LmWtKvAqTwq5GGDi7T3Oph7Sa5jI6ZCsmkTAOhj7VV1ZoWvi+viebz6J8Sro9w/+GkIPSrULx++oftkeZUJrqxic/EQeheoS6i3q14nAlCfVsfp9L4gHUya1IzZ9W3y+BWPTGrFpV4DwMPDKQGXQXzOzDD5DPYoqQPE6vsvgdpbfoN00KR6zNpU+hjl2XHoh4TmQgZ82PhlfR/qd2OmrZGbtDs+Tj7qt9EFnhxx5Tp8h8HfiY4p8VNevSmjbjgZ82VVmCWwMgpgWBKsgLiQZPfotohDqYqxyp+o9MhBKlRipRLIIy2DRCCCNFqKIQAGUUZ54kQgqNZ5YUJnh8iEJMMsADwEIIFTwLmCsaIQRreJFLFvRCAG/Hp4pck/XcrJiXgQgBccVDoxKIMGqIaRCDJKAnEshQJwQTt+Zo9mQgB5/vHo0nHKlXSXn4M5imQhjZnS5fF8dgyIQQTjIQgE/9k=")

        with col2:

            st.image("https://media.istockphoto.com/id/1196700514/fr/photo/sceau-de-harpe.jpg?s=612x612&w=0&k=20&c=MQEPIDtUkiR9IPU2gWmF53CSmA5wBDnpiHR5RhorSbU=")

        with col3:

            st.image("https://ih1.redbubble.net/image.5046995421.9431/raf,360x360,075,t,fafafa:ca443f4786.jpg")

if st.session_state["authentication_status"]:

  accueil()

elif st.session_state["authentication_status"] is False:

    st.error("L'username ou le password est/sont incorrect")

elif st.session_state["authentication_status"] is None:

    st.warning('Les champs username et mot de passe doivent être remplie')
