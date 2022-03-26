# -*- coding: utf-8 -*-
__author__ = 'SirHades696'
__email__ = 'djnonasrm@gmail.com'

instructions = [
    'DROP TABLE IF EXISTS email;',
    """
        CREATE TABLE email (
            id INT PRIMARY KEY AUTO_INCREMENT,
            email TEXT NOT NULL,
            subject TEXT NOT NULL,
            content TEXT NOT NULL
        ) 
    """
]