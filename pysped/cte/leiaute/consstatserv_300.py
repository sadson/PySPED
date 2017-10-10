# -*- coding: utf-8 -*-

from pysped.xml_sped import *
from pysped.cte.leiaute import ESQUEMA_ATUAL_VERSAO_300 as ESQUEMA_ATUAL
import os

DIRNAME = os.path.dirname(__file__)

class ConsStatServCTe(XMLNFe):
    def __init__(self):
        super(ConsStatServCTe, self).__init__()
        self.versao  = TagDecimal(nome='consStatServCte', codigo='FP02', propriedade='versao', namespace=NAMESPACE_CTE, valor='3.00', raiz='/')
        self.tpAmb = TagInteiro(nome='tpAmb', codigo='FP03', tamanho=[1, 1, 1], raiz='//consStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, valor=2)
        self.xServ = TagCaracter(nome='xServ', codigo='FP04', tamanho=[6, 6], raiz='//consStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, valor='STATUS')
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'consStatServCTe_v3.00.xsd'
    
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.xServ.xml
        xml += '</consStatServCte>'
        return xml
        
    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.tpAmb.xml  = arquivo
            self.xServ.xml  = arquivo
            
    xml = property(get_xml, set_xml)
    
    
class RetConsStatServCTe(XMLNFe):
    def __init__(self):
        super(RetConsStatServCTe, self).__init__()
        self.versao  = TagDecimal(nome='retConsStatServCte', codigo='FR02', propriedade='versao', namespace=NAMESPACE_CTE, valor='3.00', raiz='/')
        self.tpAmb = TagInteiro(nome='tpAmb', codigo='FR03', tamanho=[1, 1, 1], raiz='//retConsStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, valor=2)
        self.verAplic = TagCaracter(nome='verAplic', codigo='FR04', tamanho=[1, 20], raiz='//retConsStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.cStat = TagInteiro(nome='cStat', codigo='FR05', tamanho=[3, 3, 3], raiz='//retConsStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.xMotivo = TagCaracter(nome='xMotivo', codigo='FR06', tamanho=[1, 255], raiz='//retConsStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.cUF = TagInteiro(nome='cUF', codigo='FR07', tamanho=[2, 2, 2], raiz='//retConsStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.dhRecbto = TagDataHora(nome='dhRecbto', codigo='FR08', raiz='//retConsStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False)
        self.tMed = TagInteiro(nome='tMed', codigo='FR09', tamanho=[1, 4], raiz='//retConsStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.dhRetorno = TagDataHora(nome='dhRetorno', codigo='FR10', raiz='//retConsStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.xObs = TagCaracter(nome='xObs', codigo='FR11', tamanho=[1, 255], raiz='//retConsStatServCte', namespace=NAMESPACE_CTE, namespace_obrigatorio=False, obrigatorio=False)
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/', ESQUEMA_ATUAL + '/')
        self.arquivo_esquema = 'consStatServCTe_v3.00.xsd'
    
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.cUF.xml
        xml += self.dhRecbto.xml
        xml += self.tMed.xml
        xml += self.dhRetorno.xml
        xml += self.xObs.xml
        xml += '</retConsStatServCte>'
        return xml
        
    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml    = arquivo
            self.tpAmb.xml     = arquivo
            self.verAplic.xml  = arquivo
            self.cStat.xml     = arquivo
            self.xMotivo.xml   = arquivo
            self.cUF.xml       = arquivo
            self.dhRecbto.xml  = arquivo
            self.tMed.xml      = arquivo
            self.dhRetorno.xml = arquivo
            self.xObs.xml      = arquivo
            
    xml = property(get_xml, set_xml)
    