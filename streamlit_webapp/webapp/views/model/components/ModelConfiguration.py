import streamlit as st


class ModelConfiguration:

    def configuration(self):
        with st.expander("Selecciona el modelo que quiere utilizar"):
            selection = self._select_box()
            st.session_state.selected_model = selection
            st.write(f"Has seleccionado: {selection}")

    @staticmethod
    def _select_box():
        seleccion = st.selectbox(
            "Elige una opción:",
            ["blip_vqa vqav2", "pnp_vqa base", "blip2_t5 pretrain_flant5xl", "blip2_opt caption_coco_opt2.7b"],
            index=0
        )
        return seleccion