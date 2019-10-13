from selfdrive.car import dbc_dict

class CAR:
  IMPREZA = "SUBARU IMPREZA LIMITED 2019"

FINGERPRINTS = {
  CAR.IMPREZA: [
  # SUBARU IMPREZA 2019 (commaai)
  {
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 280: 8, 281: 8, 290: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 544: 8, 545: 8, 546: 8, 552: 8, 554: 8, 557: 8, 576: 8, 577: 8, 722: 8, 801: 8, 802: 8, 805: 8, 808: 8, 816: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1614: 8, 1617: 8, 1632: 8, 1650: 8, 1657: 8, 1658: 8, 1677: 8, 1697: 8, 1722: 8, 1743: 8, 1759: 8, 1786: 5, 1787: 5, 1788: 8, 1809: 8, 1813: 8, 1817: 8, 1821: 8, 1840: 8, 1848: 8, 1924: 8, 1932: 8, 1952: 8, 1960: 8
  },
  # SUBARU XV 2018 (mlp)
  {
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 256: 8, 280: 8, 281: 8, 290: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 372: 8, 544: 8, 545: 8, 546: 8, 554: 8, 557: 8, 576: 8, 577: 8, 722: 8, 801: 8, 802: 8, 805: 8, 808: 8, 811: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1614: 8, 1617: 8, 1632: 8, 1650: 8, 1657: 8, 1658: 8, 1677: 8, 1697: 8, 1759: 8, 1786: 5, 1787: 5, 1788: 8
  },
  # SUBARU XV 2.0i-S 2018 (aztan)
  {
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 280: 8, 281: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 372: 8, 552: 8, 557: 8, 576: 8, 577: 8, 722: 8, 808: 8, 811: 8, 816: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1614: 8, 1617: 8, 1632: 8, 1640: 8, 1650: 8, 1657: 8, 1658: 8, 1677: 8, 1722: 8, 1759: 8, 1786: 5, 1787: 5, 1788: 8
  },
  # Forester Sport 2019 (sirged)
  {
    2: 8, 64: 8, 65: 8, 72: 8, 73: 8, 280: 8, 281: 8, 282: 8, 290: 8, 312: 8, 313: 8, 314: 8, 315: 8, 316: 8, 326: 8, 372: 8, 552: 8, 544: 8, 545: 8, 546: 8, 554: 8, 557: 8, 576: 8, 577: 8, 722: 8, 801: 8, 802: 8, 803: 8, 805: 8, 808: 8, 811: 8, 816: 8, 826: 8, 837: 8, 838: 8, 839: 8, 842: 8, 912: 8, 915: 8, 940: 8, 1614: 8, 1617: 8, 1632: 8, 1650: 8, 1651: 8, 1657: 8, 1658: 8, 1677: 8, 1697: 8, 1698: 8, 1722: 8, 1743: 8, 1759: 8, 1787: 5, 1788: 8, 1809: 8, 1813: 8, 1817: 8, 1821: 8, 1840: 8, 1848: 8, 1924: 8, 1932: 8, 1952: 8, 1960: 8
  },    
  # END IMPREZA
  ],
}

STEER_THRESHOLD = {
  CAR.IMPREZA: 80,
}

class ECU:
  CAM = 0

ECU_FINGERPRINT = {
  ECU.CAM: [290, 356],   # steer torque cmd
}

DBC = {
  CAR.IMPREZA: dbc_dict('subaru_global_2017', None),
}
