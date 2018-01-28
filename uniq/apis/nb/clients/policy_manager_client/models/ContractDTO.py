#!/usr/bin/env python
#pylint: skip-file
# This source code is licensed under the Apache license found in the
# LICENSE file in the root directory of this project.


class ContractDTO(object):


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'description': 'str',
            
            
            'name': 'str',
            
            
            'accessClause': 'AccessClauseDTO',
            
            
            'id': 'str',
            
            
            'createTime': 'int',
            
            
            'lastUpdateTime': 'int'
            
        }

        self.attributeMap = {
            
            'description': 'description',
            
            'name': 'name',
            
            'accessClause': 'accessClause',
            
            'id': 'id',
            
            'createTime': 'createTime',
            
            'lastUpdateTime': 'lastUpdateTime'
            
        }       

        
        #description
        
        self.description = None # str
        
        #name
        
        self.name = None # str
        
        #accessClause
        
        self.accessClause = None # AccessClauseDTO
        
        #id
        
        self.id = None # str
        
        #createTime
        
        self.createTime = None # int
        
        #lastUpdateTime
        
        self.lastUpdateTime = None # int
        
