# -*- coding: utf-8 -*-

from .webservices_flags import *

#Ultima atualização: 01/12/2016

METODO_WS = {
    WS_CTE_RECEPCAO: {
        'webservice': 'CteRecepcao',
        'metodo'    : 'cteRecepcaoLote',
    },
    WS_CTE_RET_RECEPCAO: {
        'webservice': 'CteRetRecepcao',
        'metodo'    : 'cteRetRecepcao',
    },
    WS_CTE_INUTILIZACAO: {
        'webservice': 'CteInutilizacao',
        'metodo'    : 'cteInutilizacaoCT',
    },
    WS_CTE_CONSULTA: {
        #u'webservice': u'CteConsultaProtocolo',
        'webservice': 'CteConsulta',
        'metodo'    : 'cteConsultaCT',
    },
    WS_CTE_STATUS_SERVICO: {
        'webservice': 'CteStatusServico',
        'metodo'    : 'cteStatusServicoCT',
    },
    WS_CTE_EVENTO: {
        'webservice': 'CteRecepcaoEvento',
        'metodo'    : 'cteRecepcaoEvento',
    },
    WS_CTE_CONSULTA_CADASTRO: {
        'webservice': 'CadConsultaCadastro',
        'metodo'    : 'consultaCadastro2',
    }
}

SVRS = {
    CTE_AMBIENTE_PRODUCAO: {
        'servidor'            : 'cte.svrs.rs.gov.br',
        WS_CTE_RECEPCAO        : 'ws/cterecepcao/CteRecepcao.asmx',
        WS_CTE_RET_RECEPCAO : 'ws/cteretrecepcao/cteRetRecepcao.asmx',
        WS_CTE_INUTILIZACAO    : 'ws/cteinutilizacao/cteinutilizacao.asmx',
        WS_CTE_CONSULTA    : 'ws/cteconsulta/CteConsulta.asmx',
        WS_CTE_STATUS_SERVICO        : 'ws/ctestatusservico/CteStatusServico.asmx',
        WS_CTE_EVENTO        : 'ws/cterecepcaoevento/cterecepcaoevento.asmx'
        },
    CTE_AMBIENTE_HOMOLOGACAO: {
        'servidor'            : 'cte-homologacao.svrs.rs.gov.br',
        WS_CTE_RECEPCAO        : 'ws/cterecepcao/CteRecepcao.asmx',
        WS_CTE_RET_RECEPCAO : 'ws/cteretrecepcao/cteRetRecepcao.asmx',
        WS_CTE_INUTILIZACAO    : 'ws/cteinutilizacao/cteinutilizacao.asmx',
        WS_CTE_CONSULTA    : 'ws/cteconsulta/CteConsulta.asmx',
        WS_CTE_STATUS_SERVICO        : 'ws/ctestatusservico/CteStatusServico.asmx',
        WS_CTE_EVENTO        : 'ws/cterecepcaoevento/cterecepcaoevento.asmx'
        }
}

SVSP = {
    CTE_AMBIENTE_PRODUCAO: {
        'servidor'            : 'nfe.fazenda.sp.gov.br',
        WS_CTE_RECEPCAO        : 'cteWEB/services/CteRecepcao.asmx',
        WS_CTE_RET_RECEPCAO : 'cteWEB/services/CteRetRecepcao.asmx',
        WS_CTE_CONSULTA    : 'cteWEB/services/CteConsulta.asmx',
        WS_CTE_STATUS_SERVICO        : 'cteWEB/services/CteStatusServico.asmx',
        },
    CTE_AMBIENTE_HOMOLOGACAO: {
        'servidor'            : 'homologacao.nfe.fazenda.sp.gov.br',
        WS_CTE_RECEPCAO        : 'cteWEB/services/CteRecepcao.asmx',
        WS_CTE_RET_RECEPCAO : 'cteWEB/services/CteRetRecepcao.asmx',
        WS_CTE_CONSULTA    : 'cteWEB/services/CteConsulta.asmx',
        WS_CTE_STATUS_SERVICO        : 'cteWEB/services/CteStatusServico.asmx',
        }
}

UFMT = {
    CTE_AMBIENTE_PRODUCAO: {
        'servidor'            : 'cte.sefaz.mt.gov.br',
        WS_CTE_RECEPCAO        : 'ctews/services/CteRecepcao',
        WS_CTE_RET_RECEPCAO : 'ctews/services/CteRetRecepcao',
        WS_CTE_INUTILIZACAO    : 'ctews/services/CteInutilizacao',
        WS_CTE_CONSULTA    : 'ctews/services/CteConsulta',
        WS_CTE_STATUS_SERVICO        : 'ctews/services/CteStatusServico',
        WS_CTE_EVENTO        : 'ctews2/services/CteRecepcaoEvento?wsdl'
        },
    CTE_AMBIENTE_HOMOLOGACAO: {
        'servidor'            : 'homologacao.sefaz.mt.gov.br',
        WS_CTE_RECEPCAO        : 'ctews/services/CteRecepcao',
        WS_CTE_RET_RECEPCAO : 'ctews/services/CteRetRecepcao',
        WS_CTE_INUTILIZACAO    : 'ctews/services/CteInutilizacao',
        WS_CTE_CONSULTA    : 'ctews/services/CteConsulta',
        WS_CTE_STATUS_SERVICO        : 'ctews/services/CteStatusServico',
        WS_CTE_EVENTO        : 'ctews2/services/CteRecepcaoEvento?wsdl'
        }
}

UFMS = {
    CTE_AMBIENTE_PRODUCAO: {
        'servidor'            : 'producao.cte.ms.gov.br',
        WS_CTE_RECEPCAO        : 'ws/CteRecepcao',
        WS_CTE_RET_RECEPCAO : 'ws/CteRetRecepcao',
        WS_CTE_INUTILIZACAO    : 'ws/CteInutilizacao',
        WS_CTE_CONSULTA    : 'ws/CteConsulta',
        WS_CTE_STATUS_SERVICO        : 'ws/CteStatusServico',
        WS_CTE_CONSULTA_CADASTRO : 'ws/CadConsultaCadastro',
        WS_CTE_EVENTO        : 'ws/CteRecepcaoEvento'
        },
    CTE_AMBIENTE_HOMOLOGACAO: {
        'servidor'            : 'homologacao.cte.ms.gov.br',
        WS_CTE_RECEPCAO        : 'ws/CteRecepcao',
        WS_CTE_RET_RECEPCAO : 'ws/CteRetRecepcao',
        WS_CTE_INUTILIZACAO    : 'ws/CteInutilizacao',
        WS_CTE_CONSULTA    : 'ws/CteConsulta',
        WS_CTE_STATUS_SERVICO        : 'ws/CteStatusServico',
        WS_CTE_CONSULTA_CADASTRO : 'ws/CadConsultaCadastro',
        WS_CTE_EVENTO        : 'ws/CteRecepcaoEvento'
        }
}

UFMG = {
    CTE_AMBIENTE_PRODUCAO: {
        'servidor'            : 'cte.fazenda.mg.gov.br',
        WS_CTE_RECEPCAO        : 'cte/services/CteRecepcao',
        WS_CTE_RET_RECEPCAO : 'cte/services/CteRetRecepcao',
        WS_CTE_INUTILIZACAO    : 'cte/services/CteInutilizacao',
        WS_CTE_CONSULTA    : 'cte/services/CteConsulta',
        WS_CTE_STATUS_SERVICO        : 'cte/services/CteStatusServico',
        WS_CTE_EVENTO        : 'cte/services/RecepcaoEvento'
        },
    CTE_AMBIENTE_HOMOLOGACAO: {
        'servidor'            : 'hcte.fazenda.mg.gov.br',
        WS_CTE_RECEPCAO        : 'cte/services/CteRecepcao',
        WS_CTE_RET_RECEPCAO : 'cte/services/CteRetRecepcao',
        WS_CTE_INUTILIZACAO    : 'cte/services/CteInutilizacao',
        WS_CTE_CONSULTA    : 'cte/services/CteConsulta',
        WS_CTE_STATUS_SERVICO        : 'cte/services/CteStatusServico',
        WS_CTE_EVENTO        : 'cte/services/RecepcaoEvento'
        }
}

UFPR = {
    CTE_AMBIENTE_PRODUCAO: {
        'servidor'            : 'cte.fazenda.pr.gov.br',
        WS_CTE_RECEPCAO         : 'cte/CteRecepcao',
        WS_CTE_RET_RECEPCAO     : 'cte/CteRetRecepcao',
        WS_CTE_INUTILIZACAO     : 'cte/CteInutilizacao',
        WS_CTE_CONSULTA         : 'cte/CteConsulta',
        WS_CTE_STATUS_SERVICO   : 'cte/CteStatusServico',
        WS_CTE_EVENTO           : 'cte/CteRecepcaoEvento'
        },
    CTE_AMBIENTE_HOMOLOGACAO: {
        'servidor'            : 'homologacao.cte.fazenda.pr.gov.br',
        WS_CTE_RECEPCAO         : 'cte/CteRecepcao',
        WS_CTE_RET_RECEPCAO     : 'cte/CteRetRecepcao',
        WS_CTE_INUTILIZACAO     : 'cte/CteInutilizacao',
        WS_CTE_CONSULTA         : 'cte/CteConsulta',
        WS_CTE_STATUS_SERVICO   : 'cte/CteStatusServico',
        WS_CTE_EVENTO           : 'cte/CteRecepcaoEvento'
        }
}

UFRS = {
    CTE_AMBIENTE_PRODUCAO: {
        'servidor'            : 'cte.svrs.rs.gov.br',
        WS_CTE_RECEPCAO         : 'ws/cterecepcao/CteRecepcao.asmx',
        WS_CTE_RET_RECEPCAO     : 'ws/cteretrecepcao/cteRetRecepcao.asmx',
        WS_CTE_INUTILIZACAO     : 'ws/cteinutilizacao/cteinutilizacao.asmx',
        WS_CTE_CONSULTA         : 'ws/cteconsulta/CteConsulta.asmx',
        WS_CTE_STATUS_SERVICO   : 'ws/ctestatusservico/CteStatusServico.asmx',
        WS_CTE_EVENTO           : 'ws/cterecepcaoevento/cterecepcaoevento.asmx',
        },
    CTE_AMBIENTE_HOMOLOGACAO: {
        'servidor'            : 'cte-homologacao.svrs.rs.gov.br',
        WS_CTE_RECEPCAO         : 'ws/cterecepcao/CteRecepcao.asmx',
        WS_CTE_RET_RECEPCAO     : 'ws/cteretrecepcao/cteRetRecepcao.asmx',
        WS_CTE_INUTILIZACAO     : 'ws/cteinutilizacao/cteinutilizacao.asmx',
        WS_CTE_CONSULTA         : 'ws/cteconsulta/CteConsulta.asmx',
        WS_CTE_STATUS_SERVICO   : 'ws/ctestatusservico/CteStatusServico.asmx',
        WS_CTE_EVENTO           : 'ws/cterecepcaoevento/cterecepcaoevento.asmx',
        }
}

UFSP = {
    CTE_AMBIENTE_PRODUCAO: {
        'servidor'            : 'nfe.fazenda.sp.gov.br',
        WS_CTE_RECEPCAO         : 'cteWEB/services/cteRecepcao.asmx',
        WS_CTE_RET_RECEPCAO     : 'cteWEB/services/cteRetRecepcao.asmx',
        WS_CTE_INUTILIZACAO     : 'cteWEB/services/cteInutilizacao.asmx',
        WS_CTE_CONSULTA         : 'cteWEB/services/cteConsulta.asmx',
        WS_CTE_STATUS_SERVICO   : 'cteWEB/services/cteStatusServico.asmx',
        WS_CTE_EVENTO           : 'cteweb/services/cteRecepcaoEvento.asmx',
        },
    CTE_AMBIENTE_HOMOLOGACAO: {
        'servidor'            : 'homologacao.nfe.fazenda.sp.gov.br',
        WS_CTE_RECEPCAO         : 'cteWEB/services/cteRecepcao.asmx',
        WS_CTE_RET_RECEPCAO     : 'cteWEB/services/cteRetRecepcao.asmx',
        WS_CTE_INUTILIZACAO     : 'cteWEB/services/cteInutilizacao.asmx',
        WS_CTE_CONSULTA         : 'cteWEB/services/cteConsulta.asmx',
        WS_CTE_STATUS_SERVICO   : 'cteWEB/services/cteStatusServico.asmx',
        WS_CTE_EVENTO           : 'cteweb/services/cteRecepcaoEvento.asmx',
        }
}

#
# Informação obtida em 
# http://www.cte.fazenda.gov.br/portal/webServices.aspx?tipoConteudo=wpdBtfbTMrw=
#  Última verificação: 01/12/2016
#Estados que utilizam a SVSP - Sefaz Virtual de São Paulo: AP, PE, RR 
#Estados que utilizam a SVRS - Sefaz Virtual do RS: AC, AL, AM, BA, CE, DF, ES, GO, MA, PA, PB, PI, RJ, RN, RO, SC, SE, TO
#

ESTADO_WS = {
    'AC': SVRS,
    'AL': SVRS,
    'AM': SVRS,
    'AP': SVSP,
    'BA': SVRS,
    'CE': SVRS,
    'DF': SVRS,
    'ES': SVRS,
    'GO': SVRS,
    'MA': SVRS,
    'MG': UFMG,
    'MS': SVRS,
    'MT': UFMT,
    'PA': SVRS,
    'PB': SVRS,
    'PE': SVSP,
    'PI': SVRS,
    'PR': UFPR,
    'RJ': SVRS,
    'RN': SVRS,
    'RO': SVRS,
    'RR': SVSP,
    'RS': UFRS,
    'SC': SVRS,
    'SE': SVRS,
    'SP': UFSP,
    'TO': SVRS
}   
