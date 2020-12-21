import models
import db_dummy
from sqlalchemy.orm import Session
from db.entidades import Contacto


def eliminar_contacto(db: Session, id):
    contacto_en_db: Contacto = db.query(Contacto).get(id)
    db.delete(contacto_en_db)
    db.commit()


def obtener_contacto_por_id(db: Session, id):
    return db.query(Contacto).get(id)


def actualizar_contacto(db: Session, contacto):
    contacto_en_db: Contacto = db.query(Contacto).get(contacto.id)
    contacto_en_db.nombre = contacto.nombre
    contacto_en_db.direccion = contacto.direccion
    db.commit()


def lista_contactos(db: Session):
    return db.query(Contacto).all()


def crear_contacto(db: Session, contacto: Contacto):
    if not db.query(Contacto).get(contacto.id) is None:
        return False
    else:
        db.add(contacto)
        db.commit()
        return True


def lista_contactos_resumen():
    lista_contactos_resumen = []
    contactos = db_dummy.obtener_contactos()
    for id, contacto in contactos.items():
        contacto_resumen = models.ContactoResumen(
            id=contacto.id, nombre=contacto.nombre)
        lista_contactos_resumen.append(contacto_resumen)
    return lista_contactos_resumen


def obtener_contacto_con_telefonos(id: str):
    contacto = db_dummy.obtener_contacto_por_id(id)
    if contacto is None:
        return None
    telefonos = db_dummy.obtener_telefonos_de_contacto(id)
    #contacto_con_telefonos = models.ContactoConTelefono(id=contacto.id, nombre=contacto.nombre, direccion=contacto.direccion, telefonos=telefonos)
    contacto_con_telefonos = models.ContactoConTelefono(
        **contacto.dict(), telefonos=telefonos)
    return contacto_con_telefonos
