from time import sleep

import parlai.mturk.core.mturk_utils as mturk_utils


def main():

    mturk_utils.setup_aws_credentials()
    client = mturk_utils.get_mturk_client(False)

    assignment_id = input("Assignment ID: ")
    reason = input("Reason: ")

    response = client.approve_assignment(AssignmentId=assignment_id, RequesterFeedback=reason, OverrideRejection=True)

    print(response)


if __name__ == '__main__':
    assignments = ["3ERET4BTVQ36CHBPNRMSGA8ITAI9KE", "3TVSS0C0E5UGRWEKABACVL3PAOUWTX", "3RKNTXVS3QSZ3YWRU5DC5OU62684AW", "3LQ8PUHQFPM8LS3KL0P8GBRTKJYHIY", "3T111IHZ5IKSZLOKDBVPHMUWO1ER9P", "3G0WWMR1UZEDCMDE16PUUXFBX4TQNM", "31N2WW6R9VK9HTUV57UL9KDRLMOF3Y", "3GGAI1SQEZS303IVKN9ZXD1UO0DCM0", "35BLDD71IARZYJNEQTUYV7LSOAHVZ3", "382M9COHEL91A97IPG6GEBIRMXZUE7", "3QAPZX2QN87TZ7JMYPXVN3LV96X022", "3COPXFW7XF6R44RW4GIP208XYEVKPF", "32M8BPYGAXGULW891U7QVBFS5IZIGC", "3MX2NQ3YCDOTVU8KJKO0UOBI3MP5XH", "30OG32W0SY5OFJN9SFUU0GQXE2ZENU", "33SA9F9TR1OE2DWNKGLHWZ3O7E3EWL", "3DPNQGW4LP9YGWKO4SW0PJSK6MO46A", "3KXIR214I8AAYV1NHQKXZ6B8QHM42T", "3PW9OPU9PUET6W44U81V1845EX4216", "33FBRBDW6STOFEGRQMZGSV0Z4UNC89", "3GD6L00D3WRJD08X4QKFGHI3K3J1MW", "3TK8OJTYM5F5KFL83KWW49JEEC4PV8", "3ZWFC4W1UY110VFXGXVHRIG7RZ7RFF", "3W2LOLRXLF9CGH7BH8ME7V8CZVORKH", "38F71OA9GXQA3F25BPZ05JMXLD4MFK", "3IJXV6UZ11DLAMHNH512UFTZ7SVRI4", "3A4TN5196OCH8PHKTQTM58TY7ECCHP", "37FMASSAYGLYUF0YL8FCU0OVP6RIBH", "31LM9EDVOPMWQZ916G5LXW3PJ92JNP", "3R5F3LQFV6E48ZEHPH8K0FRKSHKOZU", "39ASUFLU611TRD1DULH3YIHVGG9XEX", "3QUO65DNQYINM0K7JU9CJNC5Q0YOU0", "3K5TEWLKGZ5D3TY4QP6CVCI2SXTIV7", "36WLNQG7834MEAYCPPPL9LQ3XC6BEL", "3JC6VJ2SAFDHZH0R8AWMAG0K21MA5O", "32SVAV9L3J3EL2DNUR8TVJ20O5VA3Y", "30H4UDGLT6CMUSRZPSV5HD01NHBPM6", "3ZAZR5XV05C3ZAHEZCZT5FX3329ZCE", "39RP059MELNKQYQP6ND4MTVC6D3MBP", "3SLE99ER0R7KP5P8LC3YUVRLLHLBZV", "3VBEN272MOTJFAB56614ZDLFEFRGSQ", "3RSDURM96EGIRIRNZH35HWO4IK8EYL", "3Z4AIRP3CA7U7C71IXMORYY1R6V1X6", "3J2UYBXQQP6HH82NLR9YDG27PAQ60E", "30X31N5D67KI5JY2K69U3RACGLZSAD", "33M4IA01QKVI0H6IGR13XPGEV4PXRY", "3X87C8JFVA5ASZ5J926GTRPHK2DSQA", "3XCC1ODXDP5YRK56UD6B3HKLY0SRQJ", "384PI804XWVM460KS4C1ELYZ7ZF0SM", "3WOKGM4L75A76E8RLNVSUGOYAAC0OP", "3AAPLD8UCGBYU6JVFCOCUIT2VY4THD", "3HVVDCPGTIMKG19KPCS0GIO5LUHTYC", "3GNCZX450MHLSRIASP508M51T0MPAM", "3I2PTA7R3XOC4GSB4TXE25Y7383QKU", "3EFVCAY5L73BNSMX0EG2FZDUUETJ8R", "3P1L2B7AD5JK3AXDAGHBS0GMD82OL1", "3IXEICO796DIXHZEJTX8XR4CMLL6TO", "32EYX73OY43QJDCNBMQGDIHA1M8UR3", "38SKSKU7R5RA7OMACL4683K010DLIF", "3NOKK93PR52KLDAWZGRBATWO0A5EEC", "3N8OEVH1FVKS9V0AN8X3KHKG8C1OOA", "3PPTZCWALUE7TBRX4U0OPKMK7IOZQZ", "3WJ1OXY92EA0MZJT683PM0AB4SZ8A2", "33PPO7FECZ9R9CYIZ46IPQCVSR1IDM", "358010RM5INATONZPB6DYM5HG9RXVE", "3DZQRBDBSP9ILYZHBRUKGJW6AAV3SE", "3U8YCDAGXTAARQL700NWJLJYPB20Q5", "3KAKFY4PGYWTRKWL6F06CHQJ1D4I3E", "3KKG4CDWKMSLYFMM2ZZC9TJMWM549S", "3ND9UOO81OWS8J6F128L9UT8G9LLWS", "3018Q3ZVOMK644YP5H9PDH5GUJHRAP", "3DEL4X4ELAFRXII4UMTX5L9BYR5XY1", "3X4MXAO0BKI3BH1S6M5HV627M2RWRC", "3ZAZR5XV05C3ZAHEZCZT5FX333SZCZ", "33LK57MYLXZJ6R6AWYPTKK1LP5TSZZ", "3K2755HG5WX7ZLWSYW0XMTZ3CXTDF6", "36WLNQG7834MEAYCPPPL9LQ3XC9EBR", "3ON104KXQOQWABZUVA94NDRXUOWW4I", "3YMU66OBIR2UP1XPVCP5VZED54KGHF", "3MB8LZR5BJN1DJCYCOPILJZDT2ALKU", "384PI804XWVM460KS4C1ELYZ7ZE0SL", "39K0FND3AL9F7OLX09D8RIB6OW8AMA", "3DY46V3X3TCKTBOADE5525KYAMG556", "37W3JXSD6A2C8IDEKHXB32V4PONWYT", "3BWI6RSP7K3ZCYVMC8D54J47ELB7EP", "3Z4GS9HPNZ4E3JGCP0ZZY9CQSY7773", "351SEKWQS4BD5VO9KJ4AHJJC90PMDA", "3A1PQ49WVLBXLM7MDT42OCA73HNH16", "3GFK2QRXXDBE6U3U9FSES5XBUL5W53", "3QILPRALQ9P76IDIFC8U86UB3Z2N85", "3B3WTRP3DFWBV17ZYLGOGEMOC96920", "3HFNH7HEML872UWSE2CZ4D6EWSFGQC", "34MAJL3QP8HZJDX6LQY2IGG0WVK432", "3UNH76FOCWZG36J0GFROU4TDRNZYMW", "3HFNH7HEML872UWSE2CZ4D6EWSCGQ9", "39JEC7537YVMQQC4YFAQK9K7FSYVC7", "3DH6GAKTY2JG2DIJV4HI26PM6SDYZB", "3B1NLC6UG3QM2IVDEPXA48G4RXGPGJ", "3WMINLGALFX2Y296NKJUOM6UUJOACE", "3D8YOU6S9IEXXUE3JYNI2NQE505U6I", "3018Q3ZVOMK644YP5H9PDH5GUJQRAY", "3NXNZ5RS1ERIH2454XXJC53WNPF973", "3IO1LGZLKDRZZX7QGVMD6V8P88L86M", "31QNSG6A5VNI3XLVZ5R5C98L3J578K", "3EF8EXOTT5PTCS2C1T7N0PQMG9SJ1E", "38F5OAUN5R6BW8MO29LBPM1K63OH74", "3DUZQ9U6SQI2X710V10QZEOP1W8VSR", "35GCEFQ6I9IFMALV6JOSCCT9XRG3Z8", "354P56DE9OX0MH04D3XAT08MFE4S7Z", "3K772S5NPC5W5N1YPHZHVWT1SQRHEP", "3K2755HG5WX7ZLWSYW0XMTZ3CY2FDJ", "3MYYFCXHJ710DP9UG55M1A590094GU", "3MAOD8E57U4XLJEQNKKMO5B4U86XNI", "3OJSZ2ATDWQZGF2T17K20PYU1US576", "3S0TNUHWKXCYK6M5QIURC1IHPT7D8G", "3IUZPWIU1S1HODOXG2WKUUGTR97KWF", "32SVAV9L3J3EL2DNUR8TVJ20O41A32", "34S9DKFK77JMLO40SG6O7JIDWCUYNF", "3HWRJOOET9WLVWFE0BBGZA0310XESU", "3M23Y66PO61HIHMZUTSINM8QK296S1", "3KMS4QQVK6KFDR22QDMKQ6UTW7TFKQ", "3MX2NQ3YCDOTVU8KJKO0UOBI3MUX5E", "3JWH6J9I9W7Q8GBPIOS4Z8KCB46BN9", "3JMSRU9HQMO1NOWIU6GLAXKA04KVE9", "3LBXNTKX0VPCWHAWMA1H64GKPIF9XJ", "39OWYR0EPOLAXWRJUSNBZE94UM4YF6", "3Z4AIRP3CA7U7C71IXMORYY1R5RX1W", "36PW28KO43QHV0TKJBPPEA6XFTNEAT", "3PEIJLRY6XNN8DN4FLB9KOOVNJDXWA", "31LVTDXBLB4N0NPT28YFMVLROVOLR9", "31QTRG6Q2X7MO9GD8VJGB8N8WSTYPB", "3Y9N9SS8L25CJ9GZE1ZVLKA698VD36", "33L7PJKHCKS51VI2C8U6H503SF1T8L", "3ZOTGHDK5M577NS3UPEC4MUH51RSOY", "30H4UDGLT6CMUSRZPSV5HD01NHBPM6", "3IHR8NYAMBV6Q22TJOV9VJJ11QRP4C", "323Q6SJS8MAOB11UKSJNDEE14PMHFJ", "3AAJC4I4FKMQ7ONK94GFSJAYTMKJZE", "3QRYMNZ7F2BQ4256IAJPZ2QYHA2TNB", "3TMFV4NEPC8XTCMW7DZH4P72W9LW8G", "36DSNE9QZ9SE8K9D7V5YCL3U9IEOJE", "37Z929RLGD2NKFXBQ60BYW044AOST2", "30H4UDGLT6CMUSRZPSV5HD01NIQPMN", "3DUZQ9U6SQI2X710V10QZEOP1V9SVN", "3MHW492WW47ZZCOVB444N5PJ96QMV4", "39LOEL67OWZ02EK8XTOFZSW5YH9381", "3ZAZR5XV05C3ZAHEZCZT5FX3342CZO", "37XITHEIS03UXJVNPV5GJCV4UNJCRV", "3P59JYT76PEUFGGDWRL57EN06HST25", "3VAR3R6G1TVPO3DUGR87NVUGT93O8H", "3MAOD8E57U4XLJEQNKKMO5B4U7NNXN", "30BUDKLTXHPKPUH3OFY86ZQBNGC5E6", "3CN4LGXD51I0ZGUUABRS8ACD5X8Y4X", "3O6CYIULEHVVR9T9AG0M0HPRT2WUWH", "3IFS6Q0HJMDXB1H0WU17KPYVTUDSIS", "3MH9DQ75706ZUN39VBW4EE33ZE6UGI", "3TDXMTX3CFOSO3J3PHY4JK23B5H6IL", "37C0GNLMHJXBGS3HX3XTSNMQJ096DJ", "3ZOTGHDK5M577NS3UPEC4MUH53GSOR", "3Z3ZLGNNSMO68IK4JN5FLJH5SOZQ35", "31EUONYN2ZXNZF97OKJHF9EO477VOW", "32UTUBMZ7KQ3GLKYKFEV9PEPX8NVBR", "3BDCF01OG1OWXO1FG3Q9UREORIGLYO", "37U1UTWH9ZGSLG5A8JPBHQZL4V28RN", "336KAV9KYUMQW2F76X84FVFFLIN2YE", "3VNXK88KKGCKSS51MV0ZIJJZ97V9V4", "39JEC7537YVMQQC4YFAQK9K7FSZVC8", "3LQ8PUHQFPM8LS3KL0P8GBRTKI8HI6"]
    reason = "Rejection was probably a bug, sorry! Your assignment status is now changed to 'accepted'. Will try to fix this in the next round."
    mturk_utils.setup_aws_credentials()
    client = mturk_utils.get_mturk_client(False)
    for assignment in assignments:
        try:
            print(client.approve_assignment(AssignmentId=assignment, RequesterFeedback=reason, OverrideRejection=True))
        except:
            pass
        sleep(1)

    # main()