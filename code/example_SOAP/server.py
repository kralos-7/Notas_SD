from spyne import Application, rpc, ServiceBase, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

# 1. Definición del Servicio y su Lógica
class ServicioDivisas(ServiceBase):

    @rpc(Float, _returns=Float)
    def convertir_dolar_a_euro(ctx, cantidad):
        """Toma una cantidad en USD y devuelve EUR"""
        tasa_cambio = 0.92
        return cantidad * tasa_cambio

# 2. Configuración de la Aplicación
application = Application(
    [ServicioDivisas],
    tns='practica.soap.python',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

# 3. Despliegue del Servidor
if __name__ == '__main__':
    wsgi_app = WsgiApplication(application)
    server = make_server('127.0.0.1', 8000, wsgi_app)

    print("Servidor SOAP activo en http://127.0.0.1:8000")
    print("WSDL disponible en http://127.0.0.1:8000/?wsdl")

    server.serve_forever()