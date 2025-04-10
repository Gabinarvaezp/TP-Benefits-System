import streamlit as st
import pandas as pd
from datetime import datetime

class TPBenefitsSystem:
    def __init__(self):
        # Datos de ejemplo
        self.employee_data = {
            "1234": {
                "nombre": "Juan Pérez",
                "turno": "Mañana",
                "tarjeta_tostao": "T123456",
                "tarjeta_novaventa": "N123456",
                "estado": "Activo",
                "ultima_actualizacion": "2024-01-01"
            }
        }
        
        # Horarios por turno
        self.update_schedule = {
            "Mañana": "9:00 AM - 12:00 PM",
            "Tarde": "2:00 PM - 5:00 PM",
            "Noche": "8:00 PM - 10:00 PM"
        }
        
        # Valores de beneficios
        self.benefit_values = {
            "Tostao": 100000,
            "Novaventa": 40000
        }

    def verify_employee(self, employee_id):
        """Verifica estado de beneficios del empleado"""
        if employee_id in self.employee_data:
            employee = self.employee_data[employee_id]
            return {
                "status": employee["estado"],
                "nombre": employee["nombre"],
                "turno": employee["turno"],
                "ultima_actualizacion": employee["ultima_actualizacion"]
            }
        return {"status": "No encontrado"}

    def process_update(self, employee_id, shift):
        """Procesa actualización de beneficios"""
        if employee_id in self.employee_data:
            self.employee_data[employee_id].update({
                "estado": "Activo",
                "ultima_actualizacion": datetime.now().strftime("%Y-%m-%d"),
                "turno": shift
            })
            return f"Beneficios actualizados para {self.employee_data[employee_id]['nombre']}"
        return "Empleado no encontrado"

def main():
    st.set_page_config(page_title="Sistema de Beneficios TP", page_icon="💳")

    # Título principal
    st.title("💳 Sistema de Beneficios TP")

    # Inicializar sistema
    system = TPBenefitsSystem()

    # Menú lateral
    menu = st.sidebar.selectbox(
        "Seleccione Operación",
        ["Inicio", "Actualizar Beneficios", "Verificar Estado"]
    )

    if menu == "Inicio":
        st.write("### 👋 Bienvenido al Sistema de Beneficios")
        st.write("Seleccione una opción del menú para comenzar.")

        # Mostrar estadísticas básicas
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"Total Empleados: {len(system.employee_data)}")
        with col2:
            st.success(f"Beneficios Activos: {sum(1 for emp in system.employee_data.values() if emp['estado'] == 'Activo')}")

    elif menu == "Actualizar Beneficios":
        st.header("🔄 Actualización de Beneficios")
        
        employee_id = st.text_input("ID Empleado")
        shift = st.selectbox("Turno", ["Mañana", "Tarde", "Noche"])
        
        if st.button("Procesar Actualización"):
            result = system.process_update(employee_id, shift)
            st.success(result)

    elif menu == "Verificar Estado":
        st.header("🔍 Verificación de Estado")
        
        employee_id = st.text_input("ID Empleado a Verificar")
        if st.button("Verificar"):
            status = system.verify_employee(employee_id)
            if status["status"] != "No encontrado":
                st.info(f"""
                    📋 Información del Empleado:
                    - Nombre: {status['nombre']}
                    - Estado: {status['status']}
                    - Turno: {status['turno']}
                    - Última Actualización: {status['ultima_actualizacion']}
                """)
            else:
                st.error("❌ Empleado no encontrado")

if __name__ == "__main__":
    main()
