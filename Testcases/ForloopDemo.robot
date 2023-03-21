*** Settings ***
*** Test Cases ***
#Forloop1
 #     FOR   ${i}    IN RANGE    1   10

#        LOG TO CONSOLE    ${i}
#     END
#Forloop2
#    FOR    ${i}    IN    1 2 3 4 5 6 7 8    # Here i gave single space value so it printed in single line
#        LOG TO CONSOLE    ${i}
#    END
#Forloop3
#    FOR    ${i}    IN    1  2   3   4  5   6  7  8    # Here i gave double space so values it printed in line by line
#        LOG TO CONSOLE    ${i}
#    END

#Forloop4withList
#    @{items}    create list  1 2 3 4 5
#    FOR    ${i}    IN    @{items}
#        LOG TO CONSOLE    ${i}
#    END
#Forloop5
#    FOR    ${i}    IN    RAM    VARUN   NIKIL
#        LOG TO CONSOLE    ${i}
#    END
Forloop6
   @{nameslist}     create list    RAM     JACK     JOHNE   RAVI
   FOR    ${i}    IN    @{nameslist}
          exit for loop if    '${i}'=='JOHNE'
          LOG TO CONSOLE    ${i}
   END

