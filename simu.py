import numpy
import math

tiempo = 0
st = 0
fll = 0
revalida = None

CostoOperativo = 0
Alta_porcentajeTicketsVencidos = 0
Baja_porcentajeTicketsVencidos = 0
Consulta_porcentajeTicketsVencidos = 0
Modificacion_porcentajeTicketsVencidos = 0
ticketsNormales = 0
ticketsCriticos = 0
proximaRevalida = 999999999

intervencionesServerTeam = 0

totalNtpc = 0
totalNtpa = 0
totalNtpb = 0
totalNtpm = 0

totalNtpcVencidos = 0
totalNtpaVencidos = 0
totalNtpbVencidos = 0
totalNtpmVencidos = 0

costoNtpcVencidos = 0
costoNtpaVencidos = 0
costoNtpbVencidos = 0
costoNtpmVencidos = 0

ntpcn = 0
ntpan = 0
ntpbn = 0
ntpmn = 0

ntpcc = 0
ntpac = 0
ntpbc = 0
ntpmc = 0

ntpcv = 0
ntpav = 0
ntpbv = 0
ntpmv = 0

costoOperativo = 0,


def funcionRevalida():
    numero = 0
    numero = 5 * numpy.random.uniform(low=0, high=1.0, size=None) + 5
    return int(numero)


def funcionTicketNormal():
    i = 0
    numero = 0
    while (i < 24):
        numero = numero + numpy.random.uniform(low=0, high=1.0, size=None) + 1
        i = i + 1
    return int(numero)


def funcionTicketCritico():
    i = 0
    numero = 0
    while (i < 24):
        numero = numero + 0.16 * numpy.random.uniform(low=0, high=1.0, size=None) + 0.04
        i = i + 1
    return int(numero)


def cantidad_de_tickets_atendidos_dia(operarios):
    ta = 0
    cantidad_tickets_por_dia = 0

    while (ta <= 8):
        ta = ta + 2.5 * numpy.random.uniform(low=0, high=1.0, size=None) + 1.5
        cantidad_tickets_por_dia = cantidad_tickets_por_dia + 1

    return int(cantidad_tickets_por_dia * operarios)


def aplanador(tickets_posibles_por_dia, ticketsPendientes):
    if (tickets_posibles_por_dia >= ticketsPendientes):
        tickets_posibles_por_dia = tickets_posibles_por_dia - ticketsPendientes
        ticketsPendientes = 0
    else:
        ticketsPendientes = ticketsPendientes - tickets_posibles_por_dia
        tickets_posibles_por_dia = 0
    return tickets_posibles_por_dia, ticketsPendientes


# Parametros de entrada
cantidadDeDias = int(input('Insertar cantidad de dias \n'))
cantidadDeAnalistas = int(input('Insertar cantidad de Analistas \n'))
limiteDePedidosAlServerTeam = int(input('Insertar cantidad limite de pedidos al server team \n'))

while (tiempo < cantidadDeDias):
    tiempo = tiempo + 1

    ticketsNormales = funcionTicketNormal()
    ticketsCriticos = funcionTicketCritico()




    ntpcn = int(ticketsNormales * 0.1)
    ntpmn = int(ticketsNormales * 0.6)
    ntpan = int(ticketsNormales * 0.15)
    ntpbn = int(ticketsNormales * 0.15)

    ntpcc = ntpcc + int(ticketsCriticos * 0.1)
    ntpmc = ntpmc + int(ticketsCriticos * 0.6)
    ntpac = ntpac + int(ticketsCriticos * 0.15)
    ntpbc = ntpbc + int(ticketsCriticos * 0.15)

    # alta masiva
    if (numpy.random.uniform(low=0, high=1.0, size=None) <= 0.15):
        ntpan = ntpan + 30 * numpy.random.uniform(low=0, high=1.0, size=None) + 50
        print('Alta de cliente')
    # baja masiva

    if (numpy.random.uniform(low=0, high=1.0, size=None) <= 0.15):
        ntpbn = ntpbn + 15 * numpy.random.uniform(low=0, high=1.0, size=None) + 35
        print('Perdida de cliente')

    totalNtpc = totalNtpc + ntpcc + ntpcn
    totalNtpa = totalNtpa + ntpac + ntpan
    totalNtpb = totalNtpb + ntpbc + ntpbn
    totalNtpm = totalNtpm + ntpmc + ntpmn

    print('Los tickets al llegar el dia ', tiempo, ' son :')
    print('Tickets normales de consulta: ', ntpcn)
    print('Tickets normales de modificacion: ', ntpmn)
    print('Tickets normales de alta: ', ntpan)
    print('Tickets normales de baja: ', ntpbn)
    print('Tickets criticos de consulta: ', ntpcc)
    print('Tickets criticos de modificacion: ', ntpmc)
    print('Tickets criticos de alta: ', ntpac)
    print('Tickets criticos de baja: ', ntpbc)
    print('Tickets vencidos de consulta: ', ntpcv)
    print('Tickets vencidos de modificacion: ', ntpmv)
    print('Tickets vencidos de alta: ', ntpav)
    print('Tickets vencidos de baja: ', ntpbv)

    if (proximaRevalida == tiempo):
        proximaRevalida = 99999999
        revalida = None
        ntpav = ntpav * 0.4
        ntpbv = ntpbv * 0.4
        ntpac = ntpac * 0.4
        ntpbc = ntpbc * 0.4
        ntpan = ntpan * 0.4
        ntpbn = ntpbn * 0.4

    tickets_posibles_por_dia = cantidad_de_tickets_atendidos_dia(cantidadDeAnalistas)

    tickets_posibles_por_dia, ntpcv = aplanador(tickets_posibles_por_dia, ntpcv)
    tickets_posibles_por_dia, ntpav = aplanador(tickets_posibles_por_dia, ntpav)
    tickets_posibles_por_dia, ntpbv = aplanador(tickets_posibles_por_dia, ntpbv)
    tickets_posibles_por_dia, ntpmv = aplanador(tickets_posibles_por_dia, ntpmv)
    tickets_posibles_por_dia, ntpcc = aplanador(tickets_posibles_por_dia, ntpcc)
    tickets_posibles_por_dia, ntpac = aplanador(tickets_posibles_por_dia, ntpac)
    tickets_posibles_por_dia, ntpbc = aplanador(tickets_posibles_por_dia, ntpbc)
    tickets_posibles_por_dia, ntpmc = aplanador(tickets_posibles_por_dia, ntpmc)
    tickets_posibles_por_dia, ntpcn = aplanador(tickets_posibles_por_dia, ntpcn)
    tickets_posibles_por_dia, ntpan = aplanador(tickets_posibles_por_dia, ntpan)
    tickets_posibles_por_dia, ntpbn = aplanador(tickets_posibles_por_dia, ntpbn)
    tickets_posibles_por_dia, ntpmn = aplanador(tickets_posibles_por_dia, ntpmn)

    print('Los tickets antes de cambiar el dia son ', tiempo, ' son :')
    print('Tickets normales de consulta: ', ntpcn)
    print('Tickets normales de modificacion: ', ntpmn)
    print('Tickets normales de alta: ', ntpan)
    print('Tickets normales de baja: ', ntpbn)
    print('Tickets criticos de consulta: ', ntpcc)
    print('Tickets criticos de modificacion: ', ntpmc)
    print('Tickets criticos de alta: ', ntpac)
    print('Tickets criticos de baja: ', ntpbc)
    print('Tickets vencidos de consulta: ', ntpcv)
    print('Tickets vencidos de modificacion: ', ntpmv)
    print('Tickets vencidos de alta: ', ntpav)
    print('Tickets vencidos de baja: ', ntpbv)

    totalNtpcVencidos = totalNtpcVencidos + int(ntpcc)
    totalNtpaVencidos = totalNtpaVencidos + int(ntpac)
    totalNtpbVencidos = totalNtpbVencidos + int(ntpbc)
    totalNtpmVencidos = totalNtpmVencidos + int(ntpmc)

    ntpcv = ntpcv + ntpcc
    ntpav = ntpav + ntpac
    ntpbv = ntpbv + ntpbc
    ntpmv = ntpmv + ntpmc

    ntpcc = ntpcn
    ntpac = ntpan
    ntpbc = ntpbn
    ntpmc = ntpmn

    ntpcn = 0
    ntpan = 0
    ntpbn = 0
    ntpmn = 0

    costoNtpcVencidos = costoNtpcVencidos + ntpcv * 10
    costoNtpaVencidos = costoNtpaVencidos + ntpav * 10
    costoNtpbVencidos = costoNtpbVencidos + ntpbv * 10
    costoNtpmVencidos = costoNtpmVencidos + ntpmv * 10



    print('Los tickets modificados al cambiar el dia \n', tiempo, ' son : ')
    print('Tickets normales de consulta: \n', ntpcn)
    print('Tickets normales de modificacion: \n', ntpmn)
    print('Tickets normales de alta: \n', ntpan)
    print('Tickets normales de baja: \n', ntpbn)
    print('Tickets criticos de consulta: \n', ntpcc)
    print('Tickets criticos de modificacion: \n', ntpmc)
    print('Tickets criticos de alta: \n', ntpac)
    print('Tickets criticos de baja: \n', ntpbc)
    print('Tickets vencidos de consulta: \n', ntpcv)
    print('Tickets vencidos de modificacion: \n', ntpmv)
    print('Tickets vencidos de alta: \n', ntpav)
    print('Tickets vencidos de baja: \n', ntpbv)

    if ((ntpcc + ntpac + ntpbc + ntpmc) >= limiteDePedidosAlServerTeam and revalida is None):
        revalida = True
        intervencionesServerTeam = intervencionesServerTeam + 1
        proximaRevalida = funcionRevalida() + tiempo

porcentajeTicketConsulta = totalNtpcVencidos / totalNtpc * 100
porcentajeTicketAlta = totalNtpaVencidos / totalNtpa * 100
porcentajeTicketBaja = totalNtpbVencidos / totalNtpb * 100
porcentajeTicketModificacion = totalNtpmVencidos / totalNtpm * 100

print('tickets vencidos de consulta  fue de : \n', totalNtpcVencidos)
print('tickets vencidos de alta fue de : \n', totalNtpaVencidos)
print('tickets vencidos de baja fue de : \n', totalNtpbVencidos)
print('tickets vencidos de modificacion fue de : \n', totalNtpmVencidos)

print('tickets total de consulta  fue de : \n', totalNtpc)
print('tickets total de alta fue de : \n', totalNtpa)
print('tickets total de baja fue de : \n', totalNtpb)
print('tickets total de modificacion fue de : \n', totalNtpm)

print('El porcentaje de tickets vencidos de consulta  fue de : \n', porcentajeTicketConsulta)
print('El porcentaje de tickets vencidos de alta fue de : \n', porcentajeTicketAlta)
print('El porcentaje de tickets vencidos de baja fue de : \n', porcentajeTicketBaja)
print('El porcentaje de tickets vencidos de modificacion fue de : \n', porcentajeTicketModificacion)

costoOperativo = costoNtpcVencidos + costoNtpaVencidos + costoNtpbVencidos + costoNtpmVencidos + cantidadDeAnalistas * (
            1071 / 30) * tiempo + intervencionesServerTeam * 400

print('Intervenciones Unix Team:\n', intervencionesServerTeam)
print('El costo operativo fue de : \n', costoOperativo)
print('El costo operativo mensual fue de : \n', costoOperativo / 30)
