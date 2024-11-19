from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName
from fhir.resources.contactpoint import ContactPoint
from fhir.resources.identifier import Identifier

# Crear el recurso FHIR de paciente con parámetros opcionales
def create_patient_resource(document_number=None, family_name=None, given_name=None, birth_date=None, gender=None, phone=None):
    patient = Patient()

    # Agregar el identificador (número de documento) si está disponible
    if document_number:
        identifier = Identifier()
        identifier.system = "http://CamiyVicky.org"  # Puede ser un identificador de sistema específico
        identifier.value = document_number
        patient.identifier = [identifier]

    # Agregar el nombre del paciente si está disponible
    if family_name or given_name:
        name = HumanName()
        if family_name:
            name.family = family_name
        if given_name:
            name.given = [given_name]
        patient.name = [name]
    
    # Agregar la fecha de nacimiento si está disponible
    if birth_date:
        patient.birthDate = birth_date

    # Agregar el género si está disponible
    if gender:
        patient.gender = gender

    # Agregar información de contacto si está disponible
    if phone:
        contact = ContactPoint()
        contact.system = "phone"
        contact.value = phone
        contact.use = "mobile"
        patient.telecom = [contact]

    return patient
