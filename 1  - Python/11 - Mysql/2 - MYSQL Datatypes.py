
# MYSQL Datatypes

# in mysql there 3 type of categories of data 


# 1 - Numeric
# 2 - String
# 3 - Date and Time

##########################################################################

# storage 

# tiny int   = 1 bytes
# small int  = 2 bytes
# medium int = 3 bytes
# int        = 4 bytes
# bigint     = 8 bytes




# 1 - Numeric

# a - TINYINT
    # Tinyint is a very small signed and unsigned integer
    # for signed data the range from -128 to 127
    # unsigned data the range from 0 to 255
    # maximum width is 4 digit 


# b - SMALLINT
    # SMALLINT is a  signed and unsigned integer
    # for signed data the range from -32768 to 32767
    # unsigned data the range from 65535
    # maximum width is 5 digit 


# c - MEDIUMINT
    # for signed data the range from -8388608 to 8388607
    # unsigned data the range from 0 to 16777215
    # maximum limit 9 digits
    
# d - INT
    # for signed data the range from -2147483648 to 2147483647
    # unsigned data the range from 0 to 4294967295
    # maximum limit 11 digits
    
# e - BIGINT
    # maximum limit 20 digits

# f - DECIMAL(M,D)
    # store point values

    
############################################################################

## 2 - String


    # 1 - CHAR(M)      
        # limit 0 to 255

        
    # 2 - VARCHAR(M)   
        # limit 1 to 255

        
    # 3 - TEXT
        # maximum length of field is 65535 characters

#############################################################################


# 3 - Date and Time

    # 1 - Date
        # it is  "YYYY-MM-DD" format
        # todays date   "2022-02-08"

    
    # 2 - DATETIME
        # it is "YYYY-MM-DD HH:MM:SS" formate
        # todays date and time "2022-02-08 17:55:52"
    
    # 3 - TIME
        # it is "HH:MM:SS" formate
        # current time "17:56:54"

    
    # 4 - YEAR
        # it is "YYYY"
        # "2022"



#############################################################################




