"""GeoJSON transfers shared by local SQLite and isolated cloud sessions."""

import os

from src.app.saved_locations_repository import SavedLocationStorageError
from src.app.saved_locations_service import (
    SavedLocationDuplicateError,
    SavedLocationServiceError,
    SavedLocationsService,
)
from src.app.saved_locations_validation import SavedLocationValidationError


def render_locations_transfer(st) -> None:
    with st.expander("Importar / exportar localizações"):
        if os.getenv("SAVED_LOCATIONS_STORAGE", "sqlite") == "session":
            st.warning(
                "As localizações ficam somente nesta sessão e não são compartilhadas "
                "com outros visitantes. Exporte o GeoJSON antes de sair ou recarregar "
                "a página; importe-o quando voltar."
            )
        st.caption(
            "GeoJSON com até 100 áreas Polygon e 2 MB. "
            "Cada Feature deve ter properties.name. Nomes existentes não são sobrescritos."
        )
        upload = st.file_uploader(
            "Arquivo de localizações (.geojson ou .json)",
            type=["geojson", "json"],
            key="locations_geojson_upload",
        )
        if st.button("Importar localizações", disabled=upload is None):
            try:
                count = SavedLocationsService().import_locations(upload.getvalue())
            except (SavedLocationValidationError, SavedLocationDuplicateError) as error:
                st.error(str(error))
            except (SavedLocationStorageError, SavedLocationServiceError):
                st.error("Não foi possível importar as localizações. Tente novamente.")
            else:
                st.session_state.show_saved_locations = True
                st.success(f"{count} localização(ões) importada(s). Abra Localizações salvas.")

        if st.button("Preparar GeoJSON para download"):
            try:
                payload = SavedLocationsService().export_locations()
            except (SavedLocationValidationError, SavedLocationStorageError, SavedLocationServiceError):
                st.error(
                    "Não foi possível exportar. Verifique se existem localizações "
                    "e se o conjunto respeita os limites de 100 áreas e 2 MB."
                )
            else:
                st.download_button(
                    "Baixar minhas localizações",
                    data=payload,
                    file_name="minhas_localizacoes.geojson",
                    mime="application/geo+json",
                    on_click="ignore",
                )
