# -*- coding: utf-8 -*-
#
# PySPED - Python libraries to deal with Brazil's SPED Project
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira at tauga.com.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Library General Public License as
# published by the Free Software Foundation, either version 2.1 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# PySPED - Bibliotecas Python para o
#          SPED - Sistema Público de Escrituração Digital
#
# Copyright (C) 2010-2012
# Copyright (C) Aristides Caldeira <aristides.caldeira arroba tauga.com.br>
#
# Este programa é um software livre: você pode redistribuir e/ou modificar
# este programa sob os termos da licença GNU Library General Public License,
# publicada pela Free Software Foundation, em sua versão 2.1 ou, de acordo
# com sua opção, qualquer versão posterior.
#
# Este programa é distribuido na esperança de que venha a ser útil,
# porém SEM QUAISQUER GARANTIAS, nem mesmo a garantia implícita de
# COMERCIABILIDADE ou ADEQUAÇÃO A UMA FINALIDADE ESPECÍFICA. Veja a
# GNU Library General Public License para mais detalhes.
#
# Você deve ter recebido uma cópia da GNU Library General Public License
# juntamente com este programa. Caso esse não seja o caso, acesse:
# <http://www.gnu.org/licenses/>
#



from pysped.xml_sped import XMLNFe
import os


DIRNAME = os.path.dirname(__file__)


class Signature(XMLNFe):
    def __init__(self):
        super(Signature, self).__init__()
        self.URI = ''
        self.DigestValue = ''
        self.SignatureValue = ''
        self.X509Certificate = ''
        self.caminho_esquema = os.path.join(DIRNAME, 'schema/')
        self.arquivo_esquema = 'xmldsig-core-schema_v1.01.xsd'

    def get_xml(self):
        if not len(self.URI):
            self.URI = '#'

        if self.URI[0] != '#':
            self.URI = '#' + self.URI

        xml  = '<Signature xmlns="http://www.w3.org/2000/09/xmldsig#">'
        xml +=     '<SignedInfo>'
        xml +=         '<CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315" />'
        xml +=         '<SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1" />'
        xml +=         '<Reference URI="' + self.URI + '">'
        xml +=             '<Transforms>'
        xml +=                 '<Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" />'
        xml +=                 '<Transform Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315" />'
        xml +=             '</Transforms>'
        xml +=             '<DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1" />'
        xml +=             '<DigestValue>' + self.DigestValue + '</DigestValue>'
        xml +=         '</Reference>'
        xml +=     '</SignedInfo>'
        xml +=     '<SignatureValue>' + self.SignatureValue + '</SignatureValue>'
        xml +=     '<KeyInfo>'
        xml +=         '<X509Data>'
        xml +=             '<X509Certificate>' + self.X509Certificate + '</X509Certificate>'
        xml +=         '</X509Data>'
        xml +=     '</KeyInfo>'
        xml += '</Signature>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.URI = self._le_tag('//sig:Signature/sig:SignedInfo/sig:Reference', 'URI') or ''
            self.DigestValue = self._le_tag('//sig:Signature/sig:SignedInfo/sig:Reference/sig:DigestValue') or ''
            self.SignatureValue = self._le_tag('//sig:Signature/sig:SignatureValue') or ''
            self.X509Certificate = self._le_tag('//sig:Signature/sig:KeyInfo/sig:X509Data/sig:X509Certificate') or ''
        return self.xml

    xml = property(get_xml, set_xml)
