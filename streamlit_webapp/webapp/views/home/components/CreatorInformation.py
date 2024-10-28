import streamlit as st

class CreatorInformation:

    @staticmethod
    def display():
        st.write("")
        st.write("")
        st.write("")

        with st.expander("Información Adicional"):
            st.write("""
            Para dudas o consultas sobre el proyuecto, su funcionamiento y/o utilidad contactar con:
            - **Desarrollador**: Jorge Hernández Hernández
            - **Contacto**: jorge.hernandez127@alu.ulpgc.es
            """)
            st.write("¡Gracias por visitar la aplicación!")