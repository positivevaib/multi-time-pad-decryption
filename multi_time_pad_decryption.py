#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 09:21:06 2018

@author: vaibgadodia
"""
def strhex(a):
    '''Converts a hex digit to its corresponding int.'''
    hex_dict = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "a":10, "b":11, "c":12, "d":13, "e":14, "f":15}
    return hex_dict[a]

def hexstr(a):
    '''Converts an int (0-15) to its corresponding hex digit.'''
    str_dict = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
    return str_dict[a]

def hexint(a):
    '''Converts hex to int.'''
    int_value = 0
    for i in range(len(a)):
        int_value += strhex(a[i])*(16**(len(a)-1-i))
    return int_value

def strxor(a, b):
    '''XORs two hex encoded strings and returns a hex encoded string.'''
    xor_hex = ""
    for i in range(len(a)):
        xor_hex += hexstr(strhex(a[i])^strhex(b[i]))
    return xor_hex

def alphaindex(mat, j):
    '''Returns the row index of the first a-z/A-Z char in the given column of a matrix and returns -1 if the required char is not found.'''
    ind = -1
    for i in range(len(mat)):
        if (mat[i][j] >= 65 and mat[i][j] <= 90) or (mat[i][j] >= 97 and mat[i][j] <= 122):
            ind = i
            return ind
    return ind

def nonprintindex(mat, j):
    '''Returns the row index of the first non-printable char in the given column of a matrix and returns -1 if the required char is not found.'''
    ind = -1
    for i in range(len(mat)):
        if mat[i][j] >= 0 and mat[i][j] <= 31:
            ind = i
            return ind
    return ind

def changecase(a):
    '''Changes char case.'''
    if chr(a).isupper():
        return ord(chr(a).lower())
    else:
        return ord(chr(a).upper())
    
def alphaxor(a, alpha):
    '''XORs two hex encoded chars and returns the corresponding int value.'''
    return hexint(strxor(a, alpha))

def alpharange(a):
    '''Returns the ASCII value of A/a according to the given char's value.'''
    if a >= 65 and a <= 90:
        return 65
    else:
        return 97

def main():
    #Hex encoded ciphertexts
    c1 = "070d07074507104554595f00380b4555070c4d064f1f0a0d4518450d41002900131b434e15040c5a0e451a413a1c0c1d5449124e104804441c4245541b491d174f060800454b031c4f542c17041b0c411a0c4541050415572e0d4907520815461d0b4b"
    c2 = "00000000001d1c4f1848044c030112535410021000040e44470e0b1c5c412d004105594c0001154c0e45095d311d0d1c52081d441b05454f010b48541d040845501105170e4b2c0d0e492a450209404c110c455018000c4a3b1a081d44061e00160d06411a1d00000001084547150f01520a111c4a0037100c0a4952540917454b1718403007045d"
    c3 = "1d0e490a4f1c0100161a0a571c0b170010060816001e0e10001810095e4f2b11411c4445543f00422817005e2007282369491a54541d16451c4e114811493e11411e070b520f45334f563816021a45500048265212150d4174240011520801595440366a2c224c0000064d02451e0416411f005940553407041a5f0e"
    c4 = "00000c536507144c1d1b0d0038070e49040c090c41500817001f0d1c0e6537020d015f485904044e0c10184931480c17491d1a4f1a480a464f1a0d45540f1f0045500e0a4c020b1c0e453706180b404f040d01490a452e473f0119164400120e542e0a55010a0044540603451145412e410510185c59795751581d0c540111000216595a3c0d4915491b0054540d01491b070a4e54060b4577190a0d500e01104f0e"
    c5 = "19090710480c0054111a45750107114510492b0a4f0403054c07453a42553b49410b434d19070b4c124512403b1f0753411a536d15064b003a000c54110d4d0a5250120d4d1b09000e75370c150d480c540116000a45095c3b0e0c0053001c4e150445460001114215050145431c14060009040a4b44790c0f48634c104831520a031f41260c4553671b1641000d1700220f0b431c0c1e1145024d44650502154f4e3d49411c44410048064f06151c5a311b491a4e490748114835520a030c4506492100411714010c4b11114b002d0a11484a4c1d0f0d544b0a1f0e11060e1f491a1b0012070a540d0f094c5a"
    c6 = "00000c536507144c1d1b0d0009010a5416080109001c0405471e00595d592a11040500001504164f4b0e174123064912534907481148034f001a074118054d1559020009490f495947537904411b49521d0d1600040359473a1c0c0143061d4e110b11450b4e0945150e18005350070b524b081c40072a45001b5f4f17010454020a170e3207060742081f4c540b09550d1d45491a49280b471c000a4447450e4754314512015400000d044d18451f5c3b0549244105165354090b444f010b45540f1f0a4d50261145190b0a4b5979040d1b4300170708500e1110403346"
    c7 = "00000c534d061745060645470e030000001b0c064503410d541845165c493e0c0f1b0c541b4854185d5659593c0d075354011600380912534f0103000001084567110c01001c000b4b003617080f454e150409594b06164a3d0e001644491a4e542d0b47030f0b44540b14457418044466040a0d4c41350941295f531b0b0c411f0c16407a"
    c8 = "01060d165249074811480841010f0245190c0311001f074467020a0f4f4e370c413c5e4104091154040b1002741c0116000a1f551648124f014e5413541d1f0a50180801534b0c170e543100411c494e541100411916594c310e0601454942194c5e49000600064c010d040b4750120d584b091c4f472c00411c4554180d16000a0b1d0e32011f1600001d54111a0b411b070a4e15054d1149040d0153"
    c9 = "160d001d47491a4e54090b00000803531d0d0845501f120d54020a170e492a450f0758001506454f0d031c40370d491a4e491a54070d0946434e075500490c45501c001d4519450a4100290a120158491b0600444b12114b3a481d1b45491141180445491c4e154c1510080100160e16570a171d0e42204500485845150508411f0059593d04055343061e4d1d1c4554070b454f120f1e0c4415410b460d00174d45790c07485848111145420e06164331484b1a4e1f1c4c020d010006004541171d041345501108411247550e57310c02000c491a0b09550f000a0e260d0a16491f1a4e134811480a4e0741180543"
    c10 = "00000c534e0c1644540e0a524f0f45531d070a094550030b4412450d41003613041a5f4511480453180a1a47351c001c4e49154f1b1c074103024542110a0c0845500014500a171c4054790415485848114807450c0c17403d060e534f0f53541c0d45125f1a0d00170c031155021844570211110e54310041014243060d0453020b1e0e240719064c0801490011454f094e0c4e000c1f0b4104080b4e0a095948492111141a49535a"
    
    #Ciphertext list
    c_list = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
    #Ciphertext matrix
    c_mat = []
    
    #Hex encoded target ciphertext
    c_target = "1b0e0f00490d16001d1b454f010b454f1249190d45500d05571845164800381612074f49151c0c4f05451f413b1c0b124c055f001707014909070044540003456c111644115a451648002d0d04486041031b454f0d450d4631482e124d0c5d"
    m_target_list = ["*"]*int(len(c_target)/2)
    #Target string
    m_target_str = ""
    
    #Adding hex encoded chars to c_mat
    for c in c_list:
        temp_mat = []
        for i in range(0, len(c), 2):
            temp_mat.append(c[i:i+2])
        c_mat.append(temp_mat)
    
    temp_mat = []
    for i in range(0, len(c_target), 2):
        temp_mat.append(c_target[i:i+2])
    c_mat.append(temp_mat)
    
    #Matrix of XORed chars
    xor_mat = []
    #Adding chars of ciphertexts XORed with c_target in xor_mat
    for i in range(len(c_mat)-1):
        temp_mat = []
        for j in range(len(c_mat[10])):
            xor_ord = hexint((strxor(c_mat[i][j], c_mat[10][j])))
            temp_mat.append(xor_ord)
        xor_mat.append(temp_mat)
       
    #Decrypting c_target
    for j in range(len(xor_mat[0])):
        alpharow = alphaindex(xor_mat, j)
        if alpharow == -1:
            continue
        else:
            new_alpha_ord = changecase(xor_mat[alpharow][j])
            range_min = alpharange(new_alpha_ord)
            range_max = range_min + 25
            
            non_print_row = nonprintindex(xor_mat, j)
            if non_print_row == -1:
                continue
            else:
                alpha_xor_ord = alphaxor(chr(xor_mat[non_print_row][j]).encode("utf-8").hex(), chr(new_alpha_ord).encode("utf-8").hex())
                if alpha_xor_ord >= range_min and alpha_xor_ord <= range_max:
                    m_target_list[j] = chr(new_alpha_ord)
                else:
                    m_target_list[j] = " "
    
    #Concatenating the decrypted message string
    for char in m_target_list:
        m_target_str += char
    
    print(m_target_str)
    
main()