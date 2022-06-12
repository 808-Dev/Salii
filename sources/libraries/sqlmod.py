#Author: 808-Dev
#License: GPL - GNU General Public License
#Version: V.1.0.0 (Version 1)
#-----------------------------------------
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.
#------------------------------------------
#You didn't get a copy cuz your a loser! Ahaha
#------------------------------------------
from libraries.styling import *
import mysql.connector
import json
def SQLConnect():
    DatabaseCredentials = mysql.connector.connect(host='10.0.0.19',user='salii',password='pufpoLM10$!',database='salii')
    return(DatabaseCredentials.cursor(),DatabaseCredentials)
def SQLPost(template,data,connection):
    SQLAutheticatedSession = connection[0]
    SQLSessionRaw = connection[1]
    SQLAutheticatedSession.execute(template, data)
    try:
        SQLSessionRaw.commit()
        return(True)
    except:
        return(False)
def IsSQL(table,haystack,needle,node):
    SQLAutheticatedSession = node[0]
    SQLSessionRaw = node[1]
    template = ('SELECT * FROM {table} WHERE `{haystack}` = %s'.format(table=table,haystack=haystack))
    data = [needle]
    SQLAutheticatedSession.execute(template,data)
    result = SQLAutheticatedSession.fetchall()
    if not result:
        return(False)
    else:
        return(True)
def SQLSelect(table,haystack,needle,node,column):
    SQLAutheticatedSession = node[0]
    SQLSessionRaw = node[1]
    template = ('SELECT {column} FROM {table} WHERE `{haystack}` = %s'.format(table=table,haystack=haystack,column=column))
    data = [needle]
    SQLAutheticatedSession.execute(template,data)
    result = SQLAutheticatedSession.fetchone()
    if not result:
        return(False)
    else:
        return(result)
def SQLSelectAll(table,haystack,needle,node,column):
    SQLAutheticatedSession = node[0]
    SQLSessionRaw = node[1]
    template = ('SELECT {column} FROM {table} WHERE `{haystack}` LIKE%s'.format(table=table,haystack=haystack,column=column))
    data = ['%'+needle+'%']
    SQLAutheticatedSession.execute(template,data)
    result = SQLAutheticatedSession.fetchall()
    if not result:
        return(False)
    else:
        return(result)
def SQLUpdate(table,haystack,needle,type,value,column,node):
    
    SQLAutheticatedSession = node[0]
    SQLSessionRaw = node[1]
    
    ItemArray = SQLSelect(haystack=haystack,needle=needle,node=node,column=column,table=table)
    
    Item = json.loads(ItemArray[0])
    
    if(type=='ADD'):
        Item.append(value)
        ReturnedItem = str(json.dumps(Item))
    if(type=='REMOVE'):
        Item.remove(value)
        ReturnedItem = str(json.dumps(Item))
    template = ('UPDATE {table} SET {column} = \'{value}\' WHERE {haystack} LIKE \'%{needle}%\''.format(table=table,haystack=haystack,needle=needle,column=column,value=ReturnedItem))
    SQLAutheticatedSession.execute(template)
    try:
        SQLSessionRaw.commit()
        PrintGood('Interaction successfully posted!')
        return(True)
    except:
        PrintBad('Interaction not posted successfully.')
        return(False)
def SQLDelete(table,haystack,needle,node):
    SQLAutheticatedSession = node[0]
    SQLSessionRaw = node[1]
    template = ('DELETE FROM {table} WHERE {haystack} = \'{needle}\''.format(table=table,haystack=haystack,needle=needle))
    SQLAutheticatedSession.execute(template)
    try:
        SQLSessionRaw.commit()
        PrintGood('Group successfully removed!')
        return(True)
    except:
        PrintBad('Group not removed successfully.')
        return(False)
def MayBeSQL(table,haystack,needle,node,length):
    SQLAutheticatedSession = node[0]
    template = ('SELECT * FROM {table} WHERE `{haystack}` LIKE %s'.format(table=table,haystack=haystack))
    data = ['%'+needle+'%']
    SQLAutheticatedSession.execute(template,data)
    result = SQLAutheticatedSession.fetchall()
    if result and len(needle)==length:
        return(True)
    else:
        return(False)