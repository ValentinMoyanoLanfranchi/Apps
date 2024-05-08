import random
import streamlit as st
def participantes():
    Image = False
    if 'participants_list' not in st.session_state:
        st.session_state.participants_list = []
    if 'Img_List' not in st.session_state:
        st.session_state.Img_List = []
    Left_NameP_Column, Right_Img_Column = st.columns(2)
    Left_NameP_Column.write("Ingrese el nombre de cada participante")
    H_imagenes = Right_Img_Column.toggle("Habilitar Imagenes")
    nombre_participante = st.text_input("Nombre de los participantes")
    if H_imagenes:
        Image = st.text_input("URL de la Imagen")
    left_column, middleL_column, middleR_column, right_column = st.columns(4)
    Start_GiveAway = left_column.button("Empezar Sorteo")
    Mostrar_Lista = middleL_column.button("Participantes")
    clean_participants = middleR_column.button("Limpiar Lista")
    Inscribir_Participante = right_column.button("Añadir Participante")
    if Inscribir_Participante:
        add_participant(st.session_state.participants_list, nombre_participante, st.session_state.Img_List, Image, H_imagenes)
    if Start_GiveAway:
        start(st.session_state.participants_list, st.session_state.Img_List)
    if clean_participants:
            st.session_state.participants_list = []
            st.session_state.Img_List = []
    if Mostrar_Lista:
        ShowList(st.session_state.participants_list)

def winner(name_list, img_list):
    ganador = random.randint(0, (len(name_list)-1))
    st.write(f"El ganador es ", st.session_state.participants_list[ganador])
    st.image(f"{img_list[ganador]}")

def add_participant(name_list, name, Img_List, Image, Img_ON):
    if name == "":
            st.write("Porfavor introduzca un nombre")
    else:
        if Img_List != [] and (Image == "" or  not Img_ON):
             st.write("ERROR, todos deben tener foto")
        else:
            name_list.append(name)
            if Image is not False:
                Img_List.append(Image)

def start(name_list, Img_List):
    if name_list == []:
        st.write("ERROR, no se ingreso ningun participante")
    else:
        winner(name_list, Img_List)

def ShowList(name_list):
        if name_list == []:
            st.write("No hay participantes")
        else:
            for Participantes in name_list:
                st.write(Participantes)

st.set_page_config(page_title="Sorteo", page_icon="", layout="centered")
st.title("Sorteos")
ganador = participantes()


